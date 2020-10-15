from django.shortcuts import render

def csr(request):
      return render(request, 'pages/csr.html', {})
    