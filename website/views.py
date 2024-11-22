from django.shortcuts import get_object_or_404, redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import logout
from .models import Voter,Ballot

# Create your views here.
def home(request):
    return render(request, 'login.html')


def login_user(request):
    leaders = Ballot.objects.all()
    voters = Voter.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'login.html', {'leaders': leaders, 'voters': voters})
        else:
            messages.info(request, "Invalid credentials. Please try again.")
            return redirect('login')
    else:
        return render(request, 'login.html', {'leaders': leaders, 'voters': voters})



def logout_user(request):
    logout(request)
    return redirect('login')
    
def register_user(request):
    if request.method == "POST":
        voter_id=request.POST['voter_id']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address=request.POST['address']
        is_voted=False

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists..")
                return redirect('register')
            elif Voter.objects.filter(voter_id=voter_id).exists():
                messages.info(request, "Voter id already exists..")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "user name already exists..")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                Voter.objects.create(voter_id=voter_id,user_name=username,email=email,is_voted=is_voted,address=address)
                messages.success(request, "Registration successful!")
                return redirect('login')
        else:
            messages.info(request, "Both passwords are not the same...")
            return redirect( 'register')
    else:
        return render(request, 'register.html')
    
def vote(request, pk1, pk2):
    leader = get_object_or_404(Ballot, id=pk1)
    voter = get_object_or_404(Voter, user_name=pk2)
    
    if voter.is_voted:
        return redirect('home')
    leader.total_votes += 1
    leader.save()
    voter.is_voted = True
    voter.save()
    messages.info(request,"You successfully casted your vote! Thank you for voting.")
    return redirect('logout')


def results(request):
    ballots=Ballot.objects.all()
    return render(request,'results.html',{'leaders':ballots})