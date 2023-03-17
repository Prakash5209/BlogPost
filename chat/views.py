from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from chat.models import Message
from chat.forms import ChatForm

User = get_user_model()

def message(request):
    users = User.objects.filter().exclude(id = request.user.id)
    context = {'users':users}
    return render(request,'message.html',context)

def message_to_user(request,username):
    users = User.objects.filter().exclude(id = request.user.id)
    to_user = User.objects.get(username = username)
    messages = Message.objects.filter(
        from_user__in = [request.user,to_user],
        to_user__in = [request.user,to_user],
    )
    form = ChatForm(request.POST or None)
    if form.is_valid():
        message = form.save(commit = False)
        message.from_user = request.user
        message.to_user = to_user
        message.save()
        return HttpResponseRedirect(reverse('chat:message_to_user', args=(username,)))
    context = {'form':form,'conversation':messages,'users':users,'username':username}
    return render(request,'message.html',context)