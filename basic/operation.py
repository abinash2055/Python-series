##import datetime
##import read
##
##def read_land():
##    # Header for the table
##    header = ["Kitta", "  City", "   Direction", "Anna", "Price", "Availability"]
##    data = []
##    # Reading data from the file
##    file = open("land_files.txt", "r")
##    for line in file:
##        row = line.strip().split(",")
##        data.append(row)
##    
##    # Call d2d function to display data in tabular form
##    d2d(header, data)
##    #print(data)
##    return data
##    
##
##def d2d(header, data):
##    print("------------------------------------------------------------------------------")
##    # Print the header
##    print("\t".join(header))
##    
##    # Print a separator line
##    print("------------------------------------------------------------------------------")
##    # Print each row of data
##    for row in data:
##        print("\t".join(row))
##
##
##
##def operation_rent(data):
##    y = True
##    while y == True:
##        try:
##            print("------------------------------------------------------------------------------")
##            print("------------------------------------------------------------------------------")
##            kitta_num = input("Enter the kitta number: ")
##            rent_duration = int(input("Enter the rent duration (in months): "))
##            
##            customer_data = {'name':input("Enter your name: "),
##                             'phone':input("Enter your phone number: "),
##                             'address':input("Enter your address: ")}
##            
##            for row in data:
##                if row[0] == kitta_num:
##                    if row[-1].strip().lower() == "available":
##                        anna = int(row[3])
##                        price = int(row[4])
##                        total_price = (anna * price) * rent_duration
##                        print("Land rented successfully. Your invoice has been generated.")
##                        print("------------------------------------------------------------------------------")
##                        print("------------------------------------------------------------------------------")
##                        #return rent_invoice()
##                        row[-1] ="Not Available"
##                        #generate_invoice(row, customer_data, rent_duration, total_price)
##                        rent_invoice(row, customer_data['name'], customer_data['phone'], customer_data['address'], rent_duration, total_price)
##                        return
##                    else:
##                        print("The land is not available for rent.")
##                        break
##            else:
##                print("Invalid Kitta number!")
##
##            
##        except ValueError:
##            print("Invalid input!")
##
##        retry = input("Do you want to try again. (yes/no): ")
##        if retry.lower() == "no":
##            print("Thank you! please visit us again.")
##            break
##
##def rent_invoice(land_info, customer_name, customer_phone, customer_address, rent_duration, total_price):
##    try:
##        kitta_number = land_info[0]
##        city = land_info[1]
##        direction = land_info[2]
##        anna = int(land_info[3])
##        price = int(land_info[4])
##        invoice_filename = str("rent_invoice_" + customer_name + "_" + kitta_number + ".txt")
##
##        # Open the file in write mode
##        file = open(invoice_filename, "w")
##        file.write("Customer Info:\n")
##        file.write("Customer Name: " + customer_name + "\n")  # Add newline character
##        file.write("Customer address: " + customer_address + "\n")  # Add newline character
##        file.write("Customer phone: " + customer_phone + "\n")  # Add newline character
##        file.write("Land Info:\n")
##        file.write("Kitta Number: " + kitta_number + "\n")
##        file.write("Direction: " + direction + "\n")
##        file.write("District: " + city + "\n")
##        file.write("Aana: " + str(anna) + "\n")  # Correct variable name
##        file.write("Total price: " + str(total_price) + "\n")  # Correct variable name
##        file.write("Date and Time of Rent: " + str(datetime.datetime.now()))
##        
##    except Exception as e:  # Catch all exceptions
##        print("Error Generating Invoice:", e)
##
##        
##def operation_return(data):
##    y = True
##    while y == True:
##        try:
##            print("------------------------------------------------------------------------------")
##            print("------------------------------------------------------------------------------")
##            kitta_num = input("Enter the kitta number of the land to return: ")
##            for row in data:
##                if row[0] == kitta_num:
##                    if row[-1].strip().lower() == "not available":
##                        customer_name = input("Enter your name: ")
##                        customer_phone = input("Enter your phone number: ")
##                        customer_address = input("Enter your address: ")
##                        rent_duration = int(input("Enter the rent duration (in months): "))
##                        anna = int(row[3])
##                        price = int(row[4])
##                        total_price = anna * price * rent_duration
##                        print("Land with " + kitta_num + " kitta number has been returned succesfully. You Invoice has been generated....")
##                        row[-1] = "Available"
##                        return_invoice(row, customer_name, customer_phone, customer_address, rent_duration, total_price)
##                        return
##                    else:
##                        print("Land with " + kitta_num + " kitta number is already available!")
##                        break
##            else:
##                print("Invalid Kitta number!")
##
##        except ValueError:
##            print("Invalid Input!")
##
##    retry = input("Do you want to try again. (yes/no): ")
##    if retry.lower() == "yes":
##        print("Thank you! please visit us again.")
##        operation_return(data)
##
##
##def return_invoice(land_info, customer_name, customer_phone, customer_address, rent_duration, total_price):
##    try:
##        kitta_number = land_info[0]
##        city = land_info[1]
##        direction = land_info[2]
##        anna = int(land_info[3])
##        price = int(land_info[4])
##        invoice_filename = str("return_invoice_" + customer_name + "_" + kitta_number + ".txt")
##
##        # Open the file in write mode
##        file = open(invoice_filename, "w")
##        file.write("Customer Info:\n")
##        file.write("Customer Name: " + customer_name + "\n")  # Add newline character
##        file.write("Customer address: " + customer_address + "\n")  # Add newline character
##        file.write("Customer phone: " + customer_phone + "\n")  # Add newline character
##        file.write("Land Info:\n")
##        file.write("Kitta Number: " + kitta_number + "\n")
##        file.write("Direction: " + direction + "\n")
##        file.write("District: " + city + "\n")
##        file.write("Aana: " + str(anna) + "\n")  # Correct variable name
##        file.write("Price per aana: " + str(price) + "\n")
##        file.write("Rent Details:\n")
##        file.write("Rent Duration: " + str(rent_duration) + "\n")
##        file.write("Total Price: " + str(total_price) + "\n")
##        file.write("Date and Time of Return: " + str(datetime.datetime.now()))
##    
##    except Exception as e:  # Catch all exceptions
##        print("Error Generating Invoice:", e)
##     
##
##land_data = read_land()
### Call operation_rent() to execute
##operation_rent(land_data)
##operation_return(land_data)
##
from write import *
import datetime

