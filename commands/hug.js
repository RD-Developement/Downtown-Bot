const { MessageEmbed } = require('discord.js')

module.exports = {
    category: 'Testing',
    description: 'Replies with pong',

    slash: 'both',
    testOnly: true,

    minArgs: 1,
    expectedArgs: '<user>',
    expectedArgsTypes: ['USER'],

    callback: ({ message, interaction}) => {
        if (message) {
            user = message.author
        } else {
            user = interaction.user
        }
        
        if (message) {
            mentionedUser = message.mentions.users?.first()
        } else {
            mentionedUser = interaction.options.getUser('user')
        }

        let { hugs } = require('./hug_gifs.json')
        const hug = hugs[Math.floor(Math.random() * hugs.length)]

        const hugEmbed = new MessageEmbed()
            .setColor('DARK_PURPLE')
            .setDescription(`**${user} gives a big hug to ${mentionedUser}**`)
            .setImage(hug)
            .setTimestamp()
            .setFooter({ text: 'Downtown Bot', iconURL: 'https://bot.relaxed-downtown.com/img/bot-icon.png' });

        return hugEmbed
    }      
}