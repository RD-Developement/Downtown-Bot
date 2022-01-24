module.exports = {
    category: 'Testing',
    description: 'Replies with pong',

    slash: 'both',
    testOnly: true,

    callback: ({}) => {
        return 'Pong'
    }      
}