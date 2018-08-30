from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload

from cmd import Cmd
import sys
import os

# If modifying these scopes, delete the file token.json.
# Get yout
# https://developers.google.com/sheets/api/quickstart/python
# https://developers.google.com/drive/api/v3/quickstart/python
SCOPES = [  'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive.file']

class MyPrompt(Cmd):

    def do_list(self, args):
        if len(args) == 0:
            size = 20
        else:
            size = args.split()[-1]

        results = drive_service.files().list(
            pageSize=size, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print('{0} ({1})'.format(item['name'], item['id']))

    def do_create_folder(self, args):
        if len(args) == 0:
            name = 'none'
        else:
            name = args.split()[-1]

        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()

        print(folder)

    def do_create_spreadsheet(self, args):
        if len(args) == 0:
            name = 'none'
        else:
            name = args.split()[-1]

        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.spreadsheet'
        }

        spreadsheet = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()

        print(spreadsheet)

    def do_create_document(self, args):
        if len(args) == 0:
            name = 'none'
        else:
            name = args.split()[-1]

        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.document'
        }

        document = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()

        print(document)

    def do_create_drawing(self, args):
        if len(args) == 0:
            name = 'none'
        else:
            name = args.split()[-1]

        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.drawing'
        }

        drawing = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()

        print(drawing)

    def do_create_form(self, args):
        if len(args) == 0:
            name = 'none'
        else:
            name = args.split()[-1]

        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.form'
        }

        form = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()

        print(form)

    def do_create_slide(self, args):
        if len(args) == 0:
            name = 'none'
        else:
            name = args.split()[-1]

        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.presentation'
        }

        slide = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()

        print(slide)

    def do_create_file(self, args):
        name = args.split()[0]
        folder_id = args.split()[1]
        path = args.split()[2]
        type = 'image/jpeg'

        print(name + ' ' + folder_id + ' ' + path + ' ' + type)

        file_metadata = {
            'name': name,
            'parents': [folder_id]
        }
        media = MediaFileUpload(path,
                                mimetype=type,
                                resumable=True)
        file_created = drive_service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print(file_created)

    def do_delete(self, args):
        id = args.split()[0]

        file_deleted = drive_service.files().delete(fileId=id).execute()
        print('File deleted')

    def do_logout(self, args):
        os.remove("token.json")

    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit


if __name__ == '__main__':

    global drive_service
    global sheets_service

    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    drive_service = build('drive', 'v3', http=creds.authorize(Http()))
    sheets_service = build('sheets', 'v4', http=creds.authorize(Http()))

    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
