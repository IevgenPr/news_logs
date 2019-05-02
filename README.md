# News logs engine
`
Query news postgres database with predefined queries.

Invoke `python3 news.py` to get help.

Sample output:

```
$ python3 news.py query get_bad_daysd
Your query is: get_bad_daysd
No such a query, please provide one of the following:
get_most_popular_3
get_popular_authors
get_bad_days

$ python3 news.py query get_bad_days
Your query is: get_bad_days
(datetime.date(2016, 7, 17), 2.26268624680273)

$ python3 news.py query get_popular_authors
Your query is: get_popular_authors
('Ursula La Multa', 507594)
('Rudolf von Treppenwitz', 423457)
('Anonymous Contributor', 170098)
('Markoff Chaney', 84557)

$ python3 news.py query get_most_popular_3
Your query is: get_most_popular_3
('Candidate is jerk, alleges rival', 338647)
('Bears love berries, alleges bear', 253801)
('Bad things gone, say good people', 170098)

$ python3 news.py list
get_most_popular_3
get_popular_authors
get_bad_days

```