def operation_rent(data):
    y = True
    while y == True:
        try:
            print("------------------------------------------------------------------------------")
            print("------------------------------------------------------------------------------")
            kitta_num = input("Enter the kitta number: ")
            rent_duration = int(input("Enter the rent duration (in months): "))
            
            customer_data = {'name':input("Enter your name: "),
                             'phone':input("Enter your phone number: "),
                             'address':input("Enter your address: ")}
            
            for row in data:
                if row[0] == kitta_num:
                    if row[-1].lower() == " available":
                        anna = int(row[3])
                        price = int(row[4])
                        total_price = (anna * price) * rent_duration
                        print("Land rented successfully. Your invoice has been generated.")
                        print("------------------------------------------------------------------------------")
                        print("------------------------------------------------------------------------------")
                        #return rent_invoice()
####                        file = open("land_files.txt", "w")
####                        for line in lines:
####                            if row[-1] in line:
####                                line = line.strip()+ "Not Available\n"
####                            file.write(line)
####                        #file.write.row[-1] ="Not Available"
####                        file.close()
                        #generate_invoice(row, customer_data, rent_duration, total_price)
                        rent_invoice(row, customer_data['name'], customer_data['phone'], customer_data['address'], rent_duration, total_price)
                        return
                    else:
                        print("The land is not available for rent.")
                        break
            else:
                print("Invalid Kitta number!")

            
        except ValueError:
            print("Invalid input!")

        retry = input("Do you want to try again. (yes/no): ")
        if retry.lower() == "no":
            print("Thank you!")
            break

def operation_return(data):
    y = True
    while y == True:
        try:
            print("------------------------------------------------------------------------------")
            print("------------------------------------------------------------------------------")
            kitta_num = input("Enter the kitta number of the land to return: ")
            for row in data:
                if row[0] == kitta_num:
                    if row[-1].lower() == " not available":
                        customer_name = input("Enter your name: ")
                        customer_phone = input("Enter your phone number: ")
                        customer_address = input("Enter your address: ")
                        rent_duration = int(input("Enter the rent duration (in months): "))
                        anna = int(row[3])
                        price = int(row[4])
                        total_price = anna * price * rent_duration
                        print("Land with " + kitta_num + " kitta number has been returned succesfully. You Invoice has been generated....")
                        row[-1] = "Available"
                        return_invoice(row, customer_name, customer_phone, customer_address, rent_duration, total_price)
                        return
                    else:
                        print("Land with " + kitta_num + " kitta number is already available!")
                        break
            else:
                print("Invalid Kitta number!")

        except ValueError:
            print("Invalid Input!")

    retry = input("Do you want to try again. (yes/no): ")
    if retry.lower() == "yes":
        print("Thank you! please visit us again.")
        operation_return(data)



