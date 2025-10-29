
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone
from datetime import timedelta

# Додатковий профіль користувача
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	phone = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return f"Profile for {self.user.username}"


class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

	def active_ads_count(self):
		return self.ads.filter(is_active=True).count()


class Ad(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ads')

	def __str__(self):
		return self.title

	def short_description(self):
		return self.description[:100] + ('...' if len(self.description) > 100 else '')

	def deactivate_if_expired(self):
		if self.is_active and timezone.now() > self.created_at + timedelta(days=30):
			self.is_active = False
			self.save()
		return self.is_active


class Comment(models.Model):
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

	def __str__(self):
		return f"Comment by {self.user.username} on {self.ad.title}"

	@staticmethod
	def count_for_ad(ad):
		return Comment.objects.filter(ad=ad).count()
