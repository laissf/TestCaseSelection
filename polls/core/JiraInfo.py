import inspect
from .Spreadsheet import open_sheet
from jira import JIRA
from fuzzywuzzy import fuzz

#acessing dalek
def access_jira(coreid, password, directory = 'https://dalek.mot.com/'):
    jira = JIRA(server=directory, auth=(coreid, password))
    return jira

#geting all the tcs for a specific filter
def filter_jira(jira,filter):
    tcs_list = jira.search_issues(filter, maxResults=3000)
    return tcs_list

#geting TP id
def identific_tp (jira, id_tp):
    tp = jira.issue(id_tp)
    return tp

def comp(s1, s2):
    if fuzz.partial_token_sort_ratio(s1, s2) > 80:
        return True
    else:
        return False

#comparing spreadsheet features x tcs features
def compare_features(tcs_list, url_features, reg_level):
    cell_list = open_sheet(url_features)
    tcs_in = []
    tcs_out = []
    for feat in cell_list:
        for tc in tcs_list:
            primary_dom = tc.fields.customfield_10101
            secondary_dom = tc.fields.customfield_10102
            reglevel = tc.fields.customfield_10104
            label = tc.fields.labels
            title = tc.fields.summary
            key = tc.key
            tc = {"key": key, "title": title}


            if str(reglevel) not in reg_level:
                tcs_out.append(tc)
            else:
                if (comp(feat[0],primary_dom)):
                    tcs_in.append(tc)
                else:
                    tcs_out.append(tc)

                for i in secondary_dom.split(','):
                    if comp(feat[0], i) and tc not in tcs_in:
                        tcs_in.append(tc)
                    elif tc not in tcs_out:
                        tcs_out.append(tc)

                for i in label:
                    if comp(feat[0], i) and tc not in tcs_in:
                        tcs_in.append(tc)
                    elif tc not in tcs_out:
                        tcs_out.append(tc)

                for i in title.split(' '):
                    if comp(feat[0], i) and tc not in tcs_in:
                        tcs_in.append(tc)
                    elif tc not in tcs_out:
                        tcs_out.append(tc)
    for i in tcs_out:
        print(i)
    return tcs_in, tcs_out













