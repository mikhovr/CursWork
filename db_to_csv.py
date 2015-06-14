# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3
import re
 
conn = sqlite3.connect('D:/cw/tweets_april.db')
c = conn.cursor()
tw = pd.read_sql("SELECT content from tweets LIMIT 100", conn)
#http://shahmirj.com/blog/extracting-twitter-usertags-using-regex
posts = tw.ix[:,0].replace([u'(?<=^|(?<=[^a-zA-Z0-9-_\\.]))(@|#)([A-Za-zа-яА-Я0-9]+[A-Za-zа-яА-Я0-9_]+)\s',
                            '\n', 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                            u'[^a-zA-Zа-яА-ЯёЁ\s]'],
                            ['', ' ', '', ''], 
                            regex=True)
posts.to_csv('D:/cw/csvhist.csv', sep = '%', header = False, encoding = 'utf-8', index = False)
conn.commit()
conn.close()
