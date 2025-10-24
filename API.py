import requests


class Post_Pet:
    def __init__(self, pet_id, pet_name):
        self.pet_id = pet_id
        self.pet_name = pet_name

    def test_post_pet_new(self):
        data = {
                "id": self.pet_id,
                "category": {
                    "id": self.pet_id,
                    "name": self.pet_name
                },
                "name": self.pet_name,
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": self.pet_id,
                        "name": "string"
                    }
                ],
                "status": "available"
            }
        base_url = "https://petstore.swagger.io/v2/pet"
        response = requests.post(f"{base_url}/{self.pet_id}", json=data)
        print(f"Status code: {response.status_code}")
        assert response.status_code == 200, "Failed to add pet"

    def test_get_pet_by_id(self):
        base_url = "https://petstore.swagger.io/v2/pet"
        response = requests.get(f'{base_url}/{self.pet_id}')

        assert response.status_code == 200, "Pet not found"
        assert response.headers["Content-Type"] == "application/json", "Unexpected Content-Type"

        data = response.json()
        assert  data["id"] == self.pet_id, "ID does not match"
        print(f"Тест пройден успешно для питомца с ID: {self.pet_id}")


cat = Post_Pet(45,"Кот")
cat.test_post_pet_new()
cat.test_get_pet_by_id()


