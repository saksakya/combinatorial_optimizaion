

def input_number(output_string, start_num = 0, end_num = 1000):

    error_message = lambda : print('This is an unaccepted response, enter a valid value')
    
    while True:
        try:
            mode = int(input(output_string))
        except ValueError:
            error_message()
            continue
        else:
            if start_num <= mode <= end_num :
                return mode

            else:
                error_message()
                continue