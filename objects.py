import copy
class Items:
    def __init__(self):
        self.items = {}
        self.new_index = 0
    def __len__(self):
        return len(self.items)
    def get_items(self):
        _o = []
        for index in self.items.keys():
            item = self.items[index]
            _o.append({'index':index,'name':item.name,'description':item.description}.copy())
        return copy.deepcopy(_o)
    def get_item(self,id):
        item = self.items.get(id,{})
        #print(item,id,"##",type(id),self.items)
        if isinstance(item,Item):
            _o = {'name':item.name,'description':item.description}
        else:
            _o = {}
        return copy.deepcopy(_o)
    def add(self,new_item):
        self.items[self.new_index]=new_item
        _new_index = self.new_index
        self.new_index+=1
        return _new_index
    def delete(self,index):
        _r = "OK"
        if index in self.items.keys():
            del self.items[index]
        else:
            _r = "Not valid index"
        return _r
    def update(self,index,item):
        _r = "OK"
        if index in self.items.keys():
            self.items[index] = item
        else:
            _r = "Not valid index"
        return _r

class Item:
    def __init__(self,name,description=""):
        self.name = name
        self.description = description
