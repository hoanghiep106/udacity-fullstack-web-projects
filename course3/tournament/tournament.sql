-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

create DATABASE tournament;

\c tournament;

create table players(
  id SERIAL primary key,
  name varchar(120) not null
);

create table matches(
  id SERIAL primary key,
  winner integer references players(id),
  loser integer references players(id)
);


create view win_count as
  select winner, count(*) as wins from matches group by winner;


create view player_rankings as
  select players.id, players.name, coalesce(win_count.wins, 0) as wins, count(matches.id) as matches
  from players
    left join win_count on players.id = win_count.winner
    left join matches on players.id = matches.winner or players.id = matches.loser
  group by players.id, win_count.wins order by wins desc;
