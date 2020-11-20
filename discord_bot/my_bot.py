
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Merhaba ben boncuk. {0.author.mention}'.format(message))
        elif message.content.startswith('boncuk naber'):
            await message.channel.send('İyiyim sen nasılsın?. {0.author.mention}'.format(message))

client = MyClient()
client.run('discord client id')