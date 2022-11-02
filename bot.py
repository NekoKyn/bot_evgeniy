import discord
from discord.ext import commands
from config import settings
from discord.utils import get

# задаём префикс и подключаем намеренья
bot = commands.Bot(command_prefix='/',  intents=discord.Intents.all())

@bot.event

# сообщение о том, что бот подлючен
async def on_reafy():
    print('BOT connected')

# очистка чата
@bot.command()
@commands.has_any_role('Администратор')
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=int(amount))

promo = ['<name_promocode>']
# выдача ролей новичкам
@bot.event
async def on_member_join(member):
    role = get(member.guild.roles, name='Новичок')
    await member.add_roles(role)
    await member.send(embed=discord.Embed(description=f'``{member.name}``, Добро пожаловать на Луну!',
                                              color=0x18B5FF))

# выдача роли по промокоду
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if "22_MASTER_23" in message.content:
        role = discord.utils.get(message.guild.roles, name="Мастер")
        await message.author.add_roles(role)
        await message.delete()
        await message.author.send(embed=discord.Embed(
            description=f'{message.author.name}, вы активировали промокод на роль "Мастер"', color=0x18B5FF))

# берём токен из конфига
token = settings['token']
bot.run(token)
