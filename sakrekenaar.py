import subprocess
import math

#funksie om die skerm skoon te maak, werk op beide Windows en Mac/Linux
def skoonmaak():
    try:
        #probeer Windows skoonmaak opdrag
        subprocess.run('cls', shell=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        #as dit fail (soos op Mac/Linux), gebruik clear
        subprocess.run('clear', shell=True, check=True)

#funksies om twee getalle te plus
def plus(a, b):
    return a + b

#funksies om twee getalle te minus
def minus(a, b):
    return a - b

#funksies om twee getalle te maal
def maal(a, b):
    return a  * b

#funksies om twee getalle te deel
def deel(a, b):
    if b == 0:   #toets vir deling deur nul
        return 'Kan nie deur \'0\' deel nie!'
    else:
        return a / b

#sentinel variabele om die program te laat loop totdat die gebruiker besluit om te stop
hardloop = True

#as hardloop is waar, sal die program aanhou loop totdat die gebruiker besluit om te stop
while hardloop:

    try:
        
        skoonmaak()     #maak die skerm skoon

        #gebruiker voer vir die eerste getal in of tik 'stop' om die program te verlaat
        invoer1 = input('Voer die eerste getal in of tik \'stop\' om af te sluit ')

        #toets of die gebruiker 'stop' getik het, as dit waar is, sal hardloop na false verander word en die program sal stop
        if invoer1.lower() == 'stop':
            hardloop = False
            continue

        #desimale word toegelaat, daarom word float gebruik om die invoer na 'n desimale getal te omskep
        getal1 = float(invoer1)

        #gebruiker kies die bewerking wat hulle wil gebruik, dit kan +, -, *, of / wees
        bewerking = input('Kies jou bewerking: +, -, *, / ')

        #toets of die bewerking geldig is
        if bewerking not in ['+', '-', '*', '/']:
            print('Ongeldige bewerking gekies')
            input('Druk Enter om weer te probeer')
            continue
       
        #invoer vir die tweede getal of tik 'stop' om die program te verlaat
        invoer2 = input('Voer die tweede getal in of tik \'stop\' om af te sluit ')

        #toets of die gebruiker 'stop' getik het, as dit waar is, sal hardloop na false verander word en die program sal stop
        if invoer2.lower() == 'stop':
            hardloop = False
            continue

        #desimale word toegelaat, daarom word float gebruik om die invoer na 'n desimale getal te omskep
        getal2 = float(invoer2)

        #afhangend van die bewerking wat gekies is, sal die regte funksie geroep word om die berekening te doen
        #as die bewerking nie geldig is nie, sal die gebruiker gevra word om weer te probeer
        if bewerking == '+':
            totaal = plus(getal1, getal2)
        elif bewerking == '-':
            totaal = minus(getal1, getal2)
        elif bewerking == '*':
            totaal = maal(getal1, getal2)
        elif bewerking == '/':
            totaal = deel(getal1, getal2)
        
        #maak die skerm skoon voordat die resultaat vertoon word
        skoonmaak()

        #toets of getal1 n heelgetal is, as dit waar is, sal hulle na int verander word om die desimale punt te verwyder
        if getal1 % math.floor(getal1) == 0:
            getal1 = int(getal1)

        #toets of getal2 n heelgetal is, as dit waar is, sal hulle na int verander word om die desimale punt te verwyder
        if getal2 % math.floor(getal2) == 0:
            getal2 = int(getal2)

        #toets of totaal n heelgetal is, as dit waar is, sal hulle na int verander word om die desimale punt te verwyder
        if totaal % math.floor(totaal) == 0:
            totaal = int(totaal)

        #vertoon die resultaat van die berekening aan die gebruiker  
        print(' ',getal1, bewerking, getal2,)
        print('=', totaal)
        input('Druk Enter om voort te gaan')

    #word uitgevoer as die gebruiker nie n getal invoer nie
    except ValueError:
        print('Invoer was nie n getal nie')
        input('Druk Enter om weer te probeer')

#word uitgevoer as die gebruiker stop getik het
else:
    skoonmaak()
    print('Cheers!')