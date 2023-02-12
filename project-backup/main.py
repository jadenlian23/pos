from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.core.window import Window
import sqlite3
from kivy.uix.screenmanager import ScreenManager,Screen


class Log_in(Screen):
  pass


class Users(Screen):
  pass

class Create_Users(Screen):
  val=StringProperty('') 
  def checkbox_click(self,instance,value):
    if(value==True):      
      print(value)


class Inventory(Screen):
  pass



class Main_screen(Screen):
  pass





class Caja(Screen):
  referencia=StringProperty('')
  descripcion=StringProperty('')
  disponible=StringProperty('')
  precio=StringProperty('')
  ref=StringProperty('')

  def print_all_products(self):
    #to get the data from the database
    conn = sqlite3.connect("productos.db")
    cursor = conn.cursor()
    ref_data=[]
    des_data=[]
    dis_data=[]
    pre_data=[]
    #cursor.execute("select * from productos")
    #getting the data
    _referencia=cursor.execute("select referencia from productos")
    referencia_data=_referencia.fetchall()

    _descripcion=cursor.execute("select descripcion from productos")
    descripcion_data=_descripcion.fetchall()

    _disponible=cursor.execute("select disponible from productos")
    disponible_data=_disponible.fetchall()

    _precio=cursor.execute("select precio from productos")
    precio_data=_precio.fetchall()


    for i in referencia_data:
      for p in i:
        ref_data.append(p)

    for i in ref_data:
      #print(str(i)+"\n")
      self.referencia+=str(i)+"\n"
######################################
    for i in descripcion_data:
      for p in i:
        des_data.append(p)

    for i in des_data:
      #print(i+"\n")
      self.descripcion+=i+"\n"

###############################################

    for i in disponible_data:
      for p in i:
         dis_data.append(p)

    for i in dis_data:
      #print(str(i)+"\n")
      self.disponible+=str(i)+"\n"

##############################################
    for i in precio_data:
      for p in i:
        pre_data.append(p)

    for i in pre_data:
      #print(str(i)+"\n")
      self.precio+=str(i)+"\n"


    conn.commit()
    conn.close()







  def products(self,widget):
    #to get the data from the database
    conn = sqlite3.connect("productos.db")
    cursor = conn.cursor()
    x=''
    des_data=[]
    #cursor.execute("select * from productos")
    #getting the data
    _descripcion=cursor.execute("select descripcion from productos")
    descripcion_data=_descripcion.fetchall()

    for i in descripcion_data:
      for p in i:
        des_data.append(p)

    for i in des_data:
      if(widget.text in i):
        self.descripcion=""
        self.descripcion= i
        print(self.descripcion + "\n")
      else:
        self.descripcion=""
    conn.commit()
    conn.close()



  #window manager
class Manager(ScreenManager):
  pass




class posapp(App):
  title="POS"
  Window.clearcolor=(.2,.4,.2,1)

  pass



posapp().run()
