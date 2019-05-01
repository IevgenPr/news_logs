""" Interface to communicate with database"""

import psycopg2


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
        results = cursor.fetchall()
        return results

    def __del__(self):
        self.dbconn.close()
