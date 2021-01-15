from django.db import models


# class UserFeed(models.Model):
#     first_name = models.CharField(max_length=100, blank=False)
#     username = models.CharField(max_length=100, unique=True, null=False)
#     password = models.CharField(max_length=32, null=False)

#     def __str__(self):
#         return f"{self.first_name} username: {self.username}"

class SiteConfig(models.Model):
    site_address = models.CharField(max_length=120, null=False, blank=False)
    articles = models.IntegerField()
    frequency = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='site_configs', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(SiteConfig, self).save(*args, **kwargs)


class SiteContent:
    def __init__(self, site_name, content):
        self._site_name = site_name
        self._content = content
    
    @property
    def site_name(self):
        return self._site_name
    
    @property
    def content(self):
        return self._content