import smtplib

my_email = "your email"
password = "your password"

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password,)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='receiver email',
        msg='Subject:Hello\n\nThis is the body of my mail. New email'
    )

