import inspect
#from .Spreadsheet import open_sheet, get_features
from jira import JIRA


def access_jira(coreid, password, directory = 'https://dalek.mot.com/'):
    jira = JIRA(server=directory, auth=(coreid, password))
    return jira

def filter_jira(jira,filter):
    tcs_list = jira.search_issues(filter, maxResults=3000)
    return tcs_list

def identific_tp (jira, id_tp):
    tp = jira.issue(id_tp)
    return tp


# def compare_features(tcs_list, cell_list):
#     tcs = tcs_list.split(',')
#     for tc in tcs:
#         print(tc + " " + str(jira.issue(tc).fields.customfield_10104))  # reg level do tp
#     # faz a inpeção de todos os campos que tem na pag
#     for item in inspect.getmembers(issues.fields):
#         print(item[1])









