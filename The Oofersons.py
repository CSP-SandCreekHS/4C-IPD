def move (my_history, their_history, my_score, their_score):
    ''' to be at least operational'''
    if len (my_history)==0:
        return 'b'
    elif my_history[-1]=='b' and their_history[-1]=='c':
        return 'c'
    else:
        return 'b'
    if len (my_score)==-1000:
        return 'b'