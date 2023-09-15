import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Streamlit form
st.title('問い合わせフォーム')
st.caption('ご不明な点がございましたら、以下のフォームよりお問い合わせください')
with st.form(key='contact_form'):
    name = st.text_input(label='名前')
    email = st.text_input(label='メールアドレス')
    message = st.text_area(label='メッセージ')
    submit_button = st.form_submit_button(label='送信')

# Send email if form is submitted
if submit_button:
    mail_content = f'''
    名前: {name}
    メールアドレス: {email}
    メッセージ: {message}
    '''

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = 'your_email@domain.com'
    message['To'] = 'Seiya.Inagaki@modec.com'
    message['Subject'] = '問い合わせフォームからの新しいメッセージ'   
    message.attach(MIMEText(mail_content, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.office365.com', 587) # use gmail with port
    session.starttls() # enable security
    text = message.as_string()
    session.sendmail('your_email@domain.com', 'seiya.Inagaki@modec.com', text)
    session.quit()

st.success('メールが送信されました。')