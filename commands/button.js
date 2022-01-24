const { MessageActionRow, MessageButton } = require("discord.js")

module.exports = {
    category: 'Testing',
    description: 'Button testing',

    slash: true,
    testOnly: true,

    callback: async ({ interaciton: msgInt, channel }) => {
        const row = new MessageActionRow()
        .addComponents(
            new MessageButton()
            .setLabel('Success')
            .setStyle('SUCCESS')
        )
        .addComponents(
            new MessageButton()
            .setLabel('Deny')
            .setStyle('DANGER')
        )
        await msgInt.reply({
            content: 'Are you sure?',
            components: [row],
        })
    },
}