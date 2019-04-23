import discord
import asyncio
import datetime
import random
import time
import os

client = discord.Client()
now = datetime.datetime.now()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name='"DD도움" | 도리닭이 주인', type=1))


@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith("DD서버"):
        list = []
        for server in client.servers:
            list.append(server.name)
        await client.send_message(message.channel, "\n" .join(list))

    if message.content.startswith('DD핑'):
         before = time.monotonic()
         msg = await client.send_message(message.channel, '핑은...')
         ping = (time.monotonic() - before) * 1000
         text = ":ping_pong:!  {0}ms".format((round(ping,1)))
         embed = discord.Embed(title='핑~~핑이~~ 퐁',description=text,color=0x00ff00)
         await client.edit_message(msg,embed=embed)

    if "DD삭제" in message.content:
         if message.author.id == '405018851399565323':

            learn = message.content.split(' ')
            mgs = []
            number = int(learn[1])
            async for x in client.logs_from(message.channel, limit = number+1):
                mgs.append(x)
            await client.delete_messages(mgs)
            delembed = discord.Embed(title="메세지 삭제됨",color=0x4286f4)
            delmsg = await client.send_message(channel,embed = delembed)
            await asyncio.sleep(5)
            await client.delete_message(delmsg)
         else:
              await client.send_message(channel,'네놈은 이것을 사용하기에는 권한이 약하도닭.')
               
    if message.content==('DD팀멜론'):
        str1 = ['사장님 월급주세요','RPG봇 제작중!', '헤브어 사장님과 다이나믹 로동을']
        r = random.choice(str1)
        if r == '사장님 월급주세요':
            await client.send_message(message.channel,  r )
        elif r == 'RPG봇 제작중!':
            await client.send_message(message.channel, r )
        elif r == '헤브어 사장님과 다이나믹 로동을':
            await client.send_message(message.channel, r )    
    if message.content.startswith('DD키위'):
        choose = await client.send_message(message.channel, "뉴질랜드의 상징 키위새!")
        await client.add_reaction(choose, '♥')
    if message.content.startswith("DD도움"):
        embed=discord.Embed(title="DM으로 도움말을 보냈습니닭!", color=0xff0000)
        embed.add_field(name="개인 메세지를 확인해주세요!", value="확인해 주세요.", inline=True)
        await client.send_message(message.channel, embed=embed)
        await client.send_message(message.channel, "<@!"+message.author.id+">")
        embed=discord.Embed(title="도움말, 1페이지", description=None, color=0xb2ebf4)
        embed.add_field(name="DD골라", value="도리닭봇이직접골라준닭!", inline=False)
        embed.add_field(name="DD도리닭", value="도리닭의 디스코드방 링크를 알려준닭!", inline=False)
        embed.add_field(name="DD동전", value="동전던지기를 한닭.", inline=False)
        embed.add_field(name="DD러시안룰렛", value="6분의 1 확률로 유 다이!", inline=False)
        embed.add_field(name="DD복권", value="7개의 숫자에 46까지의 랜덤 숫자가 나온닭.", inline=False)
        embed.add_field(name="DD시간", value="현재 시각이 나온닭.", inline=False)
        embed.add_field(name="DD업타임", value="도리닭봇의 켜진시간이 나온닭.", inline=False)
        embed.add_field(name="DD정보", value="해당유저의 정보를 보여준닭.", inline=False)
        embed.add_field(name="DD제비뽑기", value="DD제비뽑기 <숫자>로 제비뽑기를 해보세요.", inline=False)
        embed.add_field(name="DD주사위", value="1~6중의 숫자중에 렌덤으로 나옵니닭!", inline=False)
        embed.add_field(name="DD타이머", value="DD타이머 <시간>으로 타이머를 작동시키세요.", inline=False)
        embed.add_field(name="DD핑", value="도리닭v2 봇의 응답속도를 보여준닭.", inline=False)
        await client.send_message(message.author, embed=embed)
    if message.content.startswith('DD도리닭'):
        await client.send_message(message.channel, "https://discord.gg/VmAVEFj 도리닭의 디스코드방 입니닭!")
    if message.content.startswith('DD정보'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith("DD시간"):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        f = datetime.datetime.today().second
        embed = discord.Embed(title="시계", description="현재 시각은", color=0x00ff00)
        embed.set_footer(text = str(a) + "년 " + str(b) + "월 " + str(c) + "일 | " + str(d) + ":" + str(e) + ":" + str(f))
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith("DD업타임"):
        embed = discord.Embed(title="봇이켜진 시간은", description="바로 이겁니닭.", color=0x00ff00)
        embed.set_footer(text = str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('DD타이머'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)
        vrsize = int(vrsize)
        for i in range(1, vrsize):
            Text = Text + " " + learn[i]

        secint = int(Text)
        sec = secint
        timer = await client.send_message(message.channel, embed=discord.Embed(description='타이머 작동중 : 타이머 시작'))

        for i in range(sec, 0, -1):
            print(i)
            await client.edit_message(timer, embed=discord.Embed(description='타이머 작동중 : '+str(i)+'초'))
            time.sleep(1)

        else:
            print("땡")
        await client.edit_message(timer, embed=discord.Embed(description='타이머 종료'))
        await client.send_message(message.channel, "<@!"+message.author.id+">")

    if message.content.startswith('DD골라'):
        choice = message.content.split(" ")
        choiecnumber =  random.randint(1, len(choice)-1)
        choiceruslt = choice[choiecnumber]
        await client.send_message(message.channel, choiceruslt)

    if message.content.startswith("DD복권"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7]
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="복권 숫자!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('DD주사위'):

        randomNum = random.randrange(1, 7)
        print(randomNum)
        if randomNum == 1:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:'))
        if randomNum == 2:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:'))
        if randomNum ==3:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:'))
        if randomNum ==4:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:'))
        if randomNum ==5:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:'))
        if randomNum ==6:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: '))

    if message.content.startswith('DD러시안룰렛'):

        randomNum = random.randrange(1, 7)
        print(randomNum)
        if randomNum == 1:
            await client.send_message(message.channel, embed=discord.Embed(description='살아남았다. '+ '운도좋군.'))
        if randomNum == 2:
            await client.send_message(message.channel, embed=discord.Embed(description='살아남았다. ' + '운도좋군.'))
        if randomNum ==3:
            await client.send_message(message.channel, embed=discord.Embed(description='살아남았다. ' + '운도좋군.'))
        if randomNum ==4:
            await client.send_message(message.channel, embed=discord.Embed(description='살아남았다. ' + '운도좋군.'))
        if randomNum ==5:
            await client.send_message(message.channel, embed=discord.Embed(description='살아남았다. ' + '운도좋군.'))
        if randomNum ==6:
            await client.send_message(message.channel, embed=discord.Embed(description='빵! ' + '죽었닭. '))


    if message.content.startswith('DD제비뽑기'):
        channel = message.channel
        embed = discord.Embed(
            title='제비뽑기',
            description='각 번호별로 번호를 지정합니다.',
            colour=discord.Colour.blue()
        )

        embed.set_footer(text='제비말고 닭뽑기는 없나?')


        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn) 
        vrsize = int(vrsize)
        for i in range(1, vrsize): 
            Text = Text + " " + learn[i]
        print(Text.strip()) 

        number = int(Text)

        List = []
        num = random.randrange(0, number)
        for i in range(number):
            while num in List: 
                num = random.randrange(0, number)

            List.append(num) 
            embed.add_field(name=str(i) + '번째', value=str(num), inline=True)

        print(List)
        await client.send_message(channel, embed=embed)

    if message.content==('DD동전'):

        emoji = ["앞면", "뒷면"]

        randomNum = random.randrange(0, len(emoji))
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])
        await client.send_message(message.channel, embed=discord.Embed(description=emoji[randomNum]))
            

@client.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신것을 환영합니닭!, {0.mention} 님!'
    channel = member.server.get_channel("491900612791762944")
    await client.send_message(channel, fmt.format(member, member.server))
@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("491900612791762944")
    fmt = '{0.mention} 님이 서버에서 탈주하셨셨습니닭.'
    await client.send_message(channel, fmt.format(member, member.server))

access_token = os.getenv("BOT_TOKEN")
client.run(access_token)
