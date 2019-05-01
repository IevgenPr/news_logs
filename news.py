#!/usr/bin/python3
#""" Main News log."""

import sys
import news_queries
from newslib import QueryObj
from argparse import ArgumentParser

def list_queries(args):
    for q in news_queries.queries:
        print(q)

def print_query(args):
    print(args.query_name)
    articles = news_queries.queries[args.query_name].get_data()
    for a in articles:
        print(a)
        #print("\"{:s}\" - {:d} views".format(a.title, a.views))

if __name__ == "__main__":

    args_parser = ArgumentParser(description="News log query engine")
    args_subparsers = args_parser.add_subparsers(help='commands')

    # list command
    list_parser = args_subparsers.add_parser('list', help='list queries')
    list_parser.set_defaults(func=list_queries)

    # query command
    query_parser = args_subparsers.add_parser('query',help='invoke query')
    query_parser.add_argument('query_name', 
            help="use list to get list of available queries")
    query_parser.set_defaults(func=print_query)
    
    args = args_parser.parse_args()
    args.func(args)

