import MySQLdb as sql

def connection(id,passw,database):
    """connect to database"""
    db = sql.connect("localhost",str(id),str(passw),str(database))
    cursor = db.cursor()
    return db,cursor

def getData(cursorData,table):
    """get the entire data plus field data from columnNames"""
    command = "SELECT * FROM %s"%(str(table))
    cursorData.execute(command)
    data = cursorData.fetchall()
    return data

def columnNames(cursorData,table):
    """finds the name of fields in the table"""
    command = "desc %s"% (str(table))
    cursorData.execute(command)
    results = cursorData.fetchall()
    fieldValues = []
    for info in results:
        #the field names are the first elements
        #and we get first one in each row of the description
        fieldValues.append(info[0])
    return fieldValues

def seeEntire(cursorData,table):
    """Display enitre data of the blockchain."""
    command = "SELECT * FROM %s;"%(str(table))
    cursorData.execute(command)
    dataBase = cursorData.fetchall()
    columns = columnNames(cursorData,table)
    try:
        for info in dataBase:
            for dataSet in info:
                turn = columns[info.index(dataSet)]
                print("%s:%s"%(turn,dataSet))
            print("\n\n")
    except Exception as e:
        print("Error:",e)