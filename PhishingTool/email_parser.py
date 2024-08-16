import email
from email import policy
from urllib.parse import urlparse
import re

def extract_urls(text):
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    return [url for url in urls]

def extract_headers(email_message):
    headers = {}
    for header in ['from', 'to', 'subject', 'date']:
        headers[header] = email_message.get(header, "unknown")
    return headers

def extract_body(email_message):
    body = []
    if email_message.is_multipart():
        for part in email_message.walk():
            ctype = part.get_content_type()
            if ctype == 'text/plain' and 'attachment' not in str(part.get('Content-Disposition')):
                body.append(part.get_payload(decode=True).decode())
            elif ctype == 'text/html':
                body.append(part.get_payload(decode=True).decode())
    else:
        body.append(email_message.get_payload(decode=True).decode())
    return ' '.join(body)

def parse_email(raw_email):
    email_message = email.message_from_string(raw_email, policy=policy.default)
    headers = extract_headers(email_message)
    body = extract_body(email_message)
    urls = extract_urls(body)
    return {
        'headers': headers,
        'body': body,
        'urls': urls
    }
