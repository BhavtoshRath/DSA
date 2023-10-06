def minimumWaitingTime(queries):
    sorted_queries = sorted(queries)
    ans = 0
    for idx in range(1, len(sorted_queries)):
        sub_queries = sorted_queries[0 : idx + 1]
        ans += sum(sub_queries[:-1])
    return ans


ans = minimumWaitingTime([3, 2, 1, 2, 6])
print(ans)
