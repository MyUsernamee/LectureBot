import discord

class LectureBot(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        if message.author == self.user or message.channel != "lectures":
            return
        
        # We see if the message has a audio file
        if message.attachments:
            for attachment in message.attachments:
                if attachment.content_type.startswith('audio'):
                    # We download the file
                    await attachment.save(attachment.filename)
                    # We transcribe the file
                    os.remove(attachment.filename)
                    return

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = LectureBot(intents=intents)
