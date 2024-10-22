import winsound

def show_directory():
    fh = open("Subscribers.txt","r")
    D = {}
    for line in fh:
        parts = line.split()
        name = ' '.join(parts[:-1])
        number = parts[-1]
        D[name] = number
        
    print("\nName\t\tNumber")
    print("_______\t\t_______")
    for n, nu in D.items():
        print(f"{n}\t{nu}")
    
    #k = fh.read()
    #print(k)
    fh.close()
    
def add_directory():
    fh = open("Subscribers.txt","a")
    
    name = input("Enter the name : ")
    number = input("Enter the phone number : ")
    
    fh.seek(0,2)
    fh.write(f"\n{name} ")
    fh.write(f"{number}")
    
    print("\nContact Saved\n")    
    fh.close()

def search():
    fh = open("Subscribers.txt","r")
    
    D = {}
    
    for line in fh:
        parts = line.split()
        name = ' '.join(parts[:-1])
        number = parts[-1]
        D[name] = number
        
    while True:
        print("Search with?\n1. Name\n2.Number\n")
        search_method = int(input("Please choose : "))
        
        if search_method == 1:
            name_input = input("Enter the name : ")
            
            found = False
            for key,value in D.items():
                if name_input in key:
                    print(f"\nContact Found\n{key}\t{value}\n")
                    found =True
            if not found:
                print("\nContact Not Found.\n")
            break
        elif search_method == 2:
            number_input = input("Enter the number : ")
            
            found = False
            for key,value in D.items():
                if number_input in value:
                    print(f"\nContact Foud\n{key}\t{value}\n")
                    found = True
            if not found:
                print("\nContact Not Found.\n")
            break
        else:
            print("\nInvalid Input\n")
    fh.close()

def display():
    open_sound  = r'C:\Users\Akash\Desktop\Phone Book Directory\sound_effect\opening.wav'
    winsound.PlaySound(open_sound, winsound.SND_FILENAME)
    
    intro = "PHONE BOOK DIRECTORY"
    print(intro.center(50))
    print("_______________________________________________")

    while True:
        print("\n1. Show List\n2. Add New Contact\n3. Search For Contact\n4. Exit\n")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            show_directory()
        elif choice == 2:
            add_directory()
        elif choice == 3:
            search()
        elif choice == 4:
            
            close_sound = r'C:\Users\Akash\Desktop\Phone Book Directory\sound_effect\closing.wav'
            winsound.PlaySound(close_sound, winsound.SND_FILENAME)
            break
        else:
            print("\nInvalid Input\n")
    
display()