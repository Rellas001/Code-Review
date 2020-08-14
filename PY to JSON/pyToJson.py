#Imports
import json


x = {
"shortExample" : [
"Hi",
"bye",
"hello",
"goodbye"
],
"Name": "Hi!",
"Age": 1000
}

print(json.dumps(x, indent=4, separators=(", ", " : "), sort_keys=True))
#sort_keys=True sorts in alphebetical order
