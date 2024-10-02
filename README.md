# Mail33r
Programmer @F33ri

A Simple GUI mail client written in python , tkinter
Key Features:

    Input Fields: Users can input the SMTP server, port, sender email, password, recipients (supports multiple via comma-separated list), subject, and message.
    HTML Support: The user can choose to send the email as an HTML message or plain text.
    Attachments: The user can add multiple attachments of any file type (documents, images, executables, etc.).
    Broadcast Support: The user can send the email to multiple recipients by providing a comma-separated list of emails.
    Error Handling: Includes error handling for incorrect SMTP credentials or failed connections.

Libraries Used:

    smtplib: For sending emails via SMTP.
    email: To create complex email messages with attachments and HTML.
    tkinter: To create the graphical interface for the application.

Steps:

    SMTP Server and Port: By default, smtp.gmail.com and port 587 are entered, but users can modify them.
    Email Details: Users enter the sender's email, name, password, subject, and the body of the email.
    Recipients: Multiple recipients can be entered by separating their email addresses with commas.
    HTML Message: Users can choose to send the email as an HTML message by checking the "HTML Message" checkbox.
    Attachments: Clicking on "Add Attachment" allows users to select multiple files, which are displayed in a listbox.
    Send Email: The "Send Email" button sends the email, using the specified SMTP server, to the given recipients.
