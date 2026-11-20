import json

DATA_FILE="product.json"

def load_product():
    try:
      with open(DATA_FILE,"r",encoding="utf-8") as file:
         products=json.load(file)
    except FileNotFoundError:
         return []
    except json.JSONDecodeError:
        raise ValueError("JSON file is corrupted")
def save_product(products):
      with open(DATA_FILE,"w",encoding="utf-8") as file:
         json.dump(products,file,indent=4,ensure_ascii=False)