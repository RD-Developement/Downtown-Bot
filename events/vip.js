const { MessageEmbed } = require("discord.js")

module.exports = (client) => {
    client.on('guildMemberUpdate', (oldMember, newMember) => {
        const completedAllLevels = newMember.guild.roles.cache.find((r) => r.id == '934820697702813696')
        const vip = newMember.guild.roles.cache.find((r) => r.id == '934820738714701864')
        
        const vipEmbed = new MessageEmbed()
            .setColor('DARK_PURPLE')
            .setTitle('Congratulations on VIP in Relaxed Downtown!')
            .setDescription('You just reached the VIP status on Relaxed Downtown! There are many features that come with VIP, which are listed below.')
            .addField('Perks', "➜ You will be rewarded with the @VIP's role \n ➜ You can change your nickname in 🎀︱request-a-nick \n ➜ You can choose a color role in 🎨︱color-roles \n ➜ You get access to exclusive chats and VC's (🥥︱beach-party / 🚤︱Yacht Club)", false)
            .setTimestamp()
            .setFooter({ text: 'Downtown Bot', iconURL: 'https://bot.relaxed-downtown.com/img/bot-icon.png' })
        
        if (newMember.roles.cache.has(completedAllLevels.id)) {
            newMember.roles.add(vip)
            newMember.send({embeds: [vipEmbed] })
        }
    })
}