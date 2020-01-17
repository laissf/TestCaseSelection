import inspect
from .Spreadsheet import open_sheet, get_features
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

def compare_features(tcs_list, cell_list):
    for tc in tcs_list:
        primary_dom = tc.fields.customfield_10101
        reglevel = tc.fields.customfield_10104
        secondary_dom = tc.fields.customfield_11300
        label = tc.fields.labels
        title = tc.fields.summary

        for cell in cell_list:
            if primary_dom in cell:
                list_in = tc
            elif secondary_dom in cell:
                list_in = tc
            elif label in cell:
                list_in = tc

            elif









