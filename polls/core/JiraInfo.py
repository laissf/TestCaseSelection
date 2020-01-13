from jira import JIRA
import inspect
#from .Spreadsheet import open_sheet, get_features

directory = 'https://dalek.mot.com/'

def access_jira(coreid, password, tc_id):
    jira = JIRA(server=directory, auth=(coreid, password))
    issues = jira.issue(tc_id)
    return jira

def filter_jira(jira,filter):
    tcs_list = jira.search_issues(filter, maxResults=3000)
    return tcs_list

# def compare_features(tcs_list, cell_list):
#     tcs = tcs_list.split(',')
#     for tc in tcs:
#         print(tc + " " + str(jira.issue(tc).fields.customfield_10104))  # reg level do tp
#     # faz a inpeção de todos os campos que tem na pag
#     for item in inspect.getmembers(issues.fields):
#         print(item[1])









