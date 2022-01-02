# GMailer

## Requirements

- Python 3
- python-dotenv==0.19.2
- beautifulsoup4==4.10.0

## Getting ready...

1. [Install Python3](https://www.python.org/downloads/)

2. [Create App Passwords of your Google account.](https://support.google.com/accounts/answer/185833?hl=en)

3. Copy and past `.env.example` file and then change the name to `.env`

4. Change the env file properties.
   e.g. `EMAIL_PASSWORD=super_duper_secret_password`

5. Windows OS

   - Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and then put it into the directory of the project.
   - Run `install.bat` as administrator.
   - Or you can install using `requirements.txt` on cmd window.
     `pip install -r requirements.txt`

6. Mac / Linux OS

   - Open `Terminal`
   - Move to the `directory of this project`.
     ```shell
     cd ~/Downloads/GMailer
     ```
   - Install requirements.
     ```shell
     pip install -r requirements.txt
     ```

## How to use

1. Edit `contents.html` file, which represents the contents of the email you will send.
2. Edit `recipients.txt`, which is literally recipients list separated by a comma and a line break. Also, the duplicated emails will be removed.
3. When sending emails fails, the list of addresses that failed to send email will be stored in `failed.txt`
4. Run the script using this code on the terminal or cmd window: `python3 main.py -t "<MAIL_TITLE>"`

## Cautions

- All emails will be sent in splits of 1 per 100 people because of the limitation.
