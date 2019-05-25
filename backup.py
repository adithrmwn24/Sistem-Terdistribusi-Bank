from xmlrpc.server import SimpleXMLRPCServer

daftar_transaksi= []
server = SimpleXMLRPCServer( ("0.0.0.0", 8884) )

def backup(a,b):
    hasil = daftar_transaksi.append(a)
    print (hasil)
    # print("pemberitahuan sudah di update sudah melakukan transaksi sebesar : ", a)

    # print("saldo terkini : ",b)
    return 0

server.register_function(backup, "backup")

server.serve_forever()