import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import config
import reset

# Authorize Google Sheets
try:
	scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
	credentials = ServiceAccountCredentials.from_json_keyfile_name(config.credentials, scope)
	gc = gspread.authorize(credentials)
except OSError as e:
	print("JSON file with Google account credentials not found!")
	print("Make sure you've followed the README instructions and added the filepath of your credentials file to config.py")
	exit(1)

# Open sheets
datasheet = gc.open(config.spreadsheet).worksheet("datasheet")

# Get question and options from current index

prasad_date = datasheet.cell(1, 1).value
prasad_count = datasheet.cell(1, 2).value

#if prasad_date == "":
#	print("No questions found in the Google sheet!")
#	exit(1)
#else
#print("date:" prasad_date)
#print("count:" prasad_count)
