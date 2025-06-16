# Functions that format and sends ready results to gmail;
from email.message import EmailMessage
from typing import List, Optional
import mimetypes
from email.utils import formataddr
import os

class EmailBuilder:
    def __init__(self, subject: str, sender: str, recipients: List[str]):
        self.subject = subject
        self.sender = sender
        self.recipients = recipients
        self.cc = []
        self.bcc = []
        self.body_text = ""
        self.body_html = None
        self.attachments = []

    def set_text_body(self, text: str):
        self.body_text = text

    def set_html_body(self, html: str):
        self.body_html = html

    def add_cc(self, cc_list: List[str]):
        self.cc.extend(cc_list)

    def add_bcc(self, bcc_list: List[str]):
        self.bcc.extend(bcc_list)

    def add_attachment(self, filepath: str):
        if os.path.isfile(filepath):
            self.attachments.append(filepath)
        else:
            raise FileNotFoundError(f"Attachment not found: {filepath}")

    def build(self) -> EmailMessage:
        msg = EmailMessage()
        msg['Subject'] = self.subject
        msg['From'] = formataddr(("Idea Generator Bot", self.sender))
        msg['To'] = ', '.join(self.recipients)
        if self.cc:
            msg['Cc'] = ', '.join(self.cc)

        # Set plain or multipart content
        if self.body_html:
            msg.set_content(self.body_text or "This is a multipart message in MIME format.")
            msg.add_alternative(self.body_html, subtype='html')
        else:
            msg.set_content(self.body_text)

        # Add attachments
        for filepath in self.attachments:
            with open(filepath, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(filepath)
                maintype, subtype = mimetypes.guess_type(filepath)[0].split('/')
                msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)

        return msg
