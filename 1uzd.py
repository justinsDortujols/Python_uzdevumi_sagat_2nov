"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

kas ir klase???
    klase ir objekta shabloms
    klase sastav no konstruktora/destruktora un metodēm.
kadas datu struktura zinu?
    list,arry,dict
    dict pieraksta -- {};dict()
kas ir vardnica
    datu struktura, key un tās vērtība
"""

class AAA:
    def __init__(self):
        self.roma_sk= {
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }
    def to_roman(self, num):
        result =""
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True):
            while num >= value:
                result+=numeral
                num-=value 
        return result
#ka sauc AAA ieskejo funkcjiu: to_roman // tukss saraksts: result="" 
#class ir veidne

#piemers
skaitlis=2023
#definejam objektu
kk=AAA()
#jaunajam objektam jaizsauc klases metode vai ieksejo funkciju
romiesu=kk.to_roman(skaitlis)
#noformet izdruku
print(f"{skaitlis} ar romiesu cipariem ir {romiesu}.")