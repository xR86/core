# core [![license](https://img.shields.io/badge/license-MIT-blue.svg?maxAge=2592000)](https://github.com/xR86/cs-platform/blob/master/LICENSE)

My main repo for pointing to other repos and writing core policies for all repos (usually public repos, private repo will have their own policies)

---

### Fast pointers

`In a hurry ?` Check [xr86.github.io](https://xr86.github.io/) for some highlights for what I do (`TODO`: will be updated with tags for topics).  
`Not really, but little time...` Try [students.info.uaic.ro/~dan.alexandru](http://students.info.uaic.ro/~dan.alexandru/) and see a more detailed chronology.


[![Abstract Processing Core](processing_core.png)](http://freakinlobstah.deviantart.com/art/Abstract-processing-core-455670942)


---

## Core policies in repo:

`TODO`: Automate this by unit tests and a Travis build ?

#### Accesibility:
+ use topics in repo - easier to be found, indexed ...
+ project description
+ screenshots, terminal session recording ([asciinema](https://asciinema.org/))


#### Easy usage:
+ start scripts (`.bat` on Windows, `.sh` on Linux) - [github.com/xR86/scripts](https://github.com/xR86/scripts)
+ `Makefiles`, if suitable
+ one-click deployment or faster deployment - eg:
  + `limited` - strictly frontend: [codepen](http://codepen.io/), [jsbin](https://jsbin.com/)
  + `relatively used` - small web apps: [Plunker](http://plnkr.co/), [Heroku](https://devcenter.heroku.com/articles/heroku-button)
  + `rarely used` - web apps: [Docker Cloud](https://docs.docker.com/docker-cloud/apps/deploy-to-cloud-btn/), [AWS CodeDeploy ???](https://blog.talentica.com/2017/03/22/one-click-deployment-with-aws-codedeploy/) (or [this](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-github.html)), [Travis + GAE](https://docs.travis-ci.com/user/deployment/google-app-engine/) (somewhat unsecure)
  
+ READMEs, a lot of READMEs - and badges for:
  + license
  + build status
  + code coverage
  + extra ... downloads / slack / other CIs / etc.


#### Git requirements:
+ use `.gitignore` for the languages found in that repo, ignoring:
  + compiled files (eg: `.bin`, `.pyc`, `.class` etc.);
  + data files (with the exception of small `sqlite` files);
  + big binaries (eg: `.exe`);
  + libraries (eg: `node_modules`, `bower_components` etc.).
+ use a common `.gitignore` like the one found in **this repo** (language and project-agnostic):
+ `TODO`: some Git workflow described here ?


#### Manage churn:
+ leave `TODO` comments:
  + can be checked with `Intellij`, `Android Studio`, `Webstorm`
  + can be collected by [bithound.io](https://www.bithound.io/) (Node.js only, also supports `HACK`)
+ use milestones, if needed
+ leave issues with feature requirements, bugs ...
+ add common labels to issues (`TODO`)
+ open a project board on github (at least), and organize issues in `Backlog` / `Progress` / `Done`


#### Code quality:
+ `Proposal`: refactor passes:
  + open issue with targeted feature - eg: javadoc
  + mark with emoji in commit and add reference to issue (without closing)
    + no emoji == no refactor passes
    + evaluating quality of code by the number of emojis (eg: 2 emojis - slightly better than 1 ...)

#### Reuse rights:
+ use some basic open source license from the start (usually MIT)

