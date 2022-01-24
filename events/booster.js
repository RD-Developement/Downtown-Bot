const { MessageEmbed } = require("discord.js")

module.exports = (client) => {
    client.on('guildMemberUpdate', (oldMember, newMember) => {
        const boosterRole = newMember.guild.roles.cache.find((r) => r.id == '934944247495426069')
        
        const boosterEmbed = new MessageEmbed()
            .setColor('DARK_PURPLE')
            .setTitle('Thank You for Boosting Relaxed Downtown!')
            .setDescription('Thank you so much for boosting the server, it really means a lot. Because you are a booster, you get access to all of the perks listed below.')
            .addField('Perks', "➜ You will be rewarded with the @Booster role \n ➜ You can change your nickname in 🎀︱request-a-nick \n ➜ You can choose a color role in 🎨︱color-roles \n ➜ You get access to exclusive chats and VC's (🥥︱beach-party / 🚤︱Yacht Club) \n ➜ You can post in 📈︱promo (normal members can get access to this channel in 🎨︱roles)", false)
            .setTimestamp()
            .setFooter({ text: 'Downtown Bot', iconURL: 'https://bot.relaxed-downtown.com/img/bot-icon.png' })
        
        if (newMember.roles.cache.has(boosterRole.id)) {
            newMember.send({embeds: [boosterEmbed] })
        }
    })
}