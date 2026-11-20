from storage import*
import json
def show_product():
   show=load_product()
   try:
      return show
   except:
      print("404")

def get_price(product):
    return product["price"]


def sort_product():
    products = load_product()

    print('''
    1. High>
    2. Low<
    3. Back
    ''')

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            sorted_products = sorted(products, key=get_price, reverse=False)

        elif choice == 2:
            sorted_products = sorted(products, key=get_price, reverse=True)

        elif choice == 3:
            return

        else:
            print("Wrong choice!")
            return

        for item in sorted_products:
            print(f"ID: {item['id']} | Name: {item['name']} | Price: {item['price']}")

    except ValueError:
        print("404")
def search_product():
    products = load_product()

    print("""
    1. Search by ID
    2. Search by Name
    3. Back
    """)

    try:
        choice = int(input("Enter coice: "))

        if choice == 1:
            Id = int(input("Enter ID: "))

            for product in products:
                if product["id"] == Id:
                    print(product)
                    return

            print("Product not found!")

        elif choice == 2:
            name = input("Enter name: ")

            for product in products:
                if product["name"].lower() == name.lower():
                    print(product)
                    return

            print("Product not found!")

        elif choice == 3:
            return

        else:
            print("Wrong choice!")

    except ValueError:
        print("Invalid input!")