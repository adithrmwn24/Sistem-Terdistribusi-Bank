from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


client = xmlrpc.client.ServerProxy("http://127.0.0.3:8884")
server = SimpleXMLRPCServer( ("0.0.0.0", 8886) )

b = 100000
def bank(a):
    print("permintaan sedang di proses..")
    global b
    if (a > b) :
        print("maap saldo anda kurang")
        return False
    else :
        print("saldo cukup, permintaan sedang di proses")
        return True

def bank2(a):
    print("penarikan uang..")
    global b
    if (a > b) :
        print("maap saldo anda kurang")
        return True
    else :
        b = b - a
        client.backup(a,b)
    return b

def id (x) :
    print ("permintaan sedang verifikasi")
    if (x == 1111) :
        print ("password telah terverifikasi")
        return "berhasil"
    elif (x == 2222):
        print("permintaan sedang verifikasi")
        return "berhasil"
    else :
        return "password salah"


server.register_function(bank, "bank")
server.register_function(bank2, "bank2")
server.register_function(id, "id")

server.serve_forever()
