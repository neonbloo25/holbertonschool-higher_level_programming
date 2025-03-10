-- lists all shows contained in hbtn_0d_tvshows w/o linked genre
SELECT tv_shows.title,
    tv_show_genres.genre_id
FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id is NULL
ORDER BY title ASC,
    genre_id ASC;
