def all_sum(l, nom):
    sum_cash = 0
    for i, n in zip(l, nom):
        sum_cash += i * n
    return sum_cash

def in_nom(v,nom):
    return v in nom



def next_nom(nom_sel, index, last_nom, nom):
    if (nom_sel[index] < 10 and nom[index] < 500) or nom[index] > 200:
        nom_sel[index] += 1
        if nom_sel[index] > 10:
            nom_sel[index - 1] -= 1
    else:
        nom_sel[index + 1] += 1
        nom_sel[index] -= 1
    last_nom = nom[index]
    return nom_sel, last_nom
    
def mod_():
    ind = index-1
    while ind >0:
        if (temp_cash*-1) % nom[ind] == 0:
            return ind
        ind -=1
    return -1;

def minus(index, temp_cash, nom, nom_sel):
    temp_cash *= -1
    i = index - 1
    while i > 0:
        if temp_cash < nom[i]:
            i -= 1
            continue
        nom_sel[i] -= 1
        temp_cash -= nom[i]
        if temp_cash < 0:
            nom_sel[i] = 1
            temp_cash += nom[i]
            i -= 1
        i -= 1
    return nom_sel, temp_cash


def bankomat(cash, nom):
    global nom_sel
    global temp_cash #залишок
    global last_nom
    global found
    global index
    temp_cash = cash - all_sum(nom_sel,nom)
    
    index = nom.index(last_nom)
    if temp_cash < 0:
        #print("--------",temp_cash)
        if in_nom(temp_cash*-1,nom):
            nom_sel[nom.index(temp_cash*-1)]-=1
            #print(nom_sel)
            temp_cash = 0
            #print("Видано",all_sum(nom_sel,nom))
            return
        else: #якщо раптом коли додали нову купюру залишок від'ємний, але більший ніж номінали
            nom_sel, temp_cash = minus(index, temp_cash, nom, nom_sel)
            if temp_cash > 0:
                    return None


    m = temp_cash // last_nom
    #print(nom_sel)
    #print ("Поточна купюра:",last_nom,", Залишок:",temp_cash," Беремо: ",nom[index],"-к", m)
    
    if temp_cash ==0:
        return
    if m == 0: #це означає, що грошей менше ніж номінал наступної купюри, але треба брати його, а від реши віднімати
        #print("---",index,temp_cash)
        if nom_sel[index]<=10:
            nom_sel, last_nom = next_nom(nom_sel, index, last_nom, nom)
        bankomat(cash, nom)
    elif m < 10:
         #print("m < 10")
         nom_sel[index] +=m
         #print ("Залишилося:", temp_cash)
         if temp_cash > 0 and temp_cash % last_nom == 0:
             return
         else:
            nom_sel, last_nom = next_nom(nom_sel, index, last_nom, nom)
         bankomat(cash, nom)       
    elif m > 10 and nom[index]<500: #якщо кількість купюр яку можна видати більше ніж 10
         nom_sel[index] = 10
         #print (last_nom,":",temp_cash)
         if temp_cash > 0:
            index +=1
            last_nom = nom[index]
            bankomat(cash, nom)
    elif m > 10 and nom[index]>200:
        nom_sel[index] = m
        index +=1
        last_nom = nom[index]
        bankomat(cash, nom)
    else:#це означає, що я можу використать усі купюри даного номіналу
        #print ("----")
        last_nom = nom[index]
        nom_sel[index] = m
        index +=1 
        bankomat(cash, nom)  
      
found = False    
cash = 5010
nom = [10,20,50,100,200,500,1000]

nom_sel = [0,0,0,0,0,0,0]
limit = 10
temp_sum = 0 #скільки видали
temp_cash = cash #це гроші, що залишилися
index = 0
last_nom= nom[0] #остання вибрана купюра
if cash % 10 == 0 and cash > 0:
    while temp_cash>0 :
        
        bankomat(cash, nom)
        #print(nom_sel)
        if temp_cash < 0 or temp_cash == cash:
            #print(nom_sel)
            break
        
else:
    print("Введіть суму кратну 10")

for i in range(6):
    r = 10 - nom_sel[i]
    if i<6 and r > 0 and nom[i+1]==r*nom[i]:
        nom_sel[i] += r
        nom_sel[i+1] -=1
    else:
        if i<6 and r>1 and nom[i+1]==2*nom[i] and nom_sel[i+1]>0:
            nom_sel[i] += 2
            nom_sel[i+1] -=1
print(nom_sel)
print("Запит:",cash,"Видано",all_sum(nom_sel,nom))