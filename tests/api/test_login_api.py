import pytest
 
from utils.data_generator import generate_user_data
 
 
# Test Case : Verify login with valid credentials
@pytest.mark.api
def test_verify_login_valid_credentials(api_client):
 
    user = generate_user_data()
 
    # Create a temporary test account
    account_data = {
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],
        "title": "Mr",
        "birth_date": user["day"],
        "birth_month": user["month"],
        "birth_year": user["year"],
        "firstname": user["first_name"],
        "lastname": user["last_name"],
        "company": user["company"],
        "address1": user["address"],
        "address2": user["address2"],
        "country": user["country"],
        "zipcode": user["zipcode"],
        "state": user["state"],
        "city": user["city"],
        "mobile_number": user["mobile_number"]
    }
 
    create_response = api_client.post(
        "/api/createAccount",
        data=account_data
    )
 
    assert create_response.status_code == 200
    assert create_response.json()["responseCode"] == 201, \
        "Test account creation failed"
 
    try:
        # Login using valid credentials
        response = api_client.post(
            "/api/verifyLogin",
            data={
                "email": user["email"],
                "password": user["password"]
            }
        )
 
        assert response.status_code == 200
 
        response_data = response.json()
 
        assert response_data["responseCode"] == 200, \
            "Login with valid credentials failed"
 
        print("\nValid Login Response:")
        print(response_data)
 
    finally:
        # Delete temporary account
        api_client.delete(
            "/api/deleteAccount",
            data={
                "email": user["email"],
                "password": user["password"]
            }
        )
 
 
# Test Case : Verify login with invalid credentials
@pytest.mark.api
def test_verify_login_invalid_credentials(api_client):
 
    response = api_client.post(
        "/api/verifyLogin",
        data={
            "email": "invaliduser@example.com",
            "password": "WrongPassword123"
        }
    )
 
    assert response.status_code == 200
 
    response_data = response.json()
 
    assert response_data["responseCode"] == 404, \
        "Invalid login response was incorrect"
 
    print("\nInvalid Login Response:")
    print(response_data)