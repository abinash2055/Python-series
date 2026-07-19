##def write_invoice():
##    file = open("invoice.txt", "w")
##    file.write()
##    file.write("\n")
##    file.close
##    write_invoice()
##print(write_invoice())
##
import datetime

def rent_invoice(land_info, customer_name, customer_phone, customer_address, rent_duration, total_price):
    try:
        kitta_number = land_info[0]
        city = land_info[1]
        direction = land_info[2]
        anna = int(land_info[3])
        price = int(land_info[4])
        invoice_filename = str("rent_invoice_" + customer_name + "_" + kitta_number + ".txt")

        # Open the file in write mode
        file = open(invoice_filename, "w")
        file.write("------------------------------------------------------------------------------")
        file.write("\nCustomer Info:\n")
        file.write("------------------------------------------------------------------------------")
        file.write("\nCustomer Name: " + customer_name + "\n")  # Add newline character
        file.write("Customer address: " + customer_address + "\n")  # Add newline character
        file.write("Customer phone: " + customer_phone + "\n")  # Add newline character
        file.write("------------------------------------------------------------------------------")
        file.write("\nLand Info:\n")
        file.write("------------------------------------------------------------------------------")
        file.write("\nKitta Number: " + kitta_number + "\n")
        file.write("Direction: " + direction + "\n")
        file.write("District: " + city + "\n")
        file.write("Aana: " + str(anna) + "\n")  # Correct variable name
        file.write("Total price: " + str(total_price) + "\n")  # Correct variable name
        file.write("Date and Time of Rent: " + str(datetime.datetime.now()))
        
    except Exception as e:  # Catch all exceptions
        print("Error Generating Invoice:", e)

def return_invoice(land_info, customer_name, customer_phone, customer_address, rent_duration, total_price):
    try:
        kitta_number = land_info[0]
        city = land_info[1]
        direction = land_info[2]
        anna = int(land_info[3])
        price = int(land_info[4])
        invoice_filename = str("return_invoice_" + customer_name + "_" + kitta_number + ".txt")

        # Open the file in write mode
        file = open(invoice_filename, "w")
        file.write("------------------------------------------------------------------------------")
        file.write("\nCustomer Info:\n")
        file.write("------------------------------------------------------------------------------")
        file.write("\nCustomer Name: " + customer_name + "\n")  # Add newline character
        file.write("Customer address: " + customer_address + "\n")  # Add newline character
        file.write("Customer phone: " + customer_phone + "\n")  # Add newline character
        file.write("------------------------------------------------------------------------------")
        file.write("\nLand Info:\n")
        file.write("------------------------------------------------------------------------------")
        file.write("\nKitta Number: " + kitta_number + "\n")
        file.write("Direction: " + direction + "\n")
        file.write("District: " + city + "\n")
        file.write("Aana: " + str(anna) + "\n")  # Correct variable name
        file.write("Price per aana: " + str(price) + "\n")
        file.write("------------------------------------------------------------------------------")
        file.write("\nRent Details:\n")
        file.write("------------------------------------------------------------------------------")
        file.write("\nRent Duration: " + str(rent_duration) + "\n")
        file.write("Total Price: " + str(total_price) + "\n")
        file.write("Date and Time of Return: " + str(datetime.datetime.now()))
    
    except Exception as e:  # Catch all exceptions
        print("Error Generating Invoice:", e)



        
