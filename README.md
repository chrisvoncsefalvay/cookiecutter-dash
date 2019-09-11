# cookiecutter-dash

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
