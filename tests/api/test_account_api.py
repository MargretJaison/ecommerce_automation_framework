import pytest
 
from utils.data_generator import generate_user_data
 
 
# Reusable function to prepare account details
def prepare_account_data(user):
 
    return {
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
 
 
# Reusable function to delete temporary account
def delete_test_account(api_client, user):
 
    response = api_client.delete(
        "/api/deleteAccount",
        data={
            "email": user["email"],
            "password": user["password"]
        }
    )
 
    assert response.status_code == 200
    assert response.json()["responseCode"] == 200, \
        "Temporary account deletion failed"
 
 
# Test Case : Create a new account
@pytest.mark.api
def test_create_account(api_client):
 
    user = generate_user_data()
    account_data = prepare_account_data(user)
 
    response = api_client.post(
        "/api/createAccount",
        data=account_data
    )
 
    assert response.status_code == 200
 
    response_data = response.json()
 
    assert response_data["responseCode"] == 201, \
        "Account creation failed"
 
    print("\nCreate Account Response:")
    print(response_data)
 
    delete_test_account(api_client, user)
 
 
# Test Case : Update an existing account
@pytest.mark.api
def test_update_account(api_client):
 
    user = generate_user_data()
    account_data = prepare_account_data(user)
 
    # Create an account first using POST
    create_response = api_client.post(
        "/api/createAccount",
        data=account_data
    )
 
    assert create_response.status_code == 200
    assert create_response.json()["responseCode"] == 201, \
        "Test account creation failed"
 
    try:
        # Modify existing account details
        updated_data = account_data.copy()
        updated_data["company"] = "Updated Test Company"
        updated_data["city"] = "Kochi"
        updated_data["state"] = "Kerala"
 
        # Update account using PUT
        response = api_client.put(
            "/api/updateAccount",
            data=updated_data
        )
 
        assert response.status_code == 200
 
        response_data = response.json()
 
        assert response_data["responseCode"] == 200, \
            "Account update failed"
 
        print("\nUpdate Account Response:")
        print(response_data)
 
    finally:
        # Delete temporary account
        delete_test_account(api_client, user)

# Test Case : Delete an existing account
@pytest.mark.api
def test_delete_account(api_client):
 
    user = generate_user_data()
    account_data = prepare_account_data(user)
 
    # Create temporary account
    create_response = api_client.post(
        "/api/createAccount",
        data=account_data
    )
 
    assert create_response.status_code == 200
    assert create_response.json()["responseCode"] == 201
 
    # Delete account
    response = api_client.delete(
        "/api/deleteAccount",
        data={
            "email": user["email"],
            "password": user["password"]
        }
    )
 
    print("\nDelete HTTP Status:", response.status_code)
    print("Delete API Response:", response.text)
 
    assert response.status_code == 200, \
        "Delete Account API request failed"
    
    response_data = response.json()
 
    assert response_data["responseCode"] == 200, \
        "Account deletion failed"
 
    print("\nDelete Account Successful:")
    print(response_data)


# Test Case : Get user details by email
@pytest.mark.api
def test_get_user_details_by_email(api_client):
 
    user = generate_user_data()
    account_data = prepare_account_data(user)
 
    # Create a temporary account
    create_response = api_client.post(
        "/api/createAccount",
        data=account_data
    )
 
    assert create_response.status_code == 200
    assert create_response.json()["responseCode"] == 201, \
        "Test account creation failed"
 
    try:
        # Get user details using GET
        response = api_client.get(
            "/api/getUserDetailByEmail",
            params={"email": user["email"]}
        )
 
        assert response.status_code == 200
 
        response_data = response.json()
 
        assert response_data["responseCode"] == 200, \
            "Unable to retrieve user details"
 
        assert "user" in response_data, \
            "User details are missing"
 
        user_details = response_data["user"]
 
        assert user_details["email"] == user["email"], \
            "Retrieved email does not match"
 
        print("\nGet User Details API Response:")
        print(response_data)
 
    finally:
        # Delete temporary account
        delete_test_account(api_client, user)