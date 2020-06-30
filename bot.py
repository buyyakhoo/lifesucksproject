import discord 
from discord.ext import commands
import random
import datetime
from googletrans import Translator

client = commands.Bot(command_prefix = '.')

client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready.')
    
#ping
@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    await channel.send(f'Pong! {round(client.latency * 1000)}ms') 

#datetime
@client.command(pass_context=True)
async def date(ctx):
  channel = ctx.message.channel
  now = datetime.datetime.now()
  embed = discord.Embed(
    title="Date", 
    description="Tell the absolute datetime.", 
    color=0xffc800
  )

  embed.add_field(name="Current date", value=now.strftime("%d-%m-%Y"), inline=False)
  embed.set_footer(text="Life Sucks inc.")
  await channel.send(embed=embed)

#miner
data_user = {}
@client.command(pass_context=True)
async def mine(ctx):
    channel = ctx.message.channel
    author = ctx.message.author
    if author in data_user:
        coin = random.randint(1,999)
        data_user[author] += coin

        embed = discord.Embed(
            title="Life Sucks Coin Miner", 
            description="Mine the absolutely life.", 
            color=0xff8880
        )
        embed.add_field(name="User", value=author, inline=False)
        embed.add_field(name="Coin", value=coin, inline=False)
        embed.add_field(name="Total", value=f"{data_user[author]} LSC", inline=False)
        embed.set_footer(text="Life Sucks inc.")

        await channel.send(embed=embed)

    else:
        coin = random.randint(1,999)
        data_user[author] = coin

        embed = discord.Embed(
            title="Life Sucks Coin Miner", 
            description="Mine the absolutely life.", 
            color=0xff8880
        )
        embed.add_field(name="User", value=author, inline=False)
        embed.add_field(name="Coin", value=coin, inline=False)
        embed.add_field(name="Total", value=f"{data_user[author]} LSC", inline=False)
        embed.set_footer(text="Life Sucks inc.")

        await channel.send(embed=embed)


    '''
    global ltc
    channel = ctx.message.channel
    print(ctx.message.author)
    num = random.randint(1,999)
    ltc += num

    embed = discord.Embed(
        title="Life Sucks Coin Miner", 
        description="Mine the absolutely life.", 
        color=0xff8880
    )
    embed.add_field(name="Coin", value=num, inline=False)
    embed.add_field(name="Total", value=f"{ltc} LSC", inline=False)
    embed.set_footer(text="Life Sucks inc.")

    await channel.send(embed=embed)
'''

#translator
@client.command(pass_context=True)
async def translate(ctx, sentence, lang):
    language_1 = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino'} #filipino
    language_2 = {'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer'}  #khmer
    language_3 = {'ko': 'korean', 'ku': 'kurdish (kurmanji)','ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian'}  #romanian
    language_4 = {'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh'}
    language_5 = {'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}
    language_try = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}
    language_all = [language_1, language_2, language_3, language_4, language_5]
    
    try:
        channel = ctx.message.channel
        translator = Translator()
        translated_sentence = translator.translate(sentence, src='en', dest=lang)
        embed = discord.Embed(
            title="Translate", 
            description="Translate the absolute life", 
            color=0xff90fd
        )

        embed.add_field(name="english", value=sentence, inline=False)
        embed.add_field(name=language_try[lang], value=translated_sentence.text, inline=False)
        embed.set_footer(text="Life Sucks inc.")
        
        await channel.send(embed=embed)

    except:
        channel = ctx.message.channel
        await channel.send("this is an error, and I will show you language code for correct translation.")   
        
        for language_i in language_all:
            embed = discord.Embed(
                title="Translate Code", 
                description=".translate \" \" -code-", 
                color=0xff90fd
            )
        
            for i in language_i:
                embed.add_field(name=i, value=language_i[i], inline=True)
            embed.set_footer(text="Life Sucks inc.")
            await channel.send(embed=embed)

#help command
@client.command(pass_context=True)
async def help(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title="Help", 
        description="Help the absolute life.", 
        color=0x39fffc
    )
    
    embed.set_author(name="Life Sucks")
    embed.set_image(url="https://cdn.discordapp.com/attachments/702199048115060876/702199103618285650/imagehelp.jpg")
    embed.add_field(name=".ping", value="show the latency.", inline=False)
    embed.add_field(name=".mine", value="earn LTC to use absolutely nothing", inline=False)
    embed.add_field(name=".date", value="show the date.", inline=False)
    embed.add_field(name=".translate \"sentence\" [language]", value="translate the absolute life.", inline=False)
    embed.set_footer(text="Life Sucks inc.")
    
    await channel.send(embed=embed)

client.run('NTYyNTQzNzU3MjQ1OTM5NzMy.XpVpXQ.arPQhwcLQFGMj3tIeePbpbW9zro')