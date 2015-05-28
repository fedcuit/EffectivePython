from collections import namedtuple

__author__ = 'edfeng'
# the problem with all the ways above to achieve enum in python is that:
# value can be duplicated and can take part in meaningless operation

# 1. use collections.namedtuple to define enum in python

Season = namedtuple("Season", "Spring Summer Autumn Winter")._make(range(4))
# _make method use fieldnames and the passed in iterable to build a list of tuple
if __name__ == '__main__':
    print Season.Summer

# 2. use class member to define enum in python


class Gender(object):
    MALE = 0
    FEMALE = 1


# 3. more concise way to define enum using class member


class Title(object):
    MR, MRS, MISS = range(3)