import requests
import json

# Test login endpoint
login_url = "http://127.0.0.1:8001/token"
login_data = {"username": "Aryan", "password": "Aryan123"}

print("Testing login endpoint...")
try:
    response = requests.post(login_url, data=login_data)
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")

    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get("access_token")

        if access_token:
            print(f"\n✅ Login successful! Got access token.")

            # Test protected endpoint
            print("\nTesting protected endpoint...")
            headers = {"Authorization": f"Bearer {access_token}"}
            users_url = "http://127.0.0.1:8001/users"

            users_response = requests.get(users_url, headers=headers)
            print(f"Status code: {users_response.status_code}")
            print(f"Response: {users_response.text}")

            if users_response.status_code == 200:
                print("✅ Protected endpoint access successful!")
            else:
                print("❌ Protected endpoint access failed!")
        else:
            print("❌ No access token in response!")
    else:
        print("❌ Login failed!")

except requests.exceptions.ConnectionError:
    print("❌ Could not connect to the server. Make sure it's running on port 8001.")
except Exception as e:
    print(f"❌ Error: {e}")
