from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, 'react001/index.html')

    def post(self, request):
        return render(request, 'react001/index.html')

class JSX(View):
    def get(self, request):
        return render(request, 'react001/jsx.html')

    def post(self, request):
        return render(request, 'react001/jsx.html')
