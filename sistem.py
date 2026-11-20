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
def min_max_product():
    products = load_product()

    if not products:
        print("Product yoxdur!")
        return

    cheap = min(products, key=get_price)
    expensive = max(products, key=get_price)

    print("En ucuz mehsul:", cheap)
    print("En baha mehsul:", expensive)

def app():
 while True:
            print('''
        ================================
            MINI PRODUCT SYSTEM
        ================================

        1.Bütün məhsullari göstər
        2.Sort et
        3.Search et
        4.Baha ucuz

            0. Proqramdan çix

        ================================



        ''')
            choice=int(input("Enter choice:"))
            if choice==1:
             show_product()

            elif choice==2:
             sort_product()

            elif choice==3:
                search_product()

            elif choice==4:
                min_max_product()

            elif choice==5:
             print("Exit...")
             break

            else:
                print("404")
                continue