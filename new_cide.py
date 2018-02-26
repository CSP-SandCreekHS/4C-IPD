def move(my_history, their_history, my_score, their_score):
    
    if len(my_history) == 0:     
       return 'b'
    elif len(my_history):
        return 'c'
    elif len(my_history):
        return 'c'
    elif their_history[-1] == 'c':
        return 'b'
    elif their_history[-1] == 'b':
        return 'b'
    else:
        return 'c'
