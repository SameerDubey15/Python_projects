email=input("Enter your email id :\n").strip()
name=email[:email.index("@")]
domain=email[email.index("@")+1:]
msg="Your Name Is {} and Domain Is {}".format(name,domain)
print(msg)
