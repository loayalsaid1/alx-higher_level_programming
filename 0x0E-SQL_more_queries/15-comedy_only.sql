-- List all titles with Comedy genre in the database
SELECT title
FROM tv_shows
INNER JOIN tv_show_genres
INNER JOIN tv_genres ON tv_shows.id = tv_show_genres.show_id
AND tv_show_genres.genre_id = tv_genres.id
WHERE name = 'Comedy'
ORDER BY title;
