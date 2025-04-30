from django.urls import path
from . import views
from .views import QuestionListView  # ⬅️ додано імпорт для DRF view

app_name = 'polls'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.question_list, name='question_list'),

    path('api/questions/', QuestionListView.as_view(), name='questions-api'),
]
