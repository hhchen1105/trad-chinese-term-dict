A traditional Chinese term dictionary for tokenizers
====================================================

* moe-dict/src/dict-json-to-term-txt.py
  - Generate terms (i.e., number of Chinese characters >= 2) from the json file compiled by the moe dictionary
    - moe dictionary: https://www.moedict.tw/%E5%89%97%E6%BB%85
  - The output term list is located at moe-dict/var/tw-edu-dict.dict
  
* zh-wiki-dict/src/wiki-to-term.py
  - Generate terms from the titles of Chinese Wikipedia
    - I assume the Wikipedia is stored locally in MySQL or MariaDB.  Edit zh-wiki-dict/etc/mariadb_settings.json to setup the host, db, user, and pwd.
  - The titles are transformed to traditional Chinese and Taiwan's common usage by OpenCC
    - OpenCC: https://github.com/BYVoid/OpenCC
  - The output term list is located at zh-wiki-dict/var/tw-wiki-dict.dict
  
* tokenizer/src/gen-dict.py
  - Combine the above two list of terms to generate a new term dictionary
  - The output term dictionary is located at tokenizer/var/tw-dict.dict
  
* tokenizer/src/tokenize-article.py
  - A simple script to tokenize articles
  - Sample usage: 
    python tokenize-article.py --content="中文輸入法是指為了將漢字輸入電腦或手機等電子裝置而採用的編碼方法，是中文資訊處理的重要技術。"
  - Sample output:
    Tokenizing...
    Result:
    中文輸入法
    指為
    了將
    漢字
    輸入
    電腦
    手機
    電子裝置
    採用
    編碼
    方法
    中文資訊處理
    重要
    技術
