import smtplib
import os
from tkinter import *
from tkinter import filedialog, messagebox
from email.message import EmailMessage
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Function to send the email
def send_email():
    try:
        smtp_server = smtp_entry.get()
        port = port_entry.get()
        sender_email = sender_entry.get()
        sender_name = sender_name_entry.get()
        password = password_entry.get()
        subject = subject_entry.get()
        message_body = message_text.get("1.0", END)
        recipients = recipient_entry.get().split(',')
        
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['Subject'] = subject
        
        if html_var.get():
            msg.attach(MIMEText(message_body, 'html'))
        else:
            msg.attach(MIMEText(message_body, 'plain'))

        # Attach files
        for file in attachments:
            with open(file, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(file)
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file_data)
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={file_name}')
                msg.attach(part)

        # Send the email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, password)
            for recipient in recipients:
                msg['To'] = recipient.strip()
                server.sendmail(sender_email, recipient.strip(), msg.as_string())

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

# Function to add attachments
def add_attachment():
    files = filedialog.askopenfilenames()
    for file in files:
        attachments.append(file)
        attachment_listbox.insert(END, os.path.basename(file))

# GUI Application
root = Tk()
root.title("Email Sender")
root.geometry("600x500")

attachments = []

# SMTP Server and Port
Label(root, text="SMTP Server:").grid(row=0, column=0, padx=10, pady=5, sticky=E)
smtp_entry = Entry(root, width=40)
smtp_entry.grid(row=0, column=1, pady=5)
smtp_entry.insert(0, "smtp.gmail.com")

Label(root, text="Port:").grid(row=1, column=0, padx=10, pady=5, sticky=E)
port_entry = Entry(root, width=40)
port_entry.grid(row=1, column=1, pady=5)
port_entry.insert(0, "587")

# Sender Email and Password
Label(root, text="Sender Email:").grid(row=2, column=0, padx=10, pady=5, sticky=E)
sender_entry = Entry(root, width=40)
sender_entry.grid(row=2, column=1, pady=5)

Label(root, text="Sender Name:").grid(row=3, column=0, padx=10, pady=5, sticky=E)
sender_name_entry = Entry(root, width=40)
sender_name_entry.grid(row=3, column=1, pady=5)

Label(root, text="Password:").grid(row=4, column=0, padx=10, pady=5, sticky=E)
password_entry = Entry(root, width=40, show="*")
password_entry.grid(row=4, column=1, pady=5)

# Recipient(s)
Label(root, text="Recipient(s) (comma-separated):").grid(row=5, column=0, padx=10, pady=5, sticky=E)
recipient_entry = Entry(root, width=40)
recipient_entry.grid(row=5, column=1, pady=5)

# Subject
Label(root, text="Subject:").grid(row=6, column=0, padx=10, pady=5, sticky=E)
subject_entry = Entry(root, width=40)
subject_entry.grid(row=6, column=1, pady=5)

# Message Body
Label(root, text="Message:").grid(row=7, column=0, padx=10, pady=5, sticky=NE)
message_text = Text(root, width=40, height=10)
message_text.grid(row=7, column=1, pady=5)

# HTML message option
html_var = BooleanVar()
html_check = Checkbutton(root, text="HTML Message", variable=html_var)
html_check.grid(row=8, column=1, sticky=W)

# Attachments
Label(root, text="Attachments:").grid(row=9, column=0, padx=10, pady=5, sticky=NE)
attachment_listbox = Listbox(root, width=40, height=5)
attachment_listbox.grid(row=9, column=1, pady=5)
Button(root, text="Add Attachment", command=add_attachment).grid(row=10, column=1, pady=5, sticky=W)

# Send Email Button
Button(root, text="Send Email", command=send_email).grid(row=11, column=1, pady=10, sticky=E)

root.mainloop()
