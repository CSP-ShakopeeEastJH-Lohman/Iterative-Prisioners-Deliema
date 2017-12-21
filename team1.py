#Makayla the best around town

team_name = 'makayla'
strategy_name = 'copy cat'
strategy_description = 'Tit for tat, check for repetitive patterns.'  
    
def move(my_history, their_history, my_score, their_score):
    '''basic start'''
    
    if len(my_history) < 3:
        return 'c'

    if their_history.count('b') == 0:
        return 'c'
    if their_history.count('b') >= 1:
        '''checking for very repetitive patterns'''
        if their_history[-1: -4] == 'b':
            return 'b'
        if their_history[-1: -4] == 'c':
            return 'b'
        
        '''general strat'''
        '''tit for tat
        once an opponent defects, the tit for tat player immediately responds by defecting on the next move'''
        if their_history[-1] == 'b':
            return 'b'
        if their_history[-1] == 'c':
            return 'c'  