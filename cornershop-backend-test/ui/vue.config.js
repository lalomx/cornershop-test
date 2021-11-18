module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? "/lunch" : '',
  outputDir: '../lunch/static/lunch',
  pages: process.env.NODE_ENV === 'production' ? {
    main: {
      entry: 'src/main.js',
    },
  } : undefined,

  configureWebpack: (config) => {
    config.output.filename = '[name].js';
    config.output.chunkFilename = '[name].js';
  },

  css: {
    extract: {
      ignoreOrder: true,
      filename: 'css/[name].css',
      chunkFilename: 'css/[name]-chunk.css',
    },
  },
};