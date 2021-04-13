# -*- coding: utf-8 -*-
"""
matrix
========
Module containing the matrix functions needed to create an array.
"""

# Package import
import numpy as np

# Matrix functions


def bmat(r: int) -> np.array:
    """
    Create the full-interaction matrix (B) for r basic factors.

    The B matrix is a :math:`2^r` by  :math:`2^r-1` matrix with the :math:`2^r-1` interactions of the columns
    representing the r basic factors.

    :param r: number of basic factors
    :type r: int
    :return: full-interaction matrix
    :rtype: numpy.array
    """
    vec = np.array(range(int(2 ** r)), dtype=np.uint8, ndmin=2)
    mat = np.unpackbits(vec, axis=0, bitorder='little', count=r)
    return np.array((mat[::-1].T @ mat[:, 1:]) % 2, dtype=int)


def rmat(r: int) -> np.array:
    """
    Create the basic factor matrix (R) for r basic factors.

    The R matrix is a :math:`2^r` by  :math:`r` matrix where each column represents a basic factor and each row
    represents a run. The columns are ordered such that ith columns is a repetition of :math:`2^{(r-i)}` zeros and
    :math:`2^{(r-i)}` ones.

    :param r: number of basic factors
    :return: basic factor matrix
    """
    vec = np.array(range(int(2 ** r)), dtype=np.uint8, ndmin=2)
    mat = np.unpackbits(vec, axis=0, bitorder='little', count=r)
    return np.array(mat[::-1].T, dtype=int)


def gmat(r: int) -> np.array:
    """
    Create the reduced interaction (G) matrix for r basic factors.

    The G matrix is a :math:`r` by  :math:`2^r-1` matrix where each column represents an interaction and each row
    represents a basic factor. An entry of 1 means that the i-th basic factor is used in the j-th interaction.

    :param r: number of basic factors
    :return: reduced interaction matrix
    """
    vec = np.array(range(1, int(2 ** r)), dtype=np.uint8, ndmin=2)
    mat = np.unpackbits(vec, axis=0, bitorder='little', count=r)
    return np.array(mat, dtype=int)
