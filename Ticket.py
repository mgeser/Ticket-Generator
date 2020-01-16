import random
def Ticket():
    jumlah = int(input("Masukkan Jumlah Ticket Yang Akan Di Generate: "))
    print("Jumlah Maximal 10 Ticket!")
    if jumlah <= 10:
        for i in range (jumlah):
            firstname=['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            name = random.choice(firstname)
            name2 = random.choice(firstname)
            name3 = random.choice(firstname)
            phone = random.randint(1000000000, 9999999999)
            i = i+1
            print(i, "Kode Tiket Anda:", name + name2 + name3, phone)

Ticket()