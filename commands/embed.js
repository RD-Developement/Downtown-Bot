const { MessageEmbed } = require("discord.js")

module.exports = {
    category: 'Testing',
    description: 'Uses JSON to send an embed',

    permissions: ['ADMINISTRATOR'],

    testOnly: true,

    callback: ({ message, text }) => {
        const json = JSON.parse(text)

        const embed = new MessageEmbed(json)

        return embed
    }      
}