import flask
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from sql import createConnection
from sql import executeReadQuery
from sql import executeQuery
from credentials import Creds
import hashlib
import datetime


#Initial setup for Flask
app = Flask(__name__) #sets up the application... (somehow)
app.config['DEBUG'] = True

#Initializing MySQL/AWS database connection for APIs
myCreds = Creds()
connection = createConnection(myCreds.conString, myCreds.username, myCreds.password, myCreds.dbname)
auth = {'auth': False, 'authUser': myCreds.authUser, 'authPass': myCreds.authPass}

#home/login API route
@app.route('/api/login', methods=['GET'])
def login():
    username = request.headers['username'] #get the header parameters. request headers are interpreted as dictionaries, so value access is easy and direct
    pw = request.headers['password']

    if username == auth['authUser'] and pw == auth['authPass']:
        auth['auth'] = True
        return "Access Granted! You are cleared to proceed to APIs ^v^"
    else:
        return 'SECURITY ERROR: INVALID CREDENTIALS.'

# START OF WAVE 1 TABLES CRUD API ENDPOINTS #
#Create AccountStatus
@app.route('/api/accountstatus/add', methods=['POST']) 
def addAccountStatus():
    requestData = request.get_json()
    
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO AccountStatus ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read AccountStatus
@app.route('/api/accountstatus/all', methods=['GET'])
def allAccountStatuses():
    AccountStatuses = executeReadQuery(connection, "SELECT * FROM AccountStatus")

    print("Attempting Retrieval: SELECT * AccountStatus")
    return jsonify(AccountStatuses)

