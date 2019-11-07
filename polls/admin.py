from django.contrib import admin

from .models import Question, Choice


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Question details', {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['expand']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
