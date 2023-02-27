#Author: BinaryBills
#Creation Date: January 8, 2022
#Date Modified: January 17, 2022
#Purpose: This file handle using the OpenAI API to respond to users. It also handles
#saving the memory of the AI to the SQL database, so it can engage in conversations
#with users. 

import openai
import random
from discord import app_commands
from discord.ext import commands
from config import settings
from config import sqlServer
import collections

class aiBot(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.queue = collections.deque(maxlen=50000)
     
    @commands.Cog.listener()
    async def on_message(self,message):
        try:
            if message.author == self.client.user:
                return

            # Check if there is a previous conversation with this user
            sql = "SELECT message FROM conversations WHERE user_id = %s ORDER BY created_at DESC LIMIT 1"
            previous_convo = await sqlServer.mysqli_user_query(settings.conn, sql, (message.author.id,))
            prompt = message.content if not previous_convo else previous_convo[0][0]

            #Add current message to the database
            sql = "INSERT INTO conversations (message) VALUES (%s)"
            conversation_id = await sqlServer.mysqli_user_query(settings.conn, sql, (message.content,))

            #Add message so it can remember previous message
            self.queue.append(message.content)

            prompt = f"Hey give me a response for this: {message.content}.\n"
            for i, msg in enumerate(self.queue):
                prompt += f"Message {i}: {msg}\n"


            #Get the bot's response and add it to the database
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.4,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            stop=["You:"]
            )

            #Send the response to the server
            bot_response = response.choices[0].text.strip()
            sql = "UPDATE conversations SET response = %s WHERE id = %s"
            await sqlServer.mysqli_user_query(settings.conn, sql, (bot_response, conversation_id))
            print(bot_response)

            #If the bot's response is empty, generate a new response or send a default message
            if not bot_response:
                # Option 1: Generate a new response with a different prompt
                new_prompt = f"Can you tell me more about {random.choice(['your hobbies', 'your job', 'your family'])}?\n"
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=new_prompt,
                    temperature=0.4,
                    max_tokens=150,
                    top_p=1.0,
                    frequency_penalty=0.5,
                    presence_penalty=0.0,
                    stop=["You:"]
                )
                bot_response = response.choices[0].text.strip()

            # Send the bot's response to the channel
            if bot_response != " ":
             await message.channel.send(bot_response)
           
            
        except Exception as e:
            print(f"The error '{e}' occurred")
        
             
async def setup(client):
    await client.add_cog(aiBot(client))