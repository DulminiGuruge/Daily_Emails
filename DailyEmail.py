import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import GetData as email_content
import json
import base64
from datetime import datetime



class DailyEmail():
    

    def __init__(self):
       

        #read the config details from json file format
        with open("configs.json","r")as in_file:
            json_obj=json.load(in_file)

        self.sender_email= json_obj["username"]
       
        #convert sender pwd to byte
        sender_pwd =json_obj["password"]
        sender_password=base64.b64decode(sender_pwd) 
        print(sender_password)

        json_time = json_obj["time"]
        date_format = '%H:%M:%S'
        sceduled_time = datetime.strptime(json_time,date_format)
        print(sceduled_time)






        # self.sender_email = "my@gmail.com"
        # self.receiver_email = "your@gmail.com"
        # self.password = input("Type your password and press enter:")

        # self.message = MIMEMultipart("alternative")
        # self.message["Subject"] = "multipart test"
        # self.message["From"] = self.sender_email
        # self.message["To"] = self.receiver_email

    def send_email():
        pass

    def format_email():
        weathaer =email_content.GetAPIData.get_weather_forecast
        #events = email_content.GetAPIData.get_google_calender_api
       



    # # Create the plain-text and HTML version of your message
    # text = """\
    # Hi,
    # How are you?
    # Real Python has many great tutorials:
    # www.realpython.com"""
    # html = """\
    # <html>
    # <body>
    #     <p>Hi,<br>
    #     How are you?<br>
    #     <a href="http://www.realpython.com">Real Python</a> 
    #     has many great tutorials.
    #     </p>
    # </body>
    # </html>
    # """

    # # Turn these into plain/html MIMEText objects
    # part1 = MIMEText(text, "plain")
    # part2 = MIMEText(html, "html")

    # # Add HTML/plain-text parts to MIMEMultipart message
    # # The email client will try to render the last part first
    # message.attach(part1)
    # message.attach(part2)

    # # Create secure connection with server and send email
    # context = ssl.create_default_context()
    # with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #     server.login(sender_email, password)
    #     server.sendmail(
    #         sender_email, receiver_email, message.as_string()
    #     )


daily_email = DailyEmail()
daily_email.format_email()