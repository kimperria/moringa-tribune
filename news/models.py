from django.db import models

# Create your models here.
class Editor(models.Model):
    '''
    Class that instanciates editor table
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        # try:
        #     editor = Editor.objects.get(email='example@gmail.com')
        #     print('Editor not found')
        # except DoesNotExist:
        #     print('Editor was not found')

        return self.first_name
    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name    

class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)