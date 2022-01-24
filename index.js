const DiscordJS = require('discord.js')
const { Intents } = DiscordJS
const WOKCommands = require('wokcommands')
const path = require('path')
const mongoose = require('mongoose')
const welcome = require('./events/welcome')
const vip = require('./events/vip')
const booster = require('./events/booster')
require('dotenv/config')

const client = new DiscordJS.Client({
    intents: [
        Intents.FLAGS.GUILDS,
        Intents.FLAGS.GUILD_MESSAGES,
        Intents.FLAGS.GUILD_MEMBERS,
        Intents.FLAGS.DIRECT_MESSAGES
    ]
})

client.on('ready', () =>{
    console.log('The bot is ready')
    
    client.user.setActivity('Relaxed Downtown', { type: 'WATCHING' })

    welcome(client)
    vip(client)
    booster(client)

    new WOKCommands(client, {
        commandsDir: path.join(__dirname, 'commands'),
        testServers: ['771797312581402674', '934294427709624340'],
        mongoUri: process.env.MongoURI,
    })
})



client.login(process.env.TOKEN)