from objects import *
from flask import Flask, request
import json

app = Flask(__name__)
items = Items()
"""
created_index = items.add(item)
all_items = items.get_items()
ok_or_not_ok = items.update(0,item)
ok_or_not_ok = items.delete(0)

item = Item(name="i",description="iiii")
"""
def parse_request_id(ireq):
    r = dict(ireq)
    id = eval(r.get('id',[""]))
    return id

def parse_request(ireq):
    r = dict(ireq)
    name = r.get('name',[""])
    description = r.get('description',[""])
    _new_item = Item(name[0],description[0])
    return _new_item

@app.route('/')
def index():
    return 'hire me :D'

@app.route('/items')
def get_items():
    return json.dumps({'items':items.get_items()})

@app.route('/items',methods=['POST'])
def add_item():
    item = parse_request(request.args)
    created_index = items.add(item)
    return json.dumps({'id':created_index})

@app.route('/items/<id>')
def get_item(id,methods=['GET']):
    _id = eval(id)
    print(_id,request.method)
    if request.method =="GET":
        #id = parse_request_id(request.args)
        item = items.get_item(_id)
        if len(item)>0:
            return json.dumps(item)
        else:
            return json.dumps({'error':'no existing item'})

"""
@app.route('/items/delete')
def delete_item(methods=['DELETE']):
    print("delete func",parse_request(request.args))
    ok_or_not_ok = items.delete(id)
    if ok_or_not_ok != "OK":
        return json.dumps({'error':'item does not exist'})
    else:
        return "200"

@app.route('/items/<id>')
def update_item(id,methods=['PUT','PATCH']):
    r = request.json
    name = r.get('name',"")
    description = r.get('description',"")
    _new_item = item(name,description)
    ok_or_not_ok = items.update(id,_new_item)
    if ok_or_not_ok != "OK":
        return json.dumps({'error':'item does not exist'})
    else:
        return "200"
"""
