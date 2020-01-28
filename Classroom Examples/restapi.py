import requests
url = "http://garuda.pythonanywhere.com/words"

print(requests.get(url).json())

#get

print(requests.get(url + "/air").json())

#post

payload = {"word":"benz","meaning":"car"}
print(requests.post(url,data=payload).json())