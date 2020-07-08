import requests

def status_code_equals_200():
    response = requests.post("http://localhost:8080/api/assets/123e4567-e89b-12d3-a456-426614174000")
    print(response)
    print(response.status_code)
    assert response.status_code == 200


status_code_equals_200()



"""

In the response object, the headers are available as a dictionary

"""

def check_content_type_equals_json():
    response = requests.get("http://api.zippopotam.us/us/90210")
    print(response.headers)
    assert response.headers['Content-Type'] == "application/json"


check_content_type_equals_json()


def check_city_equals_beverly_hills():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    print(response_body)
    assert response_body["places"][0]["place name"] == "Beverly Hills"


check_city_equals_beverly_hills()











