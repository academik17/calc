def window(): 
    w = []*4 
    print('введите число а')
    sa = input() #строка
    print('введите операцию')
    operation = input()
    print('введите число b')
    sb = input() #строка
    print('введите основание системы исчисления')
    m = int(input())
    w = [sa, operation, sb, m]
    return w 

w = []*4
w = window()
a = []
b = []
oper = w[1]
sa = w[0]
sb = w[2]
la = len(sa)
lb = len(sb)
m = int(w[3])
n = la + 1

# Перевод в массив
for i in range(la):
 a.insert(i, int(sa[i]))
for i in range(lb):
 b.insert(i, int(sb[i])) 

# Добавление нулей
a.insert(0, 0)
b.insert(0, 0)
if la > lb:
 n = la+1
 for i in range(la - lb):
     b.insert(i, 0)
if la < lb:
 n = lb+1
 for i in range(lb - la):
  a.insert(i, 0)

# Массив в число
def masstoint(a):
 s=""
 k = 0
 i = 0

 while a[i] == 0:
     i = i + 1
     k = k + 1
 for i in range(k, len(a)):
   s=s+str(a[i])
 return(s)

# Сравнение
def srav(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return 1
        if a[i] < b[i]:
            return 0
    if a[len(a)-1] == b[len(a)-1]:
        return 1


# Сложение
def sum(a, b, m, n):
   w = [0]*n
   c = 0
   for i in range(n):
       t = a[n - 1 - i] + b[n - 1 - i] + c 
       c = t // m
       w[n - i - 1] = (t +m)% m 
   return masstoint(w)



#Вычитание
def minus0(a,b, m, n):
    if srav(a, b) == 1:
        return masstoint(minus(a,b, m, n))
    else:
        return ('-' + masstoint(minus(b, a, m, n)))
def minus(a, b, m, n):
 w =[0]*n
 c = 0
 for i in range(n-1):
     t = a[n-1-i] - b[n-1-i] + c
     c = t // m
     w[n-1-i] = t % m
     if t < 0:
      w[n-2-i] = w[n-2-i] - 1
 return(w)



# Умножение
def mult(a,b,m,n):
    k = len(a)*len(b)
    c = 0
    w = [0]*(len(a)*len(b))
    for i in range(len(b)):
        for j in range(len(a)):
            t = a[n - 1 - j] * b[n - 1 - i] + c + w[k - i - j - 1]
            c = t  // m
            w[k - i - j - 1] = (t + m)% m
    return masstoint(w)
#print(mult(a,b,m,n))

# Деление
def delen(a, b, m, n):
  while b[0] == 0:
   b.pop(0)
  b.insert(0,0)
  i = len(b)
  q =[]
  for i in range(len(b), len(a)+1):
      k = 0
      while srav(a[:i],b) == 1:
       a[:i] = minus(a[:i],b,m,len(b))
       k +=1
      q.append(k)
      b.insert(0,0)
  return q
      
print(delen(a, b, m, n))