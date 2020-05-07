from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from econapp.forms import UserloginForm
from econapp.models import Person, User




def first_page(request):
    return render(request, 'base.html')


def dellivery(request):
    return render(request, 'dellivery.html')


def installment(request):
    return render(request, 'installment.html')


def login_view(request):
    next_ = request.GET.get("next")
    if request.method == 'POST':
        form = UserloginForm(request.POST or None)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username.strip(), password=password.strip())
            login(request, user)
            next_post = request.POST.get('next')
            rederict_path = next_ or next_post or '/'
            return redirect(rederict_path)
    else:
        form = UserloginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("base")


def personal_account(request):
    return render(request, "account.html")


def index(request):
    if request.user.is_authenticated:
        # User.login = request.user.username
        # count = Person.objects.all().count()
        # while count > 0:
        # if User.login == Person.login:
        people = Person.objects.all()
        return render(request, "account.html", {"people": people})
    else:
        return render(request, "account.html")
            # count -=1








    


