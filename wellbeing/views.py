from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Mood
from .forms import MoodForm


class HomeView(CreateView):
    '''

    '''
    template_name = 'templates/index.html'
    form_class = MoodForm

    def get(self, request, *args, **kwargs):

        context = {
            'mood_form': MoodForm,
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        form = MoodForm()


class PostMood(CreateView):
    '''

    '''
    template_name = 'index.html'
    form_class = MoodForm
    success_url = 'home'

    def post(self, request, author_id, *args, **kwargs):
        mood_form = MoodForm(data=request.POST)

        if mood_form.is_valid():
            author = get_object_or_404(User, id=author_id)
            mood_form.instance.author = author
            mood_instance = mood_form.save()
        else:
            mood_form = MoodForm()
        return HttpResponseRedirect("/")


def get_tired_page(request):
    """ View to return tired page """

    return render(request, 'tired.html')


def get_bored_page(request):
    """ View to return bored page """

    return render(request, 'bored.html')


def get_happy_page(request):
    """ View to return happy page """

    return render(request, 'happy.html')


def get_stressed_page(request):
    """ View to return stressed page """

    return render(request, 'stressed.html')
