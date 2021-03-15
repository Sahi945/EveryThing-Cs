from django.db import reset_queries
from django.db.models import query
from django.shortcuts import render, HttpResponse, redirect
# now we'll be importing home models to store the
# data in the contact model
from home.models import Contact
# for using message for alerting
from django.contrib import messages
# important we are using "auth.models" since a model "User"
# is already created in django admin which will handle user
# signup and we explicitly dont have to make a model for user
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from quesAns.models import Question

# Create your views here.


def home(request):
    top_posts = Post.objects.all().order_by('-timeStamp')[:3]
    ques = Question.objects.all().order_by('-time_stamp')[:3]
    context = {'top_posts': top_posts, 'ques': ques}

    return render(request, "home/home.html", context)


def search(request):
    query = request.GET['query']
    allposts = Post.objects.filter(title__icontains=query)
    all_questions = Question.objects.filter(title__icontains=query)
    params = {'allposts': allposts, 'allquest': all_questions}
    return render(request, "home/search.html", params)


def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        # make an object of Contact model
        if len(name) < 2:
            messages.error(request, 'your form has not been submitted')
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            # we also need to save it to as to reflect in django admin
            contact.save()
            messages.success(request, 'your issue has been submitted!')

    return render(request, 'home/contact.html')

# now makind vewis for signup page


def handleSignup(request):
    if request.method == 'POST':

        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

    # checking user inputs valid credentials
        if len(username) > 10:
            messages.error

    # creating users
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, 'your account have been successfully created!')

        return redirect("home")

    else:
        return HttpResponse("error 404 not found")

# handling login and logout


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpassword)
        # the above line will retun none if the user is not found
        # therfore:

        if user is not None:
            login(request, user)
            messages.success(request, "welcome aboard!")
            return redirect("home")
        else:
            messages.error(request, "Sorry invalid credentials, try again!")
            return redirect('home')


def handleLogout(request):
    logout(request)
    messages.warning(request, "session logged out!")
    return redirect("/")


def doubts(request):
    return render(request, "questions/doubts.html")


def loginpage(request):
    return render(request, "home/login.html")


def signuppage(request):
    return render(request, "home/signup.html")


def addpost(CreateView):
    model = Post
    template = 'add_post.html'
    fields = '__all__'
