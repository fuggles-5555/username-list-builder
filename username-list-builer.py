##################################################################
#
# Username List Builder
#
##################################################################

# libraries
import argparse
import os
import shutil
import string


# checks file exists and can be opened
def checkFile(file):
    if os.path.isfile(file):
        if os.access(file, os.R_OK):
            return True
        else:
            print("You do not have permissions to read " + file + "\n")
            return False
    else:
        print("The file " + file + " does not exits\n")
        return False

   
# generate names
def namesGenerator(firstNameFile, lastNameFile):
    # firstname.lastname
    # john.smith
    with open("firstname.lastname.txt", 'w') as outputFile:
        with open(firstNameFile, 'r') as firstfile:
            for firstname in firstfile:
                with open(lastNameFile, 'r') as lastfile:
                    for lastname in lastfile:
                        outputFile.write(firstname.strip() + "." + lastname.strip() + "\n")
    shutil.move("firstname.lastname.txt", "lists")
                        
    # firstname-lastname
    # john-smith
    with open("firstname-lastname.txt", 'w') as outputFile:
        with open(firstNameFile, 'r') as firstfile:
            for firstname in firstfile:
                with open(lastNameFile, 'r') as lastfile:
                    for lastname in lastfile:
                        outputFile.write(firstname.strip() + "-" + lastname.strip() + "\n")
    shutil.move("firstname-lastname.txt", "lists")
    
    # firstname_lastname
    # john_smith
    with open("firstname_lastname.txt", 'w') as outputFile:
        with open(firstNameFile, 'r') as firstfile:
            for firstname in firstfile:
                with open(lastNameFile, 'r') as lastfile:
                    for lastname in lastfile:
                        outputFile.write(firstname.strip() + "_" + lastname.strip() + "\n")
    shutil.move("firstname_lastname.txt", "lists")
    
    # firstinitiallastname
    # jsmith
    with open("firstinitiallastname.txt", 'w') as outputFile:
        with open(firstNameFile, 'r') as firstfile:
            for firstname in firstfile:
                with open(lastNameFile, 'r') as lastfile:
                    for lastname in lastfile:
                        outputFile.write(firstname.strip()[0] + lastname.strip() + "\n")
    shutil.move("firstinitiallastname.txt", "lists")
    
    # firstinitial.lastname
    # j.smith
    with open("firstinitial.lastname.txt", 'w') as outputFile:
        with open(firstNameFile, 'r') as firstfile:
            for firstname in firstfile:
                with open(lastNameFile, 'r') as lastfile:
                    for lastname in lastfile:
                        outputFile.write(firstname.strip()[0] + "." + lastname.strip() + "\n")
    shutil.move("firstinitial.lastname.txt", "lists")
    
    # lastname.firstname
    # smith.john
    with open("lastname.firstname.txt", 'w') as outputFile:
        with open(firstNameFile, 'r') as firstfile:
            for firstname in firstfile:
                with open(lastNameFile, 'r') as lastfile:
                    for lastname in lastfile:
                        outputFile.write(lastname.strip() + "." + firstname.strip() + "\n")
    shutil.move("lastname.firstname.txt", "lists")
    
    # lastname-firstname
    # smith-john
    with open("lastname-firstname.txt", 'w') as outputFile:
        with open(firstNameFile, 'r') as firstfile:
            for firstname in firstfile:
                with open(lastNameFile, 'r') as lastfile:
                    for lastname in lastfile:
                        outputFile.write(lastname.strip() + "-" + firstname.strip() + "\n")
    shutil.move("lastname-firstname.txt", "lists")
    
    # lastname_firstname
    # smith_john
    with open("lastname_firstname.txt", 'w') as outputFile:
        with open(firstNameFile, 'r') as firstfile:
            for firstname in firstfile:
                with open(lastNameFile, 'r') as lastfile:
                    for lastname in lastfile:
                        outputFile.write(lastname.strip() + "_" + firstname.strip() + "\n")
    shutil.move("lastname_firstname.txt", "lists")
    
    # lastnamefirstinitial
    # smithj
    with open("lastnamefirstinitial.txt", 'w') as outputFile:
        with open(firstNameFile, 'r') as firstfile:
            for firstname in firstfile:
                with open(lastNameFile, 'r') as lastfile:
                    for lastname in lastfile:
                        outputFile.write(lastname.strip()[0] + firstname.strip() + "\n")
    shutil.move("lastnamefirstinitial.txt", "lists")
    
    # lastname.firstinitial
    # smith.j
    with open("lastname.firstinitial.txt", 'w') as outputFile:
        with open(firstNameFile, 'r') as firstfile:
            for firstname in firstfile:
                with open(lastNameFile, 'r') as lastfile:
                    for lastname in lastfile:
                        outputFile.write(lastname.strip()[0] + "." + firstname.strip() + "\n")
    shutil.move("lastname.firstinitial.txt", "lists")


