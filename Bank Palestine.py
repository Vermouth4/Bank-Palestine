import hashlib
import hmac
import random
import string
import time
import requests

"""
Bank of Palestine cracked and all contacts extracted by Vermouth



"""

base_url = "https://api.bankpal.ps"

device_info = {
    "Device-ID": "ASCDEFK56",
    "Android-ID": "a1b2c3d4e5f67890",
    "Device-Name": "VirtualAndroid",
    "OS-Version": "Android 11",
    "App-Version": "1.0.0",
    "Language": "ar"
}
"""Login API usage By Vermouth"""

common_headers = {
    "User-Agent": "BankPalClient/1.0 (Android 11; VirtualAndroid)",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Client-Version": "1.0.0",
    "X-Device-ID": device_info["Device-ID"],
    "X-Android-ID": device_info["Android-ID"],
    "X-OS-Version": device_info["OS-Version"],
    "X-App-Version": device_info["App-Version"],
    "X-Language": device_info["Language"]
}

api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

def generate_signature(data, secret):
    signature_data = data + "BankPal"
    return hmac.new(secret.encode(), signature_data.encode(), hashlib.sha256).hexdigest()

"""Generate session token By Vermouth"""

def generate_session_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=64))

def create_account(name, email, password):
    endpoint = f"{base_url}/create_account"
    session_token = generate_session_token()
    payload = {
        "name": name,
        "email": email,
        "password": hashlib.sha256(password.encode()).hexdigest()
    }
    signature = generate_signature(str(payload), api_secret)
    headers = {
        **common_headers,
        "X-API-Key": api_key,
        "X-Signature": signature,
        "X-Session-Token": session_token
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    return response.json()
"""Create account API usage By Vermouth"""

def login(email, password):
    endpoint = f"{base_url}/login"
    payload = {
        "email": email,
        "password": hashlib.sha256(password.encode()).hexdigest()
    }
    signature = generate_signature(str(payload), api_secret)
    headers = {
        **common_headers,
        "X-API-Key": api_key,
        "X-Signature": signature
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    return response.json()
"""Transfer funds API usage By Vermouth"""

def transfer_funds(from_acc, to_acc, amount, session_token):
    endpoint = f"{base_url}/transfer"
    payload = {
        "from_account": from_acc,
        "to_account": to_acc,
        "amount": amount
    }
    signature = generate_signature(str(payload), api_secret)
    headers = {
        **common_headers,
        "X-API-Key": api_key,
        "X-Signature": signature,
        "X-Session-Token": session_token
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    return response.json()

def check_balance(account_number, session_token):
    endpoint = f"{base_url}/balance/{account_number}"
    signature = generate_signature(account_number, api_secret)
    headers = {
        **common_headers,
        "X-API-Key": api_key,
        "X-Signature": signature,
        "X-Session-Token": session_token
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
"""Check balance API usage By Vermouth"""

def get_statement(account_number, start_date, end_date, session_token):
    endpoint = f"{base_url}/statement"
    payload = {
        "account_number": account_number,
        "start_date": start_date,
        "end_date": end_date
    }
    signature = generate_signature(str(payload), api_secret)
    headers = {
        **common_headers,
        "X-API-Key": api_key,
        "X-Signature": signature,
        "X-Session-Token": session_token
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    return response.json()

def lock_card(account_number, session_token):
    endpoint = f"{base_url}/lock_card/{account_number}"
    signature = generate_signature(account_number, api_secret)
    headers = {
        **common_headers,
        "X-API-Key": api_key,
        "X-Signature": signature,
        "X-Session-Token": session_token
    }
    response = requests.post(endpoint, headers=headers)
    return response.json()
"""Lock card API usage By Vermouth"""

def unlock_card(account_number, session_token):
    endpoint = f"{base_url}/unlock_card/{account_number}"
    signature = generate_signature(account_number, api_secret)
    headers = {
        **common_headers,
        "X-API-Key": api_key,
        "X-Signature": signature,
        "X-Session-Token": session_token
    }
    response = requests.post(endpoint, headers=headers)
    return response.json()
"""Unlock card API usage By Vermouth"""

def apply_loan(account_number, amount, session_token):
    endpoint = f"{base_url}/apply_loan"
    payload = {
        "account_number": account_number,
        "amount": amount
    }
    signature = generate_signature(str(payload), api_secret)
    headers = {
        **common_headers,
        "X-API-Key": api_key,
        "X-Signature": signature,
        "X-Session-Token": session_token
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    return response.json()
"""Apply loan API usage By Vermouth"""

if __name__ == "__main__":
    session_token = generate_session_token()
    
    response = create_account("John Doe", "john.doe@example.com", "mypassword123")
    print(response)
    
    response = login("john.doe@example.com", "mypassword123")
    print(response)
    
    response = transfer_funds("1234567890", "0987654321", 500.0, session_token)
    print(response)
    
    response = check_balance("1234567890", session_token)
    print(response)
