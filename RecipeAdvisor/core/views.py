#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# from khayyam import *
from core.models import *
from django.conf import settings
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.http import JsonResponse
from django.core.mail import send_mail
from datetime import datetime, date
from django.utils import timezone
import json
from django.http import JsonResponse
from .form import ImageUploadForm, VideoUploadForm
from .form import ImageUploadFormProduct
from .form import FileUpload1
import urllib2
import requests
from django.db.models import Max

from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count
from django.db.models import Sum
import random
import operator

from django.db.models import Q


# Create your views here.


@requires_csrf_token
@csrf_exempt
def index(request):
    context = {}
    if request.method == "POST":
        print request.POST
        user = authenticate(
            username=request.POST["uname"],
            password=request.POST["psw"]
        )
        if user is not None:
            context["user"] = user.username
            print user.username
            request.session.set_expiry(86400)
            login(request, user)
            return redirect("/core/index/")
        else:
            context["mmm"] = True
            print "Username or Password is not valid"
    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        context["user_name"] = p.first_name + " " + p.last_name

    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))


@requires_csrf_token
@csrf_exempt
def name(request):
    print "jjhjjjjj"
    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        p.first_name = request.POST["first_name"]
        p.last_name = request.POST["last_name"]
        p.save()
    return redirect("/core/index")


@requires_csrf_token
@csrf_exempt
def terms_privacy(request):
    context = {}
    template = loader.get_template("termsAndServices.html")
    return HttpResponse(template.render(context, request))


@requires_csrf_token
@csrf_exempt
def searchPage(request):
    context = {}
    if request.method == "POST":
        print request.POST
        query = request.POST["search"]
        if query:
            query_list = query.split()
            q_f = [Q(name__icontains=q) for q in query_list]
        else:

            q_f = []

        if "Type" in request.POST:
            print "Correct"
            q_f.append(Q(type=request.POST["Type"]))

        if "Style" in request.POST:
            if request.POST["Style"] == "Vegan":
                q_f.append(Q(vegan=True))
            else:
                q_f.append(Q(vegetarian=True))

        if "health" in request.POST:
            # q1 = []
            if "cal" in request.POST["health"]:
                q_f.append(Q(Calories__lt=500))

            if "fat" in request.POST["health"]:
                q_f.append(Q(Fat__lt=50))

            # q1 = reduce(operator.or_, q1)
            # q_f.append(q1)

        if q_f:
            print reduce(operator.and_, q_f)
            result = Meal.objects.filter(reduce(operator.and_, q_f))
        else:
            result = Meal.objects.all()

        for i in result:
            print i.name
        context["meal"] = result
    template = loader.get_template("searchPage.html")
    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        context["user_name"] = p.first_name + " " + p.last_name
    return HttpResponse(template.render(context, request))


@requires_csrf_token
@csrf_exempt
def signup(request):
    print "yes*************************************ss"
    response = {}
    if request.method == 'POST':
        try:
            if Profile.objects.filter(user__username=request.POST["email"]).first():
                response["error"] = "13"
                response["uid"] = "0"
                response["res"] = "register"
                print response
                print("username field 1 error")
                response['status'] = 'error'
                response['message'] = '<span class="glyphicon glyphicon-info-sign"></span> &nbsp; The username is already in the database'
                return JsonResponse(response)
            print "11111111111"
            register_name = Profile()
            register_user = User()
            register_user.username = request.POST["email"]
            register_user.set_password(request.POST["psw"])
            print "2222222222222"
            register_user.save()
            register_name.user = register_user
            register_name.first_name = request.POST["email"]
            register_name.last_name = ""
            register_name.save()
            register_user.save()
            register_name.user = register_user

            register_name.save()
            print "1111"
            # response["user"] = {}
            # response["user"]["user_name"] = register_name.user.username
            # response["user"]["password"] = request.POST["password"]
            request.session.set_expiry(86400)
            login(request, register_user)
            print "_______________________________15"
            return redirect("/core/index/")
            # return JsonResponse(response)
        except:
            print "except______________"
            response = {}
            response["error"] = "4"
            response["uid"] = "0"
            response["res"] = "signup"
            print request.POST
            response['status'] = 'error'
            response[
                'message'] = '<span class="glyphicon glyphicon-info-sign"></span> &nbsp; Error is Sign Up, please try again.'
            response['error'] = "0"
            return redirect("/core/index/")
            # return JsonResponse(response)

    # template = loader.get_template("index.html")
    #
    # return HttpResponse(template.render(context, request))


