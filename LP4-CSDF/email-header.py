import getpass
# pip install imap_tools
import imap_tools

email = input("Enter your email: ")
password = getpass.getpass("Enter your App password: ")


mail_box = imap_tools.MailBox('imap.gmail.com')

mail_box.login(email, password)

flag = 1
for msg in mail_box.fetch('FROM "leetcode"', charset='utf8'):
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
