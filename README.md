# End-to-end ML project with with MLFlow and AWS for Wine Quality Prediction

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity (`config_entity.py`)
5. Update the configuration manager in `configuration.py`
6. Update components
7. Update the pipeline (`<task_pipeline>.py`)
8. Update `main.py`
9. Update `app.py`

# How to run?
### STEPS:

Clone the repository

```zsh
git clone https://github.com/ShreCodes2809/shres-mlops-project.git
```
### STEP 01- Create an environment after opening the repository

```zsh
python3 -m venv .mlops_env
```

```zsh
source .mlops_env/bin/activate
```


### STEP 02- install the requirements
```zsh
pip install -r requirements.txt
```


```zsh
# Finally run the following command
python app.py
```

Now, open your local host and port by pressing (Command + Click) -> Mac or (Ctrl + Click) otherwise. Here's an example of how it might look like:
```zsh
http://127.0.0.1:8080
```



## MLflow

Here's a documentation for MLFlow: [Documentation](https://mlflow.org/docs/latest/index.html)

### Creating a Dagshub account for model evaluation tracking:
1. Login into [dagshub](https://dagshub.com/) using your GitHub account
2. Click on "Create a repository" -> "Connect to a repository"
3. Click on GitHub -> "Add/revoke access to repositories" -> Select the repository
4. To start tracking the experiments, first copy the MLFlow tracking URI, username (since you're connected to your GitHub account, your username will usually be the same as your GitHub account) and password (or can use tokens created through `Settings -> Tokens -> Regenerate -> Copy Token`).

Run this to export as env variables:

```zsh
export MLFLOW_TRACKING_URI=<PASTE MLFLOW TRACKING URI HERE>
export MLFLOW_TRACKING_USERNAME=<PASTE MLFLOW USERNAME HERE> 
export MLFLOW_TRACKING_PASSWORD=<PASTE PASSWORD/TOKEN HERE>
```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model
