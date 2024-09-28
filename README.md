PROJECT URL: https://roadmap.sh/projects/blogging-platform-api

# Simple API Blog Platform

## Goals

_The goals of this project are to help you:_

* Understand what a RESTful API is, including best practices and conventions
* Learn how to create a RESTful API
* Learn about common HTTP methods such as GET, POST, PUT, PATCH, DELETE
* Learn about status codes and error handling in the API
* Learn how to perform CRUD operations using the API
* Learn how to work with databases

## Requirements

_You should create a RESTful API for a personal blogging platform. The API should allow users to perform the following operations:_

* Create a new blog post
* Update an existing blog entry
* Delete an existing blog post
* Get one blog post
* Get all the blog posts
* Filter blog posts by search queries

_You don't need to implement pagination, authentication, or authorization for this project. You can focus on the core functionality of the API._

## Installation and launch

1.`python -m venv venv`

2.`pip install -r requirements.txt`

3.Generate a secret key on this [site](https://djecrety.ir) and paste it into the Django project settings

4.`python manage.py makemigrations`

5.`python manage.py migrate`

6.`python manage.py runserver`