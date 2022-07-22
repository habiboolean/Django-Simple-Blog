
# Django-Simple-Blog 📝

Django Simple Blog is a MVP(Minimal Viable Product) blogging app in django, made as a pet project for educational purpose

# DEMO


https://user-images.githubusercontent.com/105993976/180430612-0b19d68c-9c58-4534-8ad1-16884ffcb7be.mp4





## Tech Stack
- **Frontend:** HTML / CSS / Bootstrap (5.2)
- **Backend:** Django (4.0.5) / Django-Rest-Framework (3.13.1)
- **Database:** Postgres

## Features:
- **Login / Register:** abstract user class implemented for easy customisation as [django-docs recommend](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project)
- **WYSIWYG Editor:** TinyMCE used as text editor.
- **Image Uploading:** Users can upload images for their posts, that will be converted into .webp format automatically,to save some space. Also images get into **/media/posts/year/month/day/** to reduce load on a File System
- **DRF API:** Api for future frontend side of the project. JWT not implemented because of simplicity of the project.
- **Posting / Editing:** Registered users can post and edit own posts
- **Private posts:** Users can make their posts private
- **Filtering:** Clicking on author username will show public posts of this author. Or public + private posts of current logged user.

## TODO:
- Cover with tests (pytest)
- Add comments to posts
- Likes/Dislikes rating system
- Search

## Quick Start

- Fork and Clone the repository using:
```
git clone https://github.com/habiboolean/Django-Simple-Blog.git
```
- Create virtual environment:
```
python -m venv env
env\Scripts\activate
```
- Install dependencies using:
```
pip install -r requirements.txt
```
- Put your database connection settings:
```
settings.py line 95
```
- Headover to Project Directory:
```
cd BlogPetProject
```
- Make migrations using:
```
python manage.py makemigrations
```

- Migrate Database:
```
python manage.py migrate
```
- Create a superuser:
```
python manage.py createsuperuser
```
- Run server using:
```
python manage.py runserver
```

## Useful Resources to Learn

- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [DRF](https://www.django-rest-framework.org/)
- [Bootstrap Docs](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
- [TinyMCE](https://www.tiny.cloud/)

>![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)
>![made-with-django (1)](https://user-images.githubusercontent.com/105993976/180402230-5ea9fab8-edc6-4b53-bd98-c60c5be84872.svg)


