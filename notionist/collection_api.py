from notion.client import NotionClient
import numpy as np
import pandas as pd

__all__ = ['CollectionExtract']

class CollectionExtract:
    def __init__(self, token_v2):
        r"""
        Args
            url: copy your token
        """
        self.client = NotionClient(token_v2=token_v2)

    def table_extract(self, url):
        r"""
        Args
            url: copy your table link
        """
        block = self.client.get_block(url)
        
        if block.get()['type'] == 'page': # inline collection
            chds = block.children
            for chd in chds:
                if chd.get()['type'] == 'collection_view':
                    clt = chd.collection
        elif block.get()['type'] == 'collection_view': # full page collection
            clt = block.collection

        table_rows = clt.get_rows()

        # get column information
        # TODO: other types [files, person, email, date, phone]
        table_info = clt.get()['schema']
        col_info = {}
        for c_id in table_info.keys():
            check_type = ['multi_select', 'title', 'text' ,'number', 'select', 'url', 'checkbox']
            k_info = table_info[c_id]
            if k_info['type'] in check_type:
                col_info[c_id] = {'name': k_info['name'], 'type':k_info['type'], 'values':[]}

        # extract values
        for r in table_rows:
            for k in col_info.keys():
                r_values = r.get()
                # If all observations is None, there is no properties.
                if 'properties' in r_values.keys():
                    p = r_values['properties']
                    # If one of observations is None in properties' keys, value is None
                    if k in p.keys():
                        # condition by types
                        if col_info[k]['type'] == 'url':
                            col_info[k]['values'].extend([p[k][0][1][0][1]])
                        elif col_info[k]['type'] == 'checkbox':
                            col_info[k]['values'].extend([True if p[k][0][0]=='Yes' else False])
                        else:
                            col_info[k]['values'].extend(p[k][0])
                    else:
                        col_info[k]['values'].extend([None])

        df = pd.DataFrame(data=dict((col_info[k]['name'],col_info[k]['values']) for k in col_info.keys()))
        
        return df 