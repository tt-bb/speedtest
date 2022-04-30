import speedtest
from requests import get


# Get your IP address
ip = get('https://api.ipify.org').text

print("~~~ SPEEDTEST ~~~")
print("in progress...")
print(f"From your IP address : {ip}")
test = speedtest.Speedtest()

# Speeds in bytes
download = test.download()
upload = test.upload()

# Speeds in Mbps
download *= (9.537 * (10 ** -7))
upload *= (9.537 * (10 ** -7))
download = round(download, 2)
upload = round(upload, 2)

print(f"\tDownload = {download} Mbps")
print(f"\tUpload = {upload} Mbps")
