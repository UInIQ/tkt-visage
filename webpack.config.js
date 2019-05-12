const path = require('path')

module.exports = {
    entry: [
        './src/index.jsx'
    ],
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader']
            }
        ]
    },
    resolve: {
        modules: [
            'node_modules',
            path.resolve(__dirname,'src')
        ]
    },
    output: {
        path: __dirname + '/app/static',
        filename: 'bundle.js'
    }
};
