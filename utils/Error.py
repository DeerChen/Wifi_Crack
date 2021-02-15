'''
Description:
Author: Senkita
Date: 2021-02-15 08:53:14
LastEditors: Senkita
LastEditTime: 2021-02-15 08:55:48
'''


class Error(Exception):
    def __init__(self, err):
        self.err = err

    def __repr__(self):
        return self.err
