with open('sample_auth_log.txt', 'r') as file:
    for line in file:
        if 'ERROR' in line:
            print('Found error:', line.strip())
