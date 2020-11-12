import discord
import sys
import datetime
# from discord.ext import commands

write_file_name = 'link_list.txt'
how_far_back = 5    # as a test.

# bot = commands.Bot(command_prefix='$')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(int(channel_name))
    
    async for message in channel.history(limit=how_far_back):
        if message.content.find('www.') != -1 or message.content.find('http') != -1:
            print(message.content)
            with open(write_file_name, 'a+') as text_file:
                text_file.write(f'{message.content} \t {message.jump_url}\n\n')
    with open(write_file_name, 'a+') as text_file:
        now = datetime.datetime.now()
        text_file.write(f'----FOR PREVIOUS {how_far_back} MESSAGES AT {now.strftime("%Y-%m-%d %H:%M:%S")}----\n\n')        
    print('Done')
    exit()

with open('token.txt' ,'r') as token_file:
    token_str, channel_name = token_file.readlines()
    client.run(token_str.strip())
