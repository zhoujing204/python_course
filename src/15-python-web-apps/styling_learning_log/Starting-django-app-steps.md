# 创建Django应用程序的步骤

## 1. 创建项目(Windows环境下)

1. 创建虚拟环境

    ```bash
    python -m venv venv
    ```

2. 激活虚拟环境

    ```bash
    venv\Scripts\activate
    ```

3. 安装Django

    ```bash
    pip install -r requirements.txt
    ```

4. 在Django中创建项目

    ```bash
    django-admin startproject ll_project .    
    ```

5. 创建数据库

    ```bash
    python manage.py migrate
    ```

6. 查看项目

    ```bash
    python manage.py runserver
    ```

## 2. 创建应用程序

0. 创建应用

    ```bash
    python manage.py startapp learning_logs
    ```

1. 定义模型

    编辑models.py文件：

    ```python
    from django.db import models

    class Topic(models.Model):
        """A topic the user is learning about."""
        text = models.CharField(max_length=200)
        date_added = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            """Return a string representation of the model."""
            return self.text


    class Entry(models.Model):
        """Something specific learned about a topic."""
        topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
        text = models.TextField()
        date_added = models.DateTimeField(auto_now_add=True)

        class Meta:
            verbose_name_plural = 'entries'

        def __str__(self):
            """Return a simple string representing the entry."""
            return f"{self.text[:50]}..."
    ```

2. 激活模型

    编辑settings.py文件(在目录ll_project中)：

    ```python
    INSTALLED_APPS = [
        # My apps
        'learning_logs',

        # Django apps
        'learning_logs.apps.LearningLogsConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```

    执行如下命令, 让Django修改数据库：

    ```bash
    python manage.py makemigrations learning_logs
    python manage.py migrate
    ```

3. Django管理网站

    3.1 创建超级用户
    执行下面的命令，输入超级用户的用户名、电子邮件地址和密码：

    ```bash
    python manage.py createsuperuser    
    ```

    3.2 向管理网站注册模型
    在models.py所在目录下，Django创建了admin.py文件，编辑该文件：

    ```python
    from django.contrib import admin

    # Register your models here.
    from .models import Topic
    admin.site.register(Topic)
    ```

    3.3 运行管理网站
    访问<http://localhost:8000/admin>，输入用户名和密码，登录管理网站。

4. Django shell
   可以通过交互式终端会话编程的方式查看这些数据。执行下面的命令：

    ```bash
    python manage.py shell
    ```

    在交互式终端会话中，导入模型Topic：

    ```python
    >>> from learning_logs.models import Topic
    >>> Topic.objects.all()
    <QuerySet [<Topic: Chess>, <Topic: Rock Climbing>, <Topic: Cooking>]>
    ```
