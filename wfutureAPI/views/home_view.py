from django.shortcuts import render

def home(request):
    user = request.user
    print(user)
    return render(request, 'pages/home.html')