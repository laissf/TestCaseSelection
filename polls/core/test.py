# from jira import JIRA
# import inspect
#
# directory = 'https://dalek.mot.com/'
#
#
# jira = JIRA(server=directory, auth=('laissf', 'Abre2503'))
# issues = jira.issue('MCA-2144102')
#
# # pegar tcs a partir de um filtro e mostrar na  tela
# for issue in jira.search_issues('project = 11010 AND issuetype = "Test Case" AND labels = TMO_Reg AND labels = Plat_Reg AND status != closed ORDER BY cf[10104] ASC', maxResults=3000):
#     print('{}'.format(issue.key))





#tp criado
#tcs = issues.fields.customfield_10200 #campo do tp
# tcs = issue.split(',')
# for tc in tcs:
#     print(tc+" "+str(jira.issue(tc).fields.customfield_10104)) #reg level do tp
# #faz a inpeção de todos os campos que tem na pag
# for item in inspect.getmembers(issues.fields):
#     print(item[1])


# summar = issues.fields.summary
# reglevel = issues.fields.customfield_10104
# product = issues.fields.customfield_10129
# filters = issues.fields.customfield_10154
# print(summar, reglevel, product, filters)


