from django.shortcuts import render, reverse, redirect
from django.views import View

from .models import LinkReduc
from .forms import LinkForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def main_page(request):
    return render(request, 'reducUrl/main-page.html', {'title': 'Сокра.тим'})


def about(request):
    return render(request, 'reducUrl/about.html', {'title': 'Про нас'})


class Link(LoginRequiredMixin, FormMixin, ListView):
    model = LinkReduc
    form_class = LinkForm
    template_name = 'reducUrl/link-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Link, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'
        ctx['linkform'] = LinkForm()
        ctx['LinkReducs'] = LinkReduc.objects.filter(author=self.request.user).order_by('-id')
        return ctx

    def get_success_url(self):
        return reverse('link')

    def post(self, request, *args, **kwargs):
        form = self.get_form()


        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        # reducLink = LinkReduc.objects.filter(author=self.request.user)
        # print(reducLink)
        # print(reducLink)
        self.object.save()
        return super().form_valid(form)