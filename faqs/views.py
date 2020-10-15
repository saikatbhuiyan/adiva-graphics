from django.shortcuts import render

def faqs(request):
      return render(request, 'pages/faqs.html', {})
    