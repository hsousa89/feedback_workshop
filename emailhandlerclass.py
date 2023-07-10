import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailHandler:
    """
    A class to send email messages
    """

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    sender_email = os.environ["AESJE_EMAIL_USER"]
    sender_password = os.environ["AESJE_EMAIL_PASSWORD"]

    def __init__(self, subject, body):
        """
        Initialize an instance of the Email class with the subject and body of the email message.

        Args:
            subject (str): The subject of the email message.
            body (str): The body of the email message.
        """
        self.subject = subject
        self.body = body

    @classmethod
    def set_port(cls, port):
        """
        Set the SMTP port number.

        Args:
            port (int): The port number to use for the SMTP server.
        """
        cls.port = port

    @classmethod
    def set_smtp_server(cls, server):
        """
        Set the SMTP server.

        Args:
            server (str): The address of the SMTP server to use.
        """
        cls.smtp_server = server

    @classmethod
    def set_context(cls, context):
        """
        Set the SSL context.

        Args:
            context (ssl.SSLContext): The SSL context to use for the SMTP connection.
        """
        cls.context = context

    @classmethod
    def set_sender_email(cls, email):
        """
        Set the email address of the sender.

        Args:
            email (str): The email address of the sender.
        """
        cls.sender_email = email

    @classmethod
    def set_sender_password(cls, password):
        """
        Set the password of the sender email account.

        Args:
            password (str): The password of the sender email account.
        """
        cls.sender_password = password

    def send(self, receiver_emails):
        """
        Send the email message to multiple recipients.

        Args:
            receiver_emails (list): A list of email addresses of the recipients.
        """
        # Create the plain text version of the message
        plain_text = self.body.replace("<br>", "\n")
        plain_part = MIMEText(plain_text, "plain")

        # Create the HTML version of the message
        html_part = MIMEText(self.body, "html")

        # Combine the parts into a single message
        message = MIMEMultipart("alternative")
        message["From"] = self.sender_email
        message["To"] = ", ".join(receiver_emails)
        message["Subject"] = self.subject
        message.attach(plain_part)
        message.attach(html_part)

        with smtplib.SMTP_SSL(
            self.smtp_server, self.port, context=self.context
        ) as server:
            server.login(self.sender_email, self.sender_password)
            for receiver_email in receiver_emails:
                server.sendmail(self.sender_email, receiver_email, message.as_string())
