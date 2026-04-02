import requests
import time

url = "http://localhost:8000/api/v1"

# 1. Login
r = requests.post(f"{url}/auth-token/", json={"username":"testuser", "password":"testpassword123"})
if r.status_code not in [200, 201]:
    print("Login failed", r.text)
    exit(1)

token = r.json().get('token', '')
headers = {"Authorization": f"Token {token}"}

# 2. Create app
r_app = requests.post(f"{url}/app/", json={"name": "API_App", "description": "Auto API"}, headers=headers)
app_id = r_app.json()['id']
print(f"App created with ID: {app_id}")

for apk_name in ['uptodown-social.onelife.apk', 'spotify-9-1-36-1945.apk']:
    print(f"Uploading {apk_name}...")
    with open(f"/app/apks/{apk_name}", 'rb') as f:
        r_scan = requests.post(f"{url}/scan/", data={'description': 'Analysis', 'app': app_id}, files={'apk': f}, headers=headers)
        print(f"[{apk_name}] response:", r_scan.status_code)
        if r_scan.status_code in [200, 201]:
            scan_id = r_scan.json()['id']
            print(f"Scan ID for {apk_name} is {scan_id}")
