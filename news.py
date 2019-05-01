""" Interface to communicate with database"""

import sys
import newsdb

DB = "news"
queries = dict()

"""1. What are the most popular three articles of all time?
Which articles have been accessed the most?
This information as a sorted list with
the most popular article at the top."""

queries["get_most_popular_3"] = """
        select a.title as title, count(l.id) as views
        from articles a left join log l
        on concat('/article/',a.slug) = l.path
        group by a.title order by views desc limit 3;"""

"""2. Who are the most popular article authors of all time?
That is, when you sum up all of the articles each author has written,
which authors get the most page views?
Present this as a sorted list with the most popular author at the top."""

queries["get_popular_authors"] = """
select a.name, count(l.id) as views
from (select au.name, ar.slug as arts
      from authors au, articles ar where au.id = ar.author) as a
left join log l
      on concat('/article/',a.arts) = l.path
group by a.name
order by views desc;
"""

""" On which days did more than 1% of requests lead to errors
The log table includes a column status that indicates the HTTP status
code that the news site sent to the user's browser. (Refer to this
lesson for more information about the idea of HTTP status codes.)
"""

queries["get_bad_days"] = """
select * from (select lbad.d, (100.0 * cast(lbad.c as float) / cast(lall.c as float) as bad_day
from (select date(time) as d,count(*) as c from log group by d)
as lall,  (select date(time) as d, count(*) as c
from log where status != '200 OK' group by d)
as lbad where lbad.d = lall.d) as res where bad_day>1;
"""
# next works with float
"""select * from (select lbad.d, (100.0 * cast(lbad.c as float) / cast(lall.c as float)) as bad_day from (select date(time) as d,count(*) as c from log group by d) as lall,  (select date(time) as d, count(*) as c from log where status != '200 OK' group by d) as lbad where lbad.d = lall.d) as res where bad_day>1;
"""


if __name__ == "__main__":
    # TODO: Add parameter handling with helpii
    print(sys.argv, len(sys.argv) != 2)
    if (len(sys.argv) != 2) and (sys.argv[1] not in queries.keys()):
        print("Usage: python3 news.py {}".format(queries.keys))
    db = NewsDb(DB)
    articles = db.get_data(queries["get_most_popular_3"])

    for article in articles:
        print("\"{:s}\" - {:d} views".format(a.title, a.views))
