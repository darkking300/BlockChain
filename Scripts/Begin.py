import Login
import WorkDB

print("Welcome to Blockchain encoder.")
print("Enter the details of the DBMS you want to edit"),
print("and it's credential data")


db,cursor = Login.login()          #although it is not logical to do so much returns
table_name = Login.table_operate()     #it is done so that programs can be as modular as possible



while True:
    #runs indefinitely until stated otherwise
    print("Select any one of following operations")
    print("1.Encode all data into hashes and form blockchain.")
    print("2.See all the data presently in the blockchain database.")
    print("3.Read the extended help file attached with program.")
    print("4.Exit the program")

    choice = int(input(">>>"))

    if choice == 1:
        Login.ensure(db,cursor,table_name)
    elif choice == 2:
        #to see all files
        print("The content of Blockchain as shown....")
        Login.printAll(cursor,table_name)
    elif choice == 3 :
        Login.openTxt()
    elif choice == 4:
        Login.die(db)
    else:
        print("Invalid entry.")
        print("Enter any value from 1-3")

