import os
from dotenv import load_dotenv
 
# Load environment variables from .env
load_dotenv()
 
# Application URL
BASE_URL = os.getenv(
    "BASE_URL",
    "https://automationexercise.com"
)
 
# API base URL
API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://automationexercise.com"
)
 
# Playwright settings
BROWSER = os.getenv("BROWSER", "chromium")
 
HEADLESS = os.getenv(
    "HEADLESS", "true"
).lower() == "true"
 
# Default timeout in milliseconds
DEFAULT_TIMEOUT = int(
    os.getenv("DEFAULT_TIMEOUT", "30000")
)
 
# API request timeout in seconds
API_TIMEOUT = int(
    os.getenv("API_TIMEOUT", "30")
)