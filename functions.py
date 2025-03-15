class node:
    def __init__(self,ID,brand,model,year,price,mileage):
        self.ID=ID
        self.brand=brand
        self.model=model
        self.year=year
        self.price=price
        self.mileage=mileage

class LinkedList:
    def __init__(self):
        self.next=None
    
    def append_byorder(self, ID, brand, model, year, price, mileage):
        new_node=node(ID,brand,model,year,price,mileage)
        if not self.head or year<self.head.year or (year==self.head.year and price<self.head.price):
            new_node.next=self.head
            self.head=new_node
            return
        
        current=self.head
        while(current.next and (current.next.year < year or (current.next.year == year and current.next.price < price))):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current=self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(f"Id:{self.ID}/brand:{self.brand}/model:{self.model}/price:{self.price}/mileage:{self.mileage}")
            current=current.next


    def insert(self,ID, brand, model, year, price, mileage):
        new_node=node(ID, brand, model, year, price, mileage)
        if not self.head or year < self.head.yead or (year==self.head.year and price < self.head.price):
            new_node.next=self.head
            self.head=new_node
            return
        current=self.head
        while current and current.next.year :
            pass
    
    def romove_by_Id(self,Target):
        current=self.head
        previous=None
        while current:
            if current.ID ==Target:
                if previous==None:
                    self.head = current.next
                else:
                    previous.next=current.next
                    current.next=None
                return
            previous=current
            current=current.next
        print(f"car with ID {Target} Not Fount")

    def search_by_ID(self,Target):
        current=self.head
        while current:
            if current.ID==Target:
                return f"Id:{self.ID}/brand:{self.brand}/model:{self.model}/price:{self.price}/mileage:{self.mileage}"
            current=current.next
        return None
    def search_by_brand(self,Target):
        results = []
        current=self.head
        while current:
            if current.brand==Target:
                results.append(current)
            current=current.next
        return results
    




def read_from_file(filename, linked_list):
    with open (filename,'r') as f:
            for line in f:
                line=line.split(',')
                line[5]=line[5][:-1]
                id = int(line[0].strip())
                brand = line[1].strip()
                model = line[2].strip()
                year = int(line[3].strip())
                price = float(line[4].strip())
                mileage = int(line[5].strip())

                # Insert the vehicle into the linked list in sorted order
                linked_list.append_byorder(id, brand, model, year, price, mileage)


