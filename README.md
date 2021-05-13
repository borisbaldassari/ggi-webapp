# GGI Webapp

A tentative webapp for the GGI working group. A live demonstration is running at [ggi.castalia.camp](https://ggi.castalia.camp).

The aim of this prototype is to demonstrate the work done in the working group. It is intended as a minimal working product that shall evolve as content grows and get refined, in a similar fashion to what agile-like processes use.


## Automation

The webapp uses Hugo as a static generation framework, and content is all pure Markdown.

Activities are automatically retrieved from [the GitLab boards](https://gitlab.ow2.org/ggi/ggi-castalia/-/boards/432) and converted to Hugo content files. As a result the activities listed on the webapp are **not** synchronised real-time with the GitLab issues, and a rebuild is needed to show the updates. A simple Jenkinsfile at the root of the directory holds the full process.

All other pages use pure markdown, they reside under the 'content/' directory and can be modified at will.

The repository for the webapp is [hosted on GitHub](https://github.com/borisbaldassari/ggi-webapp). The webapp is automatically deployed by a private Jenkins instance that rebuilds the repository on every push and deploys the static output to [ggi.castalia.camp](https://ggi.castalia.camp).


## Contributing

All inputs welcomed, please feel in an issue or send an email to the [GGI mailing list](https://mail.ow2.org/wws/info/ossgovernance).

More information:
* GGI Home: https://www.ow2.org/view/OSS_Governance/
* GGI Blueprint: https://gitlab.ow2.org/ggi/ggi-castalia/-/boards/449

