# -*-coding:utf-8-*-
import xmlrpclib
import csv
import os
import logging
import time
 
 
#PLEASE CHANGE
dbname = 'mmp'
user = 'admin'
passwd = 'mmp@2018'
host = 'localhost'
port = 10073
 
com = xmlrpclib.ServerProxy("http://%s:%s/xmlrpc/common" % (host, port))
uid = com.login(dbname, user, passwd)
sock = xmlrpclib.ServerProxy("http://%s:%s/xmlrpc/object" % (host, port))
print 'Logged in to ' + dbname

#PLEASE CHANGE
full_path = "/home/tosin/Downloads/decisoes1.csv"
 
BUF_SIZE = 65536
csv.field_size_limit(1000 * 1024 * 1024)
 
with open(full_path, 'rb') as csvfile:
    csvfile.seek(0)
    file_reader = csv.reader(csvfile, delimiter=';')
    header = file_reader.next()
    counter = 0
    t1 = time.time()
    tipo_condenacao_vals = dict([('p', u'Pagamento'), ('o', u'Obrigação'), ('po', u'Pagamento e Obrigação')])
    for row in file_reader:
        print row
        rowdb = {}
        dossie_id = int(row[0].split('_')[-1]) #A
        rowdb['dossie_id'] = dossie_id
        if row[1]:
            tipo_sentenca_id = sock.execute_kw(dbname, uid, passwd,'tipo.sentenca', 'search',[[['name', '=', row[1]]]],{'limit': 1})
            if tipo_sentenca_id:
                rowdb['tipo_sentenca_id'] = tipo_sentenca_id[0]
        if row[2]:
            rowdb['valor_dano_material'] = row[2]
        if row[3]:
            #tipo_condenacao = tipo_condenacao_vals.keys()[tipo_condenacao_vals.values().index(unicode(row[3]))]
            rowdb['tipo_condenacao'] = row[3]

        sock.execute_kw(dbname, uid, passwd, 'dossie.sentenca', 'create', [rowdb])
        counter += 1
        print 'Processing row: %s' %counter
    msg = "It took %s Sec in process %s records " % (time.time() - t1, counter)
    print msg