import requests
import re

# Get chnroutes.txt from upstream
url = 'https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt'
response = requests.get(url)
data = response.text

# Process each line
lines = data.split('\n')
for i in range(len(lines)):
    line = lines[i]
    if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$', line):
        # Insert IP-CIDR and ,no-resolve
        lines[i] = 'IP-CIDR,' + line
    else:
        # Output the line as is
        lines[i] = line

# Write modified data to file
with open('chnroutes.txt', 'w') as f:
    f.write('\n'.join(lines))
