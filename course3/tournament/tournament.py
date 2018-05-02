#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def execute(query, params=None):
    connection = connect()
    c = connection.cursor()
    if params:
        c.execute(query, params)
    else:
        c.execute(query)
    connection.commit()
    connection.close()
    

def fetchone(query, *args):
    connection = connect()
    c = connection.cursor()
    c.execute(query, args)
    result = c.fetchone()[0]
    connection.close()
    return result


def fetchall(query, *args):
    connection = connect()
    c = connection.cursor()
    c.execute(query, args)
    result = c.fetchall()
    connection.close()
    return result


def deleteMatches():
    """Remove all the match records from the database."""
    execute("delete from matches")


def deletePlayers():
    """Remove all the player records from the database."""
    execute("delete from players")


def countPlayers():
    """Returns the number of players currently registered."""
    return fetchone("select count(*) from players")


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    execute("insert into players(name) values (%s)", (name,))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    return fetchall("SELECT * FROM player_rankings")


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    execute("INSERT INTO matches(winner, loser) VALUES (%s, %s)", (winner, loser))
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    players = playerStandings()
    result = []
    for i in xrange(0, len(players), 2):
        result.append((players[i][0], players[i][1], players[i+1][0], players[i+1][1]))

    return result

