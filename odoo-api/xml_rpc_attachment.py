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
full_path = "/home/tosin/Downloads/attachment.csv"
 
BUF_SIZE = 65536
csv.field_size_limit(1000000 * 1024 * 1024)

with open(full_path, 'w') as csvfile:
    counter = 0
    t1 = time.time()
    fieldnames = ['id', 'name', 'index_content']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    attachment_ids = sock.execute_kw(dbname, uid, passwd,'ir.attachment', 'search',
                    [[['x_objeto_id', '!=', False], ['x_assunto_id', '!=', False]]])

    print len(attachment_ids)

    for att_id in attachment_ids:
        try:
            attachment = sock.execute_kw(dbname, uid, passwd,'ir.attachment', 'read',[att_id], {'fields': ['id', 'name','index_content']})[0]
            counter += 1
            print attachment
            print 'Processing row: %s' %counter
            writer.writerow({'id': attachment['id'], 'name': attachment['name'].encode('utf-8'), 'index_content': attachment['index_content'].encode('utf-8')})
        except:
            continue
    msg = "It took %s Sec in process %s records " % (time.time() - t1, counter)
    print msg