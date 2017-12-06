from django.db import models

# Create your models here.

class admin_user(models.Model):
    admin_user_id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    head = models.ImageField()
    password = models.CharField(max_length=100)
    email = models.EmailField()

class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    head = models.ImageField()
    password = models.CharField(max_length=100)
    email = models.EmailField()

class article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    subtitle = models.CharField(max_length=140)
    content = models.TextField(default="")
    synopsis = models.CharField(max_length=140,default="")
    time = models.DateTimeField()
    likes = models.BigIntegerField(default=0)
    public = models.BooleanField(default=True)
    reviews = models.BigIntegerField(default=0)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.title

class review(models.Model):
    review_id = models.AutoField(primary_key=True)
    article_id = models.ForeignKey(article, on_delete=models.CASCADE)
    nick = models.CharField(max_length=50)
    content = models.TextField()
    time = models.DateTimeField()
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.content

class reply(models.Model):
    reply_id = models.AutoField(primary_key=True)
    review_id = models.ForeignKey(review, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField()
    public = models.BooleanField(default=True)