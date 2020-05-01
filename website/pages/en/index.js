/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

const React = require('react');

const CompLibrary = require('../../core/CompLibrary.js');
const Showcase = require(`${process.cwd()}/core/Showcase.js`);

const MarkdownBlock = CompLibrary.MarkdownBlock; /* Used to read markdown */
const Container = CompLibrary.Container;
const GridBlock = CompLibrary.GridBlock;

class HomeSplash extends React.Component {
  render() {
    const {siteConfig, language = ''} = this.props;
    const {baseUrl, docsUrl} = siteConfig;
    const docsPart = `${docsUrl ? `${docsUrl}/` : ''}`;
    const langPart = `${language ? `${language}/` : ''}`;

    const SplashContainer = props => (
      <div className="homeContainer">
        <div className="homeSplashFade">
          <div className="wrapper homeWrapper">{props.children}</div>
        </div>
      </div>
    );

    const Logo = props => (
      <div className="projectLogo">
        <img src={props.img_src} alt="Project Logo" />
      </div>
    );

    const ProjectTitle = props => (
      <h2 className="projectTitle">
        {props.title}
        <small>{props.tagline}</small>
      </h2>
    );

    const PromoSection = props => (
      <div className="section promoSection">
        <div className="promoRow">
          <div className="pluginRowBlock">{props.children}</div>
        </div>
      </div>
    );

    const Button = props => (
      <div className="pluginWrapper buttonWrapper">
        <a className="button" href={props.href} target={props.target}>
          {props.children}
        </a>
      </div>
    );

    return (
      <SplashContainer>
        <div className="inner">
          <ProjectTitle tagline={siteConfig.tagline} title={siteConfig.title} />
          <PromoSection>
            <Button href=''>Get Started</Button>
            <Button href={siteConfig.repoUrl}>GitHub</Button>
          </PromoSection>
        </div>
      </SplashContainer>
    );
  }
}

class Index extends React.Component {
  render() {
    const {config: siteConfig, language = ''} = this.props;
    const {docsUrl, baseUrl, defaultVersionShown} = siteConfig;
    const docsPart = `${docsUrl ? `${docsUrl}/` : ''}`;
    const langPart = `${language ? `${language}/` : ''}`;
    const versionPart = `${defaultVersionShown ? `${defaultVersionShown}/` : ''}`;
    const docUrl = doc => `${docsPart}${versionPart}${langPart}${doc}`;


    const Block = props => (
      <Container
        padding={['bottom', 'top']}
        id={props.id}
        background={props.background}>
        <GridBlock
          align="center"
          contents={props.children}
          layout={props.layout}
        />
      </Container>
    );

    const FeatureCallout = () => (
      <div  className="featureShowcaseSection  paddingBottom" style={{textAlign: 'center'}}>
        <h2>Use Cases</h2>
        <MarkdownBlock>{`Document business [use cases](${docUrl('use-cases/overview')}) that drives the Project Blueprint.`}</MarkdownBlock>
      </div>
    );

    const Features = () => (
      <Block background="white" layout="fourColumn">
        {[
          {
            content: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. [Pellentesque]() pellentesque id standard`,
            image: `${baseUrl}img/feature-blank.svg`,
            imageAlign: 'top',
            title: 'Example 1',
          },
          {
            content: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. [Pellentesque]() pellentesque id standard`,
            image: `${baseUrl}img/feature-blank.svg`,
            imageAlign: 'top',
            title: 'Example 2',
          },
          {
            content: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. [Pellentesque]() pellentesque id standard`,
            image: `${baseUrl}img/feature-blank.svg`,
            imageAlign: 'top',
            title: 'Example 3',
          },
          {
            content: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. [Pellentesque]() pellentesque id standard`,
            image: `${baseUrl}img/feature-blank.svg`,
            imageAlign: 'top',
            title: 'Example 4',
            link: `${baseUrl}/appd-intro`
          }
          
        ]}
      </Block>
    );

    const UserShowcase = () => {
      if ((siteConfig.users || []).length === 0) {
        return null;
      }

      const pinnedUsers = siteConfig.users.filter(user => user.pinned);

      const pageUrl = page => baseUrl + (language ? `${language}/` : '') + page;

      return (
        <div className="userShowcase productShowcaseSection paddingTop paddingBottom">
          <h2>Who is Using Project Blueprint?</h2>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur ac pulvinar velit. Curabitur maximus dui in libero vehicula fringilla. Nam eu fringilla turpis. Pellentesque id. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent iaculis.</p>
          <Showcase users={pinnedUsers} />
          {/* exclude button to users page for now, all users shown on main page */}
          {/* <div className="more-users">
            <a className="button" href={pageUrl('users.html')}>
              All {siteConfig.title} Users
            </a>
          </div> */}
        </div>
      );
    };

    return (
      <div>
        <HomeSplash siteConfig={siteConfig} language={language} />
        <div className="mainContainer">
          <Features />
          <FeatureCallout />
          <UserShowcase />
        </div>
      </div>
    );
  }
}

module.exports = Index;