import collections

n=int(input())
numbers=list(map(int,input().split()))

max_value=sum(numbers)
min_value=sum(collections.Counter(numbers).keys())
print(max_value)
print(min_value)