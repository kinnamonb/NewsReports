#!/usr/bin/env python

import psycopg2

# Open a connection to the database and get the cursor
DBNAME = "news"
db = psycopg2.connect(database=DBNAME)
cursor = db.cursor()

# 1. Most popular three articles of all time
# Get the most popular articles based upon views
sql = '''select articles.title, count(log.path) as num from articles, log
         where log.path like '%' || articles.slug
         group by articles.title
         order by num desc
         limit 3;
'''
cursor.execute(sql)
popular_articles = cursor.fetchall()
# Print out a message to the user
print "The most popular articles are:"
num = 1
for article in popular_articles:
    print "\t%i.) %s (%i views)" % (num, article[0], article[1])
    num += 1

# 2. Most popular authors of all time
# Get the most popular authors based upon views
sql = '''select authors.name, author_views.views
            from authors,
            (select articles.author, count(log.path) as views
                from articles, log
                where log.path = '/article/' || articles.slug
                group by articles.author) as author_views
         where author_views.author = authors.id
         order by author_views.views desc;
'''
cursor.execute(sql)
popular_authors = cursor.fetchall()

# Print out the most popular authors
print "The most popular authors are:"
num = 1
for author in popular_authors:
    print "\t%i.) %s (%i views)" % (num, author[0], author[1])
    num += 1

# 3. Days with more than 1% error rate
# Get the list of days with more than a 1% error rate
sql = '''select * from
            (select total_visits.day,
            (errors.num::real / total_visits.total::real) as percent
            from total_visits, errors
            where total_visits.day = errors.day) as percents
         where percents.percent > 0.01;
'''
cursor.execute(sql)
high_error_days = cursor.fetchall()

# Print out the days with over 1% error rate
print "The days with over a 1% error rate:"
num = 1
for day in high_error_days:
    print "\t%i.) %s (%.2f%%)" % (num, day[0], day[1]*100)
    num += 1
