import requests
file = "https://csf101-server-cap1.onrender.com/get/input/357"
request_file = requests.get(file)
with open('357.txt', 'wb') as file:
    data = file.write(request_file.content)
print('Downloaded: 357.txt')

