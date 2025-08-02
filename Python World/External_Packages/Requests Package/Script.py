import requests

response = requests.get("https://httpbin.org/get")

# Response status code comes to 200 --> It means success
print(f"response.status_code = {response.status_code}")

# convert response to text
print(f"response.text = {response.text}")

# convert response to json
print(f"response.json() = {response.json()}")

# Gives metadata about the url
print(f"response headers = {response.headers}")

# ------------------------------------------------------------------- #

# GET Method
params = {'name' : 'Rohit', 'age' : 26}
response = requests.get("https://httpbin.org/get", params=params)
print(response.url)

# ------------------------------------------------------------------- #

# POST Method
data = {'username': 'rohit', 'password': '1234'}
response = requests.post("https://httpbin.org/post", data=data)
print(response.status_code)
print(response.json())

# ------------------------------------------------------------------- #

# Download a file
response = requests.get("https://upload.wikimedia.org/wikipedia/en/2/21/Web_of_Spider-Man_Vol_1_129-1.png")
with open("Web_of_Spider-Man_Vol_1_129-1.png", "wb") as f:
    f.write(response.content)


# ------------------------------------------------------------------- #

# Uploading a file
files = {'file': open('test.txt', 'rb')}
response = requests.post("https://httpbin.org/post", files=files)
print(response.json())
print(response.status_code)

# -------------------------------------------------------------------- #

