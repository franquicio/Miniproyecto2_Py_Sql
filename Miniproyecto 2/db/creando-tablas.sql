SET
  FOREIGN_KEY_CHECKS = 0;
DROP table if exists movies;
DROP table if exists actors;
DROP table if exists directors;
DROP table if exists movies_actors;
DROP table if exists movies_directors;
SET
  FOREIGN_KEY_CHECKS = 1;
CREATE TABLE movies(
    id int NOT NULL primary key comment 'primary key',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'create time',
    update_time DATETIME COMMENT 'update time',
    name VARCHAR(100) NOT NULL,
    year int,
    ranking DECIMAL(2, 1)
  ) default charset utf8 comment 'movies table';
CREATE TABLE actors(
    id int NOT NULL primary key comment 'primary key',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'create time',
    update_time DATETIME COMMENT 'update time',
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL
  ) default charset utf8 comment 'actors table';
CREATE TABLE directors(
    id int NOT NULL primary key comment 'primary key',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'create time',
    update_time DATETIME COMMENT 'update time',
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL
  ) default charset utf8 comment 'directory table';
CREATE TABLE movies_actors(
    actor_id INT NOT NULL,
    movie_id INT NOT NULL,
    role VARCHAR(100),
    PRIMARY KEY (actor_id, movie_id),
    FOREIGN KEY(actor_id) REFERENCES actors(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
  ) default charset utf8 comment 'movie and actor relation table';
CREATE TABLE movies_directors (
    director_id INT NOT NULL,
    movie_id INT NOT NULL,
    PRIMARY KEY (director_id, movie_id),
    FOREIGN KEY(director_id) REFERENCES directors(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
  ) default charset utf8 comment 'movie and directori relation table';
INSERT INTO
  movies (id, name, year, ranking)
VALUES
  ()
INSERT INTO
  actors (id, first_name, last_name)
VALUES
  ()
INSERT INTO
  directors (id, first_name, last_name)
VALUES
  ()
INSERT INTO
  movies_actors (actor_id, movie_id, role)
VALUES
  ()
INSERT INTO
  movies_directors (director_id, movie_id)
VALUES
  ()
select
  ifnull(nullif('', ''), 0)
FROM
  DUAL;
SELECT
  d.last_name,
  d.first_name,
  COUNT(movie_id) AS 'How Many'
FROM
  movies_directors AS md
  JOIN directors AS d ON d.id = md.director_id
GROUP by
  d.last_name,
  d.first_name
HAVING
  COUNT(movie_id) > 3
ORDER BY
  COUNT(movie_id) DESC;
SELECT
  a.last_name,
  a.first_name,
  COUNT(movie_id)
FROM
  actors AS a
  JOIN movies_actors as ma on ma.actor_id = a.id
GROUP BY
  a.last_name,
  a.first_name
ORDER BY
  a.last_name,
  a.first_name;
SELECT
  m.name as 'Movie',
  m.year AS 'Year',
  d.last_name AS 'Director',
  m.rank as 'Rank'
FROM
  (
    movies_directors AS md
    JOIN movies as m on m.id = md.movie_id
  )
  JOIN directors AS d ON d.id = director_id
WHERE
  m.rank > 8
ORDER BY
  m.rank DESC;
SELECT
  *
FROM
  movies_directors
SELECT
  *
from
  directors
