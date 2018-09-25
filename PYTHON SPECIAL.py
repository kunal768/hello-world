
#the question that i solved on hackerearth was quite interesting 
#there were number of test cases involving two given lines , the task involved looking the arrangement order of letters in english
and then editing your secind string in the respective order of letters as given in string one
#here's the code for that
t=int(input())
for i in range(0,t):
  d={}
  s=input()
  arr=[]
  for i in range(0,len(s)):
    arr.append(s[i])

  for i in range(0,len(arr)):
    d[arr[i]]=i+1
  s1=input()
  val_holder=[]
  for i in range(0,len(s1)):
    val_holder.append(d[s1[i]])
  val_holder.sort()
  for i in range(0,len(val_holder)):
    print(list(d.keys())[list(d.values()).index(val_holder[i])],end='')
