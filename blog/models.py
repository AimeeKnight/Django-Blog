from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, max_length=255)
	description = models.CharField(max_length=255)
	content = models.TextField()
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)

	#tell model class to return obj in descending order
	class Meta:
		ordering = ['-created']

		#returns unicode obj
		def_unicode_(self):
			return u'%s' % self.title

		#links to specific post
		def get_absolute(self):
			return reverse('blog.views.post', args=[self.slug])
