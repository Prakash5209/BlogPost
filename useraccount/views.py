from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth import get_user_model,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from useraccount.models import Profile
from useraccount.forms import SignUpForm,ProfileForm

User = get_user_model()

# def usersignup(request):
#     form = SignUpForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('post:home')
#     context = {'form':form}
#     return render(request,'signup.html',context)

class SignupView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    model = User
    success_url = reverse_lazy('useraccount:login')
    
    def form_valid(self,form):
        user = form.save()
        Profile.objects.create(user = user)
        return super().form_valid(form)

def userlogin(request):
    form = AuthenticationForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user:
            login(request,user)
            return redirect('post:home')
        else:
            return redirect('useraccount:userlogin')
    context = {'form':form}
    return render(request,'login.html',context)

def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('post:home'))

def profileview(request,username):
    user = get_object_or_404(User,username = username)
    form = None
    if request.user.is_authenticated and request.user.username == username:
        user = request.user
        initial_data = {
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email':user.email,
            }
        form = ProfileForm(instance=user.profile,initial=initial_data)
    context = {'user':user,'form':form}
    return render(request,'profile.html',context)

def profileupdate(request):
    form = ProfileForm(request.POST or None, request.FILES or None,instance = request.user.profile)
    if form.is_valid():
        user = request.user
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.email = form.cleaned_data.get('email')
        user.save()
        form.save()
        return HttpResponseRedirect(reverse('useraccount:profileview',args = (request.user.username,)))
    context = {'form':form}
    return render(request,'profile.html',context)


