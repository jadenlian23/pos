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
def create_table():
  try:
    conn = sqlite3.connect("productos.db")
  except Error as e:
    print(e)
  cursor = conn.cursor()

  cursor.execute("""create table users(
  name text,
  privillege text,
  id integer
  )""")
  conn.commit()
  conn.close()




def create_new_user():
  conn = sqlite3.connect("productos.db")
  cursor = conn.cursor()

            #declaring python vars
  myname = input('USER NAME > ')
  mypriv = input('PRIVILLEGE > ')
  myid = input("ID > ")
         #insertting info in the table                  #the first values are the rows in the db
  cursor.execute("insert into users(name, privillege,id) VALUES (?, ?,?)", (myname, mypriv,myid))
          #printing values

  cursor.execute("select * from users")
  x=cursor.fetchall()
  print(x)
  conn.commit()
  conn.close()





   ####this function creates a new product
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





def get_data():
  #to get the data from the database
  conn = sqlite3.connect("productos.db")
  cursor = conn.cursor()

  ref_data=[]
  des_data=[]
  dis_data=[]
  pre_data=[]
  #cursor.execute("select * from productos")
  #getting the data
  referencia=cursor.execute("select referencia from productos")
  referencia_data=referencia.fetchall()

  descripcion=cursor.execute("select descripcion from productos")
  descripcion_data=descripcion.fetchall()

  disponible=cursor.execute("select disponible from productos")
  disponible_data=disponible.fetchall()

  precio=cursor.execute("select precio from productos")
  precio_data=precio.fetchall()




  for i in referencia_data:
     for p in i:
      ref_data.append(p)

  for i in ref_data:
    print(str(i)+"\n")

######################################
  for i in descripcion_data:
     for p in i:
      des_data.append(p)


  for i in des_data:
    print(i+"\n")
###############################################

  for i in disponible_data:
     for p in i:
      dis_data.append(p)

  for i in dis_data:
    print(str(i)+"\n")
##############################################
  for i in precio_data:
     for p in i:
      pre_data.append(p)

  for i in pre_data:
    print(str(i)+"\n")


  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  print(cursor.fetchall())


  cursor.execute("select * from users")
  x=cursor.fetchall()
  print(x)

  conn.commit()
  conn.close()



get_data()
#create_new_user()
#create_table()


