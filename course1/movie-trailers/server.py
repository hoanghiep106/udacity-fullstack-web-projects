import fresh_tomatoes
from movies import Movies

the_avenger_infinity_war = Movies('Avengers: Infinity War',
                                'The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.',
                                'https://ia.media-imdb.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                                'https://www.youtube.com/watch?v=6ZfuNTqbHE8')

a_quiet_place = Movies('A Quiet Place',
                      'A family is forced to live in silence while hiding from creatures that hunt by sound.',
                      'https://ia.media-imdb.com/images/M/MV5BMjI0MDMzNTQ0M15BMl5BanBnXkFtZTgwMTM5NzM3NDM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                      'https://www.youtube.com/watch?v=WR7cc5t7tv8')

rampage = Movies('Rampage',
                'When three different animals become infected with a dangerous pathogen, a primatologist and a geneticist team up to stop them from destroying Chicago.',
                'https://ia.media-imdb.com/images/M/MV5BNDA1NjA3ODU3OV5BMl5BanBnXkFtZTgwOTg3MTIwNTM@._V1_UX182_CR0,0,182,268_AL_.jpg',
                'https://www.youtube.com/watch?v=coOKvrsmQiI')


movies = [the_avenger_infinity_war, a_quiet_place, rampage]

fresh_tomatoes.open_movies_page(movies)
