from cache_database.table import Table

class DataBase:
    store:dict = {}

    def __init__(self):
        pass

    def create_table(self,tableName:str,fields:list[str]):
        table = Table()
        table.create(fields)
        self.store[tableName] = table


    def use(self,tableName:str) -> Table:
        return self.store[tableName]
