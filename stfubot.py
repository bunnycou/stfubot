import discord, json, random, time, threading

intents = discord.Intents.default()
# intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # create global vars
    global msgCtr
    global msgMax
    global gifCtr
    global gifMax
    global timeCtr

    # restrict the bot to only responding in dev channel for development purposes
    # if message.channel.id != 679005649757011969:
    #     return

    # increment counters up as needed
    msgCtr += 1
    timeCtr = 0
    if len(message.attachments) > 0 or message.content.startswith("http"):
        gifCtr += 1 

    # run timer to reset counter

    # don't let bot talk to itself
    if message.author == client.user:
        return

    if msgCtr == msgMax or gifCtr == gifMax: 
        await message.channel.send(responses[random.randint(0, len(responses)-1)])
        msgCtr = 0
        msgMax = random.randint(30, 40)
        gifCtr = 0
        gifMax = random.randint(5, 10)
        

    print(msgCtr, msgMax, gifCtr, gifMax)

# global vars
# response list
responses = [
"shut the fuck up",
"shut the heck up",
"shut the frick up",
"zip your fuckin' lips",
"why are you still talking?",
"stop talking",
"PLEASE stop talking",
"I'm begging you, shut the fuck up already",
"just stop talking",
"please shut the fuck up already",
"can you stop?",
"can you just not talk?",
"you are a waste of discord server space"
"silence",
"stop talking or else :gun:"
]

# message counters
msgCtr = 0
msgMax = random.randint(30, 40)
gifCtr = 0
gifMax = random.randint(5, 10)
timeCtr = 0

def timer():
    global msgCtr
    global gifCtr
    global timeCtr
    while True:
        time.sleep(1)
        timeCtr += 1
        if timeCtr > 90:
            msgCtr = 0
            gifCtr = 0
            timeCtr = 0

t1 = threading.Thread(target=timer)
t1.start()

# load our api key
secretfile = open("secret.json")
secret = json.load(secretfile)
secretfile.close()
client.run(secret["key"])