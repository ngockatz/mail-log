import sqlite3

def connect():
    conn=sqlite3.connect('mail.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS mail(id INTEGER PRIMARY KEY,'
                +'date text, name text, no text, email text,'
                +'checkedout text, datechecked text)')

    conn.commit()
    conn.close()

def insert(date,name,no,email,checkedout,datechecked):
    conn=sqlite3.connect("mail.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO mail VALUES (NULL,?,?,?,?,?,?)"
                ,(date, name, no, email, checkedout, datechecked))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("mail.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM mail")
    rows=cur.fetchall()
    conn.close()    
    return rows                                                        

def search(date='',name='',no='',email='',checkedout='',datechecked=''):
    conn=sqlite3.connect("mail.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM mail WHERE date=? OR name=? OR"
                +" no=? OR email=? OR checkedout=? OR datechecked=?"
                ,(date,name,no,email,checkedout,datechecked))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("mail.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM mail WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,date,name,no,email,checkedout,datechecked):
    conn=sqlite3.connect("mail.db")
    cur=conn.cursor()
    cur.execute("UPDATE mail SET date=?,name=?, no=?, email=?,"
                +"checkedout=?,datechecked=? WHERE id=?"
                ,(date,name,no,email,checkedout,datechecked,id))
    conn.commit()
    conn.close()

connect()


