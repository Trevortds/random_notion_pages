'''
author:
    @tangjeff0
    https://www.notion.so/tangjeff0/Public-Home-0e2636bd409b454ea64079ad8213491f

inspired by: https://praxis.fortelabs.co/p-a-r-a-iii-building-an-idea-generator-400347ef3bb6/
with help from: https://medium.com/@jamiealexandre/introducing-notion-py-an-unofficial-python-api-wrapper-for-notion-so-603700f92369

credits:
    @jamiealexandre
    @fortelabs
    @HiredThought


'''

import sys
import os
import random
from notion.client import NotionClient

def main(num_rand_rows):
    '''
    inputs: a dictionary mapping a collection page to its URL
    outputs: a random row from each collection, plus its URL
    '''
    NOTION_TOKEN = '<replace me>'
    token_v2 = os.environ.get('NOTION_TOKEN') or NOTION_TOKEN
    if not token_v2:
        raise Exception('Please set a token in the code or your environment.')

    client = NotionClient(token_v2=token_v2)

    # replace these urls with any of the collection pages you seek to get a random note from
    # this only works on collection pages (e.g. table, board, calendar, list, gallery)
    urls = [
        'https://www.notion.so/5fe164db3dfa47f28d20c097f8677530?v=adc72e15c3f749179a4cce67dda83445', # Audiation practice 
        'https://www.notion.so/b8a91e509cd74fc7b03564bc98ea6e83?v=6f1467450edb4373b406463f957d2fc4', # Transcription
        'https://www.notion.so/8d0f68198c484e4fb133e9e8035390df?v=da239a115c3045069cbdcc2de966e0ee', # Scales
        'https://www.notion.so/0bc7fc8d1fba428b82dbc08424d07a84?v=214b1dbcb5e1411bae2ead9471b20428', # Learning the fretboard
    ]

    for url in urls:
        page = client.get_block(url)

        rows = page.collection.get_rows()
        if not rows:
            page.collection.refresh()
            rows = page.collection.get_rows()

        if not rows:
            continue

        n = len(rows)
        print(f"\n{page.title}:")
        for i in range(num_rand_rows):
            rand_idx = random.randint(0, n-1)
            rand_row = rows[rand_idx]
            title = rand_row.title
            url = rand_row.get_browseable_url()

            print(f"\ttitle={title}, url={url}\n")
            for child in rand_row.children:

                if child.type == "alias":
                    print(f"\t{child.parent.get_browseable_url() + '#' + child.id.replace('-', '')}")
                else:
                    print(f"\t{child.title}")


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    # either take in user arg for number of rows
    # default to five since the API call is kinda slow XD
    if (len(sys.argv) == 2):
        num_rand_rows = int(sys.argv[1])
    else:
        num_rand_rows = 1
    main(num_rand_rows)