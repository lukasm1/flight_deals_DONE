import smtplib
from twilio.rest import Client


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "ACf5418303292dfbd89af16fbbe74a633a"
        self.auth_token = "a16eda7674aae40b3df8cc7e3d25a653"
        self.client = Client(self.account_sid, self.auth_token)
        self.my_email = "pycharmtester1@gmail.com"
        self.password = "XX"

    def send_sms(self, sms_text):
        message = self.client.messages \
            .create(
            body=sms_text,
            from_="+15869913247",
            to = '+420777537252',
        )
        print(message.status)

    def send_emails(self, email_list, email_text, url_text):

        for email in email_list:

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.password)
                connection.sendmail(from_addr=self.my_email, to_addrs=email, msg=f"Subject:New Low Price Flight!\n\n{email_text}\n{url_text}".encode('utf-8'))

