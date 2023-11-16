from django.shortcuts import render

# Get questions and display those questions
def index(request):
    return render(request, 'pages/index.html')