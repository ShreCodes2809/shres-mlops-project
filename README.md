# 🍇 Wine Quality Prediction - End-to-End ML Project with MLflow, AWS, and Docker

This repository implements a full-stack MLOps pipeline for wine quality prediction using `scikit-learn`, tracked with `MLflow`, containerized with `Docker`, and deployed via `AWS EC2` + `ECR` using GitHub Actions.

---

## 🔀 Workflow Overview

1. Configure data ingestion and model settings via:

   * `config.yaml`
   * `params.yaml`
   * `schema.yaml`

2. Define configuration entities in `config_entity.py`

3. Implement a configuration manager in `configuration.py`

4. Build modular components (e.g. data ingestion, transformation, model trainer)

5. Construct pipeline orchestration scripts: `pipeline/<stage>_pipeline.py`

6. Define app behavior in `main.py` and `app.py`

---

## 🚀 Getting Started

### 1. Clone the repository

```zsh
git clone https://github.com/ShreCodes2809/shres-mlops-project.git
cd shres-mlops-project
```

### 2. Create and activate a virtual environment

```zsh
python3 -m venv .mlops_env
source .mlops_env/bin/activate
```

### 3. Install dependencies

```zsh
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the application

```zsh
python app.py
```

### 5. Once the application is running, access the app at its respective domain and port number as follows:

```zsh
http://127.0.0.1:8080
```

---

## 📊 MLflow Tracking

MLflow helps track, compare, and manage ML experiments.

### 🌐 Setting Up MLflow with DagsHub

1. Log in to [DagsHub](https://dagshub.com) via GitHub.
2. Create a new repo and link your GitHub repository.
3. Navigate to **Settings → Tokens** and generate a personal access token.
4. Export the following environment variables:

```bash
export MLFLOW_TRACKING_URI=<YOUR_MLFLOW_TRACKING_URI>
export MLFLOW_TRACKING_USERNAME=<YOUR_DAGSHUB_USERNAME>
export MLFLOW_TRACKING_PASSWORD=<YOUR_DAGSHUB_TOKEN>
```

📙 [Official MLflow Docs](https://mlflow.org/docs/latest/index.html)

---

## ☁️ AWS CI/CD Deployment with GitHub Actions

### ✅ Step-by-Step Breakdown

#### 1. **Login to AWS Console**

#### 2. **Create an IAM User for Deployment**

Attach the following policies:

* `AmazonEC2FullAccess`
* `AmazonEC2ContainerRegistryFullAccess`

#### 3. **Create an ECR Repository**

Save the URI (example):

```
566382916292.dkr.ecr.ap-south-1.amazonaws.com/mlproj
```

#### 4. **Create an EC2 Ubuntu Instance**

#### 5. **Install Docker on EC2**

```bash
sudo apt-get update -y && sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

#### 6. **Set Up EC2 as a GitHub Self-Hosted Runner**

`GitHub → Repo Settings → Actions → Runners → Add Runner`
Follow the shell commands as provided for Ubuntu.

#### 7. **Configure GitHub Secrets**

Go to GitHub → Settings → Secrets → Actions:

| Key                     | Value (example)                                 |
| ----------------------- | ----------------------------------------------- |
| `AWS_ACCESS_KEY_ID`     | Your AWS access key                             |
| `AWS_SECRET_ACCESS_KEY` | Your AWS secret key                             |
| `AWS_REGION`            | `us-east-1` (or your region)                    |
| `AWS_ECR_LOGIN_URI`     | `566382916292.dkr.ecr.ap-south-1.amazonaws.com` (first part of the URI) |
| `ECR_REPOSITORY_NAME`   | `mlproj` (second part of the URI)                                        |

---

## 🧠 About MLflow

MLflow provides:

* ✅ Experiment tracking
* ✅ Reproducible runs
* ✅ Model packaging and deployment
* ✅ Integration with DVC, DagsHub, and cloud platforms

Use it to **log, compare, and promote** models seamlessly in production workflows.

---

## 🛠️ Tech Stack

* **Python 3.8**
* **scikit-learn**
* **numpy**
* **pandas**
* **flask**
* **Jupyter Notebook**
* **MLflow**
* **Docker**
* **AWS EC2 + ECR**
* **GitHub Actions**
* **DagsHub** for experiment tracking

---

## 👨‍💻 Author

**Shreyash Sahare**
[GitHub](https://github.com/ShreCodes2809) • [LinkedIn](https://www.linkedin.com/in/shreyashsahare28/)

---

## 🏑️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
