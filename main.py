import speedtest


print("~~~ SPEEDTEST ~~~")
print("in progress...")
test = speedtest.Speedtest()

# Speeds in bytes
download = test.download()
upload = test.upload()

# Speeds in Mbps
download *= (9.537 * (10 ** -7))
upload *= (9.537 * (10 ** -7))
download = round(download, 2)
upload = round(upload, 2)

print(f"Download = {download} Mbps")
print(f"Upload = {upload} Mbps")