@requires_csrf_token
@csrf_exempt
def meal(request):
    m = Meal.objects.filter(id=request.GET.get('id')).first()
    fav=False

    direct = Direction.objects.filter(meal=m).order_by('order')
    ind = Ingredient.objects.filter(meal=m)
    template = loader.get_template("meal.html")

    ind_odd = []
    ind_even = []
    for i in range(len(ind)):
        if i % 2 == 1:
            ind_odd.append(ind[i].text)
        else:
            ind_even.append(ind[i].text)

    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        fav = Favorite.objects.filter(meal=m, profile=p).first()
        if fav and fav.is_favorite is True:
            fav = True
        else:
            fav = False
    context = {
        "meal": m,
        "directions": direct,
        "ind_odd": ind_odd,
        "ind_even": ind_even,
        "url": request.build_absolute_uri(),
        "fav": fav,
    }
    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        context["user_name"] = p.first_name + " " + p.last_name
    return HttpResponse(template.render(context, request))


@requires_csrf_token
@csrf_exempt
def favorite(request):
    if request.user.is_authenticated():
        print request.POST
        m = Meal.objects.filter(id=request.POST['id']).first()

        fav = Favorite.objects.filter(meal=m, profile__user=request.user).first()
        data = {}
        if fav is not None:
            if fav.is_favorite:
                fav.is_favorite = False
                fav.save()
                color = "Orange"
                background = "white"
                text = "+ Favorite"
            else:
                fav.is_favorite = True
                fav.save()
                color = "white"
                background = "Orange"
                text = "- Favorite"

        else:
            fav = Favorite()
            fav.meal = m
            fav.profile = Profile.objects.filter(user=request.user).first()
            fav.is_favorite = True
            fav.save()
            color = "white"
            background = "Orange"
            text = "- Favorite"
    else:
        color = "white"
        background = "silver"
        text = "please login"

    data = {
        "background-color": background,
        "color": color,
        "text": text
    }
    data = json.dumps(data)
    return JsonResponse({"data": data})


@requires_csrf_token
@csrf_exempt
def our_suggestion(request):
    context = {}
    fav=False
    mm = Meal.objects.all()
    a = len(mm)
    rand = random.randint(0, a - 1)
    print rand
    m = mm[rand]
    direct = Direction.objects.filter(meal=m).order_by('order')
    ind = Ingredient.objects.filter(meal=m)
    template = loader.get_template("meal.html")

    ind_odd = []
    ind_even = []
    for i in range(len(ind)):
        if i % 2 == 1:
            ind_odd.append(ind[i].text)
        else:
            ind_even.append(ind[i].text)

    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        fav = Favorite.objects.filter(meal=m, profile=p).first()
        if fav and fav.is_favorite is True:
            fav = True
        else:
            fav = False
    context = {
        "meal": m,
        "directions": direct,
        "ind_odd": ind_odd,
        "ind_even": ind_even,
        "url": request.build_absolute_uri(),
        "fav": fav,
    }
    print context
    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        context["user_name"] = p.first_name + " " + p.last_name
    return HttpResponse(template.render(context, request))


@requires_csrf_token
@csrf_exempt
def not_that_expensive(request):
    context = {}
    fav=False
    mm = Meal.objects.filter(price_level="$")
    a = len(mm)
    rand = random.randint(0, a - 1)
    print rand
    m = mm[rand]
    direct = Direction.objects.filter(meal=m).order_by('order')
    ind = Ingredient.objects.filter(meal=m)
    template = loader.get_template("meal.html")

    ind_odd = []
    ind_even = []
    for i in range(len(ind)):
        if i % 2 == 1:
            ind_odd.append(ind[i].text)
        else:
            ind_even.append(ind[i].text)
    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        fav = Favorite.objects.filter(meal=m, profile=p).first()
        if fav and fav.is_favorite is True:
            fav = True
        else:
            fav = False
    context = {
        "meal": m,
        "directions": direct,
        "ind_odd": ind_odd,
        "ind_even": ind_even,
        "url": request.build_absolute_uri(),
        "fav": fav,
    }
    print context
    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        context["user_name"] = p.first_name + " " + p.last_name
    return HttpResponse(template.render(context, request))


