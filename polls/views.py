from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Filters, QueryType
from .core.JiraInfo import access_jira, filter_jira, identific_tp, compare_features
from .core.Spreadsheet import open_sheet
from django.core.cache import caches, cache
from .core.DataBaseInfo import createBD
from django.core.paginator import Paginator
from django.http import JsonResponse


#credentials jira storage in cache
def getjira():
    return access_jira(cache.get('login'),cache.get('senha'))

def login(request):
    #inicia o DataBaseInfo
    if len(QueryType.objects.all()) <1:
         createBD()

    if request.POST and request.POST["uname"]:
        coreid=request.POST["uname"]
        password = request.POST["password"]
        try:
           access_jira(coreid, password)
           cache.set("login", coreid, 360000)
           cache.set("senha", password, 360000)
           return redirect('../info_tp/')

        except:
            erro = {"erro":"Core id or password incorrect! "}
            return render(request, 'polls/login.html', erro)
    else:
        return render(request, 'polls/login.html', {})


def info_tp(request):
    return render(request, 'polls/info_tp.html', {})


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
            return redirect(request, 'polls/info_tp.html', error)
    else:
        error = {"erro": "Sem ID"}
        return redirect(request, 'polls/info_tp.html', error)

        # reg level requisition
    if request.POST["reg_level"]:
        reg_level = request.POST["reg_level"]
        reg_level.split(",")
        cache.set("reg_level", reg_level, 360000)
        print("Salvou rl")

    else:
        error = {"erro": "sem reg level"}
        return redirect('polls/info_tp.html', args=error )

    if request.POST and request.POST["url_spreadsheet"]:
        url_spreadsheet = request.POST["url_spreadsheet"]
        cache.set("url_spreadsheet", url_spreadsheet, 360000)

        try:
            open_sheet(url_spreadsheet)
            print("Salvou link")
        except Exception as e:
            print("Error: " + str(e))
            error_spreadsheet = {"error": "Spreadsheet not found!"}
            return render(request, 'polls/info_tp.html', error_spreadsheet)
    else:
        error = {"erro": "sem sheet"}
        return redirect('polls/info_tp.html', args=error)

    lista = QueryType.objects.all()
    return render(request, 'polls/tp_filter.html', {"lista":lista})


def list_filter(request):
    if request.POST and request.POST["tp_filter"]:
        tp_filter = request.POST["tp_filter"]
        try:
            query = QueryType.objects.get(type=tp_filter)
            filters = query.filters_set.all()
            label = tp_filter
            if query.type == "Data Migration" or query.type == "Experiences":
                ed = True
            else:
                ed = False
            return render(request, "polls/list_filter.html",{"lista":filters,"query":ed, "label" : label})

        except:
            error_tp = {"erro": "You need to select an intem"}
            return render(request, 'polls/list_filter.html', error_tp)


def ajax_tc_list(request):
    filter = request.GET.get('filters', None)
    type = request.GET.get('one', None)
    type = "one_option" if type == "T" else "multi_options"
    jira = getjira()
    reg_level = cache.get('reg_level')

    try:
        if "one_option" in type:
            query = Filters.objects.get(plan=filter).query
            tcs = filter_jira(jira,query)

            tcs_in, tcs_out = compare_features(tcs, cache.get('url_spreadsheet'), reg_level)
            print(tcs_in, tcs_out, "1")

            #return render(request, 'polls/tcs_list.html', {"tcs_in":tcs_in,"tcs_out":tcs_out,})
            # paginator = Paginator(tcs_out, 30)
            # page = request.GET.get('page')
            # tcs_out = paginator.get_page(page)
            return JsonResponse({"work":False, "tcs_in":None, "tc_out":None})

        elif "multi_options" in type:
            tcs_lista_enorme = []
            filters = filter.split(",")
            filters = filters[:len(filters)]
            for item in filters:
                tcs = filter_jira(jira, item)
                tcs_lista_enorme.extend(tcs)

            tcs_in, tcs_out = compare_features(tcs_lista_enorme, cache.get('url_spreadsheet'), reg_level)
            print(tcs_in, tcs_out, "2")
            return JsonResponse({"work":False, "tcs_in":None, "tc_out":None})


    except Exception as ex:
        print("Error: " + str(ex))
        error_tcs= {"error": "Something in Jira is not working well"}
        return JsonResponse({"work":False})



def tcs_list(request):
    f = ""

    if "one_option" in request.POST:
        filter = request.POST["one_option"]
        f += filter
        return render(request, 'polls/tcs_list.html', {"filters":f,"one":"T"})

    elif "multi_options" in request.POST:
        filters = request.POST.getlist('multi_options')
        for item in filters:
            f +=item+","
        return render(request, 'polls/tcs_list.html', {"filters":f,"one":"F"})