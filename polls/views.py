from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Filters,QueryType
from .core.JiraInfo import access_jira,filter_jira

#filter_jira(access_jira("",""),QueryType.objects.find(plan="CoreApps Common"))

# Create your views here.

class loginView():
    template_name = 'polls/index.html'
    filter_jira()

