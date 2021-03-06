# core [![travis status](https://travis-ci.org/xR86/core.svg?branch=master)](https://travis-ci.org/xR86/core) [![license](https://img.shields.io/badge/license-MIT-blue.svg?maxAge=2592000)](https://github.com/xR86/cs-platform/blob/master/LICENSE)

My main repo for pointing to other repos and writing core policies for all repos (usually public repos, private repo will have their own policies)

---

### Fast pointers

`In a hurry ?` Check [xr86.github.io](https://xr86.github.io/) for some highlights for what I do (`TODO`: will be updated with tags for topics).  
`Not really, but little time...` Try [students.info.uaic.ro/~dan.alexandru](http://students.info.uaic.ro/~dan.alexandru/) and see a more detailed chronology.


[![Abstract Processing Core](processing_core.png)](http://freakinlobstah.deviantart.com/art/Abstract-processing-core-455670942)


---

## Core policies in repo:

`TODO`: Automate this by unit tests and a Travis build ?  
Simplest would be to use Python scripts and repos language, but: [github.com/travis-ci/travis-ci/issues/4090](https://github.com/travis-ci/travis-ci/issues/4090)


#### Accesibility:
+ use topics in repo - easier to be found, indexed ...
+ project description
+ screenshots, terminal session recording ([asciinema](https://asciinema.org/))
+ READMEs, a lot of READMEs - and badges for:
  + license
  + build status
  + code coverage
  + extra ... downloads / slack / other CIs / etc.
+ code quality: :star2::star2::star2: / 5
https://www.webpagefx.com/tools/emoji-cheat-sheet/

#### Manage churn (code documentation and backlog):
+ leave `TODO` comments:
  + can be checked with `Intellij`, `Android Studio`, `Webstorm`
  + can be collected by [bithound.io](https://www.bithound.io/) (Node.js only, also supports `HACK`)
+ use milestones, if needed
+ leave issues with feature requirements, bugs ...
+ add common labels to issues (`TODO`)
+ open a project board on github (at least), and organize issues in `Backlog` / `Progress` / `Done`

