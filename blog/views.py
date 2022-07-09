from django.shortcuts import render, redirect
from blog.models import Post, BlogComment
from django.contrib import messages

# Create your views here.

def error_404_view(request, exception):
    return render(request,'blog/404.html',)

def home(request):
    allPost = Post.objects.all().order_by('-time_stamp')[:5]
    context = {'allPost': allPost}
    return render(request, 'blog/index.html', context)

def showAllPost(request):
    
    posts = Post.objects.all().order_by('-time_stamp')
    context = {'posts': posts}
    return render(request, 'blog/showAllPost.html', context)

def posts(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comment = BlogComment.objects.filter(post=post, parent = None)
    parent = BlogComment.objects.filter(parent=comment)
    context = {'post': post, 'comment': comment}
    return render(request, 'blog/post.html', context)


def posts2(request,slug1,slug2):
    post = Post.objects.filter(slug=slug2).first()
    comment = BlogComment.objects.filter(post=post, parent = None)
    parent = BlogComment.objects.filter(parent=comment)
    context = {'post': post, 'comment': comment}
    return render(request, 'blog/post.html', context)


def filterposts(request,category):
    post = Post.objects.filter(category=category).all()
    context = {'post': post,}
    return render(request, 'blog/filterpost.html', context)



def postcomment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        postsno = request.POST['sno']
        post = Post.objects.get(sno=postsno)
        user = request.user
        ParentSno = request.POST['ParentSno']
        
        if ParentSno == "":
            comment = BlogComment(comment = comment, user=user, post=post)
        else:
            parent = BlogComment.objects.get(sno=ParentSno)
            comment = BlogComment(comment = comment, user=user, post=post, parent=parent)
        
        comment.save()
            
        #messages.success(request, 'your comment has been sent successfully')
        return redirect(f'/posts/{post.slug}')
        
    return redirect(f'/posts/{post.slug}')
    
def about(request):
    return render(request, 'blog/about.html')

def disclaimer(request):
    return render(request, 'blog/disclaimer.html')