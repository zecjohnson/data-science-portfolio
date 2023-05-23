import smtplib
import ssl
import csv

# Set up email content
sender_email = "test@gmail.com"
password = "dghhomzqdffdddsmib"
subject = "Test Email"
message_template = """\
Hello {name},

This is a personalized message sent using Python.

<p>

With this script, {company_name} can automate email delivery and save big in admin costs.

<p>

You know where to find us

<p>

<span style="font-size: 14px; font-style: italic;">
-- 
Sender
</span>
"""

# Connect to Gmail's SMTP server
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)

    # Read the CSV file and send an email to each recipient
    with open("Emails.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for name, email, company_name in reader:
            # Personalize the message for each recipient
            message = message_template.format(name=name,company_name=company_name)

            # Send the email
            server.sendmail(sender_email, email, f"Subject: {subject}\nMIME-Version: 1.0\nContent-type: text/html\n\n{message}")