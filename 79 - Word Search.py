def exist(board, word):
    exist = False
    wordLen = len(word)
    numRows = len(board)
    numCols = len(board[0])
    checker = 1
    for i in range(numRows):
        for j in range(numCols):
            if board[i][j] == word[0]:
                currLetter = 0
                neighbours = []
                currLetter += 1
                if i > 0 and board[i-1][j] == word[currLetter]:
                    neighbours.append(i-1, j, 'D')
                if i < numRows - 1 and board[i+1][j] == word[currLetter]:
                    neighbours.append( i+1,j, 'U')
                if j > 0 and board[i][j-1] == word[currLetter]:
                    neighbours.append(board[i][j-1], i,j-1, "R")
                if j > numCols -1 and board[i][j+1] == word[currLetter]:
                    neighbours.append( i,j+1, "L")
                if len(neighbours) > 0:
                    for k in range(len(neighbours)):
                        while currLetter < wordLen:
                            # check neighbours
                            if neighbours[k[0]] > 0 and board[neighbours[k[0]] - 1][neighbours[k[1]]] == word[currLetter]:  # up
                                currLetter += 1
                                letter[0] -= 1
                            elif letter[0] < numRows - 1 and board[letter[0] + 1][letter[1]] == word[
                                currLetter]:  # down
                                currLetter += 1
                                letter[0] += 1
                            elif letter[1] > 0 and board[letter[0]][letter[1] - 1] == word[currLetter]:  # left
                                currLetter += 1
                                letter[1] -= 1
                            elif letter[1] < numCols - 1 and board[letter[0]][letter[1] + 1] == word[
                                currLetter]:  # right
                                currLetter += 1
                                letter[1] += 1
                            else:
                                break
                            if currLetter == wordLen:
                                exist = True

                else:
                    currLetter = 0



    # while checker != 0: #for i in range(len(word)):
    #     for r in range(numRows):
    #         if not exist:
    #             for c in range(numCols):
    #                 if board[r][c] == word[0] and not exist:
    #                     currLetter = 0
    #                     letter = [r, c]
    #                     currLetter += 1
    #                     while currLetter < wordLen:
    #                         # check neighbours
    #                         if letter[0] > 0 and board[letter[0] - 1][letter[1]] == word[currLetter]:  # up
    #                             currLetter += 1
    #                             letter[0] -= 1
    #                         elif letter[0] < numRows - 1 and board[letter[0] + 1][letter[1]] == word[
    #                             currLetter]:  # down
    #                             currLetter += 1
    #                             letter[0] += 1
    #                         elif letter[1] > 0 and board[letter[0]][letter[1] - 1] == word[currLetter]:  # left
    #                             currLetter += 1
    #                             letter[1] -= 1
    #                         elif letter[1] < numCols - 1 and board[letter[0]][letter[1] + 1] == word[
    #                             currLetter]:  # right
    #                             currLetter += 1
    #                             letter[1] += 1
    #                         else:
    #                             break
    #                         if currLetter == wordLen:
    #                             exist = True
    #                 elif exist:
    #                     break
    #         else:
    #             break
    #     checker = 0


    return exist

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(exist(board, word))
