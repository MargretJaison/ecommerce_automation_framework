import pytest
import json
 
 
# API Test Case: Get all products
@pytest.mark.api
def test_get_products_list(api_client):
 
    response = api_client.get("/api/productsList")
 
    assert response.status_code == 200, "Products API request failed"
 
    response_data = response.json()
 
    assert response_data["responseCode"] == 200, "Incorrect API response code"
    assert "products" in response_data, "Products key is missing"
    assert len(response_data["products"]) > 0, "No products returned by API"
 
    # Display all products in terminal
    print("\nComplete API Response:")
    print(json.dumps(response_data, indent=4))
 
    # Display product names only
    print("\nProduct Names:")
    for product in response_data["products"]:
        print(product["name"])