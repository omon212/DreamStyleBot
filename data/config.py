from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
CHANNEL_ID = env.str("CHANNEL_ID")
GROUP_ID = env.str("GROUP_ID")
IP = env.str("ip")  # Xosting ip manzili
