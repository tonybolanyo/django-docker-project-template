## How to use

It's recommended create a virtual environment before proceed.

You need to install Django (2.0 and above) and use `django-admin` command
to create a new project using this template as shown:

```bash
mkdir src
django-admin startproject --template=https://github.com/tonybolanyo/django-project-template/archive/master.zip --extension=py <project_name> src
```

**Note:** switch master.zip to develop.zip if you want to use a night build version.

Next, edit `django.env` file and change `{{ project_name }}` with the name od your project so Django can find the settings module.
