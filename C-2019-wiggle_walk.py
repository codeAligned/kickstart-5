def findListIndex(li, key):
    length = len(li)
    index = int((length)/2)
    itr = 0
    while not (li[index][0] <= key and li[index][1] >= key) and itr < length:
        if li[index][0] > key :
            index = int(index/2)
        else :
            index = int(index + ((index+1)/2))
        itr = itr + 1
    return index
def addNonListIndex(li, key, ref_idx):
    length = len(li)
    index = ref_idx
    if index >= length:
        index = int(length/2)
    
    low = 0
    high = length
    if li[0][0] > key:
        if li[0][0] - key > 1:
            li.insert(0, [key,key])
        else:
            li[0][0] = key
        return 0
    elif li[length-1][0] < key:
        if key - li[length-1][1] > 1:
            li.append([key,key])
            return length
        else:
            li[length-1][1] = key
        return length-1
    if li[index][0] > key :
        high = index + 1
        low = 0
    elif li[index][0] < key :
        high = length
        low = index + 1
    index = int ((high+low)/2)
    while low<=high and not ((length > (index+1) and li[index][0] < key and li[index+1][0] > key) or
               (index > 0 and li[index-1][0] < key and li[index][0] > key) ) :
        if li[index][0] > key :
            high = index - 1
            index = int((high+low)/2)
        else :
            low = index + 1
            index = int((high+low)/2)

    if low>high:
        print("SOME ERROR: " + str(key) + " NOT located in list")
        print(li)
        return -1

    if length>(index+1) and li[index][0] < key and li[index+1][0] > key :
        if key - li[index][1] > 1:
            if li[index+1][0] - key > 1:
                li.insert(index+1,[key,key])
            else:
                li[index+1][0] = key
            return index+1
        else:
            if li[index+1][0] - key > 1:
                li[index][1] = key
            else:
                li[index][1] = li[index+1][1]
                del li[index+1]
            return index
    else:
        if key - li[index-1][1] > 1:
            if li[index][0] - key > 1:
                li.insert(index, [key,key])
            else :
                li[index][0] = key
            return index
        else:
            if li[index][0] - key > 1:
                li[index-1][1] = key
            else:
                li[index-1][1] = li[index][1]
                del li[index]
            return index-1

#temp_list = [[1,2], [4,5], [6,10]]
#idx = findListIndex(temp_list, 7)
#print (idx)
#move = input()
T = input()
testcases = int(T)

for itr in range (1, testcases+1) :
    iplist = input()
    tokens = iplist.split(' ')
    moves = int(tokens[0])
    rows = int(tokens[1])
    cols = int(tokens[2])
    s_row = int(tokens[3])
    s_col = int(tokens[4])
    row_intervals = {}
    col_intervals = {}
    row_intervals[s_row] = [[s_col, s_col]]
    col_intervals[s_col] = [[s_row, s_row]]

    move = input()
    row_idx = 0
    col_idx = 0
    for i in range (0, moves) :
        if move[i] == 'W':
            #if i > 0 and (move[i-1] == 'N' or move[i-1] == 'S'):
            #    idx = findListIndex(row_intervals[s_row], s_col)
            s_col = row_intervals[s_row][row_idx][0] - 1
            if row_idx > 0 and row_intervals[s_row][row_idx-1][1] == s_col - 1:
                row_intervals[s_row][row_idx-1][1] = row_intervals[s_row][row_idx][1]
                del row_intervals[s_row][row_idx]
                row_idx = row_idx-1
            else:
                row_intervals[s_row][row_idx][0] = s_col
            if s_col in col_intervals :
                tmp = col_idx
                col_idx = addNonListIndex(col_intervals[s_col], s_row, tmp)
            else :
                col_intervals[s_col] = [[s_row,s_row]]
                col_idx = 0
        elif move[i] == 'E' :
            #if i > 0 and (move[i-1] == 'N' or move[i-1] == 'S'):
            #    idx = findListIndex(row_intervals[s_row], s_col)
            s_col = row_intervals[s_row][row_idx][1] + 1
            if len(row_intervals[s_row]) > row_idx+1 and row_intervals[s_row][row_idx+1][0] == s_col + 1:
                row_intervals[s_row][row_idx][1] = row_intervals[s_row][row_idx+1][1]
                del row_intervals[s_row][row_idx+1]
            else:
                row_intervals[s_row][row_idx][1] = s_col
            if s_col in col_intervals :
                tmp = col_idx
                col_idx = addNonListIndex(col_intervals[s_col], s_row, tmp)
            else :
                col_intervals[s_col] = [[s_row,s_row]]
                col_idx = 0
        elif move[i] == 'N' :
            #if i > 0 and (move[i-1] == 'W' or move[i-1] == 'E'):
            #    idx = findListIndex(col_intervals[s_col], s_row)
            s_row = col_intervals[s_col][col_idx][0] - 1
            if col_idx>0 and col_intervals[s_col][col_idx-1][1] == s_row-1:
                col_intervals[s_col][col_idx-1][1] = col_intervals[s_col][col_idx][1]
                del col_intervals[s_col][col_idx]
                col_idx = col_idx - 1
            else:
                col_intervals[s_col][col_idx][0] = s_row
            if s_row in row_intervals :
                tmp = row_idx
                row_idx = addNonListIndex(row_intervals[s_row], s_col, tmp)
            else :
                row_intervals[s_row] = [[s_col,s_col]]
                row_idx = 0
        elif move[i] == 'S' :
            #if i > 0 and (move[i-1] == 'W' or move[i-1] == 'E'):
            #    idx = findListIndex(col_intervals[s_col], s_row)
            s_row = col_intervals[s_col][col_idx][1] + 1
            if len(col_intervals[s_col]) > col_idx+1 and col_intervals[s_col][col_idx+1][0] == s_row+1:
                col_intervals[s_col][col_idx][1] = col_intervals[s_col][col_idx+1][1]
                del col_intervals[s_col][col_idx+1]
            else:
                col_intervals[s_col][col_idx][1] = s_row
            if s_row in row_intervals :
                tmp = row_idx
                row_idx = addNonListIndex(row_intervals[s_row], s_col, tmp)
            else :
                row_intervals[s_row] = [[s_col,s_col]]
                row_idx = 0
    for l2 in row_intervals :
        del l2
    del row_intervals
    for l2 in col_intervals :
        del l2
    del col_intervals
    print ("Case #" + str(itr) + ": " + str(s_row) + " " + str(s_col))