from django.contrib import admin
from .models import Category, Ad, Comment, UserProfile

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name", "description", "active_ads_count")
	search_fields = ("name",)

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
	list_display = ("title", "user", "category", "price", "is_active", "created_at", "updated_at")
	list_filter = ("category", "is_active")
	search_fields = ("title", "description")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ("ad", "user", "created_at")
	search_fields = ("content",)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ("user", "phone", "address")
