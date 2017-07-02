# Author: Shailesh Rudra

This repository is created to collect all basic stuff and common requirement demo.

## Todo List for this repo:
* Custom User model
* Base app for common model and admin
* Custom admin panel
* Custom permission management
* Custom widgets
* S3 image field example
* Celery configuration
* Redis configuration
* Infinite load more
* Pagination demo
* Basic utility file
* Context processor example 
* Middleware example 
* REST framework demo 
* Angular demo 
* Social login 
* Internationalisation in admin panel, API and website

# Server configuration:
* Apache with uWSGI & Gunicorn
* Nginx with uWSGI & Gunicorn


## Celery setup: 

First install rabbitmq or radis server. 

For now i am using RabbitMQ:

* Install on ubuntu using apt-get:
sudo apt-get install rabbitmq-server

* For other OS please refer below link:
http://www.rabbitmq.com/install-debian.html

* Celery is working or not testing:
http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html

For development server:
celery -A standard_django worker -l info

For live server celery should be daemon process:
http://docs.celeryproject.org/en/latest/userguide/daemonizing.html#daemonizing

https://github.com/celery/celery/tree/master/extra/supervisord


# Rest Framework integration

* User registration
* Login API
* Logout API

# Swagger integration API doc integration 
