from db.database import DB

db = DB(host="localhost", user="root", passwd="franco1997", database="Cine")

def load_directors_movies():
    query = "SELECT d.last_name, d.first_name, COUNT(movie_id) AS 'How Many' \
        FROM movies_directors AS md JOIN directors AS d ON d.id =md.director_id \
            GROUP by d.last_name, d.first_name \
                HAVING COUNT(movie_id) > 3 \
                    ORDER BY COUNT(movie_id) DESC"
    return db.fetch(query, None)

def load_movies_ranking():
    query = "SELECT a.last_name, a.first_name, COUNT(movie_id) \
        FROM actors AS a JOIN movies_actors as ma on ma.actor_id = a.id \
            GROUP BY a.last_name, a.first_name \
                ORDER BY a.last_name, a.first_name"
    return db.fetch(query, None)

def load_movies_with_best_ranking():
    query = "SELECT m.name as 'Movie', m.year AS 'Year', d.last_name AS 'Director', m.ranking as 'Rank' \
        FROM (movies_directors AS md JOIN movies as m on m.id = md.movie_id) \
            JOIN directors AS d ON d.id = director_id \
                WHERE m.ranking > 8 \
                    ORDER BY m.ranking DESC"
    return db.fetch(query, None)

list = {
    1: ("1- Entregar una lista de los directores que tienen más \n"+
        "de 3 películas ordenadas en orden decreciente", load_directors_movies),
    2: ("2- Entregar una lista pero de un ranking de \n"+
        "actores y se despliega la cuenta de películas para todos ordenados por apellido", load_movies_ranking),
    3: ("3- Entregar una lista de películas, el año, su director y el \n"+
          "puntaje (rank) solo para las películas con rank mayor a 8 ordenadas en forma decreciente", load_movies_with_best_ranking)
}

if __name__ == '__main__':
    
    for n, v in list.items():
        print(v[0])
        rows = v[1]()
        if len(rows):
            for row in rows:
                print(row) 
        else:
            print("No existe información sobre esta consulta")
        print("------------------------------\n")
