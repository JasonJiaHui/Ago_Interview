

'''
1. LCS
    table[i+1][j+1] = table[i][j] + 1         if str1[i] == str2[j]
    table[i+1][j+1] = max(table[i+1][j], table[i][j+1])  otherwise
'''

def LCS(str1, str2):
    table = [[0 for i in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                table[i+1][j+1] = table[i][j] + 1
            else:
                table[i+1][j+1] = max(table[i+1][j], table[i][j+1])

    print table[-1][-1]


'''
2. LCSString
    table[i+1][j+1] = table[i][j] + 1       if str1[i] == str2[j]
    table[i+1][j+1] = 0                     otherwise
'''
def LCSString(str1, str2):
    table = [[0 for i in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    maxLen = 0
    maxIndex = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                table[i+1][j+1] = 1 + table[i][j]
                if maxLen < table[i+1][j+1]:
                    maxLen = table[i+1][j+1]
                    maxIndex = i + 1


    print "MaxLen: ", maxLen
    print "MaxIndex: ", maxIndex

'''
3. LIS
    L[i] = 1 + max(L[j])  if 0 < j < i and arr[j] < arr[i]
    L[i] = 0         otherwise
'''

def LIS(arr):

    L = [1 for i in range(len(arr))]

    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and L[j] + 1 > L[i]:
                L[i] = L[j] + 1

    print L

'''
4. knapsack

for(int i=0; i<=n; ++i){
    for(int j=0; j<=C; ++j){
        d[i][j] = i==0 ? 0 : d[i-1][j];
        if(i>0 && j>=V[i-1])  d[i][j] >?= d[i-1][j-V[i-1]]+W[i-1];
    }
 }
'''
def knapSack(W, wt, val, n):

    K = [[0 for i in range(W + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(w + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif w > wt[i-1]:
                K[i][w] = max(K[i-1][w], K[i-1][w - wt[i-1]] + val[i-1])
            else:
                K[i][w] = K[i-1][w]

'''
5. Matrix

S[i][j]=A[i][j] + max(S[i-1][j], if i>0 ; S[i][j-1], if j>0)
'''

'''
6. Money
    1, 3, 5  to get 11 with min count money

    # d[i] = min{d[i-Vj] + 1}, i-Vj > 0, Vj in 1,3,5
'''

def moneyDP(target):
    money = [1, 3, 5]
    money_length = len(money)
    d = [0 for i in range(target)]

    for i in range(target):
        potential = []
        for j in range(money_length):
            if i > money[j]:
                potential.append(d[i-money[j]] + 1)

        d[i] = min(potential)
        print "d[%d]: %d" %(i, d[i])


