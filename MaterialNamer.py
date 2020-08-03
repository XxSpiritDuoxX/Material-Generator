import random

words1 = ("Py", "Rose", "Ram", "Space", "Stor", "Cra", "Volcan", "Jux", "Jest", "Aqu", "Legend", "Joy", "Hell", "Pai", "Spi", "Mine", "Uni", "Tru", "Gem", "Oprix", "My", "Septi", "Octo", "Gole", "Dna", "Dyna", "Gene", "Past", "Anci", "Ste", "Beast", "Mr", "Memo", "Titan", "Sam", "Lor", "Dre", "Mrik", "Yal", "Bar", "Ki", "Opa", "Ro", "Xava", "Va", "Dia", "Pa", "Xol", "Des", "Met", "Bro", "Pew", "Em", "Rub", "Xy", "Zat", "Hea", "Eri", "Silo",)
words2 = ("", "", "", "", "", "", "", "", "", "", "", "", "a", "tain", "yu", "ki", "op", "zuri", "qur", "can", "ben", "real", "lie", "mux", "goe", "jur", "rin", "dev","ra", "than", "to", "se", "rin", "rax", "rom", "xi", "tri", "al", "s", "die", "er", "y", "lo", "ral", "xx", "for", "t",)
words3 = ("", "", "", "", "", "", "mite","ium", "rite", "ite", "mond", "ond", "has", "gold", "old", "by", "nite", "ald", "tite", "creel", "stone", "crystal", "vassel", "stil",)

stat1 = ("Very Low", "Low", "Slightly Low", "Normal", "Slightly High", "Slightly Low", "Normal", "Slightly High", "High", "Very High")
heat = ("Very Low", "Low", "Slightly Low", "Normal", "Slightly High", "Slightly Low", "Normal", "Slightly High","High", "Very High")
stat2 = ("No", "No", "No", "No", "No", "No", "No", "No", "No", "Yes")
shape = ("a Sphere-ish", "a Cube-ish", "a Heart-ish", "a Oval", "No exact", "No exact", "No exact", "No exact", "No exact")
rarity = ("Common","Common", "Slightly Rare", "Rare", "Very Rare","Common", "Slightly Rare", "Rare", "Very Rare", "Super Rare", "Ultra Rare","Common", "Slightly Rare", "Rare", "Very Rare", "Super Rare", "Ultra Rare", "Impossible to find")

effect = ("Breaks", "Breaks", "Melts", "Melts", "Melts", "Melts", "Melts", "Redirects it", "Explodes", "Explodes", "starts cracking", "starts cracking", "starts cracking", "starts Burning,and then explodes",)

name1 = random.choice(words1)
name2 = random.choice(words2)
name3 = random.choice(words3)

red = random.randint(0, 255)
blue = random.randint(0, 255)
green = random.randint(0, 255)
year = random.randint(1000, 2000)

str = random.randint(1, 100)
fri = random.choice(stat1)
tra = random.randint(0, 70)
exp = random.randint(1, 15)
exp2 = random.randint(0, 9)
ref = random.randint(0, 100)
lig = random.choice(stat2)
heat = random.choice(heat)
heat2 = random.choice(effect)
sha = random.choice(shape)
rar = random.choice(rarity)

print("Name | ",name1,name2,name3,sep ="")
print("")
print("----------Color----------")
print("Red | ", red)
print("Green | ", green)
print("Blue | ", blue)
print("----------Info----------")
print("Strength [1 - 100] | ", str)
print("Friction | ", fri)
print("Transparency | ", tra,"% Transparent")
print("Reflectivity | Reflects ", ref,"% of light")
print("Emits Light? | ", lig)
print("Rarity | ", rar)
print("Heat Endurance | ", heat)
print("When it Endures too much heat it", heat2)
print("Explosion Radius [Ignore if it does not explode] | ", exp,".",exp2,"m",sep = "")
print("First discovered in", year)
print("it has", sha,"shape")


























