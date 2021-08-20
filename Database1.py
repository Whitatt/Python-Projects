

import sqlite3

conn = sqlite3.connect('database1.db')

with conn:
    cur = conn.cursor() #Below I have created a table of file list
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filelist(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_items TEXT)") # in the file list, i have created a column of items.
    conn.commit()
   
conn = sqlite3.connect('database1.db')

#tuple of items
items_tuple = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loop through each object in the tuple to find the filelist that ends in .txt
for x in items_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
           #the value for each row will be one filelist out of the tuple therefore (x,)
           # will denote a one element tuple for each filelist ending with .txt
            cur.execute("INSERT INTO tbl_filelist (col_items) VALUES (?)", (x,))
            print(x)
           
conn.close()

#the output should be
#Hello.txt
#World.txt
