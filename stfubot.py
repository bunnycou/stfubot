from fileinput import close
import discord, json

intents = discord.Intents.default()
# intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # if message.author.id not in deniedUsers:
    #     print(f"messsage sender {message.author} not denied")

    if message.content.startswith("stfubot ignore"):
        if f"{message.author.id}" in deniedUsers:
            await message.delete()
            print("Denied user tried to use ignore command")
            return

        bannedID = message.content.split("ignore")[1].strip()[2:-1]
        if bannedID in deniedUsers:
            print("already denied this user")
            print(deniedUsers)
        else:
            deniedUsers.append(bannedID)
            open("banned.txt", "w").write("\n".join(deniedUsers))
            close()
            print(f"denied a new user, displaying full list")
            print(deniedUsers)

    elif message.content.startswith("stfubot allow"):
        if f"{message.author.id}" in deniedUsers:
            await message.delete()
            print("Denied user tried to use allow command")
            return

        allowedID = message.content.split("allow")[1].strip()[2:-1]
        if allowedID in deniedUsers:
            deniedUsers.remove(allowedID)
            open("banned.txt", "w").write("\n".join(deniedUsers))
            close()
            print(f"allowed a denied user, displaying full list")
            print(deniedUsers)
        else:
            print("user is not denied")

    elif (len(message.content) > 280 or message.content.startswith("http") or len(message.attachments) > 0) and f"{message.author.id}" in deniedUsers:
        await message.delete()
        print("Deleted message from denied user")

# load our banned users
deniedUsers = list()
banfile = open("banned.txt", "r")
for x in banfile.readlines():
    deniedUsers.append(x.strip())
banfile.close()

# load our api key
secretfile = open("secret.json")
secret = json.load(secretfile)
secretfile.close()
client.run(secret["key"])