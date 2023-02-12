import sqlite3
import sys

#creating database tables and manipulation of data

   #create the db
def create_db(db_name):
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)
  cursor = conn.cursor()


  conn.commit()
  conn.close()

        #this function creates a table
def create_table()
 # cursor.execute("""create table productos(
 # referencia integer,
 # descripcion text,
 # disponible integer,
 # precio integer
 # )"""#)




def create_new_product():
  conn = sqlite3.connect("productos.db")
  cursor = conn.cursor()

            #declaring python vars
  myref = input('referencia: ')
  mydes = input('nombre del articulo: ')
  mydis = input('cantidad: ')
  mypre = input('precio: ')
         #insertting info in the table                  #the first values are the rows in the db
  cursor.execute("insert into productos(referencia, descripcion, disponible, precio) VALUES (?, ?, ?, ?)", (myref, mydes, mydis, mypre))
          #printing values

  cursor.execute("select * from productos")
  x=cursor.fetchall()
  print(x)
  conn.commit()
  conn.close()




if(sys.argv[1]=="-c"):
  create_db(sys.argv[2])


