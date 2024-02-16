-- List all the shows and show the genre id if it has one
SELECT sh.title AS title,
        g.genre_id AS genre_id
    FROM tv_shows AS sh LEFT JOIN 
        tv_show_genres AS g
    ON sh.id = g.show_id
    ORDER BY title, genre_id;
