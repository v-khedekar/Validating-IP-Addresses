def isValidIP(ip_str):
    count = 0
    subnet = ip_str.split('.')
    #Check first, whether there are 4 subnet parts
    if len(subnet) == 4:
        for sub in subnet:
            if sub.isnumeric() and len(sub) <= 3 and (int(sub) >= 0 and int(sub) <= 255):
                count += 1
    if count == 4:
        return True
    else:
        return False


if isValidIP('10.0.0.25a'):
    print('Valid IP address')
else:
    print('Invalid IP address')