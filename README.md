# Setup Docker

_______

## Start docker

First, we run the docker on terminal

```
docker-compose up
```

## Connect PGAdmin to Postgres Databse

First see all dockers running in your PC 

```
docker ps
```

Second, verify the COINTAINER ID of postgres:13 and do the follow command:

```
docker inspect 'just the two first numbers of COINTAINER ID '
```

Save postgres IP Address

Third, run on browser 'http://localhost:5050/' and loggin with
```
->EmailUser: root@root.com
->pass: root
```

Fourh
```
Connect with postgresql 
-> Add New Server
General:
-> Choose you databaseName
Connection
->HostName: Enter the Postgres IP Address
->Port: 5432
->Username: postgres
->password:12345
```
## Dont Forget to setup django settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'diam_db',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'PORT': 5432,
    }
}
```

____

