# Product Analytics
Product Analytics API using DJango Framework


## Installations
```
pip install django djangorestframework django-redis
```

## Create Django Project
```
django startproject product
cd product
```

## Create App as api
```
py manage.py startapp <app_name>
```

## Run Server
```
cd product
py manage.py runserver
``` 

## Create DB into Database
```
py manage.py sqlmigrate api 0001
```

## Import Dataset into Database
> File in Management/commands/import_csv.py file runs a bulk insert command to the sqllite database.
> Run the command to insert the dataset
```
python manage.py import_csv path/to/large_dataset.csv
```

## Connection to redis cache
In `settings.py` file update the redis connection ***LOCATION*** with ***redis connection info***