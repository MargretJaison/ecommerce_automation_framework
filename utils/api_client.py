 
import requests
import truststore
truststore.inject_into_ssl()
from config.settings import API_BASE_URL, API_TIMEOUT
 
 
class APIClient:
 
    def __init__(self):
        self.base_url = API_BASE_URL
        self.timeout = API_TIMEOUT
        self.session = requests.Session()
 
    # GET request
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
 
        return self.session.get(
            url,
            params=params,
            timeout=self.timeout
        )
 
    # POST request
    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
 
        return self.session.post(
            url,
            data=data,
            timeout=self.timeout
        )
 
    # PUT request
    def put(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
 
        return self.session.put(
            url,
            data=data,
            timeout=self.timeout
        )
 
    # DELETE request
    def delete(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
 
        return self.session.delete(
            url,
            data=data,
            timeout=self.timeout
        )
 
    # Close API session
    def close(self):
        self.session.close()
 