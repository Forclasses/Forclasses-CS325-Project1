import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'amazon_reviews',
    'domain': 'com',
    'query': 'B098FKXT8L',
    'start_page': 1,
    'pages': 3,
    'parse': True
}

# Get response
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'),
    json=payload,
)

# Print prettified response to stdout.
print(response.json())
# output_file_path = "C:\CS325-Project1\output1.txt"

# with open(output_file_path, 'w') as file:
   # file.write(response.jason)