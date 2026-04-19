from django.contrib import admin

# ✅ Import ALL required models (7 classes)
from .models import Course, Lesson, Instructor, Learner, Enrollment, Question, Choice, Submission


# ✅ Inline for Choice inside Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# ✅ Inline for Question inside Lesson
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


# Existing inline (keep it)
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Course admin (unchanged)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# ✅ LessonAdmin WITH QuestionInline
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]


# ✅ QuestionAdmin WITH ChoiceInline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


# ✅ Register ALL models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)
admin.site.register(Instructor)
admin.site.register(Learner)
