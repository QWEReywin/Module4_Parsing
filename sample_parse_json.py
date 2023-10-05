import json

x ='{"name": "John","age": "30", "city": "New York City"}'

y = json.loads(x)
print("The output of json files is ", y)
print("name:", y["name"])
print("age:", y["age"])
print("city:", y["city"])
