#!/usr/bin/env python3

import logging
import pickle
import random
import string
import time
import urllib
import os
import sys
import discord
import datetime
import asyncio
import pip
import subprocess
import re
import io
from discord.ext import commands
from contextlib import suppress
from collections import deque
from discord.ext.commands import Bot, Context
from sys import argv
from discord.embeds import Embed
from string import ascii_uppercase, ascii_lowercase, digits
from contextlib import redirect_stdout
from urllib.request import urlretrieve

client = discord.Client()
loop = asyncio.get_event_loop()
akeno = discord.Client(loop=loop)

@client.event
async def on_ready():
    print('\033[34m' + '[==================================]' + '\033[39m')
    print('\033[35m' + '|' + '\033[36m' + ' v0.0.1'+ '\033[39m')
    print('\033[35m' + '|' + '\033[33m' + ' Logged in as:',client.user.name)
    print('\033[35m' + '|' + '\033[33m' + ' UID:',client.user.id) 
    print('\033[35m' + '|' + '\033[33m' + ' Discord version:',discord.version_info)
    print(' ')
    print('\033[35m' + '|' + '\033[33m' + ' Use ' + '\033[36m' + 'Control + C ' + '\033[33m' + 'to exit.'+ '\033[39m')
    print('\033[35m' + '|' + '\033[36m' + ' elijah'+ '\033[39m')
    print('\033[34m' + '[==================================]' + '\033[39m')
    print('\033[35m' + '|' + '\033[36m' + ' Connected to:'+ '\033[39m')
    for server in client.servers:
        print('\033[35m' + '-', server.name)
    print('\033[34m' + '[==================================]' + '\033[39m')

@client.event
async def on_message(message):
    if message.author == client.user:
        # MAKES A LIST WITH THE COMMAND ATRIBUTES
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index+1
        commands.append(message.content[z:])
        if message.content.startswith('$roles'):
            await client.delete_message(message)
            get_tagged = []
            for role in message.server.role_hierarchy:
                get_tagged.append(role.mention)
            chunks = [get_tagged[x:x+87] for x in range(0, len(get_tagged), 87)]
            for chunk in chunks:
                msg = await client.send_message(message.channel," ".join(chunk))
                await client.delete_message(msg)
        if message.content.startswith('$members'):
            await client.delete_message(message)
            get_tagged = []
            for member in message.server.members:
                get_tagged.append(member.mention)
            chunks = [get_tagged[x:x+87] for x in range(0, len(get_tagged), 87)]
            for chunk in chunks:
                msg = await client.send_message(message.channel," ".join(chunk))
                await client.delete_message(msg)
        if commands[0] == '$stream':
            while True :
                await client.delete_message(message)
                await client.change_presence(game=discord.Game(name='love', url="https://www.twitch.tv/kaiio", type=1))
                await asyncio.sleep(10)
                await client.change_presence(game=discord.Game(name='love', url="https://www.twitch.tv/kaiio", type=1))
                await asyncio.sleep(10)
                await client.change_presence(game=discord.Game(name='love', url="https://www.twitch.tv/kaiio", type=1))
                await asyncio.sleep(10)
                await client.change_presence(game=discord.Game(name='love', url="https://www.twitch.tv/kaiio", type=1))
        if commands[0] == '$nick':
                await client.change_nickname(message.author, " ")
        if commands[0] == '$':
            embed = discord.Embed(title="Commands", description="***STATUS***\n [x] Stream - Cycles streaming status.\n\n***GENERAL***\n [x] *Cum <@/userid> - Yea does stuff.*\n [x] *Nick - changes your nick to default username*\n [x] *Cycle - Cycles nickname*\n [x] *Avatar - Gives <@/users> avatar.*\n [x] *Cl - Clears messages.*\n [x] *Roles - tags all available roles in the server.*\n [x] *Members - Tags all members in the server.*", color=0x000000)
            embed.set_author(name="baby", icon_url="https://cdn.discordapp.com/attachments/411320520789983232/412391200277004302/dddd.jpg")
            embed.set_footer(text="Prefix = $ | alex ")
            await client.send_message(message.channel, embed=embed)
        if commands[0] == '$avatar':
           for user in message.mentions:
            url = user.avatar_url
            if url:
                await client.send_message(message.channel, "<@!{}>\n{}".format(user.id, url));
        if commands[0] == '$cycle':
            while True :
                await client.change_nickname(message.author, "a")
                await asyncio.sleep(.1)
                await client.change_nickname(message.author, "al")
                await asyncio.sleep(.1)
                await client.change_nickname(message.author, "ale")
                await asyncio.sleep(.1)
                await client.change_nickname(message.author, "alex")
        if commands[0] == '$cl':
            if len(commands) == 1:
                async for msg in client.logs_from(message.channel,limit=9999):
                    if msg.author == client.user:   
                        try:
                            await client.delete_message(msg)
                        except Exception as x:
                            pass
            elif len(commands) == 2:
                user_id = ''
                for channel in client.private_channels:
                    if commands[1] in str(channel):
                        if str(channel.type) == 'private':
                            user_id = str(channel.id)
                async for msg in client.logs_from(discord.Object(id=user_id),limit=9999):
                    if msg.author == client.user:
                        try:
                            await client.delete_message(msg)
                        except Exception as x:
                            pass
        if message.content.startswith('$cum'):
            if len(commands) == 2:
                memberz = []
                for member in message.server.members:
                    memberz.append(member)
                for member in memberz:
                    if str(member.mention) in commands[1]:
                        k = ("""
:ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        x = ("""
:ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        a = ("""
:ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        b = ("""
:ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:                
                                                  %s      
                        """ % (member.mention))
                        c = ("""
:ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        d = ("""
:ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        e = ("""
:ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        f = ("""
:ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        t = ("""
:ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
                                                  %s      
                        """ % (member.mention))
                        g = ("""
:ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
                                                  %s      
                        """ % (member.mention))
                        string = [k,a,b,c,d,e,f,t,g]
                        for z in string:
                            await client.edit_message(message,z)
                            await asyncio.sleep(.3)
                await client.delete_message(message)
    @akeno.event
    async def on_message(message):
        if message.author.id != 405750237660184576:
            return
        if not message.content.startswith('$dm ') or len(message.mentions) == 0:
            return
        target_user = message.mentions[0]
        for i in range(5):
            await akeno.send_message(target_user, faggot)
            await asyncio.sleep(0.9)

client.run('MTU1NDY5MzMwNTcyNzcxMzI4.DlXaaA.isCcLPJeyZNahgY40X8iqkKjenI', bot=False)
