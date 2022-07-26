import requests


url = "https://www.flickr.com/services/rest/"

parameters = {
    "method": "flickr.photos.getPopular",
    "api_key": "840b728efe82c5903c46be7817ced7a7", 
    "user_id" : "196147392@N04",
    "format" : "json",
    "nojsoncallback" : 1
}

r = requests.get(url = url, params = parameters)

print(r.status_code)

json_response = r.json()
print(json_response)

if (r.status_code == 200 and json_response["stat"] == "ok"):
    print("API is working correctly")
else:
    print("Not Working")
    print("Error:-", json_response["message"])
