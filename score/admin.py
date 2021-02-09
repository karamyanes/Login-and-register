from django.contrib import admin
from .models import Answer
from .models import Question
from .models import UserQuestionHistory
from .models import Result
from .models import Game



# Register your models here.
admin.site.register(Game)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(UserQuestionHistory)
admin.site.register(Result)