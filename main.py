from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import tkinter as tk
import tkinter.ttk as ttk

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)

# Creates a list of files in the SCAMALS\Games folder sorted by Name 
file_list =  drive.ListFile({'orderBy': 'title', 'q':"'1Tpzs9SqW9DGRI2LiukJ2HZ0rcMSUqvea' in parents and trashed=false", 'corpora': 'teamDrive', 'teamDriveId': '0APtj_IzaT9tWUk9PVA', 'includeTeamDriveItems': True, 'supportsTeamDrives': True}).GetList()

for file1 in file_list:
  print(file1['title'])

# UI
window = tk.Tk()
title = tk.Label(text="SCAMALS Game Downloader/Updater")
title.pack()
window.mainloop()