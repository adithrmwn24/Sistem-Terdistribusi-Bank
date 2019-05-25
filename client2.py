import xmlrpc.client


client = xmlrpc.client.ServerProxy("http://127.0.0.2:8885")

print("saldo anda Rp 100.000")
a = int(input("mau tarik uang? : 1.ya 2.tidak"))

while a==1:
    x = int(input("masukan nominal : "))
    sisa = client.copy2(x)
    if (x == False):
        print("maaf permintaan di gagal")
    else :
        print ("request anda berhasil")
        print("sisa saldo : ",sisa)
        pil = int(input("beli lagi ? : 1. ya 2.tidak"))
        a = pil
        if (a > 1):
            print("terimakasih sudah melakukan transaksi")
            break
