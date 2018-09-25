#this method is learnt to concantante a new character or string in the strings

def mutable_string(string , position,character):
    l=list(string)
    l[position]=character
    string=''.join(l)
    return string
