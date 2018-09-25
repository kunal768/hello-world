#this is a beautiful example of validation of strings using the inbuilt "any" method
#In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
#In the second line, print True if  has any alphabetical characters. Otherwise, print False.
#In the third line, print True if  has any digits. Otherwise, print False.
#In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
#In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
if __name__ == '__main__':
    s=input()
    t = type(s)
    for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
        print(any(method(c) for c in s))
#.ljust(width)
#.center(width)
#.rjust(width)
