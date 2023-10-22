

email_address = input("Enter email: ")
(username, domain_extension) = email_address.split('@')
domain, extension = domain_extension.split('.')

print("Username: {}\nDomain: {}\nExtension: {}".format(username, domain, extension))
