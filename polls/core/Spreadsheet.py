import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('../../credentials.json', scope)
client = gspread.authorize(creds)

def open_sheet (url_features):
    sheet = client.open_by_url('url_features').sheet1
    return sheet

def get_features(sheet):
    cell_list = sheet.get_all_values()
    return cell_list

