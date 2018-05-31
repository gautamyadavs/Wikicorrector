# Wikicorrector
It automates the task to find erroneous mentions in the wikipedia text. This is the interface to collect the training dataset from the users.

You can download the pickle dataset for surface names from:
https://drive.google.com/open?id=1hlwe2NCYnMhK62lf5lr2m7V88haR7qgd

You can download the wikipedia dump (enwiki-latest-pages-articles.xml.bz2) from:
https://dumps.wikimedia.org/enwiki/latest/

To setup the project:
1. Open wiki/index/views.py and set the path for pickle file
2. Run WikiExtractor.py -cb 250K -o -l extracted enwiki-latest-pages-articles.xml.bz2 after installing this repository <a href="https://github.com/attardi/wikiextractor">wikiextractor</a> on the downloaded dump and run getid.py to generate a text file to create indexes for faster access to file text.
