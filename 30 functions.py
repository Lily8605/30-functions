#1.Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից թվերի գումար
def msum(*args):
    tmp=0
    for el in args:
        tmp+=el
    return tmp
print(msum(1,5,8,6))

#2.Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից տողերի քանակը։
def length(*args):
    return len(args)
print(length('hello','world','12'))
    
#3.Գրել ֆունկցիա որը կվերադարձնի ստասած արգումենտների միջին թվաբանականը։
def midsum(*args):
    tmp=0
    for num in args:
        tmp+=num
    return tmp//len(args)
print(midsum(12,32,17,3))
        
#4.Գրել ֆունկցիա որը կստանա 2 արգումենտ և կվերադարձնի այդ արգումենտերի հետ կատարած մաթեմատիկական գործողությունների արդյունքները։
def math(a,b):
    return a+b,a-b,a*b,a//b
 
print(math(49,7))

#5.Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի այն դարձված ամբողջությամբ մեծատառ upper ֆունկցիան օգտագործել չի կարելի։
def upper(mstr):
    tmp=""
    for el in mstr:
        if  97<=ord(el)<=122:
            tmp+=chr(ord(el)-32)
        else:
            tmp+=el
    return tmp
print(upper("Hello world"))
 

#6.Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնիայն դարձված ամբողջությամբ փոքրատառ ֆունկցիան 
def lower(mstr):
    tmp=""
    for el in mstr:
        if 65<=ord(el)<=90:
            tmp+=chr(ord(el)+32)
        else:
            tmp+=el
    return tmp
print(lower("HELLO World"))

#7.Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնիայն դարձված բոլոր բառերի առաջին տառերը մեծատառ (title օգտագործել չի կարելի )
def title(mstr):
    result=""
    ml=mstr.split()
    for i in range(len(ml)):
        if 97<=ord(ml[i][0])<=122:
            ml[i]=chr(ord(ml[i][0])-32)+ml[i][1:]
    result=' '.join(ml)
        
    return result
print(title("Hello good world"))

#8.Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնիայն դարձված հակառակ։
def reverse(mstr):
    tmp=""
    for i in range(len(mstr)-1,-1,-1):
        tmp+=mstr[i]
    return tmp
print(reverse("Hello good world"))


def reverse2(mstr):
    tmp=""
    for el in mstr:
        tmp=el+tmp
    return tmp
print(reverse2("Hello good world"))

#9. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և 2 թիվ։ Այն պետք է վերադարձնի տրված թվերի արանքում եղած ենթատողը
def task(mstr,a,b):
    if a<=b<len(mstr):
        return(mstr[a:b+1])
    return "None"
print(task("Hello good world",8,12))

#10.Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառը
def maxword(mstr):
    ml=mstr.split()
    maxw=ml[0]
    for el in ml:
        if len(maxw)<len(el):
            maxw=el
    return maxw
print(maxword("Hello good world blabla"))

#11.Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաշատ օգտագործված տառը։
def maxletter(mstr):
    md={}
    for el in mstr.lower():
        if el in md:
            md[el]+=1
        else:
            md[el]=1
    ml=list(md.items())
    for i in range(len(ml)):
        for j in range(len(ml)-1-i):
            if ml[j][1]>ml[j+1][1]:
                ml[j],ml[j+1]=ml[j+1],ml[j]
    return ml[-1][0]
print(maxletter("Hello hell good world"))

#12.Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառում ամենաշատ օգտագործված տառը։
def maxwordsl(mstr):
    md={}
    mlist=mstr.split()
    maxword=mlist[0]
    myl=list(filter(lambda x:len(x)>len(maxword),mlist))
    mys=''.join(myl)
    for el in mys:
        if el in md:
            md[el]+=1
        else:
            md[el]=1
    ml=list(md.items())
    for i in range(len(ml)):
        for j in range(len(ml)-1-i):
            if ml[j][1]>ml[j+1][1]:
                ml[j],ml[j+1]=ml[j+1],ml[j]
    return ml[-1][0]
