import sys, getopt, os, re, smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv(verbose=True)

EMAIL_SENDER=os.getenv('EMAIL_SENDER')
EMAIL_SENDER_NAME=os.getenv('EMAIL_SENDER_NAME')
EMAIL_PASSWORD=os.getenv('EMAIL_PASSWORD')
RECIPIENTS_FILE=os.getenv('RECIPIENTS_FILE')
CONTENTS_FILE=os.getenv('CONTENTS_FILE')
FAILED_FILE=os.getenv('FAILED_FILE')

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def main(argv):
    FILE_NAME = argv[0]
    
    title = ''

    try:
        opts, etc_args  = getopt.getopt(argv[1:], 't')

        for index in range(len(opts)):
            opt = opts[index]
            if ('-t') in opt:
                title = etc_args[index]
    except:
        print(FILE_NAME, '-t "<title>"')
        sys.exit(2)

    if len(title) < 1:
        print(FILE_NAME, '-t "<title>"')
        sys.exit(2)

    # Chunk by 100 becuase of the limitation.
    to = chunks(recipients(), 100)
    contents_str = contents()

    for chunked in to:
        try: send_mail(chunked, title, contents_str)
        except: 
            print(f'⚠️ Failed to send the email to {chunked}')
            print('Failed list will be saved in "failed.txt". Please try later.')

            f = open(FAILED_FILE, 'a')
            failed = ',\n'.join(chunked) + ',\n'
            f.write(failed)
            f.close()
            continue

def recipients():
    mail_recipients = set()
    
    f = open(RECIPIENTS_FILE, 'r')
    lines = f.readlines()

    for line in lines:
        line = line.strip().replace(" ", "").replace(",", "")
        if isValid(line):
            mail_recipients.add(line)

    f.close()

    return list(mail_recipients)

def contents():
    with open(CONTENTS_FILE) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        return soup.decode_contents()

def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return re.fullmatch(regex, email)


def send_mail(to, title, contents):
    print(f'💬 Sending an email')
    print('\n'.join(to))

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()
    s.login(EMAIL_SENDER, EMAIL_PASSWORD)

    to = ','.join(to)

    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER_NAME
    msg['To'] = to
    msg['Subject'] = title

    msg.attach(MIMEText(contents, 'html'))

    s.sendmail(EMAIL_SENDER, to, msg.as_string())
    s.quit()

    print(f'✅ The email successfully sent!')

if __name__ == "__main__":
    main(sys.argv)
    