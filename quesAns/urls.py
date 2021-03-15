from quesAns.views import postanswer
from django.urls import path, include
from quesAns import views

urlpatterns = [
    path('ask-question-page', views.ask_question_page, name='ask-question-page'),
    path('postAnswer', views.postanswer, name='postAnswer'),
    path('answer-form/', views.answer, name='answer-form'),
    path('question-form/', views.questions, name='question-form'),
    path('questions-home', views.all_questions, name='all-questions'),
    path('<str:slug>', views.question_post, name='question_post'),

]
