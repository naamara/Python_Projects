import random
print("\t\t \tTHE REVENGE ON THE INVADERS")
print('\t\tClick on game options ')
commands = " "
health = 0
loadgame = False
while True:
	commands = input('»»»::   ').lower()
	if commands == 'game option'.lower():
		print("\t\tClick on the options below".upper())
		print('''\n-› 
		->newgame - Create a file for player                  
		-›loadgame - Open already saved file for player
		-›store - To Equip the warriors
		-›level - select stage to  play 
		-›start -  To start the Game(level to level)
		-›Attack - To fight the enemy
		-›Quit - To end the game''')
		def store1():
			a=['Ceramic', 'VeteranCap', 'Iron3', 'Metallic', 'TechGuide']
			p=[20,40,60,80,100]
			for i in p :
				print("Boost protection by",i)
				print(end=' ')
			f="protection increase by"
			print("\nHelmet---›»",[i for i in a])
			print('\t\tSelect Helmet'.upper())
			select=input("\nhelmet_type::  ")
			if select==a[0]:
				print(f,p[0])
			if select ==a[1]:
				print(f,p[1])
			if select==a[2]:
				print(f,p[2])
			if select==a[3]:
				print(f,p[3])
			if select==a[4]:
				print(f,p[4])
		
		def store2():
			b=['Nickel', 'Gold', 'Silver', 'Bronze','Steel']
			print("\nArmor---›»",[i for i in b])
			print("\t\tSelect armor".upper())
			p=[20,40,60,80,100]			
			f="protection increase by"					
			select=input('\nArmor::  ')
			if select== b[0]:
				print(f,p[0])
			if select==b[1]:
				print(f,p[1])
			if select==b[2]:
				print(f,p[2])
			if select==b[3]:
				print(f,p[3])
			if select==b[4]:
				print(f,p[4])
		
		def store3():			
			c=[25, 45, 60, 75, 100]
			print("\nHealth rate---›»",[i for i in c])
			print('\t\tSelect health kit'.upper())
			x='Your Life has been powerup by'
			select=int(input("\nHealth kit:: "))
			if select==c[0]:
				print(x,select)
			if select==c[1]:
				print(x,select)
			if select==c[2]:
				print(x,select)
			if select==c[3]:
				print(x,select)
			if select==c[4]:
				print(x,select)
		def store4():
			d=["daggers", "The Reaper","Bear hands", 'long sword', 'Kung stick']
			print("\nWeapons---›»",[i for i in d])
			print('\t\tSelect Your Weapons'.upper())
			pr=[20, 40, 60, 80, 100]
			q='You are equip with a' 			
			g='of power rate of'		
			select=input("\nWeapon::")
			if select== d[0]:
				print(q,d[0],g,pr[2])
			if select==d[1]:
				print(q,d[1],g,pr[4])
			if select==d[2]:
				print(q,d[2],g,pr[0])
			if select==d[3]:
				print(q,d[3],g,pr[3])
			if select==d[4]:
				print(q,d[4],g,pr[2])
			print("\n click on the  Level you want to play below".upper())				
		def level():
			lev=['L1','L2','L3','L4','L5']
			print("\nLevels(stages)---›»",[i for i in lev])
			x=[50, 100, 150, 200, 250]
			m_obj='Your objective is to complete all the mission in each level and eliminate your enemy to progess to the next level'
			print(lev[0:])
			selectL=input('\nSelect level:: ')
			if selectL ==lev[0]:
				print(x[0],'mission')
				print("\n",m_obj)
			if selectL==lev[1]:
				print(x[1],'mission')
				print("\n",m_obj)
			if selectL==lev[2]:
				print(x[2],'mission')
				print("\n",m_obj)
			if selectL==lev[3]:
				print(x[3],'mission')
				print("\n",m_obj)
			if selectL==lev[4]:
				print(x[4],'mission')
				print("\n",m_obj)
		def main():
			playerHT=1000	
			enemyHT=1000
			att_eff=random.randint(1,50)
			efatal_att_eff=random.randrange(100,200,5)
			pfatal_att_eff=random.randrange(100,200,5)
			i=0
			attack=1
			fullattack=2
			while i<40:
				# input 1 for normal attack in fight below and input 2 for Full attack
				fight=int(input("Attack::»»"))
				#player plan
				attack=["Weapon","ComboAttack","Hands"]
				z=random.choice(attack)
				#enemy plan
				enemy_att=["Weapon","ComboWeaponAtt","Bear hands"]
				enmy_att_eff=random.randint(1,50)
				x=random.choice(enemy_att)
				if fight==1:
					if z==attack[2] or	x==enemy_att[2] or z==attack[0] or x== enemy_att[0]:
						print("\nYour HT decrease by",enmy_att_eff,"your HT remain",playerHT-enmy_att_eff,)		
						playerHT=playerHT-enmy_att_eff
						print("Enemy HT decrease by",att_eff,"enemy HT remain", enemyHT-att_eff)
						enemyHT=enemyHT-att_eff
						if playerHT<=0 and enemyHT>0 and i<=40 :
							print("You Lose")
							break
						if enemyHT<=0 and playerHT>0 and i<=40:
							print("Finish Your Enemy")
							print("\nYou won")
							break
									
				if fight==2:
					if z==attack[1] or x==enemy_att[1]:
						print("\nYour HT decrease by",pfatal_att_eff,"your HT remain",playerHT-pfatal_att_eff)
						playerHT=playerHT-pfatal_att_eff
						print("Enemy HT decrease by",efatal_att_eff,"enemy HT remain",enemyHT-efatal_att_eff)
						enemyHT=enemyHT-efatal_att_eff
					if playerHT<=0 and enemyHT>0 and i<=40 :
						print("You Lose")
						break
					if enemyHT<=0 and playerHT>0 and i<=40:
						print("Finish Your Enemy")
						print("\nYou won !!! MISSION ACCOMPLISH")
						break
				i+=1	
			if playerHT <=0 and enemyHT>0:
				print("Replay  your prevoius mission ")
			elif playerHT>=1 and enemyHT <=0:
				print("Mission completed".upper())
				print("\n\t\tProceed to the next level	".upper())
					
																
	if commands=='newgame':
		player=input('Player name::   ')
		print(f"\t\t {player} , Welcome to the realm of invaders".upper())
		if loadgame:
			print("Select Your file")
		else:
			print("Go to the store")
	if commands=="store":
		print("Equip Your warrior".upper())

		"\n",store1()
		
		"\n",store2()
		
		"\n",store3()
			
		"\n",store4()

	if commands=='level':
		print("Choose the level You want".upper())
		
		
		"\n",level()					

	if commands=="start":
		print("\t\twarrior,the inevitable war has started ,now face off your enemy".upper())
		print("\nFight!!!"*3)
					 
	if commands=="attack":		 
		print("\t\tThe Battle has began".upper())

														
		"\n",main()
		
	if commands=="quit":		
		clicks=input("Do You want to exit the game :: ")
		if clicks=="Yes":
			print("Game Exit")
			break
		elif clicks=="No" :
			print("Game continue")							 	
			"\n",main
				 				 				 
			 
		
			
			
								
		
		
		
		
	
								
		