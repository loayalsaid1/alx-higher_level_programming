#!/usr/bin/python3
"""
module to multiply 2 matrixes with numby
instead of making it manually
"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """ multiply two matrix with numpy """
    return numpy.dot(m_a, m_b)
