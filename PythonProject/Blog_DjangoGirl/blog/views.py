from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
#immediately go to the post_detail page for our newly created blog post
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.order_by('published_date')
    
    return render(request, 'blog/post_list.html', {'posts': posts})
    #return render(request, 'blog/post_list.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    #So in our view we have two separate situations to handle: 
    # first, when we access the page for the first time and we want a blank form, 
    # and second, when we go back to the view with all form data we just typed. 
    # So we need to add a condition (we will use if for that):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            #commit=False means that we don't want to save the Post model yet 
            #Most of the time you will use form.save() without commit=False
            post = form.save(commit = False)
            #we want to add the author first (since there was no author field in the PostForm and this field is required)
            post.author = request.user
            post.published_date = timezone.now()
            #post.save() will preserve changes (adding the author) and a new blog post is created!
            post.save()
            #redirect(view.methodname, viewmethod parameters)
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request,'blog/post_edit.html',{'form':form})

def post_edit_viewname(request,pk,test):
    post = get_object_or_404(Post, pk=pk)
    test = test
    if request.method == "POST":
        #difference from post_new view
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        #difference from post_new view
        form = PostForm(instance=post)
    return render(request,'blog/post_edit.html',{'form': form})
