import pandas as pd
from db.database import DB

db = DB(host="localhost", user="root", passwd="franco1997", database="Cine")

def load_movies_with_best_ranking():
    query = "SELECT m.name as 'Movie', m.year AS 'Year', d.last_name AS 'Director', m.ranking as 'Rank' \
        FROM (movies_directors AS md JOIN movies as m on m.id = md.movie_id) \
            JOIN directors AS d ON d.id = director_id \
                WHERE m.ranking > 8 \
                    ORDER BY m.ranking DESC"
    return db.fetch(query, None)

if __name__ == '__main__':
    print("3- Crear una lista de películas, el año, su director y el \n"+
          "puntaje (rank) solo para las películas con rank mayor a 8 ordenadas en forma decreciente")
    df = pd.DataFrame(load_movies_with_best_ranking(), columns=["Pelicula", "Agno", "Director", "Puntaje"])
    
    print("\n4- Cargar en un dataframe Pandas df1 con las siguientes columnas:\n"
          +"Pelicula, Agno, Director, Puntaje")
    print(df)
    
    print("\n4.1- Recorte ese dataframe usando loc de modo de tomar solo las primeras 10\n"+
          "filas y solo las columnas Película y Puntaje. Imprima el nuevo Dataframe resultante")
    df2 = df.loc[:9][["Pelicula", "Puntaje"]]
    print(df2)
    
    print("\n4.2- Recorte nuevamente df1 ahora usando iloc de modo de tomar las filas 20 a\n"+
          "la 50 y todas las columnas. Imprima el nuevo Dataframe resultante.")
    
    df3 = df.iloc[10:]
    print(df3)
