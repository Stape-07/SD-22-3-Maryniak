from django.urls import path
from polls.views import QuestionListView

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='questions-api'),
]
