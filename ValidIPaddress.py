def isValidIP(ip_str):
    ipv4 = ip_str.split('.')
    ipv6 = ip_str.split(':')

    validIPv6Chars = 'ABCDEFabcdef:0123456789'
    v4count = 0
    v6count = 0
    v4 = False
    v6 = False

    # IP V4 check
    if len(ipv4) == 4:
        for i in ipv4:
            if i.isnumeric() and int(i) >= 0 and int(i) <= 255:
                v4count += 1
        if v4count == 4:
            v4 = True
    # IP V6 check
    elif len(ipv6) == 8:
        for i in ipv6:
            if len(i) <= 4 and all(each in validIPv6Chars for each in i):
                v6count += 1
        if v6count == 8:
            v6 = True

    # Results:
    if v4 == True:
        print('This is a valid IPv4 address')
    elif v6 == True:
        print('This is a valid IPv6 address')
    else:
        print('Not a valid IP address!')
