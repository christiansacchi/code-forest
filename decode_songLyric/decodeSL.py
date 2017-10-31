# -*- coding: utf-8 -*-

# createDB.py - 2017 

import sqlite3 as lite

conn = lite.connect('decodeSL.db')
c = conn.cursor()

createTable_autore = ''' CREATE TABLE 'autore' (
	'id' int(10) NOT NULL,
	'nome' varchar(128) NOT NULL,
	'cognome' varchar(128) DEFAULT NULL,
	'anno' year(4) NOT NULL,

	PRIMARY KEY ('id')
); ''';

createTable_parola = ''' CREATE TABLE 'parola' (
	'id' bigint(20) NOT NULL,
	'word' varchar(256) NOT NULL,
	'lingua' varchar(128) NOT NULL,
	'len' int(10) NOT NULL,

	PRIMARY KEY ('id')
); ''';

createTable_raccolta = ''' CREATE TABLE 'raccolta' (
	'id' int(10) NOT NULL,
	'nome' varchar(256) NOT NULL,
	'tipo' varchar(256) NOT NULL,

	PRIMARY KEY ('id')
); ''';

createTable_testo = ''' CREATE TABLE 'testo' (
	'id' int(10) NOT NULL,
	'lyrics' text,
	'anno' year(4) NOT NULL,
	'id_raccolta' int(10) NOT NULL,
	'id_autore' int(10) NOT NULL,

	PRIMARY KEY ('id'),
	FOREIGN KEY ('id_raccolta') REFERENCES raccolta('id'),
	FOREIGN KEY ('id_autore') REFERENCES autore('id')
); ''';

createTable_composizione = ''' CREATE TABLE 'composizione' (
	'id_testo' int(10) NOT NULL,
	'id_parola' bigint(20) NOT NULL,
	'frequenza' int(10) NOT NULL,

	CONSTRAINT 'id_composizione' PRIMARY KEY ('id_testo','id_parola'),
	FOREIGN KEY ('id_testo') REFERENCES testo('id'),
	FOREIGN KEY ('id_parola') REFERENCES parola('id')
); ''';

c.execute(createTable_autore)
c.execute(createTable_parola)
c.execute(createTable_raccolta)
c.execute(createTable_testo)
c.execute(createTable_composizione)

c.execute('''INSERT INTO 'raccolta' ('id', 'nome', 'tipo') VALUES (1, 'singolo', 'album');''')
c.execute('SELECT * FROM raccolta')
print (c.fetchone())

conn.commit()
conn.close()
