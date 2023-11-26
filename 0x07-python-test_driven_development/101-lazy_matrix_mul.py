#!/usr/bin/python3

"""
This module includes a function for matrix multiplication
of two metrics using NumPy.

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices

    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix

    Returns:
        list of lists: The result of multipling the two matrices
    """

    return (np.matmul(m_a, m_b))
