import psycopg2

query1 = '''select articles.title, count(*) as num_views 
         from articles inner join log on log.path = concat('/article/', articles.slug)
         group by articles.title
         order by num_views desc
         limit 3;'''

query2 = '''select authors.name, count(*) as num_views
         from authors
         join articles on authors.id = articles.author
         join log on log.path = concat('/article/', articles.slug)
         group by authors.name
         order by num_views desc;'''

query3 = '''select sum_table.day, (errors::float/sum::float)*100 as percentage
         from
            (select count(*) as errors, date(time) as day
            from log
            where status = '404 NOT FOUND' 
            group by day) as errors_table
            join
            (select count(*) as sum, date(time) as day
            from log
            group by day) as sum_table
            on errors_table.day = sum_table.day
         where (errors::float/sum::float)*100 > 1;'''

tasks= ["What are the most popular articles? (In number of views)", "Who are the most popular writers? (In number of views)",
        "On which days did more than 1% of requests lead to errors?"]

queries = [query1, query2, query3]


# create a function to connect to the database
# it returns a cursor
def connect_to_db():
    try:
        print("Connecting to the database...")
        # connect to the database
        db = psycopg2.connect("dbname= news")
        # create cursor
        cur = db.cursor()
        return cur
    except Exception:
        print("Error while connection to the database!")


# fetch the result of the first query
# "What are the most popular articles?"
def popular_articles(query1):
    cur = connect_to_db()
    # execute the query
    cur.execute(query1)
    # get and return the result
    result = cur.fetchall()
    return result

# fetch the result of the second query
# "Who are the most popular writers?"
def popular_writers(query2):
    cur = connect_to_db()
    cur.execute(query2)
    result = cur.fetchall()
    return result


# fetch the result of the third query
# "On which days did more than 1% of requests lead to errors?"
def error_requests(query3):
    cur = connect_to_db()
    cur.execute(query3)
    result = cur.fetchall()
    return result


# a function to execute all the queries
def execute_queries(query):
    cur = connect_to_db()
    cur.execute(query)
    result = cur.fetchall()
    return result


# print the results to the console
def print_results():
    print("=======================================")
    # loop through the queries and tasks
    # print the result and task for every query
    for query, task in zip(queries, tasks):
        result = execute_queries(query)
        print(task)
        for col in result:
            print("\t*" + str(col[0]) + " ===> " + str(col[1]))
        print("=======================================")

# popular_articles(query1)
print_results()
