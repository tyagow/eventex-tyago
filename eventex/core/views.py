from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.list import ListView

from eventex.core.models import Speaker, Talk

# class HomeView(ListView):
#     template_name = 'index.html'
#     model = Speaker

home = ListView.as_view(template_name='index.html', model=Speaker)


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})

speaker_detail = DetailView.as_view(model=Speaker)

talk_list = ListView.as_view(model=Talk)
