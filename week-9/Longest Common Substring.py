def lcs(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n+1)]

    length = 0
    end_s1 = 0
    count = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > length:
                    length = dp[i][j]
                    end_s1 = i - 1
                    count += 1
            else:
                dp[i][j] = 0
    
    if length == 0:
        print("No common substring.")
    else:
        longest = s1[end_s1 - length + 1:end_s1 + 1]
        print(longest)
        print(count)

lcs(input(), input())
