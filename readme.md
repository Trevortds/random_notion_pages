# Get random notion pages

Usage: 



```bash
pip install requirements.txt
export NOTION_TOKEN=<your notion token here>
python main.py [number of rows per db, defaults to 1]
```

![example usage](/screenshots/2021-09-23_12-13.png)

# To get your notion token

Open Notion.so in a browser. Find your cookies (in Firefox, right click anywhere and choose "inspect", go to the storage tab, click 'cookies'). Copy the content of the cookie labeled "token_v2". Paste it in the export command above, or directly into the main.py file.

# To get your databases 

Open your database as a page. Click the three-dots menu dropdown in the upper right corner. Click "copy link". Paste this link in the "urls" list in main.py for each database you want to randomly select from. 