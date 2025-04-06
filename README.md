```
git init
```

```
git add abc.txt
git add .
```
```
git commit -m "added git commands"
```

```

git pull

```

```
dagshub

import dagshub
dagshub.init(repo_owner='shalman13091994', repo_name='fullstackdsproject', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


# to have the mlflow in the digshub repo so it can track the experiments also other can access the experiments
# dagshub uri - with digshub it will store in the digshub repo
mlflow.set_registry_uri('https://dagshub.com/shalman13091994/fullstackdsproject.mlflow')
        
tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
print(tracking_url_type_store) # output would be file n save it in digshub
        
# will get under the remote -->experiments --> using mlflow tracking
dagshub.init(repo_owner='shalman13091994', repo_name='fullstackdsproject', mlflow=True)


```

```
process involves in MLOPS:

1.Data versioning -DVC (or alternatives like LakeFS, DeltaLake)
2.Source control Monitoring -Git,Github, gitlab
3.Experiment tracking - MLFlow
4.Feature store - feast, Tecton
5.Model serving - MLflow, FastAPI, TorchServe, Seldon, KServe
6.Model registry - MLflow Model Registry, SageMaker, Azure ML
7.Model monitoring - Prometheus, Grafana, Evidently AI
8.CI/CD pipeline (workflow/scheduling) - GitHub Actions, GitLab CI, Jenkins, Airflow
9.containarisation - Docker
10.Container Orchestration & Monitoring - Kubernetes, Docker Compose, Prometheus + Grafana



Optional (but useful) Add-ons:
Infrastructure as Code – Terraform, Pulumi

Secrets Management – Vault, AWS Secrets Manager

Data Validation – Great Expectations, Deequ

Model Explainability – SHAP, LIME


🔁 Complete MLOps Lifecycle
1. Data Versioning – DVC (or alternatives like LakeFS, DeltaLake)
Tracks changes in datasets and links them to code versions.

Ensures reproducibility and consistency across environments.

2. Source Control – Git, GitHub, GitLab
Tracks changes in code, pipelines, configs.

Enables collaboration via branches, PRs, commits.

3. Experiment Tracking – MLflow, Weights & Biases, Neptune
Logs model parameters, metrics, artifacts, versions.

Helps compare and reproduce model results.

4. Feature Store – Feast, Tecton
Centralized store for preprocessed features.

Ensures consistency between training and production.

5. Model Registry – MLflow Model Registry, SageMaker, Azure ML
Version control for models.

Tracks model stages (Staging, Production, Archived).

Supports model promotion and rollback.

6. Model Serving – MLflow, FastAPI, TorchServe, Seldon, KServe
Deploys trained models as APIs or microservices.

Handles input/output and scalability.

7. Model Monitoring – Prometheus, Grafana, Evidently AI
Tracks model performance, drift, latency, errors.

Alerts if model degrades in production.

8. CI/CD Pipelines – GitHub Actions, GitLab CI, Jenkins, Airflow
Automates model training, testing, and deployment workflows.

Integrates testing, linting, container builds, deployment triggers.

9. Containerization – Docker
Packages model code + dependencies for consistent deployment.

Supports local, cloud, or Kubernetes environments.

10. Container Orchestration & Monitoring – Kubernetes, Docker Compose, Prometheus + Grafana
Manages deployment, scaling, health-checks of containers.

Monitors resource usage, uptime, and logs.

```

```
DVC - Data Version Control

using this we can able to track code + data it works like git but git has some limitation where it can't take huge data files in the repo

DVC works on the git -- like tracking using the changes even made in the files

usually it works for reproducibility like training pipeline and prediction pipelines

However, it works as acyclic graph - DAG - Data Acyclic Graph stage1 -->stage2--> stage3 --> stage4 like that

commands for dvc

1.git init       # if not already done
dvc init

2.Add files
dvc add -- to add the data 
dvc add artifacts/raw.csv

git add artifacts/raw.csv.dvc .gitignore
git commit -m "Track raw data with DVC"



if the data is already remove from the git using   git rm -r --cached 'filename'

also remove the deps files/pkl from the git so that it can be track by DVC

once added it will under dvc -->cache -->file -->md5-->14

4.add remote 

dvc remote add -d myremote <remote-url>
dvc remote add -d storage gdrive://<folder-id>
dvc remote add -d storage s3://mybucket/data

#local
dvc remote add -d remote_storage path/to/your/dvc_remote

5. dvc.yaml 

create config in dvc.yaml with the stages and what are the files to track

dvc push      # Push data to remote storage
git add .     # Track pipeline files
git commit -m "Added DVC pipeline"
git push      # Push code to GitHub



```