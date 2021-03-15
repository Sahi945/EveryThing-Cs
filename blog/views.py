from django.shortcuts import render, HttpResponse, redirect
from django.db.models import fields
from django.contrib.auth.models import User
from blog.models import Post, BlogComment, models
from django.views.generic import CreateView
from django.contrib import messages


# Create your views here.
# view is where you build the logic!


def blogHome(request):
    # we are pulling all the object of post by this command line
    allpost = Post.objects.all()
    # here we are declaring a dictionary as context.
    # we'll pass this in the render funtion
    # so that we can extract objects from it using the template coding
    context = {'allposts': allpost}
    return render(request, 'blog/blogHome.html', context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    # remember to change 'post'--> 'post content'
    # also have to change the same in blogPost.html
    print(request.user)
    # context basically help in sending the info/date
    # to the template, where we can extract it
    # note: if post is not passed in context we can
    # no longer display the posts in the blog page

    # in context every key has its value and the key is
    # used to get the data in template eg:(give different name to post)
    context = {'post': post, 'comments': comments, 'user': request.user}
    return render(request, 'blog/blogPost.html', context)
    # return HttpResponse(f'this is: {blog_name}')
    # here the blog_name is a variable


def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)

        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, 'your comment has been added')

        return redirect(f"/blog/{post.slug}")


def addblog(request):

    if request.method == 'POST':
        # image = request.FILES.get('imagefile')
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user
        slug_words = title.split()
        Slug = slug_words[0]
        for word in slug_words[1:]:
            Slug = Slug + "-" + word
        slug = Slug
        blog = Post(title=title,
                    content=content, author=author, slug=slug)
        blog.save()
    return render(request, 'blog/add_post.html')
