# Creating a python library of my own from scratch with methods to find basic statistical values 


def minimum(x):                       # MINIMUM        
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]>x[j]:
                x[i],x[j]=x[j],x[i]
    return x[0]


def maximum(x):                      #MAXIMUM
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]>x[j]:
                x[i],x[j]=x[j],x[i]
    return x[-1]

def sorts(x):                       #SORTING
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]>x[j]:
                x[i],x[j]=x[j],x[i]
    return x

def arith_mean(x):                 # ARITHMETIC MEAN
    sum1=0
    for i in x:   
        sum1=i+sum1
        mean=(sum1)/(len(x))
    return mean

def geom_mean(x):                  # GEOMETRIC MEAN
    mul=1
    for i in x:
        mul=mul*i
        mean=(mul)**(1/len(x))
    return mean

def har_mean(x):                  # HARMONIC MEAN
    sum1=0
    for i in x:
        sum1=(1/i)+sum1
        hm=len(x)/sum1
    return hm

def median1(x):                  #MEDIAN
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]>x[j]:
                x[i],x[j]=x[j],x[i]
    
    if len(x)%2!=0:
        med=x[len(x)//2]
        return med
    else:
        med1 = x[len(x)//2]
        med2 = x[len(x)//2 - 1]
        med3 = (med1 + med2)*0.5
        return med3
    
    
def var(x):                     #VARIANCE
    sum_=0
    for i in x:
        sum_=sum_+(i-arith_mean(x))**2
        var1=(sum_)/(len(x)-1)
    return var1

def stan_dev(x):                #STANDARD DEVIATION
    std_=var(x)**(1/2)
    return std_
        
def med_abs_dev(x):             # MEDIAN ABSOLUTE DEVIATION
    abs_dev=[]
    for i in x:
        if i<median1(x):
            p=median1(x)-i
            abs_dev.append(p)
        else:
            q=i-median1(x)
            abs_dev.append(q)
        mad=median1(abs_dev)
    return mad


def coeff_var(x):               #COEFFICIENT OF VARIATION
    cv=stan_dev(x)/arith_mean(x)
    return cv

def covar(x,y):                 # COVARIANCE
    sum1=0
    for i in range(len(x)):
        sum1=sum1+((x[i]-arith_mean(x))*(y[i]-arith_mean(y)))
        cvar=sum1/len(x)
    return cvar
    
def pearson_corr(x,y):          # PEARSON COEFFICIENT CORRELATION
    cor=(covar(x,y))/(stan_dev(x)*stan_dev(y))
    return cor







