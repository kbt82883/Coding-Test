n = int(input())
meetings = []

for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))
    
meetings.sort(key = lambda x: (x[1],x[0]))

cnt = 0
end_time = 0
for s, e in meetings:
    if s >= end_time:
        cnt += 1
        end_time = e
        
print(cnt)