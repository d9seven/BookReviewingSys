from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from quotes.models import Quote

class MainPage(LoginRequiredMixin, ListView):
    def check_logged(self, request):
        if request.user.is_authenticated:
            current_user = request.user
            return True, current_user
        return False, None
    
    def get(self, request, *args, **kwargs):
        template_name = 'mainpage/index.html'
        logged, current_user = self.check_logged(request)
        obj = {
            'current_user': current_user,
            'logged': logged,
        }
        return render(request, template_name, obj)
