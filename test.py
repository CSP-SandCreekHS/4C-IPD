def move(my_history, their_history, my_score=0,their_score=0):
    if len(my_history)==0:
        return 'c'
    elif my_history[-100]=='c' and their_history[0]=='b':
        return'b'
    if len (my_history)==100:
        return 'b'
    