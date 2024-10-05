from environs import Env

# enirons library
env = Env()
env.read_env()

# get data from .env file
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot Token
ADMINS = env.list("ADMINS")  # admins list
