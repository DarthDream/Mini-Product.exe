import json

DATA_FILE="product.json"
def load_product():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            products = json.load(file)
            return products

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        raise ValueError("JSON file is corrupted")