# generate services
def servicesGenerator(serviceNamesFile, prefixSuffixFile):
    # create file to write
    with open("servicenames.txt", 'w') as outputFile:
    
        # iterates each service name
        with open(serviceNamesFile, 'r') as service:
            for line in service:
                outputFile.write(line.strip() + "\n")
                with open (prefixSuffixFile, 'r') as preSuffWord:
                    for word in preSuffWord:    
                        outputFile.write(line.strip() + "-" + word.strip() + "\n")
                        outputFile.write(line.strip() + "." + word.strip() + "\n") 
                        outputFile.write(line.strip() + "_" + word.strip() + "\n") 
                        outputFile.write(line.strip() + word.strip() + "\n")
                        outputFile.write(word.strip() + "-" + line.strip() + "\n")
                        outputFile.write(word.strip() + "." + line.strip() + "\n") 
                        outputFile.write(word.strip() + "_" + line.strip() + "\n") 
                        outputFile.write(word.strip() + line.strip() + "\n")
                        
    shutil.move("servicenames.txt", "lists")
    

## generate admins
def adminGenerator():
    with open("adminnames.txt", 'w') as outputFile:
        # admina
        for letter in string.ascii_lowercase:
            outputFile.write("admin" + letter +"\n")
        # adminab
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write("admin" + letter1 + letter2 +"\n")
        # admin.a
        for letter in string.ascii_lowercase:
            outputFile.write("admin" + "." + letter +"\n")
        # admin.ab
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write("admin" + "." + letter1 + letter2 +"\n")
        # admin-a
        for letter in string.ascii_lowercase:
            outputFile.write("admin" + "-" + letter +"\n")
        # admin-ab
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write("admin" + "-" + letter1 + letter2 +"\n")
        # admin_a
        for letter in string.ascii_lowercase:
            outputFile.write("admin" + "_" + letter +"\n")
        # admin_ab
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write("admin" + "_" + letter1 + letter2 +"\n")
  
        # aadmin
        for letter in string.ascii_lowercase:
            outputFile.write(letter + "admin" + "\n")
        # abadmin
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write(letter1 + letter2 + "admin" + "\n")
        # a.admin
        for letter in string.ascii_lowercase:
            outputFile.write(letter + "." + "admin" + "\n")
        # ab.admin
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write(letter1 + letter2 + "." + "admin" + "\n")
        # a-admin
        for letter in string.ascii_lowercase:
            outputFile.write(letter + "-" + "admin" + "\n")
        # ab-admin
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write(letter1 + letter2 + "-" + "admin" + "\n")
        # a_admin
        for letter in string.ascii_lowercase:
            outputFile.write(letter + "_" + "admin" + "\n")
        # ab_admin
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write(letter1 + letter2 + "_" + "admin" + "\n")
                
	# administratora	
        for letter in string.ascii_lowercase:
            outputFile.write("administrator" + letter + "\n")
        # administratorab
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write("administrator" + letter1 + letter2 + "\n")
        # administrator.a
        for letter in string.ascii_lowercase:
            outputFile.write("administrator" + "." + letter + "\n")
        # administrator.ab
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write("administrator" + "." + letter1 + letter2 + "\n")
        # administrator-a
        for letter in string.ascii_lowercase:
            outputFile.write("administrator" + "-" + letter + "\n")
        # administrator-ab
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write("administrator" + "-" + letter1 + letter2 + "\n")
        # administrator_a
        for letter in string.ascii_lowercase:
            outputFile.write("administrator" + "_" + letter + "\n")
        # administrator_ab
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write("administrator" + "_" + letter1 + letter2 + "\n")

        # aadministrator
        for letter in string.ascii_lowercase:
            outputFile.write(letter + "administrator" + "\n")
        # abadministrator
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write(letter1 + letter2 + "administrator" + "\n")
        # a.administrator
        for letter in string.ascii_lowercase:
            outputFile.write(letter + "." + "administrator" + "\n")
        # ab.administrator
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write(letter1 + letter2 + "." + "administrator" + "\n")
        # a-administrator
        for letter in string.ascii_lowercase:
            outputFile.write(letter + "-" + "administrator" + "\n")
        # ab-administrator
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write(letter1 + letter2 + "-" + "administrator" + "\n")
        # a_administrator
        for letter in string.ascii_lowercase:
            outputFile.write(letter + "_" + "administrator" + "\n")
        # ab_administrator
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                outputFile.write(letter1 + letter2 + "_" + "administrator" + "\n")

    shutil.move("adminnames.txt", "lists")


# main
def main():
    # parse arguments
    parser = argparse.ArgumentParser(
        description="A script to build username lists using several seed files.")
    parser.add_argument(
        "-f", "--first", dest="first", type=str, required=True, help="Path to the firstname input file.")
    parser.add_argument(
        "-l", "--last", dest="last", type=str, required=True, help="Path to the lastname input file.")
    parser.add_argument(
        "-s", "--service", dest="service", type=str, required=True, help="Path to the service name input file.")
    parser.add_argument(
        "-p", "--prefixsuffix", dest="prefixsuffix", type=str, required=True, help="Path to the prefix/suffix words input file.")
    args = parser.parse_args()

    # grab argument file handles
    firstNameFile = args.first
    lastNameFile = args.last
    serviceNamesFile = args.service
    prefixSuffixFile = args.prefixsuffix
    
    # check files
    checkFile(firstNameFile)
    checkFile(lastNameFile)
    checkFile(serviceNamesFile)
    checkFile(prefixSuffixFile)

    namesGenerator(firstNameFile, lastNameFile)
    servicesGenerator(serviceNamesFile, prefixSuffixFile)
    adminGenerator()
    

if __name__ == '__main__':
    main()
