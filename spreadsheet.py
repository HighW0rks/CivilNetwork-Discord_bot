import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials

SHEET_ID = "1ASCwTHJ-jXTlWC8tVfEqxAb5bwW-32W6DcpAzOoZWQc"

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

creds = Credentials.from_service_account_file(r"C:\Users\brijk\PycharmProjects\CivilNetwork-Discord_bot\secret\service_account.json", scopes=scope)
client = gspread.authorize(creds)


def send_request(steamID, spreadsheet_ID, sheet_ID  ):
    try:
        sheet = client.open_by_key(spreadsheet_ID)
        worksheet = sheet.get_worksheet_by_id(sheet_ID)
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        worksheet.append_row([timestamp, steamID])
        print(f"Logged steamID {steamID} at {timestamp}")
    except Exception:
        print("Error has accured. Is the email on the spreadsheet?")
