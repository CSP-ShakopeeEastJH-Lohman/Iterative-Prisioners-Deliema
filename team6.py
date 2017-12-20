#Bennett blue cat
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)== 0:
        return 'c'
    if their_history[-1]== 'b':
        return 'b'
    if len(my_history) < 2 and their_history[-1]== 'c':
        return'c'
    if their_history[-2] == 'c' and their_history[-1]=='c':
        return 'c'
    if their_history[-1]=='b':
        return 'b'
    if len(my_history) ==199:
        return 'b'
    if their_history[-1:-4]==['c','c','c','c']:
        return 'c'
    if their_history[-1:-4]==['b','b','b','b']:
        return 'b'
    if their_history[-1:-4]==['c','b','c','b']:
        return 'c'
    if their_history[-1:-4]==['c','c','b','b']:
        return 'b'
    else:
        return'b'



