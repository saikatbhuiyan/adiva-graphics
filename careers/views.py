from django.shortcuts import render
from django.http import HttpResponse


def career(request):
      return render(request, 'pages/career.html', {})
    