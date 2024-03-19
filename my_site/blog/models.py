from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from datetime import date
# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Post(models.Model):
    slug = models.SlugField(default="", unique=True)
    title = models.CharField(max_length=40)
    excerpt = models.CharField(max_length=250)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    image = models.ImageField(upload_to="posts", null=True)
    
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments") #to access all posts through a related field. Adds a comments field on that instance of a post

