from telethon import TelegramClient, events

# Remember to use your own values from my.telegram.org!
api_id = 14535551
api_hash = 'ee049ec9130de53ec5336fe819e49365'

with TelegramClient('name', api_id, api_hash) as client:
   await client.send_message('me', 'Hello, myself!')
   print(client.download_profile_photo('me'))

   @client.on(events.NewMessage(pattern='(?i).*Hello'))
   async def handler(event):
      await event.reply('Hey!')

   client.run_until_disconnected()