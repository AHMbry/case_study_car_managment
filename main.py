from functions import *
linked_list = LinkedList()
def main():
    while True:
        print("\n1. Start the program (Read from file)")
        print()
        print("2. Print the linked list")
        print()
        print("3. Insert a new vehicle")
        print()
        print("4. Update vehicle information")
        print()
        print("5. Remove a vehicle")
        print()
        print("6. Search for a vehicle")
        print()
        print("7. Quit (Write to file)")
        choice = input("Enter your choice: ")

        if choice=="1":
            filename=input("file path/name")
            read_from_file(filename, linked_list)

        elif choice=="2":
            linked_list.print_list()

        elif choice=="3":
            ID=int(input("enter the Id"))
            brand=input("enter the brand name")
            model=input("enter the vehicule model")
            year=int(input("enter The manufacture year of the vehicule"))
            price=float(input("Price of the vehicule"))
            mileage=float(input("enter tha mileage of the car"))
            linked_list.insertsorted(ID, brand, model, year, price, mileage)

        elif choice=="4":
            id = int(input("Enter ID of the vehicle to update: "))
            brand = input("Enter new Brand (leave blank to keep current): ")
            model = input("Enter new Model (leave blank to keep current): ")
            year = input("Enter new Year (leave blank to keep current): ")
            price = input("Enter new Price (leave blank to keep current): ")
            mileage = input("Enter new Mileage (leave blank to keep current): ")

            year = int(year) if year else None
            price = float(price) if price else None
            mileage = int(mileage) if mileage else None
            linked_list.update_info(id,brand,model,year,price,mileage)

        elif choice=="5":
            ID=int(input("enter the Id of the car to remove"))
            linked_list.remove_by_Id(ID)
            
        elif choice=="6":
            M=input("search by /ID/ or by /Brand/ or by /Model/")
            if M.lower()=="id":
                ID=int(input("enter the Id"))
                linked_list.search_by_ID(ID)
            elif M.lower()=="brand":
                brand=input("enter the brand name")
                linked_list.search_by_brand(brand)
            elif M.lower()=="model":
                model=input("enter the vehicule model")
                linked_list.search_by_model(model)
            else:
                print("invalid input you dumass**")
                
        elif choice=="7":
            filename=input('enter the file name/path')
            write_in_newfile(filename,linked_list)
            break

main()

        
    