class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} - Price: ${self.price}"

    def update_brand(self, brand):
        self.brand = brand

    def update_model(self, model):
        self.model = model

    def update_price(self, price):
        self.price = price

    def delete_brand(self):
        self.brand = None

    def delete_model(self):
        self.model = None

    def delete_price(self):
        self.price = None


def main_menu():
    print("Phone Management System")
    print("1. Create Phone")
    print("2. Modify Phone")
    print("3. Delete Phone")
    print("4. List Phones")
    print("5. Exit")


def create_phone():
    brand = input("Enter phone brand: ")
    model = input("Enter phone model: ")
    price = float(input("Enter phone price: "))
    return Phone(brand, model, price)


def modify_phone(phone):
    print("1. Update Brand")
    print("2. Update Model")
    print("3. Update Price")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        phone.update_brand(input("Enter new brand: "))
    elif choice == 2:
        phone.update_model(input("Enter new model: "))
    elif choice == 3:
        phone.update_price(float(input("Enter new price: ")))


def delete_phone(phone):
    print("1. Delete Brand")
    print("2. Delete Model")
    print("3. Delete Price")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        phone.delete_brand()
    elif choice == 2:
        phone.delete_model()
    elif choice == 3:
        phone.delete_price()


def list_phones(phones):
    for i in range(len(phones)):
        print(f"{i+1}. {phones[i]}")

def main():
    phones = []
    while True:
        main_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            phones.append(create_phone())
        elif choice == 2:
            if phones:
                print("Select a phone to modify:")
                for i in range(len(phones)):
                    print(f"{i+1}. {phones[i]}")
                choice = int(input("Enter your choice: "))
                modify_phone(phones[choice-1])
            else:
                print("No phones to modify.")
        elif choice == 3:
            if phones:
                print("Select a phone to delete:")
                for i in range(len(phones)):
                    print(f"{i+1}. {phones[i]}")
                choice = int(input("Enter your choice: "))
                del phones[choice-1]
            else:
                print("No phones to delete.")
        elif choice == 4:
            if phones:
                list_phones(phones)
            else:
                print("No phones to list.")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()