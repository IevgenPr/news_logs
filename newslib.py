""" Interface to communicate with database"""

import psycopg2

DB = "news"


class NewsDb(object):
    """Class to work with News DB"""

    __instance = None

    @staticmethod
    def get_instance():
        """Create or get instance to DB object"""
        if NewsDb.__instance is None:
            NewsDb(dbname)
        return NewsDb.__instance

    def __init__(self, dbname):
        """ Somewhat private constructor """
        if NewsDb.__instance is not None:
            raise Exception("This is singletone class")
        else:
            NewsDb.__instance = self
        self.dbconn = psycopg2.connect("dbname={}".format(DB))

    def get_data(self, query):
        cursor = self.dbconn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def __del__(self):
        self.dbconn.close()


class QueryObj(object):

    def __init__(self, name, legend, title, desc, query):
        self.name = name
        self.title = title
        self.legend = legend
        self.desc = desc
        self.query = query

    def get_option(self):
        return (self.name, self.desc)

    def get_data(self):
        db = NewsDb(DB)
        return db.get_data(self.query)

    def get_title(self):
        return self.title

    def __str__(self):
        result = "{}\n".format(self.title)
        for (item, count) in self.get_data():
            result += "  {}  - {}{}\n".format(item, count, self.legend)
        return result
