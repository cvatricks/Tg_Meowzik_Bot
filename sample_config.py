from os import environ

# To use manual values, change these
default_bot_token = "1485038428:AAERCfgm0bkX8032SuqFClXTuqZOAtiBsAg"
default_sudo_chat_id =  -1001440655092
default_owner_id = 695291232

# Don't change these value
bot_token = environ.get("BOT_TOKEN", default_bot_token)
sudo_chat_id = int(environ.get("SUDO_CHAT_ID", default_sudo_chat_id))
owner_id = int(environ.get("OWNER_ID", default_owner_id))