#Update AccountStatus
@app.route('/api/accountstatus/update', methods=['PUT'])
def updAccountStatus():
    requestData = request.get_json()
    StatusCode = requestData['StatusCode']
    # remove StatusCode from requestData to build query below
    requestData.pop('StatusCode', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE AccountStatus SET " + ', '.join(queryFields) + f" WHERE StatusCode = {StatusCode}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete AccountStatus
@app.route('/api/accountstatus/delete', methods=['DELETE'])
def delAccountStatus():
    requestData = request.get_json()
    idToDelete = requestData['StatusCode']

    print("Attempting Deletion, Acoount StatusCode: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM AccountStatus WHERE StatusCode = %s" % idToDelete)


#Create ClientStatus
@app.route('/api/clientstatus/add', methods=['POST']) 
def addClientStatus():
    requestData = request.get_json()
    
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO ClientStatus ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read ClientStatus
@app.route('/api/clientstatus/all', methods=['GET'])
def allClientStatuses():
    ClientStatuses = executeReadQuery(connection, "SELECT * FROM ClientStatus")

    print("Attempting Retrieval: SELECT * ClientStatus")
    return jsonify(ClientStatuses)

#Update ClientStatus
@app.route('/api/clientstatus/update', methods=['PUT'])
def updClientStatus():
    requestData = request.get_json()
    StatusCode = requestData['StatusCode']
    # remove StatusCode from requestData to build query below
    requestData.pop('StatusCode', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE ClientStatus SET " + ', '.join(queryFields) + f" WHERE StatusCode = {StatusCode}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete ClientStatus
@app.route('/api/clientstatus/delete', methods=['DELETE'])
def delClientStatus():
    requestData = request.get_json()
    idToDelete = requestData['StatusCode']

    print("Attempting Deletion, Client StatusCode: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM ClientStatus WHERE StatusCode = %s" % idToDelete)


#Create ClientType
@app.route('/api/clienttype/add', methods=['POST']) 
def addClientType():
    requestData = request.get_json()
    
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO ClientType ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read ClientType
@app.route('/api/clienttype/all', methods=['GET'])
def allClientTypes():
    ClientTypes = executeReadQuery(connection, "SELECT * FROM ClientType")

    print("Attempting Retrieval: SELECT * ClientType")
    return jsonify(ClientTypes)

#Update ClientType
@app.route('/api/clienttype/update', methods=['PUT'])
def updClientType():
    requestData = request.get_json()
    StatusCode = requestData['ClientCode']
    # remove StatusCode from requestData to build query below
    requestData.pop('ClientCode', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE ClientType SET " + ', '.join(queryFields) + f" WHERE ClientCode = {StatusCode}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete ClientType
@app.route('/api/clienttype/delete', methods=['DELETE'])
def delClientType():
    requestData = request.get_json()
    idToDelete = requestData['ClientCode']

    print("Attempting Deletion, ClientType ClientCode: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM ClientType WHERE ClientCode = %s" % idToDelete)


#Create EmployeeStatus
@app.route('/api/employeestatus/add', methods=['POST']) 
def addEmployeeStatus():
    requestData = request.get_json()
    
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO EmployeeStatus ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read EmployeeStatus
@app.route('/api/employeestatus/all', methods=['GET'])
def allEmployeeStatuses():
    EmployeeStatuses = executeReadQuery(connection, "SELECT * FROM EmployeeStatus")

    print("Attempting Retrieval: SELECT * EmployeeStatus")
    return jsonify(EmployeeStatuses)

#Update EmployeeStatus
@app.route('/api/employeestatus/update', methods=['PUT'])
def updEmployeeStatus():
    requestData = request.get_json()
    StatusCode = requestData['StatusCode']
    # remove StatusCode from requestData to build query below
    requestData.pop('StatusCode', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE EmployeeStatus SET " + ', '.join(queryFields) + f" WHERE StatusCode = {StatusCode}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete EmployeeStatus
@app.route('/api/employeestatus/delete', methods=['DELETE'])
def delEmployeeStatus():
    requestData = request.get_json()
    idToDelete = requestData['StatusCode']

    print("Attempting Deletion, Client StatusCode: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM EmployeeStatus WHERE StatusCode = %s" % idToDelete)


#Create IncidentStatus
@app.route('/api/incidentstatus/add', methods=['POST']) 
def addIncidentStatus():
    requestData = request.get_json()
    
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO IncidentStatus ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read IncidentStatus
@app.route('/api/incidentstatus/all', methods=['GET'])
def allIncidentStatuses():
    IncidentStatuses = executeReadQuery(connection, "SELECT * FROM IncidentStatus")

    print("Attempting Retrieval: SELECT * IncidentStatus")
    return jsonify(IncidentStatuses)

#Update IncidentStatus
@app.route('/api/incidentstatus/update', methods=['PUT'])
def updIncidentStatus():
    requestData = request.get_json()
    StatusCode = requestData['StatusCode']
    # remove StatusCode from requestData to build query below
    requestData.pop('StatusCode', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE IncidentStatus SET " + ', '.join(queryFields) + f" WHERE StatusCode = {StatusCode}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete IncidentStatus
@app.route('/api/incidentstatus/delete', methods=['DELETE'])
def delIncidentStatus():
    requestData = request.get_json()
    idToDelete = requestData['StatusCode']

    print("Attempting Deletion, Client StatusCode: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM IncidentStatus WHERE StatusCode = %s" % idToDelete)


#Create InvoiceStatus
@app.route('/api/invoicestatus/add', methods=['POST']) 
def addInvoiceStatus():
    requestData = request.get_json()
    
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO InvoiceStatus ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read InvoiceStatus
@app.route('/api/invoicestatus/all', methods=['GET'])
def allInvoiceStatuses():
    InvoiceStatuses = executeReadQuery(connection, "SELECT * FROM InvoiceStatus")

    print("Attempting Retrieval: SELECT * InvoiceStatus")
    return jsonify(InvoiceStatuses)

#Update InvoiceStatus
@app.route('/api/invoicestatus/update', methods=['PUT'])
def updInvoiceStatus():
    requestData = request.get_json()
    StatusCode = requestData['StatusCode']
    # remove StatusCode from requestData to build query below
    requestData.pop('StatusCode', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE InvoiceStatus SET " + ', '.join(queryFields) + f" WHERE StatusCode = {StatusCode}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete InvoiceStatus
@app.route('/api/invoicestatus/delete', methods=['DELETE'])
def delInvoiceStatus():
    requestData = request.get_json()
    idToDelete = requestData['StatusCode']

    print("Attempting Deletion, Client StatusCode: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM InvoiceStatus WHERE StatusCode = %s" % idToDelete)


# START OF WAVE 2 TABLES CRUD API ENDPOINTS #
#Create Employee
@app.route('/api/employee/add', methods=['POST']) 
def addEmployee():
    requestData = request.get_json()
    
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO Employee ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read Employee
@app.route('/api/employee/all', methods=['GET'])
def allEmployees():
    Employees = executeReadQuery(connection, "SELECT * FROM Employee")

    print("Attempting Retrieval: SELECT * Employee")
    return jsonify(Employees)

#Update Employee
@app.route('/api/employee/update', methods=['PUT'])
def updEmployee():
    requestData = request.get_json()
    EmployeeID = requestData['EmployeeID']
    # remove employeeID from requestData to build query below
    requestData.pop('EmployeeID', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE Employee SET " + ', '.join(queryFields) + f" WHERE EmployeeID = {EmployeeID}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete Employee
@app.route('/api/employee/delete', methods=['DELETE'])
def delEmployee():
    requestData = request.get_json()
    idToDelete = requestData['EmployeeID']

    print("Attempting Deletion, EmployeeID: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM Employee WHERE EmployeeID = %s" % idToDelete)


#Create Client
@app.route('/api/client/add', methods=['POST']) 
def addClient():
    requestData = request.get_json()
   
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO Client ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read Client
@app.route('/api/client/all', methods=['GET'])
def allClients():
    Clients = executeReadQuery(connection, "SELECT * FROM Client")

    print("Attempting Retrieval: SELECT * Client")
    return jsonify(Clients)

#Update Client
@app.route('/api/client/update', methods=['PUT'])
def updClient():
    requestData = request.get_json()
    ClientID = requestData['ClientID']
    # remove clientID from requestData to build query below
    requestData.pop('ClientID', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE Client SET " + ', '.join(queryFields) + f" WHERE ClientID = {ClientID}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete Client
@app.route('/api/client/delete', methods=['DELETE'])
def delClient():
    requestData = request.get_json()
    idToDelete = requestData['ClientID']

    print("Attempting Deletion, ClientID: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM Client WHERE ClientID = %s" % idToDelete)


#Create Service
@app.route('/api/service/add', methods=['POST']) 
def addService():
    requestData = request.get_json()
   
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO Service ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read Service
@app.route('/api/service/all', methods=['GET'])
def allServices():
    Services = executeReadQuery(connection, "SELECT * FROM Service")

    print("Attempting Retrieval: SELECT * Service")
    return jsonify(Services)

#Update Service
@app.route('/api/service/update', methods=['PUT'])
def updService():
    requestData = request.get_json()
    ServiceID = requestData['ServiceID']
    # remove serviceID from requestData to build query below
    requestData.pop('ServiceID', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE Service SET " + ', '.join(queryFields) + f" WHERE ServiceID = {ServiceID}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete Service
@app.route('/api/service/delete', methods=['DELETE'])
def delService():
    requestData = request.get_json()
    idToDelete = requestData['ServiceID']

    print("Attempting Deletion, ServiceID: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM Service WHERE ServiceID = %s" % idToDelete)# START OF WAVE 2 TABLES #


# START OF WAVE 3 TABLES CRUD API ENDPOINTS #
#Create EmployeeIncident
@app.route('/api/employeeincident/add', methods=['POST']) 
def addEmployeeIncident():
    requestData = request.get_json()
    
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO EmployeeIncident ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read EmployeeIncident
@app.route('/api/employeeincident/all', methods=['GET'])
def allEmployeeIncidents():
    EmployeeIncidents = executeReadQuery(connection, "SELECT * FROM EmployeeIncident")

    print("Attempting Retrieval: SELECT * EmployeeIncident")
    return jsonify(EmployeeIncidents)

#Update EmployeeIncident
@app.route('/api/employeeincident/update', methods=['PUT'])
def updEmployeeIncident():
    requestData = request.get_json()
    EmployeeIncidentID = requestData['EmployeeIncidentID']
    # remove EmployeeIncidentID from requestData to build query below
    requestData.pop('EmployeeIncidentID', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE EmployeeIncident SET " + ', '.join(queryFields) + f" WHERE EmployeeIncidentID = {EmployeeIncidentID}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete EmployeeIncident
@app.route('/api/EmployeeIncident/delete', methods=['DELETE'])
def delEmployeeIncident():
    requestData = request.get_json()
    idToDelete = requestData['EmployeeIncidentID']

    print("Attempting Deletion, EmployeeIncidentID: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM EmployeeIncident WHERE EmployeeIncidentID = %s" % idToDelete)


#Create Invoice
@app.route('/api/invoice/add', methods=['POST']) 
def addInvoice():
    requestData = request.get_json()
   
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO Invoice ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read Invoice
@app.route('/api/invoice/all', methods=['GET'])
def allInvoices():
    Invoices = executeReadQuery(connection, "SELECT * FROM Invoice")

    print("Attempting Retrieval: SELECT * Invoice")
    return jsonify(Invoices)

#Update Invoice
@app.route('/api/invoice/update', methods=['PUT'])
def updInvoice():
    requestData = request.get_json()
    InvoiceID = requestData['InvoiceID']
    # remove InvoiceID from requestData to build query below
    requestData.pop('InvoiceID', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE Invoice SET " + ', '.join(queryFields) + f" WHERE InvoiceID = {InvoiceID}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete Invoice
@app.route('/api/invoice/delete', methods=['DELETE'])
def delInvoice():
    requestData = request.get_json()
    idToDelete = requestData['InvoiceID']

    print("Attempting Deletion, InvoiceID: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM Invoice WHERE InvoiceID = %s" % idToDelete)


#Create JanitorialAccount
@app.route('/api/janitorialaccount/add', methods=['POST']) 
def addJanitorialAccount():
    requestData = request.get_json()
   
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO JanitorialAccount ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read JanitorialAccount
@app.route('/api/janitorialaccount/all', methods=['GET'])
def allJanitorialAccounts():
    JanitorialAccounts = executeReadQuery(connection, "SELECT * FROM JanitorialAccount")

    print("Attempting Retrieval: SELECT * JanitorialAccount")
    return jsonify(JanitorialAccounts)

#Update JanitorialAccount
@app.route('/api/janitorialaccount/update', methods=['PUT'])
def updJanitorialAccount():
    requestData = request.get_json()
    JanitorialAccountID = requestData['AccountID']
    # remove JanitorialAccountID from requestData to build query below
    requestData.pop('AccountID', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE JanitorialAccount SET " + ', '.join(queryFields) + f" WHERE AccountID = {JanitorialAccountID}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete JanitorialAccount
@app.route('/api/janitorialaccount/delete', methods=['DELETE'])
def delJanitorialAccount():
    requestData = request.get_json()
    idToDelete = requestData['AccountID']

    print("Attempting Deletion, AccountID: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM JanitorialAccount WHERE AccountID = %s" % idToDelete)


# START OF WAVE 4 TABLES CRUD API ENDPOINTS #
#Create EmployeeAccount
@app.route('/api/employeeaccount/add', methods=['POST']) 
def addEmployeeAccount():
    requestData = request.get_json()
    
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO EmployeeAccount ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read EmployeeAccount
@app.route('/api/employeeaccount/all', methods=['GET'])
def allEmployeeAccounts():
    EmployeeAccounts = executeReadQuery(connection, "SELECT * FROM EmployeeAccount")

    print("Attempting Retrieval: SELECT * EmployeeAccount")
    return jsonify(EmployeeAccounts)

#Update EmployeeAccount
@app.route('/api/employeeaccount/update', methods=['PUT'])
def updEmployeeAccount():
    requestData = request.get_json()
    EmployeeAccountID = requestData['EmployeeAccountID']
    # remove EmployeeAccountID from requestData to build query below
    requestData.pop('EmployeeAccountID', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE EmployeeAccount SET " + ', '.join(queryFields) + f" WHERE EmployeeAccountID = {EmployeeAccountID}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete EmployeeAccount
@app.route('/api/employeeaccount/delete', methods=['DELETE'])
def delEmployeeAccount():
    requestData = request.get_json()
    idToDelete = requestData['EmployeeAccountID']

    print("Attempting Deletion, EmployeeAccountID: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM EmployeeAccount WHERE EmployeeAccountID = %s" % idToDelete)


#Create WorkOrder
@app.route('/api/workorder/add', methods=['POST']) 
def addWorkOrder():
    requestData = request.get_json()
   
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO WorkOrder ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read WorkOrder
@app.route('/api/workorder/all', methods=['GET'])
def allWorkOrders():
    WorkOrders = executeReadQuery(connection, "SELECT * FROM WorkOrder")

    print("Attempting Retrieval: SELECT * WorkOrder")
    return jsonify(WorkOrders)

#Update WorkOrder
@app.route('/api/workorder/update', methods=['PUT'])
def updWorkOrder():
    requestData = request.get_json()
    WorkOrderID = requestData['WorkOrderID']
    # remove WorkOrderID from requestData to build query below
    requestData.pop('WorkOrderID', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE WorkOrder SET " + ', '.join(queryFields) + f" WHERE WorkOrderID = {WorkOrderID}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete WorkOrder
@app.route('/api/workorder/delete', methods=['DELETE'])
def delWorkOrder():
    requestData = request.get_json()
    idToDelete = requestData['WorkOrderID']

    print("Attempting Deletion, WorkOrderID: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM WorkOrder WHERE WorkOrderID = %s" % idToDelete)


# START OF WAVE 5 (&Beyond!) TABLES CRUD API ENDPOINTS #
#Create ServiceIncident
@app.route('/api/serviceincident/add', methods=['POST']) 
def addServiceIncident():
    requestData = request.get_json()
    
    # dynamically build the SQL query
    keys = ', '.join(f"`{key}`" for key in requestData.keys())
    values = ', '.join(f"'{value}'" for value in requestData.values())
    query = f"INSERT INTO ServiceIncident ({keys}) VALUES ({values})"

    print(f"Attempting Query: {query}")
    return executeQuery(connection, query)

#Read ServiceIncident
@app.route('/api/serviceincident/all', methods=['GET'])
def allServiceIncidents():
    ServiceIncidents = executeReadQuery(connection, "SELECT * FROM ServiceIncident")

    print("Attempting Retrieval: SELECT * ServiceIncident")
    return jsonify(ServiceIncidents)

#Update ServiceIncident
@app.route('/api/serviceincident/update', methods=['PUT'])
def updServiceIncident():
    requestData = request.get_json()
    ServiceIncidentID = requestData['ServiceIncidentID']
    # remove ServiceIncidentID from requestData to build query below
    requestData.pop('ServiceIncidentID', None)

    # dynamically build the SQL query
    queryFields = [f"`{key}` = '{value}'" for key, value in requestData.items()]
    query = "UPDATE ServiceIncident SET " + ', '.join(queryFields) + f" WHERE ServiceIncidentID = {ServiceIncidentID}"

    print("Attempting Query: '%s" % query)
    return executeQuery(connection, query)

#Delete ServiceIncident
@app.route('/api/serviceincident/delete', methods=['DELETE'])
def delServiceIncident():
    requestData = request.get_json()
    idToDelete = requestData['ServiceIncidentID']

    print("Attempting Deletion, ServiceIncidentID: '%s" % idToDelete)
    return executeQuery(connection, "DELETE FROM ServiceIncident WHERE ServiceIncidentID = %s" % idToDelete)

app.run()
