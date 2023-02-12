import sqlite3
   #create the db
def create():
  try:
    conn = sqlite3.connect("productos.db")
  except Error as e:
    print(e)
  cursor = conn.cursor()


  conn.commit()
  conn.close()


create()
###################################################
  #this is more to create the table the db is created on top
 # cursor.execute("""create table productos(
 # referencia integer,
 # descripcion text,
 # disponible integer,
 # precio integer
 # )"""#)
  #conn.commit()
  #conn.close()