print(maxwordsl("Hello little world"))
        
#13.Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և թիվ։Կվերադարձնի այդ թվին համապատասխն ինդեքսում եղած էլէմենտները՝ սկզբից և վերջից։
def find(mstr, num):
    tmp=""
    first=mstr[num]
    for i in range(len(mstr)-1,-1,-1):
        tmp+=mstr[i]
    end=tmp[num]
    return first,end
print(find("Hello good world",6))

#15.Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կստուգի պոլինդրոմ է այն թե ոչ։
def polindrome (num):
    if str(num)==str(num)[::-1]:
        return True
    return False
print(polindrome(3123))


#16. Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կվերադարձնի իրեն ամենամոտ պոլինդրոմ թիվը։
def findp (num):
    def polindrome(n):
        if str(n)==str(n)[::-1]:
            return n
        
    if polindrome(num):
        return num
    bigger=num
    smaller=num
    while True:
        if polindrome(bigger):
            return bigger
        elif polindrome(smaller):
            return smaller
        bigger+=1
        smaller-=1
        
print(findp(1231))


#17. Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կվերադարձնի իր առաջին և վերջին թվանշանների արտադրյալը։
def multiple (num):
    return int(str(num)[0])*int(str(num)[-1])
print(multiple(8523468))


#18.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում եղած տողերի քանակությունը։
def listcount (ml):
    tmp=[el for el in ml if type(el)==str]
    return len(tmp)
print(listcount([123,"hello",25,"good","world"]))


#19. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում առկա թվերից առավելագույնը։
def maxnum(ml):
    tmp=[el for el in ml if type(el)==int]
    if not tmp:
        return None
        
    tmp.sort()
    return tmp[-1]
    
print(maxnum([123,"hello",25,"good",'world',535,78,'lala',64]))

#20.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի այդ լիստում առկա երկնիշ զույգ թվերը։
def evenlist(ml):
    tmp=[el for el in ml if type(el)==int and el%2==0 and 0<el/10<10]
    return tmp
print(evenlist([123,"hello",25,"good",'world',535,78,'lala',64])) 

#21.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի այդ լիստում առկա թվերի միջին թվաբանականը։
def mid(ml):
    result=0
    for el in ml:
        result+=el
    return result/len(ml)
print(mid([12,5,64,3,18,7,6,12]))

#22. Գրել ֆունկցիա որը որպես առգումենտ կստանա տողերի լիստ և կվերադարձնի այդ տողերի երկարությունները պարունակող լիստ։
def strlen(ml):
    tmp=[len(el) for el in ml]
    return tmp
print(strlen(["hello",'good','beautiful','so','python','world']))

#23.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում առկա թվերը դասավորված նվազման կարգով։
def numlist(ml):
    nl=list(filter(lambda x:type(x)==int,ml))
    nl.sort()
    return nl[::-1]
print(numlist([123,"hello",25,"good",'world',535,78,'lala',64]))
    
#24. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում առկա տողերը դասավորված երկարությունների նվազման կարգով։
def strlist(ml):
    tmp=[el for el in ml if type(el)==str ]
    
    for i in range(len(tmp)):
        for j in range(len(tmp)-1-i):
             if len(tmp[j]) < len(tmp[j + 1]):
                tmp[j], tmp[j + 1] = tmp[j + 1], tmp[j]
    return tmp
print(strlist([123,'hello',25,"good",'world',535,78,'and',64,'beautiful','so']))



#25.Գրել ֆունկցիա որը որպես արգումենտ կընդունի  տողերի լիստ և կվերադարձնի այն բառը որը կպարունակի ամենաշատ ձայնավորները
def mostvowels(ml):
    def vowelscount(mstr):
        return  sum(1 for el in mstr if el.lower() in "aeoui")
    for i in range(len(ml)):
        for j in range(len(ml)-1-i):
            if vowelscount(ml[j])>vowelscount(ml[j+1]):
                ml[j],ml[j+1]=ml[j+1],ml[j]
    return ml[-1]