@requires_csrf_token
@csrf_exempt
def something_fast(request):
    context = {}
    fav=False
    mm = Meal.objects.all()
    a = len(mm)
    rand = random.randint(0, a - 1)
    print rand
    m = mm[rand]
    direct = Direction.objects.filter(meal=m).order_by('order')
    ind = Ingredient.objects.filter(meal=m)
    template = loader.get_template("meal.html")

    ind_odd = []
    ind_even = []
    for i in range(len(ind)):
        if i % 2 == 1:
            ind_odd.append(ind[i].text)
        else:
            ind_even.append(ind[i].text)
    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        fav = Favorite.objects.filter(meal=m, profile=p).first()
        if fav and fav.is_favorite is True:
            fav = True
        else:
            fav = False
    context = {
        "meal": m,
        "directions": direct,
        "ind_odd": ind_odd,
        "ind_even": ind_even,
        "url": request.build_absolute_uri(),
        "fav": fav,
    }
    print context
    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        context["user_name"] = p.first_name + " " + p.last_name
    return HttpResponse(template.render(context, request))


@requires_csrf_token
@csrf_exempt
def something_healthy(request):
    context = {}
    fav=False
    mm = Meal.objects.filter(Calories__lt=500, Carbohydrates__lt=30)
    a = len(mm)
    rand = random.randint(0, a - 1)
    print rand
    m = mm[rand]
    direct = Direction.objects.filter(meal=m).order_by('order')
    ind = Ingredient.objects.filter(meal=m)
    template = loader.get_template("meal.html")

    ind_odd = []
    ind_even = []
    for i in range(len(ind)):
        if i % 2 == 1:
            ind_odd.append(ind[i].text)
        else:
            ind_even.append(ind[i].text)
    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        fav = Favorite.objects.filter(meal=m, profile=p).first()
        if fav and fav.is_favorite is True:
            fav = True
        else:
            fav = False
    context = {
        "meal": m,
        "directions": direct,
        "ind_odd": ind_odd,
        "ind_even": ind_even,
        "url": request.build_absolute_uri(),
        "fav": fav,
    }
    print context
    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        context["user_name"] = p.first_name + " " + p.last_name
    return HttpResponse(template.render(context, request))


@requires_csrf_token
@csrf_exempt
def select_mood(request):
    context = {}
    fav=False
    print request.build_absolute_uri()
    mm = Meal.objects.filter(mood=request.GET.get('mood'))
    a = len(mm)
    rand = random.randint(0, a - 1)
    print rand
    m = mm[rand]
    direct = Direction.objects.filter(meal=m).order_by('order')
    ind = Ingredient.objects.filter(meal=m)
    template = loader.get_template("meal.html")

    ind_odd = []
    ind_even = []
    for i in range(len(ind)):
        if i % 2 == 1:
            ind_odd.append(ind[i].text)
        else:
            ind_even.append(ind[i].text)
    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        fav = Favorite.objects.filter(meal=m, profile=p).first()
        if fav and fav.is_favorite is True:
            fav = True
        else:
            fav = False
    context = {
        "meal": m,
        "directions": direct,
        "ind_odd": ind_odd,
        "ind_even": ind_even,
        "url": request.build_absolute_uri(),
        "fav": fav,
    }
    print context
    if request.user.is_authenticated():
        p = Profile.objects.filter(user=request.user).first()
        context["user_name"] = p.first_name + " " + p.last_name
    return HttpResponse(template.render(context, request))


@requires_csrf_token
@csrf_exempt
def logout_page(request):
    print "ghabl"
    logout(request)
    print "badesh"
    return redirect("/core/index/")
