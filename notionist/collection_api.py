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
        page = self.client.get_block(url)
        table_rows = page.collection.get_rows()

        # get column information
        # TODO: other types [check, files, person, url, email, date, phone]
        table_info = page.collection.get()['schema']
        col_info = {}
        for c_id in table_info.keys():
            check_type = ['multi_select', 'title', 'text' ,'number']
            k_info = table_info[c_id]
            if k_info['type'] in check_type:
                col_info[c_id] = {'name': k_info['name'], 'values':[]}

        # extract values
        for r in table_rows:
            for k in col_info.keys():
                r_values = r.get()
                if 'properties' in r_values.keys():
                    p = r_values['properties']
                    if k in p.keys():
                        col_info[k]['values'].extend(p[k][0])
                    else:
                        col_info[k]['values'].extend([None])

        df = pd.DataFrame(data=dict((col_info[k]['name'],col_info[k]['values']) for k in col_info.keys()))
        return df 