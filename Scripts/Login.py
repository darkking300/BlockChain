import FetchDB
import WorkDB
import webbrowser

def login():
    """Used to log into database with provided credentials"""
    try:
        id = input("\t                Id>>>")
        passw = input("\t          Password>>>") #appears as plain text on screen
        dataBase = input("\t     Database Name>>>") #naame of database in system
        return FetchDB.connection(id, passw, dataBase)

    except Exception as e:
        print("Error during Login:")
        print("Incorrect details.")
        print("Closing program.")


def printAll(cursor,table):
    """Used to bridge Begin.py to FetchDB.py without importing latter in first"""
    FetchDB.seeEntire(cursor,table)


def table_operate():
        """opens the table on which work is to be done"""
        print("Enter the name of table in the database ")
        tableName = input("\t     Table Name>>>")
        return tableName


def openTxt():
    """opens the help file"""
    webbrowser.open("Help.txt")


def die(db):
    """ closes the connection do database"""
    try:
        Threads.close(db)
    except:
        print("Closing program")
        exit(0)



def ensure(db,cursor,table):
    """important as it permanently alters database in a system.
    Performs check to ensure that user is serious.
    Well as serious they can be."""

    print("Warning!!!!")
    print("This process is irreversible and will alter the entire table in provided database.")
    print("Press Y to continue or N to stop")
    choice = input(">>>")
    if 'n' in choice or 'N' in choice:
        exit("Execution stop requested")
    else:
         WorkDB.updateTable(db,cursor,table)