#this is the solution to Find the Runner Up Score on HackerRank
#link to the problem is https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__=='__main__':
    n=int(input())
    arr=list(map(int , input().split()))
    print(sorted(list(set(arr)))[n-2])
