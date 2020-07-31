
import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn =  sqlite3.connect("files.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            fileName TEXT NOT NULL \
            )")
    for file in fileList:
        if 'txt' in file:
            cur.execute("INSERT INTO tbl_files \
                (fileName) \
                VALUES (?)", [file])
    conn.commit()

    cur.execute("SELECT fileName FROM tbl_files")
    txtFiles = cur.fetchall()
    Files= ()
    for file in txtFiles:
        Files += file
    print("The files in the database are:\n{}\n{}".format(Files[0], Files[1]))
        
conn.close


