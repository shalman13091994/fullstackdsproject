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