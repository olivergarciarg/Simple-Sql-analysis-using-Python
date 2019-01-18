#!/usr/bin/env python3
"""This code executes 3 queries and prints the results."""

import psycopg2

database_name = "news"


def run_query(sql_string):
    """Connect to database."""
    db = psycopg2.connect('dbname=' + database_name)
    db_cursor = db.cursor()
    """Runs the query"""
    db_cursor.execute(sql_string)
    """Stores query results in rows"""
    rows = db_cursor.fetchall()
    """Close database connection"""
    db.close()
    return rows


def popular_articles():
    """Find the top 3 most popular articles."""
    sql_string = """
        SELECT
            articles.title,
            count(log.id) AS view_count
        FROM articles
            LEFT JOIN log
                ON log.path LIKE '%' || articles.slug || '%'
        GROUP BY
            articles.title
        ORDER BY
            view_count desc
        LIMIT 3;
    """

    """Run query and show results"""
    articles = run_query(sql_string)
    print('\nMost popular articles:')
    for i in articles:
        print("Article " + i[0] + " has " + str(i[1]) + " views")


def authors_popularity():
    """Sort the authors from most read to least read."""
    sql_string = """
        SELECT
            authors.name,
            count(log.id) AS view_count
        FROM (authors LEFT JOIN articles
            ON authors.id = articles.author)
            LEFT JOIN log
            ON log.path LIKE '%' || articles.slug || '%'
        GROUP BY
            authors.name
        ORDER BY
            view_count DESC;
    """

    """Run query and show results"""
    authors = run_query(sql_string)
    print('\nAuthor popularity:')
    for i in authors:
        print("Author " + i[0] + " has " + str(i[1]) + " views")


def high_error_dates():
    """Find dates with more than 1% of errors."""
    sql_string = """
        SELECT * FROM
            (SELECT
                time::date AS my_date,
                100.0*sum(CASE
                            WHEN status = '200 OK' THEN 0
                            ELSE 1
                        END)/count(status) AS error_percentage
            FROM log
            GROUP BY
                my_date) subquery1
        WHERE error_percentage > 1;
    """

    """Run query and show results"""
    high_error_date = run_query(sql_string)
    print('\nDates with more than 1% error rate:')
    for i in high_error_date:
        days = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1], 1))
        print(days + " has " + errors + "% error rate")


popular_articles()
authors_popularity()
high_error_dates()
print('\n')
