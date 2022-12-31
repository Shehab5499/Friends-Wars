import streamlit as st
st.write('# Friends Wars Program')
def female_no_intervere(check, upset):
    if check in ['y','yes']:
        st.write('Valid input')
        sex = st.text_input('Are you male or female? male/female \n').lower()
        if sex == 'female':
            st.write(f'# Sorry! You have to leave {upset.title()} alone right now!')
        elif sex == 'male':
            st.write(f'# Just forget everything and stick to {upset.title()}.')
    elif check in ['n','no']:
        st.write('Valid input')
        st.write('That\'s sad!')
    else:
        st.write('Invalid input')
    return sex
upset = st.selectbox(
    'Who upset you?',
    ('','Omar', 'Marwan', 'Shehab'))
# try:
if upset:
    st.write(f'# I see {upset} has upset you!😞')
    if upset == 'Omar':
        check = st.text_input('Did you know that Omar is enduring very hard conditions right now 😶? y/n \n').lower()
        if check:
            female_no_intervere(check,upset)
    elif upset == "Marwan":
        check = st.text_input(f'Do you accept that {upset.title()} might be irrational sometimes? 🙁 y/n \n').lower()
        if check:
            female_no_intervere(check,upset)

    elif upset == "Shehab":
        inquire = st.text_input(f"What did he do/say to you that made you upset?\n")
        if inquire:
            st.write('## Oh 😳, how could he do this!😞')
        check = st.text_input(f"Do you want me (the program) to tell {upset.title()} about that? y/n \n").lower()
        if check in ['y','yes']:
            st.write('Valid input')
            st.write('# Ok, I will send him an email 📧 about that.')
        elif check in ['n','no']:
            st.write('Valid input')
            st.write('# Ok, I will not tell him 🤐')
        else:
            st.write('Invalid input')
else:
        st.write('Answer the question')
    # if check == 'y':
if check is True and upset is True:
    if check in ['y','yes'] and upset == "shehab":
        import smtplib

        # import os
        # EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        # EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
        # inquire= 'Hello from emailing'
        with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            sender='shehabvodafone04@gmail.com'
            smtp.login(sender,'ngudtbhvlrckmhpi')

            subject = 'Friends Wars Program'
            body = inquire
            msg = f'Subject:{subject}\n\n{body}'

            reciever = 'shoby1998eg@gmail.com'
            # smtp.sendmail(SENDER,RECIVER,msg)
            smtp.sendmail(sender, reciever, msg)
    # except:
    #     st.write(Exception())
    #     st.write('Answer the questions')