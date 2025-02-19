import os
os.system('cls')

'''
__author__  = "Pablo"
__version__ = "1.0.0"
__email__   = "pablo.anderssonmelian@elev.ga.ntig.se"
'''

def add_name(name_list, name): # Funktion för att kunna lägga till namn med append
    name_list.append(name)

def remove_name(name_list, name):  # Funktion för att ta bort ett namn med pop
    if name in name_list:
        name_list.pop()

def update_name(name_list, old_name, new_name):       # Funktion för att ändra namn genom att ge old_name till till din vald namn.
    if old_name in name_list:
        index = name_list.index(old_name)
        name_list[index] = new_name


names = []




print("Välkommen till din vänlista!")    
while True:
    print("\nDin Kompis Lista:", names)#Introduktion av kommandon
    print("1: Lägg till namn")
    print("2: Ta bort namn")
    print("3: Ändra namn")
    print("4: Avsluta")

    try:
        choice = int(input("Välj ett alternativ: "))  #Matar in det du vill göra 
    except ValueError:                                                              # Stoppar dig från att skriva bokstäver
        print("Vänligen ange ett giltigt nummer!")
        continue
    

    if choice == 1:
        new_name = input("Ange namnet som ska att lägga till: ").upper()  #Lägg till ett nytt namn
        add_name(names, new_name)
        os.system('cls')   
    elif choice == 2:
        if  not any(isinstance(item, str) for item in names):           # Ser till att du inte försöker ta bort ett namn när du inte ens har lagt till 1 namn
             print("Du måste ha ett namn i listan för att ta bort en!")
             continue
        else:
            remove_name_input = input("Ange hela namnet för att ta bort: ").upper()  #Ta bort ett namn
            remove_name(names, remove_name_input)
            os.system('cls')   
        if remove_name_input == 4:
            exit()
        
    elif choice == 3:
        if  not any(isinstance(item, str) for item in names):               # Ser till att du inte försöker ändra ett namn när du inte ens har lagt till 1 namn
             print("Du måste ha ett namn i listan för att ändra en!")
             continue
        else:
            old_name = input("Ange hela namnet som ska ändras: ").upper()  # Ändra ett namn
            new_name = input("Ange det nya namnet: ").upper()
            update_name(names, old_name, new_name)
            os.system('cls')   
    elif choice == 4:          # Avslutar programmet
        print("Hej då!")
        print("avslutar...")
        exit()

        
       
        
    else:
            os.system('cls')
            print("Skriv ett nummer mellan 1-4 tack") # Ser till så att du verkligen skriver ett nummer mellan 1-4
  
