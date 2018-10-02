# Google-Drive-CMD

### Requirements
Python 3+ and Pip3

### Step 1: Turn on the Google Sheets API
Access https://developers.google.com/sheets/api/quickstart/python

### Step 2: Install the Google Client Library
Run the following command to install the library using pip:

```shell
pip3 install --upgrade google-api-python-client oauth2client
```

See the library's installation page for the alternative installation options.


### Step 3: Run it
Run the app using the following command:

```python
python3 main.py
```

## Commands

- List

```
$ list <number>
```

- Empty Trash

```
$ empty_trash
```

- Get Item

```
$ get <id>
```

- Create

```
$ create_folder <name>
$ create_spreadsheet <name>
$ create_document <name>
$ create_drawing <name>
$ create_form <name>
$ create_slide <name>
$ create_file <name> <id> <path> <type>
```

- Delete

```
$ delete <id>
```

- Logout

```
$ logout
```

- Quit

```
$ quit
```





