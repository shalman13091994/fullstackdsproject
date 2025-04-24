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
