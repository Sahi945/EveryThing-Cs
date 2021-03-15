from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from quesAns.models import Question, answer
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def questions(request):
    if request.method == 'POST':
        ques_title = request.POST['title']
        content = request.POST['content']
        author = request.user
        slug_words = ques_title.split()
        Slug = slug_words[0]
        for word in slug_words[1:]:
            Slug = Slug + "-" + word
        slug = Slug
        ques = Question(title=ques_title, content=content,
                        author=author, slug=slug)
        ques.save()

    messages.success(request, 'your question has been posted')
    return redirect('all-questions')


def postanswer(request):
    if request.method == 'POST':
        Answer = request.POST.get('answer')
        author = request.user
        title = request.POST.get('question')
        question = Question.objects.get(title=title)
        ans = answer(question=question, answer=Answer, author=author)
        ans.save()
        messages.success(request, 'your answer has been posted')

        return redirect(f"/doubts/{question.slug}")


def all_questions(request):
    allques = Question.objects.all()
    context = {'allques': allques}
    return render(request, 'questions/questions_home.html', context)


def question_post(request, slug):
    question = Question.objects.filter(slug=slug).first()
    answers = answer.objects.filter(question=question)
    context = {'question': question, 'answers': answers}
    return render(request, 'questions/question_post.html', context)


def ask_question_page(request):
    return render(request, 'questions/ask_question.html')
