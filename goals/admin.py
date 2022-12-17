from django.contrib import admin

from goals.models.models import GoalCategory, Goal, GoalComment, Board


class BaseAdmin(admin.ModelAdmin):
	list_display = ("title", "user", "created", "updated")
	search_fields = ("title", "user")
	readonly_fields = ("created", "updated")


class GoalCategoryAdmin(BaseAdmin):
	pass


class GoalAdmin(BaseAdmin):
	list_display = ("title", "user", "category", "created", "updated")
	search_fields = ("title", "user", "category")


class GoalCommentAdmin(BaseAdmin):
	list_display = ("goal", "user", "created", "updated")
	search_fields = ("goal", "user", "text")


class BoardAdmin(BaseAdmin):
	list_display = ("title", "created", "updated")
	search_fields = ("title",)


admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(GoalComment, GoalCommentAdmin)
admin.site.register(Board, BoardAdmin)