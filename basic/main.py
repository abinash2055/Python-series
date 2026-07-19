##print("\t\t\t\tName of company")
##print("\n\t\tKamalpokhari, Kathmandu | Phone: 9851215870")
##print("\n.............................................................................")
##print("\twelcome to the system Admin. I hope you have a good day!")
##print(".............................................................................")
##print("\n.............................................................................")
##print("  Given below are options for you to carryout the operations in the system.")
##print(".............................................................................")
##print("\nPress 1: To rent the land to customer.")
##print("Press 2: To return the land from customer.")
##print("Press 3: To exit from the system.")
##
##print("\n.............................................................................")
##print(".............................................................................")
##
##press = int(input("\nEnter the option to continue: "))
##if press == 1:
##    print("hello")
##elif press == 2:
##    print("hi")
##elif press == 3:
##    print("namaste")
##else:
##    print("please choose the option properly!")
##

from read import *
from write import *
from operation import *
def main_gui():
        print("\t\t\tTechno Property Nepal")
        print("\n\t\tKamalpokhari, Kathmandu | Phone: 9851215870")
        print("\n------------------------------------------------------------------------------")
        print("\twelcome to the system Admin. I hope you have a good day!")
        print("------------------------------------------------------------------------------")
        print("\n------------------------------------------------------------------------------")
        print("  Given below are options for you to carryout the operations in the system.")
        print("------------------------------------------------------------------------------")
        print("\nPress 1: To see the land")
        print("Press 2: To rent the land to customer.")
        print("Press 3: To return the land from customer.")
        print("Press 4: To exit from the system.")
        print("\n------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
main_gui()


def main_final():
    z = True
    while z == True:
        
        try:        
            press = int(input("\nEnter the option to continue: "))

            if press == 1:
                try:                
                    land_data = read_land()  # Print the land data
                    print("------------------------------------------------------------------------------")
                    print("------------------------------------------------------------------------------")
                    return main_final()
                except Exception as e:
                    print("Error: ", e)
            elif press == 2:
                try:
                    land_data = read_land()  # Read land data
                    operation_rent(land_data)
                    while True:
                        cont = input("Do you continue to rent the land. (yes/no): ")
                        if cont.lower() == "yes":
                            operation_rent(land_data)
                        else:
                            return main_final()
                    
                except Exception as e:
                    print("Error: ", e)
            elif press == 3:
                try:
                    land_data = read_land()  # Read land data
                    operation_return(land_data)
                    while True:
                        contd = input("Do you continue to return the land. (yes/no): ")
                        if contd.lower() == "yes":
                            operation_return(land_data)
                        else:
                            return main_final()
                except Exception as e:
                    print("Error: ", e)
            elif press == 4:
                print("------------------------------------------------------------------------------")
                print("Exiting from the system. Please visit us again!")
                print("------------------------------------------------------------------------------")
                break
            else:
                print("Invalid option. Please choose again.")
        except ValueError:
            print("Invalid Input!")
            return main_final()


main_final()
