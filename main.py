attempts=0
while attempts<3:
    username=input('username?')
    password=input('password?')
    if username=='correctusername'and password=='correctpassword':
        print('you are in!')
    else:
        attempts+=1
        print('incorrect!')
        if attempts==3:
            print('too many attempts')
