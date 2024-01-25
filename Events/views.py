from django.shortcuts import render,redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Event,RegisteredUser
from .forms import UserRegisterForm,UserSignUpForm,UsersLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.hashers import make_password





def index(request):
    context = {
        'Events': Event.objects.all()
    }
    return render(request, 'Events/index.html', context)


class AdminEventListView(LoginRequiredMixin,ListView):
    
    model = Event
    template_name = 'Events/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Events'
    
    

class AddNewEventCreateView(LoginRequiredMixin,CreateView):
    
    model = Event
    fields = ['name', 'description','location','registration_deadline' ]
    success_url = reverse_lazy('event-index')
    

    

class AdminEventUpdateView(LoginRequiredMixin,UpdateView):
    
    model = Event
    fields = ['name', 'description','location','registration_deadline' ]
    success_url = reverse_lazy('event-index')

class AdminEventDeleteView(LoginRequiredMixin,DeleteView):
    
    model = Event
    success_url = reverse_lazy('event-index')

def home(request):
    context = {
        'Events': Event.objects.all()
        
    }
    return render(request, 'Events/home.html', context)



class HomeEventListView(ListView):
    model = Event
    template_name = 'Events/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Events'

class HomeEventDetailView(DetailView):
    model = Event

def register(request,pk):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            event = Event.objects.get(id=pk)
            event.participant.add(new_user)
            return redirect('event-home')
    else:
        form = UserRegisterForm() 

        
    return render(request, 'Events/Register.html', {'form': form})

def participants(request,pk):
    event = Event.objects.get(id=pk)
    
   

    
    return render(request, 'Events/participant.html', {'event': event})

def SignUp(request):
    form = UserSignUpForm()
    errors = []
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data.get('username')
            user.set_password(user.password)
            user.save()
            return redirect('login')
    else:
            error = form.errors
            form = UserSignUpForm()
            context = {
		'form':form,
		'errors': errors
		
	}
    return render(request, 'Events/sign_up.html', context)

def LogIn(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome back {username} !!')
            return redirect('event-index')
        else:
           form = UsersLoginForm
    form = UsersLoginForm()
    return render(request, 'Events/login.html', {'form':form})




    

   




    


    

    

