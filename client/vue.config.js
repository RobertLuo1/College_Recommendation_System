//vue.config.js
module.exports = {
    configureWebpack: {
        externals: {
            'BMap': 'BMap',
            'BMapLib': 'BMapLib'
        }
    },
}