from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Information, Answer
from django.urls import reverse, reverse_lazy

class ListInformationView(ListView):
    template_name = 'agendapp/index.html'
    model = Information

class ListFlipView(ListView):
    template_name = 'agendapp/flip.html'
    model = Information
    # fields = ('title', 'text', 'thumbnail','category')
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET
        if q := query.get('cate'): #python3.8以降
            queryset = queryset.filter(category=q)

        return queryset

class PhotoView(LoginRequiredMixin, CreateView):
    template_name = 'agendapp/create.html'
    model = Answer
    fields = ('title', 'text', 'thumbnail')
    success_url = reverse_lazy('kurashi')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Answer.objects.get(pk=self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)
    