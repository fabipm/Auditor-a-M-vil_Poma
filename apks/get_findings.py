import requests
import json

url = "http://localhost:8000/api/v1"
r = requests.post(f"{url}/auth-token/", json={"username":"testuser", "password":"testpassword123"})
token = r.json().get('token', '')
headers = {"Authorization": f"Token {token}"}

for scan_id in [1, 2]:
    r_scan = requests.get(f"{url}/scan/{scan_id}/", headers=headers)
    print(f"Scan {scan_id}:", json.dumps(r_scan.json(), indent=2))
