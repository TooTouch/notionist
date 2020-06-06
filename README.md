# Notionist
> *Life is divided into before and after meeting Notion*

This is Notion collection extraction repository for people who use Notion. 

I saw `notion-py`, unofficial python API for Notion.so made by `jamalex`, and appreciated `jamalex`. Thanks to `notion-py`, I'm using Notion better. However, there is no table extraction function. I want to use my table contents in python without extracting zip file. Therefore, I make this repository. At first, this repo was for me, but now I want to share this repo for notion users. 

Please contact me if you want to join this repo.

# Quick Start

You can install this module entering `pip install notionist` in your command or bash.

```
pip install notionist
```

# How to Use

## 1. Get token_v2

First of all, you need `token_v2` to use this module. You can find you token_v2 in your cookies after enterting your id and passward to Notion as follows. 

`F12 (User Defined Key) > Application > Cookies > https://www.notion.so > token_v2`

![token_v2](https://user-images.githubusercontent.com/37654013/83939185-d2a48b80-a815-11ea-8a77-11465e01920d.JPG)

## 2. Make a table in notion

When you make a table in notion, you can copy your table link as follows (If you work in web, you can use url).

**TODO:** Only particular types such as Number, Text, Multi-select, and Select can be extracted from notion. I will try others as soon as possible.

![table](https://user-images.githubusercontent.com/37654013/83939246-72fab000-a816-11ea-9894-8cd5e3d729c1.JPG)

## 3. Using CollectionExtract

```python
from notionist import collection_api

token_v2 = 'YOUR token_v2'
extraction = collection_api.CollectionExtract(token_v2=token_v2)

url = 'https://www.notion.so/tootouch/ae60f9946dc54de78fbd4850ccf48b40?v=9d07e70306b2498eb82805b83f882140'
extraction.table_extract(url)
```

Tags |number|    text |Name
---|---|---|---
0    |A     | 1  | apple    |1
1    |B     | 2  |banana    |2
2    |C     | 3  |orange    |3


# TODO 

- [ ] Extract other types in table 
- [ ] Plotting based on table data in Notion page
