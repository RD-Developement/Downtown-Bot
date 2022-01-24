const { MessageEmbed } = require("discord.js")

module.exports = (client) => {
    const channelId = '934804172316999721'
    const rulesChannel = '934812602872254515'
    const rolesChannel = '934812611273441310'
    const introductionsChannel = '934812623403352075'

    client.on('guildMemberAdd', (member) => {        
        const welcomeEmbed = new MessageEmbed()
            .setColor('DARK_PURPLE')
            .setTitle(`Welcome, ${member.displayName}`)
            .setDescription(`Welcome to the Relaxed side of Discord, **${member.displayName}**!`)
            .addField(`Make sure to check out:`, `${member.guild.channels.cache.get(rulesChannel)} \n ${member.guild.channels.cache.get(rolesChannel)} \n ${member.guild.channels.cache.get(introductionsChannel)}`, false)
            .setThumbnail('http://bot.relaxed-downtown.com/img/server-icon.gif')
            .setTimestamp()
            .setFooter({ text: 'Downtown Bot', iconURL: 'https://bot.relaxed-downtown.com/img/bot-icon.png' });

        const channel = member.guild.channels.cache.get(channelId)
        
        channel.send(`<@${member.id}>`)
        channel.send({embeds: [welcomeEmbed] })
    })
}