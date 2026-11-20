from storage import*
import json
def show_product():
   show=load_product()
   try:
      return show
   except:
      print("404")
