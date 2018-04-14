#this method is very important as it is a substring checker

def count_substring(s1,s2):
  cnt = 0
  for i in range(len(s1)):
    if s1[i:].startswith(s2):
      cnt += 1
    #i += x
  return(cnt)


if __name__ == '__main__':
    string = input()
    position , character= input().split()
    new_string = mutable_string(string,int(position),character)
    print(new_string)
    s1="ABCDCDC"
    s2="CDC"
    count=count_substring(s1,s2)
    print(count)
