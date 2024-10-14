from telethon import TelegramClient
import asyncio

# Replace 'API_ID', 'API_HASH', and 'PHONE' with your actual credentials
api_id = 'API_ID'
api_hash = 'API_HASH'
phone = 'PHONE'

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)

    # Replace 'source_channel' with the channel to scrape from
    async for message in client.iter_messages('source_channel'):
        print(message.sender_id, message.text)
        # Send the scraped message to another channel
        await client.send_message('target_channel', message.text)

with client:
    client.loop.run_until_complete(main())
