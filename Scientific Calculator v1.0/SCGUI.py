from tkinter import*
import math
import sympy as sp

m=Tk()
m.geometry("795x458")
m.title("Scientific Calculator v1.0")
mlabel=Label(m,text='Scientific Calculator',bg='dark gray',font=("consolas",24,'bold'))
mlabel.pack(side=TOP)
m.config(background='dark gray')
textin=StringVar()
operator=""

#Button Click
def clickbut(number):   
     global operator
     operator=operator+str(number)
     textin.set(operator)
#add
def equlbut():
     global operator
     add=str(eval(operator))
     textin.set(add)
     operator=''
#sub
def equlbut():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''
#mul
def equlbut():
     global operator
     mul=str(eval(operator))
     textin.set(mul)
     operator=''
#div
def equlbut():
    global operator
    div=str(eval(operator))
    textin.set(div)
    operator=''
#exp
def equlbut():
     global operator
     exp=str(eval(operator))
     textin.set(exp)
     operator=''
#trigo
def sinbut():
    global operator
    m=float(operator)
    sin=sp.sin(math.radians(m))
    textin.set('sin'+operator+'='+str(sin))
    operator=''
def sininvbut():
    global operator
    m=float(operator)
    sininv=math.degrees(math.asin(m))
    sininv="%0.2f"%sininv
    textin.set('sin\u207B\u00B9'+operator+'='+str(sininv))
    operator=''
def cosbut():
    global operator
    n=float(operator)
    p=int(n/90)
    if p%2==1 and n%90==0:
        cos=0
    else:
        cos=sp.cos(math.radians(n))
    textin.set('cos'+operator+'='+str(cos))
    operator=''
def cosinvbut():
    global operator
    m=float(operator)
    cosinv=math.degrees(math.acos(m))
    cosinv="%0.2f"%cosinv
    textin.set('cos\u207B\u00B9'+operator+'='+str(cosinv))
    operator=''
def tanbut():
    global operator
    o=float(operator)
    q=int(o/90)
    if q%2==1 and o%90==0:
        tan='Undefined'
    else:
        tan=sp.tan(math.radians(o))
    textin.set('tan'+operator+'='+str(tan))
    operator=''
def taninvbut():
    global operator
    m=float(operator)
    taninv=math.degrees(math.atan(m))
    taninv="%0.2f"%taninv
    textin.set('tan\u207B\u00B9'+operator+'='+str(taninv))
    operator=''
#squre cube root
def sqrtbut():
    global operator
    m=float(operator)
    sqrt=math.sqrt(m)
    textin.set(sqrt)
    operator=''
def sqrbut():
    global operator
    m=float(operator)
    sqr=m**2
    textin.set(sqr)
    operator=''
def cbrtbut():
    global operator
    m=float(operator)
    cbrt=math.cbrt(m)
    textin.set(cbrt)
    operator=''
def cbrbut():
    global operator
    m=float(operator)
    cbr=m**3
    textin.set(cbr)
    operator=''
#hyp trigo
def sinhbut():
    global operator
    m=float(operator)
    sinh=math.sinh(m)
    textin.set('sinh'+operator+'='+str(sinh))
    operator=''
def sinhinvbut():
    global operator
    m=float(operator)
    sinhinv=(math.asinh(m))
    sinhinv="%0.2f"%sinhinv
    textin.set('sinh\u207B\u00B9'+operator+'='+str(sinhinv))
    operator=''
def coshbut():
    global operator
    m=float(operator)
    cosh=math.cosh(m)
    textin.set('cosh'+operator+'='+str(cosh))
    operator=''
def coshinvbut():
    global operator
    m=float(operator)
    coshinv=(math.acosh(m))
    coshinv="%0.2f"%coshinv
    textin.set('cosh\u207B\u00B9'+operator+'='+str(coshinv))
    operator=''
def tanhbut():
    global operator
    m=float(operator)
    tanh=math.tanh(m)
    textin.set('tanh'+operator+'='+str(tanh))
    operator=''
