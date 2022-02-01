def draw_result(player_mark_list):
    for i in range(len(player_mark_list)):
        # ajust space
        if i%3 == 0:
            print('  ',end='')

        # get data from ele
        ele = str(player_mark_list[i])
        # draw a mark
        print(ele, end=' ')

        # adjust layout
        if i % 3 != 2:
            print('|',end=' ')
        # create border
        if i%3 == 2 and i != len(player_mark_list)-1:
            print('')
            print('','---|---|---')
    
    # line break
    print('')
