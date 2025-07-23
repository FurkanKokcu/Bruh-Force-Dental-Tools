print('''
_____________________ ________                 __         .__    ___________           .__          
\______   \_   _____/ \______ \   ____   _____/  |______  |  |   \__    ___/___   ____ |  |   ______
 |    |  _/|    __)    |    |  \_/ __ \ /    \   __\__  \ |  |     |    | /  _ \ /  _ \|  |  /  ___/
 |    |   \|     \     |    `   \  ___/|   |  \  |  / __ \|  |__   |    |(  <_> |  <_> )  |__\___ \ 
 |______  /\___  /    /_______  /\___  >___|  /__| (____  /____/   |____| \____/ \____/|____/____  >
        \/     \/             \/     \/     \/          \/                                       \/
''')

while True:
    a = input ("Hastalık ismini giriniz: ").lower()
    b = input ("Uygulanacak işlemi yazınız: ").lower()
    c = input ("Hasta kullandığı ilacı biliyor mu? biliyorsa 'evet' bilmiyorsa 'hayır' yazınız: ").lower()

    if c == "evet":
        kilac = input("İlacın ismi: ")
    else:
        kilac = str("bilmediği")
    print(f"Hastada alınan sözlü anamnezde {a} geçmişi olduğu ilaç kullandığı kullandığı ilacın ismini {kilac} öğrenilmiştir. Hastaya {b} uygulanacaktır. Tarafınızca değerlendirilmesi rica olunur.")