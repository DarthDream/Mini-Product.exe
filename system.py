from storage import *
import json


def show_product():
    products = load_product()

    if not products:
        print("Product yoxdur!")
        return

    for product in products:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: {product['price']}")


def get_price(product):
    return product["price"]


def sort_product():
    products = load_product()

    print('''
    1. High to Low
    2. Low to High
    3. Back
    ''')

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            sorted_products = sorted(products, key=get_price, reverse=True)

        elif choice == 2:
            sorted_products = sorted(products, key=get_price, reverse=False)

        elif choice == 3:
            return

        else:
            print("Wrong choice!")
            return

        for product in sorted_products:
            print(f"ID: {product['id']} | Name: {product['name']} | Price: {product['price']}")

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
        choice = int(input("Enter choice: "))

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

    print("\nEn ucuz mehsul:")
    print(f"ID: {cheap['id']} | Name: {cheap['name']} | Price: {cheap['price']}")

    print("\nEn baha mehsul:")
    print(f"ID: {expensive['id']} | Name: {expensive['name']} | Price: {expensive['price']}")

def app():
    while True:
        print('''
        ================================
            MINI PRODUCT SYSTEM
        ================================

        1. Butun mehsullari goster
        2. Sort et
        3. Search et
        4. En baha ve en ucuz

          0. Proqramdan cix

        ================================
        ''')

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                show_product()

            elif choice == 2:
                sort_product()

            elif choice == 3:
                search_product()

            elif choice == 4:
                min_max_product()

            elif choice == 0:
                print("Exit...")
                break

            else:
                print("Wrong choice!")

        except ValueError:
            print("Invalid input!")
