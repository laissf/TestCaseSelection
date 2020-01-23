import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
path = os.path.abspath('credentials.json')
creds = ServiceAccountCredentials.from_json_keyfile_name(path, scope)
client = gspread.authorize(creds)

def open_sheet (url_features):
    sheet = client.open_by_url(url_features).sheet1
    cell_list = sheet.get_all_values()
    return cell_list

