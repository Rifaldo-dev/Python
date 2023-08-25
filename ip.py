#pip install request
import requests

def get_public_ip_address():
    response = requests.get('https://api.ipify.org')
    ip_address = response.text.strip()
    return ip_address

# Dapatkan IP address publik
public_ip = get_public_ip_address()

# Cetak IP address publik
print("IP Address Publik:", public_ip)
