def main():

    logged = False
    points = 0

    while True:
        print("Welcome.")
        print(f'Your point number is {points}.')
        print('1. Play\n2. Top-up\n3. Login\n4. Quit')
        user_input = input(">>> ").strip()

        if user_input == '1':
            if not points:
                while True:
                    print('You have no points. Choose to login (1) or sign up (2) before topping up.')
                    choice = input('>>> ').strip()

                    if choice == '2':
                        new_login()
                        logged = True
                        break

                    elif choice == '1':
                        points = old_login()
                        logged = True
                        break

                    else:
                        print('Invalid')
            print()
            play()
        
        elif user_input == '2':

            if not logged:
                while True:
                    print('Choose to login (1) or sign up (2) before topping up.')
                    choice = input('>>> ').strip()

                    if choice == '2':
                        new_login()
                        logged = True
                        break

                    elif choice == '1':
                        points = old_login()
                        logged = True
                        break

                    else:
                        print('Invalid')
                        
            points = int(points)
            top_up_amount = top_up()
            points += top_up_amount

        elif user_input == '3':
            points = old_login()
            logged = True

        elif user_input == '4':
            quit()

        else:
            print("Invalid.")

def new_login():

    while True:
        username = input('New Username: ').strip()
        password = input('New Password: ').strip()

        if not username or not password:
            print('Invalid')
            continue
        
        with open("username_password_points.txt", 'a') as file:
            file.write(f'{username}, {password}, 0\n')
            break

def old_login():

    while True:
        login_username = input('Username: ').strip()
        login_password = input('Password: ').strip()

        with open('username_password_points.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                username, password, points = line.split(', ')
                if username == login_username and password == login_password:
                    return points
            else:
                print('Username/Password not found.')

def top_up():
    while True:
        print('''
1. Credit/Debit
2. TNG
3. Quit''')
        
        pay_choice = input('>>> ').strip()

        if pay_choice == '1':

            if not credit_debit():
                continue
            else:
                break

        elif pay_choice == '2':

            if not tng():
                continue
            else:
                break

        elif pay_choice == '3':
            return 0

        else:
            print("Invalid.")

    while True:
        try:
            amount = int(input('Your top-up amount: '))
        except ValueError:
            print('Invalid.')
        else:
            return amount

def credit_debit():

    invalid = False
    break_loop = False
    
    while True:

        if invalid:
            quit_func = input('Maybe you have pressed wrongly, do you want to quit? (Enter to quit)')
            if not quit_func:
                break_loop = True
                break
            else:
                invalid = False

        try:
            card_number = input('Card_no (16 digits): ').strip()


            if len(card_number) != 16:
                print('Invalid card no.\n')
                invalid = True

                continue

            card_number = int(card_number)

        except ValueError:
            print('Invalid character.\n')
            invalid = True

        else:
            break

    while True:

        if break_loop:
            break

        try:
            cvv = input('cvv (3 digits): ').strip()
            
            if len(cvv) != 3:
                print('Invalid cvv.\n')

                continue

            cvv = int(cvv)

        except ValueError:
            print('Invalid no for cvv.\n')

        else:
            break
    
    while True:

        if break_loop:
            break

        try: 
            exp_year, exp_month = input('Expiry date (YY/MM): ').strip().split('/')
            exp_year = int(exp_year)
            exp_month = int(exp_month)
            
        except ValueError:
            print('Invalid no for exp.\n')


        else:
            if exp_year < 10:
                exp_year = '0' + str(exp_year)
                
            if exp_month < 10:
                exp_month = '0' + str(exp_month)

            if 0 <= int(exp_year) <= 99 and 1 <= int(exp_month) <= 12: 
                break


            else:
                print('Invalid date.\n')            

                continue

    
    if not break_loop:
        with open("credit_debit_card.txt", 'a') as file:
            file.write(f'{card_number}, {cvv}, {exp_year}/{exp_month}\n')
            return True
    return False

def tng():
    
    invalid = False
    break_loop = False

    # 11 digit phone no
    # 6 digit password

    while True:

        if invalid:
            quit_func = input('Maybe you have pressed wrongly, do you want to quit? (Enter to quit)')
            if not quit_func:
                break_loop = True
                break
            else:
                invalid = False

        phone_number = input('Phone number (01X-XXXX-XXXX): ').strip()

        if phone_number[:2] == '01' and len(phone_number.replace('-', '')) == 11:
            break
        else:
            print('Invalid phone number.')
            invalid = True
            continue
        

    while True:
        
        if break_loop:
            break

        password = input('Password (6 digit): ').strip()

        if not password.isdigit() or len(password) != 6:
            print('Please type 6 digits only.')
            continue
        
        break
    
    if not break_loop:
        with open("tng.txt", 'a') as file:
            file.write(f'{phone_number}, {password}\n')
            return True
    return False

def play(): # 自己来
    print('play')

main()