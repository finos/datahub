// FINOS project blueprint setup for Docusaurus 1.x project documentation websites
// 
// Check comments below to know how to adapt the default configuration to your FINOS project.
// If a configuration is not commented, please do not change it.
//
// See https://docusaurus.io/docs/site-config for all the possible
// site configuration options.

const siteConfig = {
  title: 'DataHub',
  tagline: 'DataHub - produce synthetic datasets',
  url: 'https://datahub.finos.org',
  cname: 'datahub.finos.org',
  baseUrl: '/',
  projectName: 'datahub',
  repoUrl: 'https://github.com/finos/datahub',
  organizationName: 'FINOS',

  // Header menu
  // We suggest that Docs, Roadmap, Team and GitHub items are available
  headerLinks: [
    {doc: 'home', label: 'Docs'},
    {doc: 'roadmap', label: 'Roadmap'},
    {doc: 'team', label: 'Team'},
    {href: 'https://github.com/finos/databub', label: 'GitHub'},
    {blog: false}
  ],
  
  // Update icon files with program/project logos
  headerIcon: 'img/favicon/favicon-finos.ico',   
  footerIcon: 'img/favicon/favicon-finos.ico',
  favicon: 'img/favicon/favicon-finos.ico',

  colors: {
    primaryColor: '#0086bf',
    secondaryColor: '#0033A0'
  },

  // Change the copyright info with correct program/project names */
  copyright: `Copyright © ${new Date().getFullYear()} DataHub - Citigroup`,

  highlight: {
    theme: 'default',
  },

  scripts: ['https://buttons.github.io/buttons.js'],
  onPageNav: 'separate',
  cleanUrl: true,

  // Update Open Graph and Twitter cards/links, if project have dedicated ones
  ogImage: 'img/undraw_online.svg',
  twitterImage: 'img/undraw_tweetstorm.svg',
  twitterUsername: 'FinosFoundation'
};

module.exports = siteConfig;
