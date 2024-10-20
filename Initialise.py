import sqlite3
conn = sqlite3.connect("circuitdata.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE tblcomponents
    (
    compID INTEGER,
    comptype TEXT,
    xpos INTEGER,
    ypos INTEGER,
    midleftx INTEGER,
    midlefty INTEGER,
    midbottomx INTEGER,
    midbottomy INTEGER,
    midrightx INTEGER,
    midrighty INTEGER,
    midtopx INTEGER,
    midtopy INTEGER,
    rotation INTEGER,
    powered BOOLEAN,
    resistance INTEGER,
    voltage INTEGER,
    uniquestate INTEGER,
    voltageaccross FLOAT,
    currentaccross FLOAT,
    level INTEGER,
    primary key (compID))
    """)

cursor.execute('DELETE FROM tblcomponents where compID = ""')
conn.commit()

cursor.execute("""
    CREATE TABLE tblpositiveconnections
    (
    ROWID INTEGER,
    compID INTEGER,
    positiveterminalconnectedto INTEGER,
    connectamount INTEGER,
    ignore BOOLEAN,
    primary key (ROWID))
    """)

cursor.execute('DELETE FROM tblpositiveconnections where ROWID = ""')
conn.commit()

cursor.execute("""
    CREATE TABLE tblnegativeconnections
    (
    ROWID INTEGER,
    compID INTEGER,
    negativeterminalconnectedto INTEGER,
    connectamount INTEGER,
    primary key (ROWID))
    """)

cursor.execute('DELETE FROM tblnegativeconnections where ROWID = ""')
conn.commit()
