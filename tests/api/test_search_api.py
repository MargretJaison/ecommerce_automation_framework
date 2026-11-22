import json
import pytest
 
 
# API Test Case: Search product
@pytest.mark.api
def test_search_product(api_client):
 
    response = api_client.post(
        "/api/searchProduct",
        data={"search_product": "top"}
    )
 
    assert response.status_code == 200, "Search API request failed"
 
    response_data = response.json()
 
    assert response_data["responseCode"] == 200
    assert "products" in response_data
    assert len(response_data["products"]) > 0
 
    print("\nSearch API Response:")
    print(json.dumps(response_data, indent=4))
 
    print("\nMatching Products:")
    for product in response_data["products"]:
        print(product["name"])