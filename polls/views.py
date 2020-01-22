from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Filters, QueryType
from .core.JiraInfo import access_jira, filter_jira, identific_tp, compare_features
from .core.Spreadsheet import open_sheet
from django.core.cache import caches, cache
from .core.DataBaseInfo import createBD


#credentials jira storage in cache
def getjira():
    return access_jira(cache.get('login'),cache.get('senha'))

# Create your views here.
def login_user(request):
    #inicia o DataBaseInfo
    if len(QueryType.objects.all()) <1:
        createBD()

    if request.POST and request.POST["uname"]:
        coreid =request.POST["uname"]
        password = request.POST["psw"]
        try:
           access_jira(coreid, password)
           cache.set("login", coreid, 360000)
           cache.set("senha", password, 360000)
           return redirect('../tpinformation/')
           return redirect('../tpinformation/')

        except:
            erro = {"erro":"Core id or password incorrect! "}
            return render(request, 'polls/login.html', erro)
    else:
        return render(request, 'polls/login.html', {})

#id tp requisition
def info_tp(request):
    return render(request, 'polls/info.html', {})


#filters list
def tp_filter(request):
    if request.POST["id_tp"]:
        id_tp = request.POST["id_tp"]
        try:
            acess = getjira()
            identific_tp(acess, id_tp)
            cache.set("acessoJira", acess, 360000)
            cache.set("id_tp", id_tp, 360000)
            print("Salvou id")
        except:
            error = {"erro": "Test Plan not found. Try again"}
            return render(request, 'polls/info.html', error)
    else:
        error = {"erro": "Sem ID"}
        return render(request, 'polls/info.html', error)

        # reg level requisition
    if request.POST["reg_level"]:
        reg_level = request.POST["reg_level"]
        reg_level.split(",")
        cache.set("reg_level", reg_level, 360000)
        print("Salvou rl")

    else:
        error = {"erro": "sem reg level"}
        return redirect('tpinformation/', args=error )

        # spreadsheet requisition
    if request.POST and request.POST["url_spreadsheet"]:
        url_spreadsheet = request.POST["url_spreadsheet"]
        cache.set("url_spreadsheet", url_spreadsheet, 360000)

        try:
            open_sheet(url_spreadsheet)
            print("Salvou link")
        except Exception as e:
            print("Error: " + str(e))
            error_spreadsheet = {"error": "Spreadsheet not found!"}
            return render(request, 'polls/info.html', error_spreadsheet)
    else:
        error = {"erro": "sem sheet"}
        return redirect('tpinformation/', args=error)
    lista = QueryType.objects.all()
    return render(request, 'polls/filter.html', {"lista":lista})

#list types of regression plans
def list_filter(request):
    if request.POST and request.POST["tp_filter"]:  # nomenclatura no html
        tp_filter = request.POST["tp_filter"]  # nomenclatura no html
        try:
            query = QueryType.objects.get(type=tp_filter)
            filters = query.filters_set.all()
            label = tp_filter
            if query.type == "Experiences" or query.type == "Data Migration":
                ed = True
            else:
                ed = False
            return render(request, "polls/list_filter.html",{"lista":filters,"query":ed, "label" : label})

        except:
            error_tp = {"erro": "You need to select an intem"}
            return render(request, 'polls/list_filter.html', error_tp)


def tcs_list(request):
    jira = getjira()
    reg_level = cache.get('reg_level')

    if "one_option" in request.POST:
        filter = request.POST["one_option"]
        print(filter)
        query = Filters.objects.get(plan=filter).query
        tcs = filter_jira(jira,query)

        tcs_in, tcs_out = compare_features(tcs, cache.get('url_spreadsheet'), reg_level)
        return render(request, "polls/tcs_list.html", {"tcs_in": tcs_in, "tcs_out": tcs_out})

    elif "multi_options" in request.POST:
        tcs_lista_enorme = []
        filters = request.POST.getlist('multi_options')
        for item in filters:
            tcs = filter_jira(jira, item)
            tcs_lista_enorme.extend(tcs)

        tcs_in, tcs_out = compare_features(tcs_lista_enorme, cache.get('url_spreadsheet'), reg_level)
        return render(request, "polls/tcs_list.html", {"tcs_in": tcs_in, "tcs_out": tcs_out})
