from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db import connection
from django.contrib.auth import authenticate, login
from .models import Choice, Question, User
# from .models import Choice, Question
# from django.contrib.auth.models import User


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_user_list = User.objects.order_by('-id')[:5]
    context = {
        'latest_question_list': latest_question_list,
        'latest_user_list': latest_user_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def login_page(request, username):
    username = get_object_or_404(User, username=username)
    return render(request, 'polls/login_page.html', {'username': username})
    # if str(request.user) == str(username):
    #     return render(request, 'polls/login_page.html', {'username': username})
    # else:
    #     return HttpResponseRedirect(reverse('polls:index'))


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def register(request):
    name = request.POST['your_name']
    password = request.POST['password']
    if not User.objects.filter(username=name).exists():
        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO polls_user (username, password) VALUES('{name}','{password}')")
        # new_user = User.objects.create(username=name, password=password)
        ## new_user = User.objects.create_user(username=name, password=password)
        ## login(request, new_user)

    return HttpResponseRedirect(reverse('polls:index'))


def login_own(request):
    username = request.POST['login_name']
    userpassword = request.POST['login_password']
    try:
        user = User.objects.get(username=username)
        if user.password == userpassword:
            return HttpResponseRedirect(reverse('polls:login_page', args=(username,)))
        else:
            return HttpResponseRedirect(reverse('polls:index'))
    except:
        return HttpResponseRedirect(reverse('polls:index'))
    # user = authenticate(request, username=username, password=userpassword)
    # if user is not None:
    #     login(request, user)
    #     return HttpResponseRedirect(reverse('polls:login_page', args=(username,)))
    # else:
    #     return HttpResponseRedirect(reverse('polls:index'))
