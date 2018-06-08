# -*-coding:utf-8-*-
import xmlrpclib
import time
import datetime
import xmltodict


#PLEASE CHANGE
dbname = 'mmp'
user = 'admin'
passwd = 'mmp@2018'
host = 'localhost'
port = 10073
 
full_path = ['/home/tosin/Downloads/bigdata_sample.xml',
            ]

t1 = time.time()
com = xmlrpclib.ServerProxy("http://%s:%s/xmlrpc/common" % (host, port))
uid = com.login(dbname, user, passwd)
sock = xmlrpclib.ServerProxy("http://%s:%s/xmlrpc/object" % (host, port))
print 'Logged in to ' + dbname


for path in full_path:
    with open(path, 'rb') as movimentacao_xml:
        print path
        movimentacao_dict = xmltodict.parse(movimentacao_xml, xml_attribs=False)
        counter = 0
        movimentacaos = movimentacao_dict[movimentacao_dict.keys()[0]]

        while(len(movimentacaos) > counter):
            movimentacao = movimentacaos['item'+str(counter)]
            estado_id = sock.execute_kw(dbname, uid, passwd, 'res.country.state', 'search', [[['name','ilike',movimentacao["estado"]]]],{'limit':1})
            
            processo = movimentacao['processo'][9:-3]

            dossie_id = sock.execute_kw(dbname, uid, passwd, 'dossie.dossie', 'search', [[['name','ilike',processo]]],{'limit':1})
            if not dossie_id:
                dossie_id = sock.execute_kw(dbname, uid, passwd, 'dossie.dossie', 'create', [{'name':processo,'processo':processo,'estado_id':estado_id[0]}])
            
            try:
                dossie_id = dossie_id[0]
            except:
                pass

            rowdb = {
                'processo':processo,
                'movimentacao':movimentacao['publicacao'][9:-3],
                'data': movimentacao['DataPublicacao'],
                'dossie_id': dossie_id,
            }
            
            sock.execute_kw(dbname, uid, passwd, 'dossie.movimentacao', 'create', [rowdb])
            counter += 1
            print 'Processing row: %s with processo: %s' %(counter, rowdb['processo'])

        print "It took %s sec in process %s records " % (time.time() - t1, counter)