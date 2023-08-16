# PyDrive 
from dotenv import load_dotenv
import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def send_to_drive(filename, folder = 'private', title = None):
	
	if folder == 'public':
		load_dotenv()
		folder = os.environ.get("statsFolder")
	elif (folder == 'private') or (folder is None):
		load_dotenv()
		folder = os.environ.get("statsPrivate")
	if title is None:
		title = filename
	file = drive.CreateFile({'title': title,'parents': [{'id': folder}]})
	file.SetContentFile(filename)
	file.Upload()
