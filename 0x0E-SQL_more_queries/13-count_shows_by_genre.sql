-- LIST ALL THE GENRES WITH THE COUNT OF EACH DATABASE RELATED TO IT
SELECT g.name AS genre,
        COUNT(sg.show_id) AS number_of_shows
    FROM tv_genres AS g INNER JOIN
        tv_show_genres AS sg
    ON g.id = sg.genre_id
    GROUP BY(genre)
    ORDER BY number_of_shows DESC;
