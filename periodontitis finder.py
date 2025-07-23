print('''
_____________________ ________                 __         .__    ___________           .__          
\______   \_   _____/ \______ \   ____   _____/  |______  |  |   \__    ___/___   ____ |  |   ______
 |    |  _/|    __)    |    |  \_/ __ \ /    \   __\__  \ |  |     |    | /  _ \ /  _ \|  |  /  ___/
 |    |   \|     \     |    `   \  ___/|   |  \  |  / __ \|  |__   |    |(  <_> |  <_> )  |__\___ \ 
 |______  /\___  /    /_______  /\___  >___|  /__| (____  /____/   |____| \____/ \____/|____/____  >
        \/     \/             \/     \/     \/          \/                                       \/
''')

while True:
    print("Hasta sigara içiyorsa veya diyabeti varsa evrenin derecesi 1 artar!!!")
    girdi = input("Periodontal kaynaklı diş kaybı var mı? (Y)ok, (4) ve daha az, (5)ve daha fazla: (Y) (4) (5): ")
    a = girdi.upper()
    if a == "Y":
        girdi2 = input("Klinik ataçman kaybı ne kadar? (A)1-2mm (B)3-4mm: ")
        b = girdi2.upper()
        if b == "A":
            print("Hastada evre 1 periodontitis mevcut.")
        elif b == "B":
            print("Hastada evre 2 periodontitis mevcut.")
        else:
            print("Yanlış tuşa basıldı")

    elif a == "4":
        print("Hastada evre 3 periodontitis mevcut.")
    elif a == "5":
        print("Hastada evre 4 periodontitis mevcut.")
    else:
        print("Yanlış tuşa basıldı")