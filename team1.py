#Makayla

team_name = 'no me gusta'
strategy_name = 'yah'
strategy_description = 'it tries its best'  
    
def move(my_history, their_history, my_score, their_score):
    '''basic start'''
    if len(my_history) == 0:
        return 'b'
        
    '''checks the basic c,b,c,b,c,b pattern'''
    if their_history[-1] == their_history[-3]:
        if their_history[-1] == 'c':
            return 'b'
        elif their_history[-1] == 'b':
            return 'c'
    
    '''checks the c,b,b pattern'''
    if their_history[-1] == their_history[-4]:
        if their_history[-1] == 'c':
            return 'b'
        elif their_history[-1] == 'b':
            return 'c'
    
    '''checks cccb pattern'''
    if their_history[-1] == their_history[-5]:
        if their_history[-1] == 'b':
            return 'c'
        if their_history[-1] == 'c':
            return 'b'
        
    '''checking for very repetitive patterns'''
    if their_history[-1] and their_history[-2] and their_history[-3] and their_history[-4] == 'b':
        return 'b'
    if their_history[-1] and their_history[-2] and their_history[-3] and their_history[-4] == 'c':
        return 'b'
        
    '''score plans'''
    if their_score > 0:
        if their_history[-1] == their_history[-3]:
            if their_history[-1] == 'c':
                return 'b'
            elif their_history[-1] == 'b':
                return 'c'
        if their_history[-1] == 'c':
            return 'b'
        elif their_history[-1] == 'b':
            return 'c'
        if their_history[-1] == their_history[-5]:
            if their_history[-1] == 'b':
                return 'c'
            if their_history[-1] == 'c':
                return 'b'
    if my_score < 0:
        return 'b'
        
    '''backup plan / basic checks'''    
    if their_history[-1] and their_history[-2] == 'c':
        return 'b'
    if their_history[-1] and their_history[-2] == 'b':
        return 'c'
    if their_history[-3] == 'b':
        return 'b'
