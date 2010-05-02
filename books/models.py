from django.db.models import *

class Publisher(Model):
    name = CharField(max_length=30)
    address = CharField(max_length=50)
    city = CharField(max_length=60)
    state_province = CharField(max_length=30)
    country = CharField(max_length=50)
    website = URLField()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering =["name"]

    class Admin:
        pass

class Author(Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=40)
    email = EmailField('e-mail', blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Admin:
        pass

class Book(Model):
    title = CharField(max_length=100)
    authors = ManyToManyField(Author)
    publisher = ForeignKey(Publisher)
    publication_date = DateField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Admin:
        list_display = ('title', 'publisher', 'publication_date')
        list_filter = ('publisher', 'publication_date')
        ordering = ('-publication_date',)
        search_fields = ('title',)
