""" Queries that can be submitted to news.db"""

from newslib import QueryObj

queries = dict()


name1 = "get_most_popular_3"

title1 = "Most popular articles:"

legend1 = " views"

desc1 = """1. What are the most popunamelar three articles of all time?
Which articles have been accessed the most?
This information as a sorted list with
the most popular article at the top."""

query1 = """
        select a.title as title, count(l.id) as views
        from articles a left join log l
        on concat('/article/',a.slug) = l.path
        group by a.title order by views desc limit 3;"""

queries[name1] = QueryObj(name=name1, title=title1, desc=desc1,
                          legend=legend1, query=query1)


name2 = "get_popular_authors"

title2 = "Most popular authors:"

legend2 = " views"

desc2 = """2. Who are the most popular article authors of all time?
That is, when you sum up all of the articles each author has written,
which authors get the most page views?
Present this as a sorted list with the most popular author at the top."""

query2 = """
select a.name, count(l.id) as views
from (select au.name, ar.slug as arts
      from authors au, articles ar where au.id = ar.author) as a
left join log l
      on concat('/article/',a.arts) = l.path
group by a.name
order by views desc;
"""

queries[name2] = QueryObj(name=name2, title=title2, desc=desc2,
                          legend=legend2, query=query2)


name3 = "get_bad_days"

title3 = "Days with more than 1% errors:"

legend3 = "% errors"

desc3 = """ On which days did more than 1% of requests lead to errors
The log table includes a column status that indicates the HTTP status
code that the news site sent to the user's browser. (Refer to this
lesson for more information about the idea of HTTP status codes.)
"""

query3 = """
select * from
(select to_char(lbad.d :: date, 'Mon dd, yyyy'),
round( cast((100.0 * cast(lbad.c as float) / cast(lall.c as float))
as numeric),2) as bad_day from
(select date(time) as d, count(*) as c from log group by d) as lall,
(select date(time) as d, count(*) as c from log
where status != '200 OK' group by d) as lbad
where lbad.d = lall.d) as res where bad_day>1;
"""

queries[name3] = QueryObj(name=name3, title=title3, desc=desc3,
                          legend=legend3, query=query3)
