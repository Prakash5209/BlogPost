from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect,JsonResponse
from post.forms import CreatePostForm,GroupDiscussionForm
from post.models import CreatePost,GroupDiscussion,Like

def home(request):
    variable = CreatePost.objects.all()
    context = {'variable':variable}
    return render(request,'home.html',context)

@login_required
def createpost(request):
    form = CreatePostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.user = request.user 
        obj.save()
        messages.add_message(request,messages.SUCCESS,'Post Created!')
        return HttpResponseRedirect(reverse('post:home'))
        # return redirect('post:home')
    context = {'form':form}
    return render(request,'createpost.html',context)

@login_required
def selectedTopic(request,pk):
    post = get_object_or_404(CreatePost,id = pk)
    discussion = post.group_chat.all()
    form = GroupDiscussionForm(request.POST or None)
    if form.is_valid():
        discussions = form.save(commit = False)
        discussions.post = post
        discussions.user = request.user if request.user.is_authenticated else None
        discussions.save()
        return HttpResponseRedirect(reverse('post:selectedTopic', args = (pk,)))
    context = {'post':post,'discussion':discussion,'form':form}
    return render(request,'groupdiscussion.html',context)

@login_required
def editTopic(request,pk):
    post = get_object_or_404(CreatePost,id=pk,user = request.user)
    form = CreatePostForm(request.POST or None, request.FILES or None, instance = post)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.user = request.user
        obj.save()
        messages.add_message(request,messages.SUCCESS,'post updated!')
        return HttpResponseRedirect(reverse('post:selectedTopic', args = (pk,)))
        # return redirect('post:selectedTopic',args=(pk,))
    context = {'form':form}
    return render(request,'editpost.html',context)    

@login_required
def delete_post(request,pk):
    obj = get_object_or_404(CreatePost,id = pk,user = request.user)
    if request.method == 'POST':
        obj.delete()
        messages.add_message(request,messages.INFO,'post deleted!')
        return HttpResponseRedirect(reverse('post:home'))
        # return HttpResponseRedirect(reverse('post:selectedTopic',args=(pk,)))
    context = {'obj':obj}
    return render(request,'deletepost.html',context)


@login_required
def like_post(request,postid):
    post = get_object_or_404(CreatePost,id = postid)
    user = request.user
    like,created = Like.objects.get_or_create(post = post,user = user)
    if not created:
        if like.is_liked:
            like.is_liked = False
        else:
            like.is_liked = True
        like.save()
    total_likes = post.likes.filter(is_liked = True).count()
    return JsonResponse({"likes":total_likes},safe = False)