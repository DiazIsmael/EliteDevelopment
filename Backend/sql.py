import mysql.connector
from mysql.connector import Error
from credentials import Creds
myCreds = Creds()
auth = {'auth': False, 'authUser': myCreds.authUser, 'authPass': myCreds.authPass}

def createConnection(hostname, username, password, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            passwd = password,
            database = dbname
        )
        print("Successfully connected to MySQL Database!")
    except Error as e:
        print(f"The error '{e}' occurred :(")
    
    return connection

def executeReadQuery(query):
    connection = createConnection(myCreds.conString, myCreds.username, myCreds.password, myCreds.dbname)
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred :(")
    finally:
        cursor.close()
        connection.close()

def executeQuery(query):
    connection = createConnection(myCreds.conString, myCreds.username, myCreds.password, myCreds.dbname)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        return ("Query successfully executed!")
    except Error as e:
        return f"(The error '{e}' has occurred :("
    finally:
        cursor.close()
        connection.close()