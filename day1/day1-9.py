def vowel(i,n,word,res):
    if i == n:
        print("no of vowels",res)
        return
    k  = "aeiouAEIOU"
    if word[i] in k:
        res = res + 1
    vowel(i+1,n,word,res)
def bvowel(i,n,word):
    if i == n:
        return 0
    nvc = bvowel(i+1,n,word)
    k = "aeiouAEIOU"
    if word[i] in k:
        nvc += 1
    return nvc
p = bvowel(0,7,"Prudhvi")
print(p)
vowel(0,7,"Prudhvi",0)
