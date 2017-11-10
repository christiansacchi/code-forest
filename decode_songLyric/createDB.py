# -*- coding: utf-8 -*-

# createDB.py - 2017 

import sqlite3 as lite
from pathlib import Path

class Wordb (object):

	def __init__ (self, dbname):
		"""try:
			my_dir = Path("/db")
			my_dir.mkdir()
		except FileNotFoundError as e:
			raise"""

		self.dbname = "{0}.db".format(dbname)
		self.dbdir = 'db'
		self.dbname_f = "{0}/{1}".format(self.dbdir, self.dbname)
		self.conn = None
		self.c = None

		self.ID_AUTORE = 0
		self.ID_PAROLA = 1
		self.ID_RACCOLTA = 2
		self.ID_TESTO = 3
		self.CONTs = [0, 0, 1, 0]

	def start (self):
		self.conn = lite.connect(self.dbname_f)
		self.c = self.conn.cursor()

		self.c.execute('SELECT * FROM idcounter')
		self.AUTORE = self.c.fetchone()[2]
		self.PAROLA = self.c.fetchone()[2]
		self.RACCOLTA = self.c.fetchone()[2]
		self.TESTO = self.c.fetchone()[2]

	def end (self):
		self.conn.commit()
		self.conn.close()

	def create (self):
		self.conn = lite.connect(self.dbname_f)
		self.c = self.conn.cursor()

		self.c.execute("""CREATE TABLE autore (id int(10) NOT NULL,nome varchar(128) NOT NULL,cognome varchar(128) DEFAULT NULL,anno year(4) NOT NULL,genere varchar(128) DEFAULT NULL,PRIMARY KEY (id));""")
		self.c.execute("""CREATE TABLE parola (id bigint(20) NOT NULL,word varchar(256) NOT NULL,lingua varchar(128) NOT NULL,iniziale varchar(1) NOT NULL,len int(10) NOT NULL,isbad boolean NOT NULL,PRIMARY KEY (id));""")
		self.c.execute("""CREATE TABLE raccolta (id int(10) NOT NULL,nome varchar(256) NOT NULL,tipo varchar(256) NOT NULL,PRIMARY KEY (id));""")
		self.c.execute("""CREATE TABLE testo (id int(10) NOT NULL,num int(5) NOT NULL,nome varchar(256) NOT NULL,lyrics text,anno year(4) NOT NULL,id_raccolta int(10) NOT NULL,id_autore int(10) NOT NULL,PRIMARY KEY (id),FOREIGN KEY (id_raccolta) REFERENCES raccolta(id),FOREIGN KEY (id_autore) REFERENCES autore(id));""")
		self.c.execute("""CREATE TABLE composizione (id_testo int(10) NOT NULL,id_parola bigint(20) NOT NULL,frequenza int(10) NOT NULL,CONSTRAINT id_composizione PRIMARY KEY (id_testo,id_parola),FOREIGN KEY (id_testo) REFERENCES testo(id),FOREIGN KEY (id_parola) REFERENCES parola(id));""")
		self.c.execute("""CREATE TABLE idcounter (id int(10) NOT NULL,nome varchar(15) NOT NULL,cont bigint(20) NOT NULL,PRIMARY KEY (id));""")

		self.c.execute("""INSERT INTO raccolta (id, nome, tipo) VALUES (0, 'singolo', 'album');""")
		self.c.execute("""INSERT INTO idcounter (id, nome, cont) VALUES (0, 'autore', 0),(1, 'parola', 0),(2, 'raccolta', 1),(3, 'testo', 0);""")

		self.end()
		self.start()



	def increment_id (self, _idtable):
		self.CONTs[_idtable] += 1
		ext = """UPDATE idcounter SET cont={0} WHERE id={1};""".format(self.CONTs[_idtable], _idtable);
		self.c.execute(ext)
		self.conn.commit()

		return self.CONTs[_idtable] - 1



	def add_testo (self, num, nome, anno, id_autore, id_raccolta, lyrics='NULL'):
		ext = """INSERT INTO testo (id, num, nome, lyrics, anno, id_raccolta, id_autore) 
				VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')
				""".format(self.CONTs[self.ID_TESTO], num, nome, lyrics, anno, id_raccolta, id_autore);
		self.c.execute(ext)

		return self.increment_id(self.ID_TESTO)



	def add_autore (self, nome, cognome, anno, genere):
		ext = """INSERT INTO autore (id, nome, cognome, anno, genere) 
				VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')
				""".format(self.CONTs[self.ID_AUTORE], nome, cognome, anno, genere);
		self.c.execute(ext)
		
		return self.increment_id(self.ID_AUTORE)



	def add_raccolta (self, nome, tipo):
		ext = """INSERT INTO raccolta (id, nome, tipo) VALUES ('{0}', '{1}', '{2}')
				""".format(self.CONTs[self.ID_RACCOLTA], nome, tipo);
		self.c.execute(ext)
		
		return self.increment_id(self.ID_RACCOLTA)



	def add_parola (self, word, lingua, iniziale, _len, isbad):
		ext = """INSERT INTO parola (id, word, lingua, iniziale, len, isbad) 
				VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')
				""".format(self.CONTs[self.ID_PAROLA], word, lingua, iniziale, _len, isbad);
		self.c.execute(ext)
		
		return self.increment_id(self.ID_PAROLA)



	def add_composizione (self, id_testo, id_parola, frequenza):
		ext = """INSERT INTO 'composizione' (id_testo, id_parola, frequenza) VALUES ('{0}', '{1}', '{2}')
				""".format(id_testo, id_parola, frequenza);
		self.c.execute(ext)



