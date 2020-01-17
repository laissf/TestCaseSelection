from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Filters, QueryType
from .core.JiraInfo import access_jira, filter_jira, identific_tp
from .core.Spreadsheet import open_sheet, get_features
from django.core.cache import caches, cache
from .core.DataBaseInfo import createBD

#filter_jira(access_jira("",""),QueryType.objects.find(plan="CoreApps Common"))

# Create your views here.

def login_user(request):
    #QueryType.objects.all().delete()
    #inicia o DataBaseInfo
    if len(QueryType.objects.all()) <1:
        createBD()

    if request.POST and request.POST["uname"]:
        coreid =request.POST["uname"]
        password = request.POST["psw"]
        try:
           access_jira(coreid, password)

        except:
            erro = {"erro":"Core id or password incorrect! "}
            return render(request, 'polls/login.html', erro)
    else:
        return render(request, 'polls/login.html', {})

#id tp requisition
def info_tp(request):
    if request.POST and request.POST["id_tp"]:
        id_tp =request.POST["id_tp"]

        try:
            identific_tp(getjira(),id_tp)

        except:
            error = {"erro":"Test Plan not found. Try again"}
            return render(request, 'polls/info.html', error)
    else:
        return render(request, 'polls/info.html', {})

#reg level requisition
    if request.POST and request.POST["reg_level"]:
        reg_level=request.POST["reg_level"]

        try:
            if (reg_level>0)and(reg_level<=4):
                return render(request, 'polls/info.html', reg_level)

        except:
            erro_reg_level = {"erro_reg_level ":"This is  not a valide value Try again"}
            return render(request, 'polls/info.html', erro_reg_level)
    else:
        return render(request, 'polls/info.html', {})

#spreadsheet requisition
    if request.POST and request.POST["url_spreadsheet"]:  # nomenclatura no html
        url_spreadsheet = request.POST["url_spreadsheet"]  # nomenclatura no html

        try:
           open_sheet(url_spreadsheet)

        except:
            error_spreadsheet = {"erro": "Spreadsheet not found!"}
            return render(request, 'polls/info.html', error_spreadsheet)
    else:
        return render(request, 'polls/info.html', {})

#credentials jira storage
def getjira():
    return access_jira(cache.get('login'),cache.get('senha'))

#filters list
def list_filters(request):
    if request.POST and request.POST["tp_filter"]:  # nomenclatura no html
        tp_filter = request.POST["tp_filter"]  # nomenclatura no html
        filter_jira(getjira(),QueryType.objects.find(plan=tp_filter))
    else:
        lista = QueryType.objects.all()
        return render(request, 'polls/filter.html', {"lista":lista})

