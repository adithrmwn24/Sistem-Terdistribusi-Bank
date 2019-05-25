from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


client = xmlrpc.client.ServerProxy("http://127.0.0.2:8886")
server = SimpleXMLRPCServer( ("0.0.0.0", 8885) )

def copy2(a):

    print("server copy meminta req ke server core.....")
    req = client.bank(a)
    if (req>0) :
        saldo = client.bank2(a)
        print("permintaan sukses,saldo : ")
        print(saldo)
        return saldo
    else :
        print("permintaan gagal, saldo kurang")
        return False
# Register fungsinya
server.register_function(copy2, "copy2")

# Jalankan servernya
server.serve_forever()