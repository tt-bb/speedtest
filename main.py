import speedtest
import requests
import json
from env import API_KEY


print("~~~ SPEEDTEST ~~~")
print("in progress...")

# Get IP information
ip = requests.get('https://api.ipify.org').text
key = API_KEY
url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={key}&ip_address={ip}"
response = requests.get(url)
result = json.loads(response.content)

print(f"\tFrom your IP address : {ip}")
city = result["city"]
print(f"\tCity : {city}")
country = result["country"]
print(f"\tCountry : {country}")
fai = result["connection"]["isp_name"]
print(f"\tFAI : {fai}")

# Speedtest
test = speedtest.Speedtest()

# Speeds in bytes
download = test.download()
upload = test.upload()

# Speeds in Mbps
download *= (9.537 * (10 ** -7))
upload *= (9.537 * (10 ** -7))
download = round(download, 2)
upload = round(upload, 2)

print(f"\n\t∇ : {download} Mbps")
print(f"\t∆ : {upload} Mbps")
