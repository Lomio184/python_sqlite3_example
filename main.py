from distutils.log import ERROR
from common import *
from backend_api import *
from user import *

def main( db_conn : DBConnector = None ):
    if ERROR_CODE == db_conn.Connect():
        print("DB Connect is Fail")
        return ERROR_CODE
    
    ex = [User(age = _) for _ in range(0, 10)]
    
    if ERROR_CODE == db_conn.Execute("User ( \
                                      id string primary key, \
                                      name string , \
                                      age integer )", MakeQuery.QUERYTYPE.CREATE):
        print("Table Not Created")
        return -1
    
    for user_data in ex:
        if ERROR_CODE == db_conn.Execute(
            "User( id , name , age ) VALUES ( ?, ?, ? ) ",
            MakeQuery.QUERYTYPE.INSERT,
            ( str(uuid.uuid4()), user_data.username, user_data.age) ):
            print("Insert Fail")
            return -1

    return_val, errCode = db_conn.Execute(
        " * FROM User", 
        MakeQuery.QUERYTYPE.SELECT
    )

    if ERROR_CODE == errCode :
        print("Select is Fail")
        return -1

    [print("row : " , _) for _ in return_val]
    
    return 0

if __name__ == "__main__":

    print("Sqlite3 db maker")

    db_conn = DBConnector()

    if os.path.exists("temp.sqlite") is not True :
        print("Base db is not exists. Create New one")
        os.system("sqltie3 temp.sqlite")

    db_conn.SetFilePath(os.path.abspath("temp.sqlite"))

    if NORMAL_CODE == main( db_conn ):
        print("Sqlite3 DB Maker end")
    else:
        print("Sqlite3 DB Maker Error Occur")