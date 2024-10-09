# Hollymovies

Filmová databáze.

## Funkcionalita

-[ ] informace o filmu
-[ ] informace o režisérech/hercích
-[ ] vkládání/editace/mazání filmu, režiséra, herce,...
-[ ] hodnocení filmu
-[ ] filtrování filmů na základě žánru, roku, herce, země...
-[ ] seřazení filmů podle ratingu, roku,...
-[ ] vyhledávání filmu/režiséra/herce...

## Databáze

-[x] movie
  -[x] id
  -[x] title_orig
  -[x] title_cz
  -[x] year
  -[x] length (min)
  -[x] novel_id -> novel
  -[x] productions (n:m -> production_company)
  -[x] directors (n:m -> creator)
  -[x] actors (n:m -> creator)
  -[x] countries (n:m -> country)
  -[x] genres (n:m -> genre)
  -[x] rating
  -[x] medias (n:m -> media)
  -[x] awards (n:m -> award)
  -[x] description
  -[x] reviews -> review
-[x] review
  -[x] id
  -[x] movie_id -> movie
  -[x] reviewer -> user 
  -[x] rating
  -[x] comment 
  -[x] time  
-[x] award
  -[x] id
  -[x] name (-> award_name)
  -[x] category (-> category_name)
  -[x] year 
-[x] production_company
  -[x] id
  -[x] name
  -[x] foundation_year
  -[x] country_id
-[x] novel
  -[x] id  
  -[x] title
  -[x] author -> creator
-[x] creator
  -[x] id
  -[x] first_name
  -[x] last_name
  -[x] date_of_birth
  -[x] date_of_death
  -[x] nationality -> country
  -[x] biography
  -[x] awards (n:m -> award)
  -[x] movies_actor (n:m -> movie)
  -[x] movies_director (n:m -> movie)
-[x] genre
  -[x] id
  -[x] name
-[x] country
  -[x] id
  -[x] name
-[x] user
  -[x] id
  -[x] username
  -[x] first_name
  -[x] last_name
-[x] media
  -[x] id
  -[x] type (image/video/text/sound)
  -[x] url
  -[x] movie_id -> movie
  -[x] actors (n:m -> creators)
  -[x] description

![ER diagram](files/er_diagram_v1.png)
