from ecommerce_project.database import Database
from ecommerce_project.user import UserManager
from ecommerce_project.cart import CartManager

def main():
    db = Database()
    user_manager = UserManager()
    cart_manager = CartManager()
    while True:
        print("\n\nPlease choose: \n")
        print("1. User\n")
        print("2. Product\n")
        print("3. Order\n")
        print("4. Exit\n")
        choose = int(input("Choose: \n\n"))
        match choose:
            case 1:
                while True:
                    print("\n\nPlease choose: \n")
                    print("1. Register\n")
                    print("2. Update user\n")
                    print("3. Show user\n")
                    print("4. Exit\n")
                    choose1 = int(input("Choose: \n\n"))
                    match choose1:
                        case 1: 
                            username = input("Enter username: ")
                            email = input("Enter email: ")
                            user_manager.add_user(username, email)
                            print("\nUser added successfully!")
                        case 2:
                            user_id = input("Enter user id: ")
                            user_name = input("Edit user name: ")
                            user_email = input("Edit user email: ")
                            user = user_manager.update_user(user_id, user_name, user_email)
                            if user:
                                print("\nEdit user successfully!")
                                print(f"name: {user['username']}, email: {user['email']}")
                            else:
                                print("User not found.")
                        case 3: 
                            user_id = input("Enter user id: ")
                            user = user_manager.get_user(user_id)
                            if user:
                                print(f"name: {user['username']}, email: {user['email']}")
                            else:
                                print("User not found.")
                        case 4:
                            print("Exiting...")
                            break
            case 2:
                while True:
                    print("\n\nPlease choose: \n")
                    print("1. Create product\n")
                    print("2. Search product\n")
                    print("3. Show all product\n")
                    print("4. Update product\n")
                    print("5. Delete product\n")
                    print("6. Exit")
                    choose2 = int(input("Choose: \n\n"))
                    match choose2:
                        case 1: 
                            while True:
                                name_product = input("\nEnter name product: ")
                                description_product = input("\nEnter description product: ")
                                price_product = int(input("\nEnter price product: "))
                                stock_product = int(input("\nEnter stock product: "))
                                
                                db.add_product(name_product, description_product, price_product, stock_product)
                                
                                x = input("Do you want to add more? 1. Yes / 2. No: ")
                                if x != '1':
                                    break
                            print("You done! \n\n")
                        case 2: 
                            id_product = int(input("Enter id product: "))
                            products = db.get_product(id_product)
                            if products:
                                print(f"name: {products['name']}, description: {products['description']}, price: {products['price']}, stock: {products['stock']}")
                            else:
                                print("Product not found.")
                        case 3:
                            print("All product: ")
                            db.get_products()
                        case 4: 
                            name_product = input("Enter name product: ")
                            description_product = input("Enter description product: ")
                            price_product = input("Enter price product: ")
                            stock_product = input("Enter stock product: ")
                            db.update_product(name_product, description_product, price_product, stock_product)
                            print("Edit product successfully")
                        case 5: 
                            id_product = input("Enter id product: ")
                            db.delete_product(id_product)
                            print("Delete product successfully")
                        case 6:
                            print("Exiting...")
                            break
            case 3: 
                 while True:
                    print("\n\nPlease choose: \n")
                    print("1. Order\n")
                    print("2. View cart\n")
                    print("3. Exit\n")
                    choose = int(input("Choose: \n\n"))
                    match choose:
                        case 1:
                            id_user = int(input("Moi ban nhap id user"))
                            id_product = int(input("Moi ban nhap id product"))
                            soluong = int(input("Moi ban nhap so luong"))
                            cart_manager.add_to_cart(id_user, id_product, soluong)
                            print("Order successfully")
                        case 2: 
                            id_user = int(input("Moi ban nhap id user"))
                            cart_manager.view_cart(id_user)
                        case 3:
                            print("Exiting...")
                            break
            case 4:
                print("Exiting...")
                break
if __name__ == "__main__":
    main()
