from django.db import models
from django.utils import timezone

# Create your models here.
class Entry(models.Model):
    entry_name = models.CharField(max_length=200)
    entry_text = models.TextField(max_length=10000)
    entry_author = models.CharField(max_length=30)
    publish_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return u'%s %s %s %s' % (self.entry_name, self.entry_text, self.entry_author, self.publish_date)

class Archive(models.Model):
    all_entries = models.ForeignKey(Entry)    
    
    def __unicode__(self):
        return self.all_entries
#more research needs to be done about function below and the permalink() decorator        
    def get_absolute_url():
        return "/archive/%i/" % self.id    
        

class Author(models.Model):
    entries_by_author = models.ForeignKey(Entry)
    
    def __unicode__(self):
        return self.entries_by_author
        
    def get_absolute_url():
        return "/author/%i/" % self.id