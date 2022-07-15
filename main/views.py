from django.views.generic import FormView

from . import forms
# Create your views here.


class MainView(FormView):
    form_class = forms.MainForm
    template_name = 'main/main.html'