# python_sqlite3_example
just for example how to use sqlite3 in python
if u have a any question, please comment it

## main.py
python main.py -> execute all query

## common.py
this file for version management 

## user.py
example structure db schema

## backend_api.py
MakeQuery
	\ QueryType -> divide query type
	\ Make sql query sentence 
		\ if you want using the transaction variable

DBConnector
	\ connect db file
	\ execute query on current db file
