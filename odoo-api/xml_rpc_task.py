# -*-coding:utf-8-*-
import xmlrpclib
import csv
import os
import logging
import time
import datetime
 
 
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
full_path = "/home/tosin/Downloads/data_limite.csv"
 
BUF_SIZE = 65536
csv.field_size_limit(1000 * 1024 * 1024)
 
with open(full_path, 'rb') as csvfile:
    csvfile.seek(0)
    file_reader = csv.reader(csvfile, delimiter=';')
    header = file_reader.next()
    counter = 0
    t1 = time.time()
    for row in file_reader:
        print row
        rowdb = {}
        task_id = int(row[0].split('_')[-1]) #A
        if row[1]:
            rowdb['data_cppro'] = datetime.datetime.strptime(row[1], '%d/%m/%Y').strftime('%m/%d/%Y')

        if row[2]:
            rowdb['date_deadline'] = datetime.datetime.strptime(row[2], '%d/%m/%Y').strftime('%m/%d/%Y')

        sock.execute_kw(dbname, uid, passwd, 'project.task', 'write', [task_id, rowdb])
        counter += 1
        print 'Processing row: %s' %counter
    msg = "It took %s Sec in process %s records " % (time.time() - t1, counter)
    print msg