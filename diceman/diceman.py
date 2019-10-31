#!/usr/bin/env python3

import discord
import logging
import os
import roll


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!d') or message.content.startswith('!diceman'):
        await message.channel.send('Hello!')

def get_secrets(file: str = 'secret.txt') -> str:
    secret: str = ""
    with open(file, 'r') as s_file:
        secret = s_file.readline()
    return secret

def main():

    try:
        token = os.environ['DICEMAN_TOKEN']
    except KeyError:
        logging.warning(
            "diceman.py:__main__ - DICEMAN_TOKEN environment variable not set"
        )

        # If token environment variable is not set, look for a token file
        try:
            client.run(get_secrets())

        except FileNotFoundError:
            logging.error(
                "diceman.py:__main__ - DICEMAN_TOKEN variable is not set and the token file can not be found"
            )
            exit(1)


# end main


if __name__ == '__main__':
    main()