print(mostvowels(["hello",'good','beautiful','so','python','world']))
    

#26.Գրել ֆունկցիա որը որպես արգումենտ կընդունի նախադասությունների լիստ և կվերադարձնի այն նախադասությունը որը կպարունակի , ամենաշատ բառերը։
def longsent(ml):
    tmp=[el.split() for el in ml]
    maxsent=tmp[0]
    for i in range (len(tmp)):
        if len(tmp[i])>len(maxsent):
            maxsent=tmp[i]
        
    return " ".join(maxsent)
    
    
    
nl= [
    "Stars twinkle in the night sky.",
    "Cats play in the garden.",
    "Books line the library shelves.",
    "Snow covers the landscape."
]
print(longsent(nl))
    
    
#27 . Գրել ֆունկցիա որը որպես արգումենտ կստանա տող իրականում նախադասություն և կվերադարձնի այդ նախադասությունում առկա / ամենամեծ թիվը ոչ թե թվանշանը ։
def maxnumber(mstr):
    ml=mstr.split()
    tmp=[int(el) for el in ml if el.isdigit()]
    if tmp:
        return max(tmp)
    else:
        return None
    
    
    
print(maxnumber("Hello good 123 world. I'm 99 years old and I have 156 cats. 12 years ago I was 87"))

#28. Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝ մարդկանց նկարագրող և կվերադարձնի այն բառարանը որում մարդու , , տարիքն ամենամեծն է։
def mage(ml):
    maxage=ml[0]["age"]
    maxagedict=ml[0]
    for el in ml:
        if el["age"]>maxage:
            maxage =el["age"]
            maxagedict=el
    return maxagedict
            
    
people= [
    {"name": "Alice", "age": 30, "work": "Engineer", "country": "USA"},
    {"name": "Bob", "age": 25, "work": "Designer", "country": "Canada"},
    {"name": "Charlie", "age": 35, "work": "Teacher", "country": "UK"},
    {"name": "David","age": 28,"work": "Programmer","country":"Germany"},
    {"name": "Eva", "age": 40, "work": "Doctor", "country": "Australia"}
]
print(mage(people))

#29.Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝ ուսանողների նկարագրող և կվերադարձնի այդ ուսանողների լիստը դասավորված աճման կարգով՝ ըստ միասվորների։
def studentslist(ml):
    for i in range (len(ml)):
        for j in range (len(ml)-1-i):
            if ml[j]["score"]>ml[j+1]["score"]:
                ml[j],ml[j+1]=ml[j+1],ml[j]
    return ml

students= [
    {"name": "Alice", "score": 85, "grade": "A", "country": "USA"},
    {"name": "Bob", "score": 72, "grade": "B", "country": "Canada"},
    {"name": "Charlie", "score": 95, "grade": "A+", "country": "UK"},
    {"name": "David", "score": 68, "grade": "C", "country": "Germany"},
    {"name": "Eva", "score": 90, "grade": "A-", "country": "Australia"}
]
print(studentslist(students ))

#30.Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝ համալսարանների նկարագրող և կվերադարձնի այն համալսարանը որի , անվանումն ամենաերկարն է։
def longname(ml):
    maxname=ml[0]["name"]
    maxdict=ml[0]
    for el in ml:
        if len(el["name"])>len(maxname):
            maxname=el["name"]
            maxdict=el
    return maxdict


universities= [
    {"name": "Harvard", "location": "Cambridge", "prestige": "Ivy League", "academic_focus": "Distinguished Faculty"},
    {"name": "Stanford", "location": "Stanford", "prestige": "Technology", "innovation": "Excellence"},
    {"name": "MIT", "location": "Cambridge", "innovation": "Leader", "research": "Technology"},
    {"name": "Oxford", "location": "Oxford", "prestige": "Rich History", "academic_focus": "Excellence"},
    {"name": "Cambridge", "location": "Cambridge", "research": "Top-Ranking", "innovation": "Research"}
]
print(longname(universities))