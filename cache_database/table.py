class Table:
    store:list[dict] =[]
    id_index:int = 0
    arr:list = []

    def __init__(self):
        pass

    def create(self,arr:list):
        self.arr = arr
        return self.arr

    def insert(self,data:dict) -> int:
        self.id_index += 1
        insert_data = {"id":self.id_index}
        for key in self.arr:
            insert_data[key] = data[key]
        self.store.append(insert_data)
        return self.id_index

    def select(self,id:int) -> dict:
        for i in self.store:
            if i["id"] == id:  
                return i

    def delete(self,id:int) -> bool:
        for i in self.store:
            if i["id"] == id: 
                self.store.remove(i)
                return True
        return False        

    def update(self,id:int,data:dict) -> bool:
        for i in self.store:
            if i["id"]==id:
                for key in self.arr:
                    i[key]=data[key]
                return True
        return False














