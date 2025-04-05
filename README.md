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

```