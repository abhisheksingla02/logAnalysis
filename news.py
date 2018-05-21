 #!/usr/bin/env python2.7
# Database library has been imported
import psycopg2
# The news database has been included
DBNAME = "news"


# Function created for query 1
def database_query():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select articles.title,log_output.count from log_output inner join articles on log_output.article=articles.slug limit 3")  # NOQA
    result = c.fetchall()
    print("Q-1: What are the most popular 3 articles of all time?\n")
    for val in result:
        # The output has been formatted to get the desired output on the screen
        print('"{p[0]}"- {p[1]} views\n'.format(p=val))
    db.commit()
    db.close()


# Function created for query 2
def database_query2():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select authors.name,articles_log.sum from authors inner join articles_log on authors.id=articles_log.author;")  # NOQA
    result = c.fetchall()
    print("Q-2:Who are the most popular article authors of all time?\n")
    for val in result:
        # The output has been formatted to get the desired output on the screen
        print('{p[0]}- {p[1]} views\n'.format(p=val))
    db.commit()
    db.close()


# Function created for query 3
def database_query3():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select date,error from results where error >1;")
    result = c.fetchall()
    print("Q-3: On which day did more than 1% of requests lead to errors?\n")
    for val in result:
        # The output has been formatted to get the desired output on the screen
        print('{p[0]}- {p[1]} %errors\n'.format(p=val))
    db.commit()
    db.close()
# Respective functions have been called
database_query()
database_query2()
database_query3()
