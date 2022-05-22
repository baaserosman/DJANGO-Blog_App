from django.db import models
from users_base.models import User

#! Create your models here.


# def user_directory_path(instance, filename):
#    return "myapp/{0}/{1}".format(instance.author.id, filename)
class Category(models.Model):
   name = models.CharField(max_length=100)
   class Meta:
      verbose_name_plural ="Categories"
   def __str__(self):
      return self.name
class Post(models.Model) :
   OPTIONS = (
      ("d", "Draft"),
      ("p", "Published")
   )
   title = models.CharField(max_length=40)
   content = models.TextField(max_length=500)
   image = models.ImageField(upload_to="myapp/", default="django.png")
   publish_date = models.DateTimeField(auto_now_add=True)
   last_update = models.DateTimeField(auto_now=True)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="cars")    
   status = models.CharField(max_length=10, choices=OPTIONS, default="Draft")
   slug = models.SlugField(blank=True, unique=True)         #* django-is-perfekt


   def __str__(self):
      return f"{self.title} - {self.content} - {self.image} - {self.publish_date} - {self.last_update} - {self.category} - {self.status} - {self.slug}"

   # def comment_count(self):
   #    return self.comment_set.all().count()





