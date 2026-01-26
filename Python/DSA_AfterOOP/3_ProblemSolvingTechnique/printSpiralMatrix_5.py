# print matrix element in spiral format:


def spiralOrder(arr: list[list[int]]):
    # row
    n = len(arr)
    # coln
    m = len(arr[0])
    

    col_start, col_end = 0, m - 1
    row_start, row_end = 0, n - 1

    ans = []

    while len(ans) < n * m:
        # print row from col start to col end
        for i in range(col_start, col_end + 1):
            ans.append(arr[row_start][i])
        row_start += 1

        if len(ans) == n * m:
            break

        # print col from row start to row end:
        for j in range(row_start, row_end + 1):
            ans.append(arr[j][col_end])
        col_end -= 1

        if len(ans) == n * m:
            break


        #print reverse row from col end to col start:

        for i in range(col_end, col_start-1,-1):
            ans.append(arr[row_end][i])
        row_end-=1

        if len(ans) == n*m:
            break

        #print col_start from row_end to row_start:
        for i in range(row_end,row_start-1,-1):
            ans.append(arr[i][col_start])
        col_start+=1

    return ans;

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]));
