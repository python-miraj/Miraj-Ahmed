a=float(input('Enter markes in Bangla       :'))
b=float(input('Enter markes in Engilish     :'))
c=float(input('Enter markes in Math         :'))
d=float(input('Enter markes in Physis       :'))
e=float(input('Enter markes in Chemestry    :'))
f=float(input('Enter markes in Bialogy      :'))
g=5.00
h=4.00
k=3.00
l=2.00
m=0.00
n= 'invalide number'

#----------for Bangla-------------
if a>100:
    a=n
elif a>=80<=100:
    a=g
elif a>=70<80:
    a=h
elif a>=60<70:
    a=k
elif a>=50<60:
    a=l
elif a<50:
    a=m
#----------for Enlish-------------
if b>100:
    b=n
elif b>=80<=100:
    b=g
elif b>=70<80:
    b=h
elif b>=60<70:
    b=k
elif b>=50<60:
    b=l
elif b<50:
    b=m
#----------Math-------------
if c>100:
    c=n
elif c>=80<=100:
    c=g
elif c>=70<80:
    c=h
elif c>=60<70:
    c=k
elif c>=50<60:
    c=l
elif c<50:
    c=m
#----------Physis-------------
if d>100:
    d=n
elif d>=80<=100:
    d=g
elif d>=70<80:
    d=h
elif d>=60<70:
    d=k
elif d>=50<60:
    d=l
elif d<50:
    d=m

#---------Chemestry----------
if e>100:
    e=n
elif e>=80<=100:
    e=g
elif e>=70<80:
    e=h
elif e>=60<70:
    e=k
elif e>=50<60:
    e=l
elif e<50:
    e=m
#---------Bialogy ----------

if f>100:
    f=n
elif f>=80<=100:
    f=g
elif f>=70<80:
    f=h
elif f>=60<70:
    f=k
elif f>=50<60:
    f=l
elif f<50:
    f=m

#-----------------Calculation---------
t=(a*b*b*c*d*e*f)
if t==0:
    t=0
elif t>0:
    t=1
result=((a+b+c+d+e+f)/6)*t
GPA=round(result,2)

if GPA>=5.00:
    print('Your Grade is A+, Your GPA = ',GPA)
elif GPA>=4.00<=5.00:
    print('Yor Grade is A, Your GPA = ' ,GPA)
elif GPA>=3.00<4.00:
    print('Your Grade is A-, Your GPA = ',GPA)
elif GPA>=2.00<3.00:
    print('Yor Grade is A+, Your GPA = ', GPA)
elif GPA<2.00:
    print('You are fail in Exam , Your GPA= ', GPA)











