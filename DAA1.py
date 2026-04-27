"""def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("sorted array:", arr)"""
#2nd PROGRAM
"""def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("sorted array:", arr)"""
#3RD PROGRAM
"""def sequential_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
arr=[10,20,30,40,50]
key=30
result=sequential_search(arr,key)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")"""
#4TH PROGRAM
"""def rabin_karp_search(text, pattern):
    d = 256  
    q = 101  
    M = len(pattern)
    N = len(text)
    p = 0  
    t = 0  
    h = 1

    for i in range(M-1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(N - M + 1):
        if p == t:
            if text[i:i+M] == pattern:
                print("Pattern found at index", i)

        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t += q
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
rabin_karp_search(text, pattern)"""
#5TH PROGRAM
"""import itertools
import sys
def traveling_salesman(graph, start):
    min_cost = sys.maxsize
    n = len(graph)
    vertices=[i for i in range(n) if i != start]
    min_path = sys.maxsize
    for perm in itertools.permutations(vertices):
        cost=graph[start][perm[0]]
        for i in range(len(perm)-1):
            cost += graph[perm[i]][perm[i+1]]
        cost += graph[perm[-1]][start]
        min_cost = min(min_cost, cost)
    return min_cost
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
    ]
print("Minimum cost:",traveling_salesman(graph, 0))"""
#6TH PROGRAM
def knapsack(W, wt, val, n):
    dp=[[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w - wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print("Maximum value in Knapsack =", knapsack(W, wt, val, n))