str1=input("enter the string1")
str2=input("enter the string2 ")
if len(str1)!=len(str2):
    print("not anagram")
else :
    count1={}
    count2={}
    for ch in str1:
        count1[ch]=count1.get(ch,0)+1
    for ch in str2:
        count2[ch]=count2.get(ch,0)+1
    if count1==count2:
         print("anagram")
    else:
        print("not anagram")
