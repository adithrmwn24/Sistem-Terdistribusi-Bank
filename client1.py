import xmlrpc.client


client = xmlrpc.client.ServerProxy("http://127.0.0.1:8888")
client2 = xmlrpc.client.ServerProxy("http://127.0.0.1:8886")

b = int(input("masukan password : "))
ack = client2.id(b)
print (ack)
if (ack == "berhasil" ):
    print("saldo anda Rp 100.000")
    a = int(input("mau tarik uang? : 1.ya 2.tidak"))
    while a == 1:
        x = int(input("masukan nominal : "))
        sisa = client.copy1(x)
        if (x == False):
            print("maaf permintaan di gagal")
        else:
            print("request anda berhasil")
            print("sisa saldo : ", sisa)
            pil = int(input("beli lagi ? : 1. ya 2.tidak"))
        a = pil
        if (a > 1):
            print("terimakasih sudah melakukan transaksi")
            break
else :
    print ("maaf password gagal")