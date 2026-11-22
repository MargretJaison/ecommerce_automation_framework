import random
import string
from datetime import datetime
 
 
def generate_unique_email():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    return f"testuser_{timestamp}@example.com"
 
 
def generate_password(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(
        random.choices(characters, k=length)
    )
 
 
def generate_user_data():
 
    return {
        "name": "Test User",
        "email": generate_unique_email(),
        "password": generate_password(),
 
        "gender": "Male",
        "day": "10",
        "month": "5",
        "year": "1998",
 
        "first_name": "Test",
        "last_name": "User",
        "company": "Test Company",
        "address": "Test Address",
        "address2": "",
        "country": "India",
        "state": "Kerala",
        "city": "Trivandrum",
        "zipcode": "695001",
        "mobile_number": "9876543210",
 
        "newsletter": False,
        "special_offers": False
    }