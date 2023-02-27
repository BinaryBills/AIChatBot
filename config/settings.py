#Author: BinaryBills
#Creation Date: December 21, 2022
#Date Modified: December 21, 2022
#Purpose: This file is responsible for loading the bot's sensitive data,
#connecting to the targeted SQL server, and adding all the tables to 
#the database needed for the bot to function.

import os
import openai
from dotenv import load_dotenv
from config import sqlServer
from config import sqlTable

############################################
#        Loading secret data               #
############################################
"""Loads data from .env to get the discord bot API key and SQL server credentials"""
load_dotenv()
openai.api_key  = os.getenv("OPENAI_API_KEY")
TOKEN = os.getenv("DISCORD_API_TOKEN")
HOSTNAME = str(os.getenv("HOST_NAME"))
USERNAME = str(os.getenv("USER_NAME"))
PASSWD = str(os.getenv("PASSWORD_NAME"))
DB = str(os.getenv("DATABASE_NAME"))
serverInfo = [HOSTNAME, USERNAME, PASSWD, DB]

############################################
#      Connecting to server                #
############################################
"""Connects and creates database if it does not already exist"""
conn = sqlServer.connectToServer(HOSTNAME, USERNAME, PASSWD)
sqlServer.mysqli_query(conn, f"CREATE DATABASE IF NOT EXISTS {DB}" )
conn = sqlServer.connectToDatabase(HOSTNAME, USERNAME, PASSWD, DB)

############################################
#      Creating the SQL Tables             #
############################################
"""Initializing SQL TABLES"""
sqlServer.mysqli_query(conn, sqlTable.history)

############################################
#        Loading secret data               #
############################################
"""Loads data from .env to get the discord bot API key and SQL server credentials"""
load_dotenv()
CTOKEN = os.getenv("OPENAI_API_KEY")
DTOKEN = os.getenv("DISCORD_API_TOKEN")



