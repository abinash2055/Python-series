##def openland():
##    file = open("land_files.txt", "r")
##    print(file.read())
##    file.close()
###print(openland())
##
##def d2d():
##    file = open("land_files.txt", "r")
##    l = []
##    for each in file:
##        b = each.replace("\n", "")
##        l.append(b.split(","))
##    return l
##print (d2d())

##def read_land():
##    # Header for the table
##    header = ["Kitta", "City", "Direction", "Anna", "Price", "Availability"]
##    data =[]
##    # Reading data from the file
##    file = open("land_files.txt", "r")
##    for line in file:
##        row = line.strip().split(",")
##        data.append(row)
##    
##    # Call d2d function to display data in tabular form
##    d2d(header, data)
##
##def d2d(header, data):
##    #print("-" * (len("|".join(header))))
##    print("------------------------------------------------------------------------------")
##    # Print the header
##    print("\t".join(header))
##    
##    # Print a separator line
##    #print("-" * (len("|".join(header))))
##    print("------------------------------------------------------------------------------")
##    # Print each row of data
##    for row in data:
##        print("\t".join(row))


def read_land():
    r = True
    while r == True:
        try:
            # Header for the table
            header = ["Kitta", "  City", "   Direction", "Anna", "Price", "Availability"]
            data = []
            # Reading data from the file
            file = open("land_files.txt", "r")
            for line in file:
                row = line.strip().split(",")
                data.append(row)
            
            # Call d2d function to display data in tabular form
            d2d(header, data)
            return data
        
        except FileNotFound:
            print("File not found!")


def d2d(header, data):
    try:
        print("------------------------------------------------------------------------------")
        # Print the header
        print("\t".join(header))
        
        # Print a separator line
        print("------------------------------------------------------------------------------")
        # Print each row of data
        for row in data:
            print("\t".join(row))
    except FileNotFound:
        print("File not found!")


