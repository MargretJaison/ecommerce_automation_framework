 
import json
import pytest
 
 
# API Test Case: Get all brands
@pytest.mark.api
def test_get_brands_list(api_client):
 
    response = api_client.get("/api/brandsList")
 
    # Verify HTTP status
    assert response.status_code == 200, "Brands API request failed"
 
    # Convert response into JSON
    response_data = response.json()
 
    # Verify API response code
    assert response_data["responseCode"] == 200, "Incorrect API response code"
 
    # Verify brands key exists
    assert "brands" in response_data, "Brands key is missing"
 
    # Verify brands are returned
    assert len(response_data["brands"]) > 0, "No brands returned by API"
 
    # Display complete API response
    print("\nComplete Brands API Response:")
    print(json.dumps(response_data, indent=4))
 
    # Display brand names
    print("\nBrand Names:")
    for brand in response_data["brands"]:
        print(brand["brand"])