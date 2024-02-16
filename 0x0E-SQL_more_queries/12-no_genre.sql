-- LIST ALL SHOW WITHOUT A GENRE LINKED TO IT
SELECT sh.title AS title,
        g.genre_id AS genre_id
    FROM tv_shows AS sh LEFT JOIN
        tv_show_genres AS g
    ON sh.id = g.show_id
    WHERE genre_id IS NULL
    ORDER BY title, genre_id;
