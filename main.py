import urllib3
import json

package_name = input("Package name: ")

# Starting request
http = urllib3.PoolManager()
r = http.request('GET', f'https://aur.archlinux.org/rpc/?v=5&type=search&arg={package_name}')

# Getting JSON result list
results = json.loads(r.data.decode('utf-8'))['results']

# "Seeing" all list and checking if the package name is equals to the value passed on package_name (the variable)
for result in results:
    if result['Name'] == package_name:
        print('Name:', result['Name'])
        print('URL:', result['URL'])
        print('Popularity:', result['Popularity'])
        print('Votes:', result['NumVotes'])
