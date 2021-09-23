def knap_sack_recustion(wt, val, max_wt: int, n: int):
    if n == 0 or max_wt == 0:
        return 0
    if max_wt >= wt[n - 1]:
        return max(val[n - 1] + knap_sack_recustion(wt, val, max_wt - wt[n - 1], n - 1),
                   knap_sack_recustion(wt, val, max_wt, n - 1))
    else:
        return knap_sack_recustion(wt, val, max_wt, n - 1)


mem = [-1 for each in range(50)]
mem = [mem for e in range(50)]


def knap_sack_meomization(wt, val, max_wt, n):
    if n == 0 or max_wt == 0:
        return 0
    if mem[n][max_wt] != -1:
        return mem[n][max_wt]
    if max_wt >= wt[n - 1]:
        mem[n][max_wt] = max(val[n - 1] + knap_sack_recustion(wt, val, max_wt - wt[n - 1], n - 1),
                             knap_sack_recustion(wt, val, max_wt, n - 1))
    else:
        mem[n][max_wt] = knap_sack_recustion(wt, val, max_wt, n - 1)
        return mem[n][max_wt]


def subset_sum(n, arr, sum):
    m = [[0 for i in range(101)] for j in range(101)]
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j >= arr[i - 1]:
                m[i][j] = max(m[i - 1][j - arr[i - 1]] + arr[i - 1], m[i - 1][j])
            else:
                m[i][j] = m[i - 1][j]
    if m[n][sum] == sum:
        return 1
    else:
        return 0