def tanhinvbut():
    global operator
    m=float(operator)
    tanhinv=(math.atanh(m))
    textin.set('tanh\u207B\u00B9'+operator+'='+str(tanhinv))
    operator=''
#log
def logbut():
    global operator
    m=float(operator)
    log=math.log10(m)
    textin.set('log'+operator+'='+str(log))
    operator=''
def lnbut():
    global operator
    m=float(operator)
    ln=math.log(m)
    textin.set('ln'+operator+'='+str(ln))
    operator=''
#factorial, permutation, combination
def factbut():
    global operator
    m=int(operator)
    fact=math.factorial(m)
    textin.set(fact)
    operator=''
def percebut():
    global operator
    mul=(eval(operator))
    perc=mul/100
    textin.set(perc)
    operator=''
def permbut():
    global operator
    m=operator.split(',')
    n=[]
    for i in m:
        i=int(i)
        n.append(i)
    x=n[0]
    y=n[1]
    perm=math.factorial(x)/math.factorial(x-y)
    textin.set(perm)
    operator=''
def combbut():
    global operator
    m=operator.split(',')
    n=[]
    for i in m:
        i=int(i)
        n.append(i)
    x=n[0]
    y=n[1]
    comb=math.factorial(x)/((math.factorial(x-y))*(math.factorial(y)))
    textin.set(comb)
    operator=''
#Clear Screen and Del   
def clrbut():
    global operator
    operator=''
    textin.set('')
def delbut():
    global operator
    operator=operator.replace(operator[-1],'',1)
    textin.set(operator)

mtext=Entry(m,font=("tempus sans itc",18,'bold'),textvar=textin,width=45,bd=5,bg='powder blue')
mtext.pack()
but1=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=10,y=100)

but2=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=10,y=170)

but3=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=10,y=240)

but4=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=75,y=100)

but5=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=75,y=170)

but6=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=75,y=240)

but7=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=140,y=100)

but8=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=140,y=170)

but9=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=140,y=240)

but0=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=75,y=310)

butdot=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=10,y=310)

butcomma=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(","),text=",",font=("Courier New",16,'bold'))
butcomma.place(x=595,y=310)

