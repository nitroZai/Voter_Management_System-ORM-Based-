
from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Admin, Candidates, Voter
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):

    admins = Admin.objects.all()
    context = {'admins': admins}

    return render(request, 'register.html', context)

def register_save(request):
    
    voter = Voter()

    username = request.POST.get('username')
    email = request.POST.get('email')
    print(request.POST['hub'])
    admin = Admin.objects.get(hub_name = request.POST.get('hub'))
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    
    voter.username = username
    voter.email = email
    voter.admin = admin
    voter.password = password
    voter.password2 = password2
    voter.save()

    return redirect('login')

def login(request):

    context = {}

    return render(request, 'login.html', context)



def loggedin(request):

    username = request.POST.get(
        'username'
    )

    password = request.POST.get(
        'password'
    )

    user = Voter.objects.get(username = username)
    allUsers = Voter.objects.all()

    if user.is_admin == True:
        return render(request, 'adminview.html', {'users':allUsers})

    candidates = Candidates.objects.all()

    context = {
        'user':user,
        'candidates': candidates
    }
    
    try:
        user = Voter.objects.get(username=username)
    except:
        return HttpResponse("<h2>Wrong Username</h2>")
    if user.password == password:
        return render(request, "loggedin.html", context)
    else:
        return HttpResponse("<h2>Wrong Password</h2>")

def aftervote(request):

    username = request.POST.get('username')
    c_name = request.POST.get('vote')
    print(c_name)

    qVar = Candidates.objects.get(name = c_name)
    quantity = qVar.votes
    quantity += 1

    candidate_voted = Candidates.objects.filter(name = c_name).update(votes=quantity)
    rights_off = Voter.objects.filter(username = username).update(is_voted = True)

    return render(request, 'aftervote.html')