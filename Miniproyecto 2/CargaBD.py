from file.load import File
from db.database import DB

db = DB(host="localhost", user ="root", passwd="franco1997", database="Cine")

def clear_db(table):
    db.query("SET foregin_key_checks = 0", None)
    db.delete("DELETE FROM {}".format(table), None)
    db.query("SET foregin_key_checks", None)

def load_movies(file):
    file = File(file)
    rows = list()

    for row in file.readUrl():
        rows.append(( int(row[0]), row[1], int(row[2]), float(row[3].replace('NULL','0.0')) ))    
    query = "INSERT INTO movies (id, name, year, ranking) VALUES \
                (%s, %s, %s, %s )"
    db.insertmany(query, rows)

def load_actors(file):
    file = File(file)
    rows = list()
    for row in file.readUrl():
        rows.append(tuple(row))
    query = "INSERT INTO actors (id, first_name, last_name) VALUES \
        (%s, %s, %s)"            
    db.insertmany(query, rows)

def load_directors(file):
    file = File(file)
    rows = list()
    for row in file.readUrl():
        rows.append(tuple(row))
    query = "INSERT INTO directors (id, first_name, last_name) VALUES \
        (%s, %s, %s)"
    db.insertmany(query, rows)

def load_movies_actors(file):
    file = File(file)
    rows = list()
    for row in file.readUrl():
        rows.append(tuple(row))
    query = "INSERT INTO movies_actors (actor_id, movie_id, role) VALUES \
        (%s, %s, %s)"
    db.insertmany(query, rows)
    

def load_movies_directors(file):
    file = File(file)
    rows = list()
    for row in file.readUrl():
        rows.append(tuple(row))
    query = "INSERT INTO movies_directors (director_id, movie_id) VALUES \
        (%s, %s)"
    db.insertmany(query, rows)

files = {
    'movies' : ('movies.csv', load_movies),
    'actors' : ('actors.csv', load_actors),
    'directors' : ('directors.csv', load_directors),
    'movies_actors' : ('movies_actors.csv', load_movies_actors),
    'movies_directors' : ('movies_directors.csv', load_movies_directors),
}
    
if __name__ == '__main__':
    for table, value in files.items():
        clear_db(table)
        print(f"Cargando el archivo : {value[0]} ...")
        value[1](value[0])
        print(f"Tabla {table} cargada con éxito \n")
        
