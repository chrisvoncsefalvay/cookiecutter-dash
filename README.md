# cookiecutter-dash

![Proudly created at Starschema](https://img.shields.io/badge/Created_at-Starschema-red) ![GitHub top language](https://img.shields.io/github/languages/top/chrisvoncsefalvay/cookiecutter-dash) ![GitHub All Releases](https://img.shields.io/github/downloads/chrisvoncsefalvay/cookiecutter-dash/total) ![GitHub issues](https://img.shields.io/github/issues/chrisvoncsefalvay/cookiecutter-dash) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/chrisvoncsefalvay/cookiecutter-dash) ![GitHub forks](https://img.shields.io/github/forks/chrisvoncsefalvay/cookiecutter-dash?label=Fork%20me%21&style=social) ![Twitter Follow](https://img.shields.io/twitter/follow/chrisvcsefalvay?style=social)

A cookiecutter to generate Dash app skeletons.

* `Makefile` to generate Docker image (`make image`)
* Bootstrap integration and navbar chrome
* Dockerfile for deployment on ECS (see [instructions](https://www.chrisvoncsefalvay.com/2019/08/28/deploying-dash-on-amazon-ecs/))
* `DangerouslySetInnerHTML` included to allow you to inject pure HTML
* A choice of auto-generated licenses


## Usage

To build your Dash app, use

```
cookiecutter https://github.com/chrisvoncsefalvay/cookiecutter-dash
```

Parameters:


| Parameter                	| Default value          	| Description                                 	|
|--------------------------	|------------------------	|---------------------------------------------	|
| `project_name`           	| `My Dash application`  	| Project name – appears in description, etc. 	|
| `repo_name`              	|                        	| Normalised repo name                        	|
| `package_name`           	|                        	| Normalised package name                     	|
| `àuthor_name`            	| `Your name`            	| Package author's name                       	|
| `author_email`           	| `you@are.aweso.me`     	| Package author's e-mail                     	|
| `author_github_username` 	| `your_github_username` 	| Package author's github username            	|
| `description`            	|                        	| Your project's short description            	|
| `version`                	| `0.1.0`                	| Project version                             	|
| `license`                	|                        	| Choice of a number of licenses.             	|


## Support

There's a [dedicated discussion thread on the Plotly Discourse server for `cookiecutter-dash`](https://community.plot.ly/t/the-fastest-way-to-get-started-building-a-dash-app-cookiecutter-dash/28568). For questions that aren't issues or bugs, you might want to go there. 

If you detect a bug, please file an issue under the Issues tab.


## Contributing

Contributions are welcome! Go to the Issues tab to see where we need help. If you have a feature suggestion, please propose it as an issue before creating a pull request, so that it can be properly discussed. Thanks!
