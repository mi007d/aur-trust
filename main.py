import os
import emoji

import urllib3
import json

package_name = input("Package name: ")

# Starting request
http = urllib3.PoolManager()
response = http.request('GET', f'https://aur.archlinux.org/rpc/?v=5&type=search&arg={package_name}')

# Getting JSON result list
results = json.loads(response.data.decode('utf-8'))['results']

# "Seeing" all list and checking if the package name is equals to the value passed on package_name (the variable)
for result in results:
    if result['Name'] == package_name:
        os.system("clear")
        print(f'{emoji.emojize(":package:", use_aliases=True)} Name: {result["Name"]}')
        print(f'{emoji.emojize(":dart:", use_aliases=True)} URL: {result["URL"]}')
        print(f'{emoji.emojize(":fire:", use_aliases=True)} Popularity: {result["Popularity"]:.0f}')
        print(f'{emoji.emojize(":top:", use_aliases=True)} Votes: {result["NumVotes"]:.0f}')
