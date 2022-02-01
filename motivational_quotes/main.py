import smtplib, os, datetime
import random as rd

weekday = datetime.datetime.now().weekday()

if weekday in range(0, 5):
    SMTP_HOST = "smtp.gmail.com"
    PORT = "587"

    EMAIL = "[DEFAULT_EMAIL]"
    PASSWD = os.getenv("email_key")

    # create quotes
    with open("./quotes.txt", "r") as text:
        all_quotes = text.readlines()
        quote = rd.choice(all_quotes)

    print(quote.strip())

    # create SMTP connection

    with smtplib.SMTP(host=SMTP_HOST, port=PORT) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="random@mail.com",
            msg=f"""Subject:Quote of the day!
                \n\n
        Here is a quote to keep you up:
        {quote.strip()}
        \nStay awesome!
        \nRafael Heineck
                """,
        )
