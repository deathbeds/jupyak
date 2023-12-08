// @ts-check
const webpack = require('webpack');
const CopyPlugin = require('copy-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
const path = require('path');

/** @type {import('webpack').Configuration} */
module.exports = {
  mode: 'production',
  devtool: 'source-map',
  entry: './lib/index.js',
  experiments: { outputModule: true },
  output: {
    path: path.resolve(__dirname, './dist/prjsf'),
    filename: 'prjsf.js',
    library: { type: 'module' },
    clean: true,
  },
  cache: {
    type: 'filesystem',
    cacheDirectory: path.resolve(__dirname, '../build/.cache/webpack'),
  },
  module: {
    rules: [{ test: /\.js$/, loader: 'source-map-loader', enforce: 'pre' }],
  },
  plugins: [
    new CopyPlugin({
      patterns: [{ from: 'demo/*.{json,toml,ya?ml}' }],
    }),
    new HtmlWebpackPlugin({
      filename: 'demo/index.html',
      template: 'demo/index.html',
      scriptLoading: 'module',
    }),
    new webpack.ids.HashedModuleIdsPlugin(),
  ],
  resolve: {
    alias: {
      react: 'preact/compat',
      'react-dom/test-utils': 'preact/test-utils',
      'react-dom': 'preact/compat', // Must be below test-utils
      'react/jsx-runtime': 'preact/jsx-runtime',
    },
  },
  optimization: {
    splitChunks: {
      chunks: 'async',
      minChunks: 3,
    },
    minimize: true,
    minimizer: [new TerserPlugin({ extractComments: 'all' })],
  },
};
