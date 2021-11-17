const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  publicPath: "/lunch",
  outputDir: '../lunch/static/lunch',
  pages: {
    main: {
      // entry for the page
      entry: 'src/main.js',
    },
  },
  
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
    // loaderOptions: {
    //   sass: {
    //     prependData: '@import \'~@/assets/scss/vuetify/variables\''
    //   },
    //   scss: {
    //     prependData: '@import \'~@/assets/scss/vuetify/variables\';'
    //   }
    // }
  },
};