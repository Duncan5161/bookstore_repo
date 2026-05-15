
DROP TABLE IF EXISTS films;
DROP SEQUENCE IF EXISTS films_id_seq;

CREATE SEQUENCE IF NOT EXISTS films_id_seq;
CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    film text,
    release_year text
); 

INSERT INTO films (film, release_year) VALUES ('Dune:Part I', 2021);
INSERT INTO films (film, release_year) VALUES ('Dune:Part II', 2024);
INSERT INTO films (film, release_year) VALUES ('Seven', 1995);




