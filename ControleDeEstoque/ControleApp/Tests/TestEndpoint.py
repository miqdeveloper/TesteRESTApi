
import requests
import pytest

def test_get_user_info():
    
        
        url = "http://127.0.0.1:8000/api/stock/10/" 
        response = requests.get(url)

        assert response.status_code == 200
        user_data = response.json()
        # print(user_data)
        assert "id" in user_data

