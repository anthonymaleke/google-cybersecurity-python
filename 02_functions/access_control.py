def check_access(user):
    return user in ['admin', 'sysadmin']

print(check_access('guest'))
