from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as auth_logout
from django.core.mail import send_mail
from django.http import JsonResponse
from todo.models import TodoItem
from django.contrib.auth.decorators import login_required
from django.conf import settings

def HomePage(request):
    return render(request,"index.html")

def SignupPage(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        p1=request.POST.get('currentpw')
        p2=request.POST.get('checkpw')
        print(uname,email,p1,p2)

        new_user=User.objects.create_user(uname,email,p1)
        new_user.save()
        return redirect('Login')
    return render(request,"Signup.html")

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('currentpw') 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            send_mail(
                'Subject Here',
                'Your TASKS profile was logged into',
                settings.EMAIL_HOST_USER,  # The sender's email address
                ['prajwal.gangawane14@gmail.com'],  # A list of recipient email addresses
                fail_silently=False,
            )
            return redirect('todo_list')
        else:
            # Authentication failed, handle it here (e.g., show an error message)
            # You might want to render the login page again with an error message
            return render(request, "Login.html", {'error': 'Invalid credentials'})
    return render(request, "Login.html")


#def tasklist(request):
#    return render(request,"tasks.html")
 
def logout(request):
    auth_logout(request)
    return redirect('Login')

@login_required
def todo_list(request):
    # Filter items based on the logged-in user
    items = TodoItem.objects.filter(owner=request.user)
    return render(request, 'todo_list.html', {'items': items})


@login_required
def add_item(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        # Get the logged-in user
        user = request.user
        # Create a new TodoItem associated with the logged-in user
        t = TodoItem(text=text, owner=user)
        t.save()
    return redirect('todo_list')


def toggle_item(request, item_id):
    item = TodoItem.objects.get(id=item_id)
    item.is_checked = not item.is_checked
    item.save()
    return JsonResponse({'status': 'ok'})

def delete_item(request, item_id):
    item = TodoItem.objects.get(id=item_id)
    item.delete()
    return JsonResponse({'status': 'ok'})

