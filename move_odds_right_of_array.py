def move_odds(an_array):
    evens = [i for i in an_array if i%2 == 0]
    odds = [i for i in an_array if not i%2 == 0]
    final_list = sorted(evens) + sorted(odds)
    return (final_list)

an_array = [15,8,9,1,5,35,3,2,6,12]
print(move_odds(an_array))