import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage

content = ['this is a test', 'Test sample']
email_from = 'HRIS@happymeal.com'
email_to = 'test@happymeal.com', 'Test2@happymeal.com', 'Test3@happymeal.com'
msg = EmailMessage()
msg['Subject'] = 'Test email'
msg['From'] = email_from
msg['To'] = email_to
html_template_start = """\
  <html>
    <head></head>
    <body>
    <p style="color:Red;"">
  """

html_template_end = """ </p></body>
  </html>
  """
if content.__len__ () == 0:
    exit(0)
html = ''
for i in content:
    html = html + i + '<br>'
html = html_template_start + html + html_template_end
s = smtplib.SMTP ( 'mail.happymeal.domanin.com' )

msg['X-Priority'] = '2'  # high importance  - please check on Schaduled tasks and restart them.
html = "12345678"
part = MIMEText ( html, 'text' )

#msg.attach ( part )
print(html)

msg.set_content(html)
s.send_message(msg)

s.quit ()
