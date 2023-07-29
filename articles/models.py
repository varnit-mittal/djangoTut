from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=50,null=True, blank=True)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    publish=models.DateField(auto_now_add=False,auto_now=False,default=timezone.now,null=True,blank=True)
    '''
    null=true means that database can have this field as an empty value and 
    blank=true means that it is not necessary to fill up this field
    '''

    def save(self, *args, **kwargs):
        #obj=Article.objects.get(id=1)
        #set something
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
        #obj.save()
        #do another something