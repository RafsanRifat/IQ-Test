from django.contrib import admin
from .models import Questions, Question_sets, Options, Answer

# Register your models here.

admin.site.register(Questions)
admin.site.register(Question_sets)
admin.site.register(Options)
admin.site.register(Answer)

