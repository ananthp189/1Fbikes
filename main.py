import datetime

class Bike:
    # initialize bike
    # NO represent bike number
    # age represent life time of bike
    # state represent the statement of bike
    # 0 means idle, 1 means occupied


    def __init__(self, NO, age , name = "" , phone = "" , time = "",state = 0):
        self.NO = NO
        self.age = age
        self.state = state
        self.name = name 
        self.phone = phone
        self.time = time

    def __str__(self):
        if self.state == 0:
            status = "idle"
            result = f"Bike NO:{self.NO} has running for {self.age} years, bike statement is {status}"
        else:
            result = f"Bike NO:{self.NO} occupied by {self.name} phone number {self.phone} at {self.time}"

        return result





class Manage:

    # creat a list to store all bike information
    bike_list = []


    def __init__(self):
        bike_A = Bike(1, 2)
        bike_B = Bike(2, 2)
        bike_C = Bike(3, 1)
        bike_D = Bike(4, 3)
        bike_E = Bike(5, 1)
        self.bike_list.append(bike_A)
        self.bike_list.append(bike_B)
        self.bike_list.append(bike_C)
        self.bike_list.append(bike_D)
        self.bike_list.append(bike_E)


    # system menu
    def menu(self):
        print("Welcome to the Bike Share System")
        print("1) Display bike info" + '\n'
              "2) Add a new bike" + '\n'
              "3) Rent a bike" + '\n'
              "4) Return a bike" + '\n'
              "5) Quit the system")
        select = input("Enter a number: ")

        while select != "5":
            if select == "1":
                self.info_bike()
            elif select == "2":
                self.add_bike()
            elif select == "3":
                self.lease_bike()
            elif select == "4":
                self.revert_bike()
            print("1) Display bike info" + '\n'
              "2) Add a new bike" + '\n'
              "3) Rent a bike" + '\n'
              "4) Return a bike" + '\n'
              "5) Quit the system")
            select = input("Enter a number: ")
        else:
            print("Enjoy your Low-Carbon life")



    # bike info
    def info_bike(self):
        for bike in self.bike_list:
            print(bike)
    

    # add new bike
    def add_bike(self):
        new_NO = int(input("Enter the bike number:"))
        new_age = int(input("Enter the bike lifetime:"))
        new_bike = Bike(new_NO, new_age)
        self.bike_list.append(new_bike)
        print("Successful added")


    # search bike info in the list
    def select_bike(self,NO):
        for bike in self.bike_list:
            if bike.NO == NO:
                return bike

    
    # lease bike
    def lease_bike(self):
        lease_NO = int(input("Please enter the number of the bike you lease:"))
        result = self.select_bike(lease_NO)
        name = input("Enter name :")
        phone = input("Enter the phone number :")
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        if result != None:
            if result.state == 1:
                print("Sorry, this bike has been borrowed")
            else:
                result.name = name
                result.phone = phone
                result.time = time
                print("Successful loan")
                result.state = 1
        else:
            print("invalid number")

    
    # return bike
    def revert_bike(self):
        revert_NO = int(input("Please enter the number of the bike you revert:"))
        result = self.select_bike(revert_NO)
        if result != None:
            if result.state == 1:
                print("Successful revert")
                result.state = 0
            else:
                print("This bike is idle")
        else:
            print("invalid number")


user = Manage()
print(user)
user.menu()




