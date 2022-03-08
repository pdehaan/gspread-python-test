# gspread python test

Trying to edit a [Google Sheet](https://docs.google.com/spreadsheets/d/1JqMThnZHBcKVs3GcmfD6r-FcDXhP8Tzl_kgfRrxydAc/edit#gid=0) using the [gspread](https://docs.gspread.org/en/latest/oauth2.html#service-account) library.

NOTE: Copy the generated credientials file from GCP into your ~/.config/gspread/ directory and rename the file "service_account.json", otherwise you'll get the following error:
> _FileNotFoundError: [Errno 2] No such file or directory: '/Users/xxx/.config/gspread/service_account.json'_

## Creating a virtual environment

```sh
python3 -m venv venv
source ./venv/bin/activate
pip install gspread
```

## Getting Started

Run <kbd>python test.py</kbd> and it'll either work (unlikely), or you'll run through the gauntlet of first time errors, including:

- gspread.exceptions.APIError: {'errors': [{'domain': 'usageLimits', 'reason': 'accessNotConfigured', 'message': 'Access Not Configured. Drive API has not been used in project XXX before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=XXX then retry.
- gspread.exceptions.APIError: {'code': 403, 'message': 'Google Sheets API has not been used in project xxx before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/sheets.googleapis.com/overview?project=xxx then retry.
