#!/usr/bin/python3

import sys
import news_queries
from newslib import QueryObj
from argparse import ArgumentParser


def list_queries(args):
    for q in news_queries.queries:
        print(q)


def print_query(args):
    print("Your query is: {}".format(args.query_name))
    if args.query_name not in news_queries.queries:
        print("No such a query, please provide one of the following:")
        list_queries(None)
    else:
        articles = news_queries.queries[args.query_name].get_data()
        for a in articles:
            print(a)


if __name__ == "__main__":

    args_parser = ArgumentParser(description="News log query engine")
    args_subparsers = args_parser.add_subparsers(help='commands')

    # list command
    list_parser = args_subparsers.add_parser('list', help='list queries')
    list_parser.set_defaults(func=list_queries)

    # query command
    query_parser = args_subparsers.add_parser('query', help='invoke query')
    query_parser.add_argument('query_name',
                              help="use list to get available queries")
    query_parser.set_defaults(func=print_query)

    args = args_parser.parse_args()
    args.func(args)
