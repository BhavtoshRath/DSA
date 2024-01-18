def minimumWaitingTime(queries):
    sorted_queries = sorted(queries)
    ans = 0
    for idx in range(1, len(sorted_queries)):
        ans += sum(sorted_queries[0:idx])
    return ans


ans = minimumWaitingTime([3, 2, 1, 2, 6])
print(ans)
