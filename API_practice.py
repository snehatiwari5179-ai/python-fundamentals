import requests
from pprint import pprint 
# pprint = prints complicated Python data in a cleaner format

# 1. API endpoint/URL
url= "https://jsonplaceholder.typicode.com/users" 
# URL is from a public practice API called JSONPlaceholder and /users is the endpoint.

# 2. GET = ask the API to send data
response=requests.get(url)

# 2.a. see the response object
print(response)                  # 200 = successful

print("==========================================")

# 2.b. see the actual response content
print(response.text)    # .text = shows the response body as text

print("==========================================")

# 3. stop if API returned an HTTP error
response.raise_for_status()

# 4. JSON → Python data
data = response.json()

# 4.a. see the python data
print(data)

print("==========================================")

# 5. type() = tells us what kind of py data we received
print("Data type:",type(data))

# 6. count the users
print(len(data))

# 7. get the first user
pprint(data[0])

print("==========================================")

# 8. get the first user's name
print(data[0]["name"])
# 9. get the first user's email
print(data[0]["email"])
# 10. get the first user's city
print(data[0]["address"]["city"])

print("==========================================")

# 11. go through every user
for user in data:
    print(user["name"])  # names of all users one by one

print("==========================================")

# 12. get name,email,city for every user
for user in data:
    print("name:",user["name"])
    print("email:",user["email"])
    print("city:",user["address"]["city"])

print("==========================================")

# 13. query parameter
xyz = { "id": 1 }
# xyz = our variable name
# It stores the information we want to send to the API ; "id": 1 means: "I want the user whose ID is 1"

# 14. send request with parameters
response=requests.get(url,params=xyz)
# requests.get() = fixed function argument
# params = fixed argument name expected by requests

# 15. see the url created by parameters
print(response.url)

# 16. check for HTTP errors again
response.raise_for_status()

# 17. see the response
print(response.text)  # The API should now return the user with ID 1

print("==========================================")

# 18. convert to py data
specific_user=response.json()

# 19. see specific user as py data
pprint(specific_user)

print("==========================================")

# 20. get specific user's name
print(specific_user[0]["name"])

