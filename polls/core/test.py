import os

import gspread
from jira import JIRA
import inspect

# directory = 'https://dalek.mot.com/'
#
#
# jira = JIRA(server=directory, auth=('laissf', 'Abre2503'))
# issues = jira.issue('MCA-2144102')
#
# # pegar tcs a partir de um filtro e mostrar na  tela
# for issue in jira.search_issues('project = 11010 AND issuetype = "Test Case" AND labels = TMO_Reg AND labels = Plat_Reg AND status != closed ORDER BY cf[10104] ASC', maxResults=3000):
#     primary_dom = issue.fields.customfield_10101
#     reglevel = issue.fields.customfield_10104
#     secondary_dom = issue.fields.customfield_10102
#     label = issue.fields.labels
#     title = issue.fields.summary
#     #print(str(secondary_dom))
#
#     lista_teste = ['VZW_Reg', 'Voice Call', 'Carrier App']
#     # for cell in lista_teste:
#     #     if ('VZW_Reg') in (str(label)):
#     print(str(secondary_dom))



    # print('{}'.format(issue.key))



#

# for tc in issue:
#     print(tc+" "+str(jira.issue(tc).fields.customfield_10104)) #reg level do tp


#faz a inpeção de todos os campos que tem na pag
# for item in inspect.getmembers(issues.fields.customfield_11300):
#     print(item[1])



#--------------------------------
#CODIGO DA VIEW
 # if request.POST:  # nomenclatura no html
    #     multi_options = request.POST["multi_options"]
    #
    #     compare_features(QueryType.objects.find(query=multi_options), get_features(), )
    #
    #
    # elif request.POST.get["one_option"]:
    #     one_option = request.POST.get["one_option"]
    #
    #
    # else:



 #QueryType.objects.all().delete()


# use creds to create a client to interact with the Google Drive API
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
path = os.path.abspath('credentials.json')
creds = ServiceAccountCredentials.from_json_keyfile_name(path, scope)
client = gspread.authorize(creds)

sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/11MunIhfXpPszVQd_PG3mBPVbsHrz0f7kvmr8uxXwvkc/edit#gid=726912126').sheet1
cell_list = sheet.get_all_values()
for i in cell_list:
    print(i[0])