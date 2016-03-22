# Auto_Deployment

* apt-get update
* apt-get install python-pip python-dev build-essential 
* apt-get install tree
* pip install django
* django-admin startproject mysite
* python manage.py runserver
* apt-get install -y python-mysqldb

### Time Zone
http://www.cnblogs.com/xwdreamer/archive/2013/11/06/3409947.html

### 如果让外网访问 Django
python manager.py runserver 0.0.0.0:8000

### Create admin
python manage.py createsuperuser 

### Set Time Zone
>TIME_ZONE = 'Asia/Shanghai'
>USE_TZ = False

## MySQL Time Zone

```
[mysqld]
default-time-zone = '+8:00'
```
