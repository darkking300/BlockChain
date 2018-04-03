import Hashing
import FetchDB
import Login

def alterTable(thatCursor,table):
    """add the hash column in databaseto store the sha256 hesh as a data"""
    columns = FetchDB.columnNames(thatCursor,table)
    thisLine = ' '.join(columns)

    if "HASH" not in thisLine:
        command = "ALTER TABLE %s ADD HASH char(64);"%(str(table),)
        thatCursor.execute(command)


def updateTable(db,thisCursor,table):
    """Update each row of the table on go with each data bit"""
    alterTable(thisCursor, table)

    entireDB = FetchDB.getData(thisCursor, table)
    fields = FetchDB.columnNames(thisCursor, table)
    check = entireDB[fields.index("HASH")]
    position = fields.index("HASH")
    thisData = entireDB[0]
    check = thisData[position]
    print("check:",check)         #progam runs only if the first row has empty hash column
                                  #it is assumed that if first one empty all are empty
    if 'None' in str(check):
        blocks = []
        blocks.append(Hashing.genesisBlock())
        index = 0

        try:
            for info in entireDB:
                previous_block = blocks[index]
                datEncode = blockEncoder(info,fields)
                nextBlock = Hashing.nextBlocks(previous_block,datEncode)
                blocks.append(nextBlock)
                #assuming there is atleast two columns in the database and that no to rows have common
                #data in two different columns
                #order: table,hash,first col , first data,second col,second data
                command = "UPDATE %s set HASH = \'%s\' where %s = %r ;"%(table,blocks[index].hex,
                        str(fields[0]) , info[0] )
                thisCursor.execute(command)
                db.commit()
                index = index + 1
            print("Process completed!")
        except Exception as e:
            print("Shitstorm alert:",e)
            db.rollback()
            Login.die(db)

    else:
        print("Database already converted to BlockChain.")
        print("Press Y to view dataset")
        opt = input("\ty \ n>>>")
        if 'y' or 'Y' in opt:
            FetchDB.seeEntire(thisCursor,table)

def blockEncoder(info,columns):
    """Arranges the data segments before creating block"""
    strips = ""
    for i in info:
            if info.index(i) == 0:
                strips = str(columns[info.index(i)]) + ":" + str(i)
                # strips = strips + ","
            else:
                lines = str(columns[info.index(i)]) + ":" + str(i)
                strips = strips + "," + lines
    return strips