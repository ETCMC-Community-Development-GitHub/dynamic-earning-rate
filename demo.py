import requests

# URL of the file
url = 'https://raw.githubusercontent.com/ETCMC-Community-Development-GitHub/dynamic-earning-rate/main/earning_rate.txt'

# Send a request to the URL to download the file
response = requests.get(url)

# Variable to hold the extracted value
earning_rate = None

# Check if the request was successful
if response.status_code == 200:
    # Read the content of the file
    content = response.text
    earning_rate = float(content)  # Use float() as the value is likely a decimal

earning_rate_response = f"The variable value extracted from the file is: {earning_rate}" if earning_rate is not None else "Failed to extract the variable from the file."
print(earning_rate_response)


