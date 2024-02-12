from rest_framework.test import APIClient
import json

def create_new_category():
    client = APIClient()
    client.login(username="admin", password="admin")

    category_data = {
        "category_name": "New Raw material"
    }

    json_string = json.dumps(category_data)

    response = client.post('/items/create-new-category/', json.dumps({'json_string': json_string}), content_type='application/json')

    assert response.status_code == 200

    response_data = json.loads(response.content)

    if response_data["status"] == 200:
        print("\033[92mOK\033[0m")  # Green color for OK
    else:
        print("\033[91mTest case 1 failed.\033[0m")  # Red color for failure
    
    category_data = {
        "category_name": "New Raw material and jute"
    }

    json_string = json.dumps(category_data)

    response = client.post('/items/create-new-category/', json.dumps({'json_string': json_string}), content_type='application/json')

    assert response.status_code == 200

    response_data = json.loads(response.content)

    if response_data["status"] == 200:
        print("\033[92mOK\033[0m")  # Green color for OK
    else:
        print("\033[91mTest case 2 failed.\033[0m")  # Red color for failure


def create_new_item():
    client = APIClient()
    client.login(username="admin", password="admin")

    category_data = {
        "availableStock": "10",
        "inStock": "200",
        "itemName": "Jute",
        "itemSKU": "SKU-034",
        "selectedCategory": "15",
        "selectedTags": ['3'],
    }

    json_string = json.dumps(category_data)

    response = client.post('/items/create-new-item/', json.dumps({'json_string': json_string}), content_type='application/json')

    assert response.status_code == 200

    response_data = json.loads(response.content)

    if response_data["status"] == 200:
        print("\033[92mOK\033[0m")  # Green color for OK
    else:
        print("\033[91mTest case 3 failed.\033[0m")  # Red color for failure
    
    category_data = {
        "availableStock": "10",
        "inStock": "200",
        "itemName": "bajra",
        "itemSKU": "SKU-034",
        "selectedCategory": "15",
        "selectedTags": ['3'],
    }

    json_string = json.dumps(category_data)

    response = client.post('/items/create-new-item/', json.dumps({'json_string': json_string}), content_type='application/json')

    assert response.status_code == 200

    response_data = json.loads(response.content)

    if response_data["status"] == 200:
        print("\033[92mOK\033[0m")  # Green color for OK
    else:
        print("\033[91mTest case 4 failed.\033[0m")  # Red color for failure


print("Running Test cases for create new category API...")
create_new_category()

print("Running Test cases for create new item API...")
create_new_item()
