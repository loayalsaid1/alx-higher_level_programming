-- GET ALL THE TV SHOWS AND THEIR GENRE_ID FOR EACH
-- SHOW THAT HAS  A GENRE RECORD
SELECT sh.title AS title,
        g.genre_id AS genre_id
    FROM tv_shows AS sh INNER JOIN tv_show_genres AS g
    ON sh.id = g.show_id
    ORDER BY title, genre_id;
