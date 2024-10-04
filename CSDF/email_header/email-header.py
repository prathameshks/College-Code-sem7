import getpass
# pip install imap_tools
import imap_tools

from email import policy
from email.parser import BytesParser

# Load the .eml file
eml_file_path = 'sample_mail.eml'  # replace with your .eml file path
with open(eml_file_path, 'rb') as f:
    msg = BytesParser(policy=policy.default).parse(f)

print(msg.keys())
# Extract headers
print(f"{ msg['Message-ID'] = }")
print(f"{ msg['From'] = }")
print(f"{ msg['To'] = }")
print(f"{ msg['Date'] = }")
print(f"{ msg['Subject'] = }")
print(f"{ msg['MIME-Version'] = }")
print(f"{ msg['Delivered-To'] = }")


# Using Gmail Login
email_id = input("Enter your email: ")
password = getpass.getpass("Enter your App password: ")

mail_box = imap_tools.MailBox('imap.gmail.com')
mail_box.login(email_id, password)

flag = 1
for msg in mail_box.fetch('FROM "geeksforgeeks"', charset='utf8'):
    print("\nMessage: ",flag)
    print("Message id:",msg.uid)
    print("Message from:",msg.from_)
    print("Message to:",msg.to)
    print("Message Reply to:",msg.reply_to)
    print("Message Subject:",msg.subject)
    print("Message Date:", msg.date)
    
    flag+=1
    if(flag > 5): 
        break
