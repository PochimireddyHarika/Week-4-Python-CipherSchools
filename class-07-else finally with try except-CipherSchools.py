while True:
    try:
        number = int(input('enter a number : '))
    
    except ValueError:
        print('Please type integer !! s')
    except:
        print('unexcepted error !!! ')
    else:
        print(f'user input = {number}')
        break
    finally:
        print('finally blocks .....')