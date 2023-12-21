import json


data = '{ "userId": 1, "id": 1, "title": "delectus aut autem", "completed": false}'
# to convert json string to ppython object
pythDict = json.loads(data)

print(pythDict)
print(type(pythDict))


#to convert python dict to JSON object 

json_string = json.dumps(pythDict)
print(json_string)
print(type(json_string))