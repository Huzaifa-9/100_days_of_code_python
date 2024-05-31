import requests
import datetime as dt


USERNAME = "hx101"
TOKEN = ""
pixela_endpoint = "https://pixe.la/v1/users"
ID = "graph-hx101"
header = {
    "X-USER-TOKEN": TOKEN,
}

param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# res = requests.post(pixela_endpoint, json=param)
# res.raise_for_status()
# print(res.text)


graph_body= {
    "id": ID,
    "name": "Cycling graph",
    "unit": "km",
    "type": "float",
    "color": "momiji"
}
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# res = requests.post(url=graph_endpoint, json=graph_body, headers=header)
# print(res.text)
date = dt.date.today().strftime('%Y%m%d')
print(date)
add_pixel_body = {
    "date": date,
    "quantity": "5"
}
#post_pixel= f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
# res = requests.post(url=post_pixel, json=add_pixel_body, headers=header)
# res.raise_for_status()
# print(res.text)

update_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{dt.date.today().strftime('%Y%m%d')}"
update_pixel_body = {
    "quantity": "10"
}
# res = requests.put(url=update_pixel, json=update_pixel_body, headers=header)
# res.raise_for_status()
# print(res.text)


delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{dt.date.today().strftime('%Y%m%d')}"
res = requests.delete(url=update_pixel, headers=header)
res.raise_for_status()
print(res.text)