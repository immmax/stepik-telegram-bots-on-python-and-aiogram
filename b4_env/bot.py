from environs import Env

env = Env()
env.read_env()
BOT_TOKEN = env('BOT_TOKEN')
ADMIN_ID = env.int('ADMIN_ID')

print(type(BOT_TOKEN))
print(type(ADMIN_ID))
