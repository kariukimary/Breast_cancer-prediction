import streamlit as st
import smtplib
from email.mime.text import MIMEText





body_ = """ ## How to prevent breast cancer
    - eating of vegetables, fruits and limit acohol consumption
    diet reduces the risk of breast cancer, also limiting acohol consumption to zero would be the best since acohol increases the risk of breast cancer
    - Avoid Birth Control Pills
    are taking birth control pills, they have a slightly increased risk of breast cancer. This risk goes away quickly after stopping the pill.
    - Regular Screening
    breast exams can significantly improve treatment outcomes. Women should discuss the appropriate screening schedule with their healthcare provider to reduce the risk of the breast cancer.
    - Be Physically Active
    exercise is one of the best things for your health. It can boost mood and energy. It can help keep weight in check. And it can lower the risk of many serious diseases, including breast cancer. Try to get at least 30 minutes a day, but any amount of physical activity is better than none.
    - Breastfeeding the child as much as possible
    who breastfeed may have a slightly lower risk of breast cancer. Additionally, breastfeeding has other health benefits for both the mother and the child.
    ( for more information 
    (https://www.mayoclinic.org/healthy-lifestyle/womens-health/in-depth/breast-cancer-prevention/art-20044676))
"""
    
st.markdown(body_)
def patient():

    # Taking inputs
    email_sender = 'kariukimary2021@gmail.com'
    email_receiver = st.text_input('To')
    subject = 'How to prevent breast cancer'
    body = body_
    password = 'dznl pkmb icpf dybq'

   

    if st.button("Send Email"):
        try:
            msg = MIMEText(body)
            msg['From'] = email_sender
            msg['To'] = email_receiver
            msg['Subject'] = subject

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_sender, password)
            server.sendmail(email_sender, email_receiver, msg.as_string())
            server.quit()

            st.success('Email sent successfully! 🚀')
        except Exception as e:
            st.error(f"Erreur lors de l’envoi de l’e-mail : {e}")   
if __name__ == '__main__':
    patient()