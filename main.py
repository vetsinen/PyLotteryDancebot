import asyncio
from telethon import TelegramClient, events
from telethon.tl.custom import Button
from telethon.tl.functions.users import GetFullUserRequest
import logging


api_id = 14535551
api_hash = 'ee049ec9130de53ec5336fe819e49365'

wild_dances_channel_id = -1001866935354
chat = 'openairskyiv'

# start the bot client
client = TelegramClient('bot_SESSION_NAME', api_id, api_hash)
client.start(bot_token='5616779070:AAFNDOX-H8v9Po_mmdaHWwGfv3ApwoOwjSs')

# function that sends the message
async def sendButtons():
    invitation = """
 підписники каналу __танцювальний дайджест__ можуть виграти безкоштовний вхід на сьогоднішню вечірку [just dance](https://fb.me/e/3vR7Ff2O7)
для участі натисніть кнопку під текстом
результати розіграшу будуть опубліковані після 17:00, переможець чи переможниця має підтвердити свою участь написавши ім"я і фамілію"""
    await client.send_message(chat, invitation, buttons=[[
        Button.inline("хочу безкоштовний вхід"),
    ]])

@client.on(events.NewMessage)
async def any_message_arrived_handler(event):
    print('We are handling message events')
    await client.send_message('@helvetian','some command')
    # print(event.stringify())
    command = event.original_update.message.message
    logging.info(command)
    if command=='/publish':
        print('lets start')
        await sendButtons()
        client.add_event_handler(click_handler)


# CallBackQuery event handler that gets triggered every time a user click a Button.inline
@events.register(events.CallbackQuery(chats=[chat]))
async def click_handler(event):
    # print((event.stringify())) # event contains the user choice   - <class 'telethon.events.callbackquery.CallbackQuery.Event'>
    print('userid ',event.query.user_id)
    full = await client(GetFullUserRequest(event.query.user_id))
    # print(full.stringify())
    # await client.send_message('helvetian', full.stringify())
    user = full.users[0]
    # await client.send_message('helvetian', full.users[0].first_name)
    await client.send_message('helvetian', f'user {user.first_name} {user.last_name} - @{user.username}, {event.query.user_id}')


    # print(user.first_name, user.last_name, user.username)
    # UserFull(user=User(id=1821170460, is_self=False, contact=False, mutual_contact=False, deleted=False, bot=False, bot_chat_history=False, bot_nochats=False, verified=False, restricted=False, min=False, bot_inline_geo=False, support=False, scam=False, apply_min_photo=True, fake=False, access_hash=8720590546679958276, first_name='Vitaliy', last_name='Gusak', username='harley_baldwin', phone=None, photo=UserProfilePhoto(photo_id=5269460968935636318, dc_id=2, has_video=False, stripped_thumb=None), status=UserStatusRecently(), bot_info_version=None, restriction_reason=[], bot_inline_placeholder=None, lang_code=None), settings=PeerSettings(report_spam=False, add_contact=False, block_contact=False, share_contact=False, need_contacts_exception=False, report_geo=False, autoarchived=False, invite_members=False, geo_distance=None), notify_settings=PeerNotifySettings(show_previews=True, silent=False, mute_until=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), sound='default'), common_chats_count=0, blocked=False, phone_calls_available=True, phone_calls_private=False, can_pin_message=True, has_scheduled=False, video_calls_available=True, about=None, profile_photo=Photo(id=5269460968935636318, access_hash=-4898392480451631249, file_reference=b"\x00c6\x03\x1c\xb1'\x0bu\xc96\xcd\xe99\xe2\xcc\x83R\xd9EZ", date=datetime.datetime(2022, 9, 15, 14, 2, 20, tzinfo=datetime.timezone.utc), sizes=[PhotoSize(type='a', w=160, h=160, size=10783), PhotoSize(type='b', w=320, h=320, size=38311), PhotoSize(type='c', w=640, h=640, size=134636)], dc_id=2, has_stickers=False, video_sizes=[]), bot_info=None, pinned_msg_id=None, folder_id=None, ttl_period=None, theme_emoticon=None)
    # await client.send_message('helvetian', f'user {user.first_name} {user.last_name} - @{user.username}, {event.query.user_id}')


print('launching pyTgLotterybot')
loop = asyncio.get_event_loop()
# loop.run_until_complete(sendButtons())
# client.add_event_handler(click_handler)

loop.run_forever()
