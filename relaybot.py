import requests
from discord.ext import tasks
import discord

def fetch_messages(user_token, channel_id, after=None):
    headers = {
        'Authorization': f'{user_token}',
        'Content-Type': 'application/json'
    }
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=1'
    if after:
        url += f'&after={after}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch messages. Status code: {response.status_code}")
        return None
      
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# 봇 사용자 토큰, 채널 ID 설정
BOT_TOKEN = '{bot_Token}'
USER_TOKEN = '{User_Token'
SOURCE_CHANNEL_ID = {serverID} #A서버
TARGET_CHANNEL_ID = {serverID}
last_message_id = None 

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    check_messages.start() 

@tasks.loop(minutes=0.5)  
async def check_messages():
    global last_message_id 
    messages = fetch_messages(USER_TOKEN, SOURCE_CHANNEL_ID, after=last_message_id)
    
    if messages and isinstance(messages, list) and messages:
        for message in reversed(messages):  
            message_id = message.get('id')
            message_content = message.get('content', 'No content')
            
            if last_message_id and int(message_id) <= int(last_message_id):
                continue  
              
            target_channel = client.get_channel(TARGET_CHANNEL_ID)
            if target_channel:
                await target_channel.send(message_content)
                print("Message sent to target channel.")
            
            last_message_id = message_id
            
    else:
        print("No messages found or invalid response format.")

client.run(BOT_TOKEN)
