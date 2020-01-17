from jira import JIRA
import inspect
from .Spreadsheet import open_sheet, get_features

directory = 'https://dalek.mot.com/'


jira = JIRA(server=directory, auth=('laissf', 'Abre2503'))
issues = jira.issue('MCA-2144102')
lista_teste = ['volte', 't']
# pegar tcs a partir de um filtro e mostrar na  tela
for issue in jira.search_issues('project = 11010 AND issuetype = "Test Case" AND labels = TMO_Reg AND labels = Plat_Reg AND status != closed ORDER BY cf[10104] ASC', maxResults=3000):
    primary_dom = issue.fields.customfield_10101
    reglevel = issue.fields.customfield_10104
    secondary_dom = issue.fields.customfield_10102
    label = issue.fields.labels
    title = issue.fields.summary
    #print(str(secondary_dom))
    for cell in lista_teste
    if ("VoLte") in str(secondary_dom):
        print (str(issue))
    else:
        print ("Not working")

    # print('{}'.format(issue.key))



#

# for tc in issue:
#     print(tc+" "+str(jira.issue(tc).fields.customfield_10104)) #reg level do tp


#faz a inpeção de todos os campos que tem na pag
# for item in inspect.getmembers(issues.fields.customfield_11300):
#     print(item[1])





