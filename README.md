# News logs engine
`
Query news postgres database with predefined queries.

Invoke `python3 news.py` to get help.

Below is a sample output of supported commands:

```
$ python3 news.py query get_bad_daysd
Your query is: get_bad_daysd
No such a query, please provide one of the following:
get_most_popular_3
get_popular_authors
get_bad_days

$ python3 news.py list
get_most_popular_3
get_popular_authors
get_bad_days

$ python3 news.py query get_most_popular_3
Most popular articles:
  Candidate is jerk, alleges rival  - 338647 views
  Bears love berries, alleges bear  - 253801 views
  Bad things gone, say good people  - 170098 views

$ python3 news.py query get_popular_author
Most popular authors:
  Ursula La Multa  - 507594 views
  Rudolf von Treppenwitz  - 423457 views
  Anonymous Contributor  - 170098 views
  Markoff Chaney  - 84557 views

$ python3 news.py query get_bad_days
Days with more than 1% errors:
  Jul 17, 2016  - 2.26% errors
```


