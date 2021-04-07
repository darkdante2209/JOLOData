import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)

client = gspread.authorize(creds)

sheet = client.open('huy test').sheet1

data = sheet.get_all_records()

len_old = len(data)
while True:

    data_new = sheet.get_all_records()
    len_new = len(data_new)
    if len_new > len_old:
        row_new = sheet.row_values(len_new)
        print(row_new)
        len_old = len_new