import xmlrpc.client

url = 'http://localhost:8069'
db = 'o15-learn'
username = 'admin'
password = 'admin'

# creating connection
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
# login
uid = common.authenticate(db, username, password, {})
# get models object
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# getting ids of records
ids = models.execute_kw(db, uid, password, 'biko.oa.sessions', 'search', [[]])
# reading records from database
records = models.execute_kw(db, uid, password, 'biko.oa.sessions', 'read', [ids], {'fields': ['name', 'seats']})

print(records)