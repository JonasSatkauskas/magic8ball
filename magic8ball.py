import random
import time

time.sleep(0.2)
# Pasisveikinimas su paaiškinimu
print('Labas, aš be rūpesčių atsakysiu į klausimą su pradžia "ar"')
print("\nJeigu nori išeiti, įvesk raidę 'q'")
# Galimi programos atsakymai
atsakymai = ['Taip', 
			'Ne', 
			'Aš dabar užsiėmęs... Paklausk manęs vėliau...', 
			'Tikrai taip!', 
			'Tikrai ne!', 
			'Suformuluok klausimą kitaip']


index = 1

while True:
	# Priminimas apie išėjimą
	if index % 4 == 0:
		time.sleep(0.5)
		print("Jeigu nori išeiti, įvesk raidę 'q'")
	# Atsakymo priskyrimas kintamajam, kad jį paskui būtų galima išprintint
	pasirinkimas = random.choice(atsakymai)
	print()
	
	time.sleep(0.7)
	# Vartotojo suformuluotas klausimas
	klausimas = input('Koks Tavo klausimas?\n')
	# Išėjimas iš loop'o
	if klausimas.upper() == 'Q':
		time.sleep(0.5)
		print('\nIki kitų kartų! Tikiuosi atsakiau i Tavo klausim-ą/us')
		break
	# Jeigu klausimas prasideda žodžiu 'ar', programa atsako į klausimą.
	if 'AR' in klausimas.upper():
		time.sleep(0.5)
		print('\n\t'+pasirinkimas)
		print()
	# Jei klausime yra intarpas 'robot', programa pajuokauja
	elif 'robot' in klausimas:
		print("Ehm... Error")
		print()
	# Jeig klausimas neprasideda žodžiu 'ar', programa pasako kaip derėtų suformuluoti klausimą 
	else:
		time.sleep(0.5)
		print('\nTurite užduoti klausimą su pradžia AR (gali būti ir iš mažųjų)!')
		print()
	# Prie index pridedama 1 (kas 4 klausimą programa primena apie galimybę išeit įvedus 'q')
	index += 1
		