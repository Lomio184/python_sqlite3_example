import sqlite3
import enum

class MakeQuery(object):
    class QUERYTYPE(enum.Enum):
        INSERT = 0 
        SELECT = 1
        CREATE = 2

    def __init__(self) -> None:
        self.INSERT = 'INSERT INTO '
        self.SELECT = 'SELECT '
        self.CREATE = 'CREATE TABLE IF NOT EXISTS '
        self.Transaction = 'BEGIN TRANSACTION'
        self.End = 'END'

    def _queryMaker(self, 
                    sentence : str = None, 
                    TYPE : QUERYTYPE = -1) :
        if TYPE == self.QUERYTYPE.INSERT :
            return self.INSERT + sentence
        elif TYPE == self.QUERYTYPE.SELECT :
            return self.SELECT + sentence
        elif TYPE == self.QUERYTYPE.CREATE :
            return self.CREATE + sentence
        else:
            print("Query Type Not Into Here")
            return -1

    def _updateQuery(self, sentence : str = None):
        if sentence is None:
            print("Execute sentence is None")
            return -1
    
    def _begin(self) -> str:
        return self.Transaction
    
    def _end(self) -> str:
        return self.End

class DBConnector(object):
    def __init__(
                self,
                filepath : str = '/',
                filename : str = './temp.sqlite' ) -> None:
        self.filepath = filepath
        self.filename = filename
        self.cursor   = None
        self.queryMaker = MakeQuery()
        self.conn_obj = None

    def SetFilePath(self, filepath):
        self.filepath = filepath

    def _SetCursor( self ) :
        self.cursor = self.conn_obj.cursor()
        return 0 

    def Connect(self):
        try:
            self.conn_obj = sqlite3.connect(self.filepath)
            self._SetCursor()
        except Exception as e:
            print("Sqlite3 DB is not connected : Error Message ", e)
            return -1
        print("Connect is Complete!")
        return 0
        
    def Execute(self, 
                sentence : str, 
                type : MakeQuery.QUERYTYPE, 
                args : tuple = () ) -> tuple():

        if 0 == len(sentence):
            print("Sentence is Empty")
            return ( [], -1 )

        execute_sen = self.queryMaker._queryMaker( sentence,  type )
        try:
            if 0 != len(args) :
                self.cursor.execute(execute_sen, args)
            else:
                self.cursor.execute(execute_sen)

            if type == MakeQuery.QUERYTYPE.SELECT:
                returnVal = self.cursor.fetchall()
                return ( returnVal , 0 )
            
            return ( [] , 0 )

        except Exception as e :
            print("Execution is Not done : Error msg " , e)
            return ( [] , -1 )