butpl=Button(m,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold'))
butpl.place(x=205,y=100)

butsub=Button(m,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold'))
butsub.place(x=205,y=170)

butml=Button(m,padx=14,pady=14,bd=4,bg='white',text="x",command=lambda:clickbut("*"),font=("Courier New",16,'bold'))
butml.place(x=205,y=240)

butdiv=Button(m,padx=14,pady=14,bd=4,bg='white',text="÷",command=lambda:clickbut("/"),font=("Courier New",16,'bold'))
butdiv.place(x=205,y=310)

butclear=Button(m,padx=14,pady=14,bd=4,bg='white',text="C",command=clrbut,font=("Courier New",16,'bold'))
butclear.place(x=270,y=100)

butdel=Button(m,padx=5,pady=14,bd=4,bg='white',text="Del",command=delbut,font=("Courier New",14,'bold'))
butdel.place(x=335,y=100)

butequal=Button(m,padx=14,pady=14,bd=4,bg='white',command=equlbut,text="=",font=("Courier New",16,'bold'))
butequal.place(x=140,y=310)

butpi=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(math.pi),text="\u03C0",font=("Courier New",16,'bold'))
butpi.place(x=530,y=310)

bute=Button(m,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(math.e),text="e",font=("Courier New",16,'bold'))
bute.place(x=400,y=100)

butexp=Button(m,padx=14,pady=14,bd=4,bg='white',text="^",command=lambda:clickbut("**"),font=("Courier New",16,'bold'))
butexp.place(x=465,y=100)

butsin=Button(m,padx=33,pady=14,bd=4,bg='white',text="sin",command=sinbut,font=("Courier New",16,'bold'))
butsin.place(x=270,y=170)

butcos=Button(m,padx=33,pady=14,bd=4,bg='white',text="cos",command=cosbut,font=("Courier New",16,'bold'))
butcos.place(x=270,y=240)

buttan=Button(m,padx=33,pady=14,bd=4,bg='white',text="tan",command=tanbut,font=("Courier New",16,'bold'))
buttan.place(x=270,y=310)

butsinh=Button(m,padx=33,pady=14,bd=4,bg='white',text="sinh",command=sinhbut,font=("Courier New",14,'bold'))
butsinh.place(x=400,y=170)

butcosh=Button(m,padx=33,pady=14,bd=4,bg='white',text="cosh",command=coshbut,font=("Courier New",14,'bold'))
butcosh.place(x=400,y=240)

buttanh=Button(m,padx=33,pady=14,bd=4,bg='white',text="tanh",command=tanhbut,font=("Courier New",14,'bold'))
buttanh.place(x=400,y=310)

butsininv=Button(m,padx=21,pady=14,bd=4,bg='white',text="sin\u207B\u00B9",command=sininvbut,font=("Courier New",16,'bold'))
butsininv.place(x=10,y=380)

butcosinv=Button(m,padx=21,pady=14,bd=4,bg='white',text="cos\u207B\u00B9",command=cosinvbut,font=("Courier New",16,'bold'))
butcosinv.place(x=140,y=380)

buttaninv=Button(m,padx=21,pady=14,bd=4,bg='white',text="tan\u207B\u00B9",command=taninvbut,font=("Courier New",16,'bold'))
buttaninv.place(x=270,y=380)

butsqrt=Button(m,padx=14,pady=14,bd=4,bg='white',text="√",command=sqrtbut,font=("Courier New",16,'bold'))
butsqrt.place(x=530,y=100)

butsqr=Button(m,padx=7,pady=14,bd=4,bg='white',text="x\u00b2",command=sqrbut,font=("Courier New",16,'bold'))
butsqr.place(x=595,y=170)

butcbrt=Button(m,padx=15,pady=14,bd=4,bg='white',text="∛",command=cbrtbut,font=("Courier New",16))
butcbrt.place(x=595,y=100)

butcbr=Button(m,padx=7,pady=14,bd=4,bg='white',text="x\u00b3",command=cbrbut,font=("Courier New",16,'bold'))
butcbr.place(x=595,y=240)

butlog=Button(m,padx=38,pady=14,bd=4,bg='white',text="log",command=logbut,font=("Courier New",14,'bold'))
butlog.place(x=400,y=380)

butln=Button(m,padx=43,pady=14,bd=4,bg='white',text="ln",command=lnbut,font=("Courier New",14,'bold'))
butln.place(x=530,y=380)

butfact=Button(m,padx=14,pady=14,bd=4,bg='white',text="!",command=factbut,font=("Courier New",16,'bold'))
butfact.place(x=530,y=170)

butperc=Button(m,padx=14,pady=14,bd=4,bg='white',text="%",command=percebut,font=("Courier New",16,'bold'))
butperc.place(x=530,y=240)

butsinhinv=Button(m,padx=14,pady=14,bd=4,bg='white',text="sinh\u207B\u00B9",command=sinhinvbut,font=("Courier New",16,'bold'))
butsinhinv.place(x=660,y=100)

butcoshinv=Button(m,padx=14,pady=14,bd=4,bg='white',text="cosh\u207B\u00B9",command=coshinvbut,font=("Courier New",16,'bold'))
butcoshinv.place(x=660,y=170)

buttanhinv=Button(m,padx=14,pady=14,bd=4,bg='white',text="tanh\u207B\u00B9",command=tanhinvbut,font=("Courier New",16,'bold'))
buttanhinv.place(x=660,y=240)

butperm=Button(m,padx=33,pady=14,bd=4,bg='white',text="nPr",command=permbut,font=("Courier New",16,'bold'))
butperm.place(x=660,y=310)

butcomb=Button(m,padx=33,pady=14,bd=4,bg='white',text="nCr",command=combbut,font=("Courier New",16,'bold'))
butcomb.place(x=660,y=380)

m.mainloop()
