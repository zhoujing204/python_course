import os

class UnixFS:

    @staticmethod
    def rm(filename):
        os.remove(filename)