import requests
import urllib.parse

param = {
    "amount": 15,
    # "category": 23,
    # "difficulty": "easy",
    "type": "boolean",
    "encode": "url3986"
    }

res = requests.get("https://opentdb.com/api.php", params=param)
res.raise_for_status()
data = res.json()
question_data = data["results"]
for i in range(len(data["results"])):
    question_data[i]["question"] = urllib.parse.unquote(data["results"][i]["question"])