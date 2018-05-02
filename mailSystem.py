from SpeechRecognition import speech,textTospeech

import smtplib

import config


def send_email(subject, msg,sender_mail_id):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, sender_mail_id, message)
        server.quit()
        print("Success: Email sent!")
    except Exception as e:
        print e
        print("Email failed to send.")


def convertGmail(gmail):
    gmail=gmail.split(" ")
    return ''.join(gmail)

def mailInforamtion():
    textTospeech("sender`s email id ")
    sender_email_id = speech()
    sender_email_id=convertGmail(sender_email_id)
    print sender_email_id

    textTospeech("subject of the email")
    subject=speech()
    print "subject of email :", subject

    textTospeech('mesaage of the email')
    msg=speech()

    print "message of email : ", msg
    print sender_email_id,subject,msg
    send_email(subject,msg,sender_email_id)

#send_email(subject, msg)
if __name__ == '__main__':
    mailInforamtion()
    pass