# ########################## ########################## ########################## #
# ########################## ########################## ########################## #
# ########################## ########################## ########################## #
# ########################## ########################## ########################## #






'''
lol = Wordb ('db3')
lol.create()

idAutore = lol.add_autore('caparezza', '', 1984,'rap')
idRaccolta = lol.add_raccolta('verita supposte', 'album')
idTesto = lol.add_testo(1, 'fuori dal tunnel', 2006, idAutore, idRaccolta)

q1 = """SELECT * FROM testo INNER JOIN autore ON testo.id_autore = autore.id WHERE autore.nome = 'caparezza' """
'''







'''conn = lite.connect('decodeSL.db')
c = conn.cursor()

createTable_autore = """ CREATE TABLE 'autore' (
	'id' int(10) NOT NULL,
	'nome' varchar(128) NOT NULL,
	'cognome' varchar(128) DEFAULT NULL,
	'anno' year(4) NOT NULL,
	'genere' varchar(128) DEFAULT NULL,
	PRIMARY KEY ('id')
); """;

createTable_parola = """ CREATE TABLE 'parola' (
	'id' bigint(20) NOT NULL,
	'word' varchar(256) NOT NULL,
	'lingua' varchar(128) NOT NULL,
	'iniziale' varchar(1) NOT NULL,
	'len' int(10) NOT NULL,
	'isbad' boolean NOT NULL
	PRIMARY KEY ('id')
); """;

createTable_raccolta = """ CREATE TABLE 'raccolta' (
	'id' int(10) NOT NULL,
	'nome' varchar(256) NOT NULL,
	'tipo' varchar(256) NOT NULL,
	PRIMARY KEY ('id')
); """;

createTable_testo = """ CREATE TABLE 'testo' (
	'id' int(10) NOT NULL,
	'num' int(5) NOT NULL,
	'nome' varchar(256) NOT NULL,
	'lyrics' text,
	'anno' year(4) NOT NULL,
	'id_raccolta' int(10) NOT NULL,
	'id_autore' int(10) NOT NULL,
	PRIMARY KEY ('id'),
	FOREIGN KEY ('id_raccolta') REFERENCES raccolta('id'),
	FOREIGN KEY ('id_autore') REFERENCES autore('id')
); """;

createTable_composizione = """ CREATE TABLE 'composizione' (
	'id_testo' int(10) NOT NULL,
	'id_parola' bigint(20) NOT NULL,
	'frequenza' int(10) NOT NULL,
	CONSTRAINT 'id_composizione' PRIMARY KEY ('id_testo','id_parola'),
	FOREIGN KEY ('id_testo') REFERENCES testo('id'),
	FOREIGN KEY ('id_parola') REFERENCES parola('id')
); """;

createTable_indiciCounter = """ CREATE TABLE 'idcounter' (
	'id' int(10) NOT NULL,
	'nome' varchar(15) NOT NULL,
	'cont' bigint(20) NOT NULL,
	PRIMARY KEY ('id')
); """;

c.execute(createTable_autore)
c.execute(createTable_parola)
c.execute(createTable_raccolta)
c.execute(createTable_testo)
c.execute(createTable_composizione)
c.execute(createTable_indiciCounter)

c.execute("""INSERT INTO 'raccolta' ('id', 'nome', 'tipo') VALUES (1, 'singolo', 'album');""")
c.execute('SELECT * FROM raccolta')
print (c.fetchone())

indiciCounter_entry = """
	INSERT INTO 'idcounter' ('id', 'nome', 'cont') VALUES
	(0, 'autore', 0),
	(1, 'parola', 0),
	(2, 'raccolta', 0),
	(3, 'testo', 0)
;"""
c.execute(indiciCounter_entry)
c.execute('SELECT * FROM idcounter')
print (c.fetchone())

conn.commit()
conn.close()'''
