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
SCOPES = 'https://www.googleapis.com/auth/drive'

class MyPrompt(Cmd):
    global service

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print ("Hello, %s" % name)

    def do_list(self, args):
        if len(args) == 0:
            size = 20
        else:
            size = args.split()[-1]

        results = service.files().list(
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

        folder = service.files().create(body=file_metadata,
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

        spreadsheet = service.files().create(body=file_metadata,
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

        spreadsheet = service.files().create(body=file_metadata,
                                        fields='id').execute()

        print(spreadsheet)

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
        file_created = service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print(file_created)

    def do_delete(self, args):
        id = args.split()[0]

        file_deleted = service.files().delete(fileId=id).execute()
        print('File deleted')

    def do_logout(self, args):
        os.remove("token.json")

    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit


if __name__ == '__main__':


    global service

    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
