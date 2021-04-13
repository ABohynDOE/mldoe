# -*- coding: utf-8 -*-
"""
matrix
========
Module containing the matrix functions needed to create an array.
"""

# Package import
import numpy as np


def r_mat(r):
    """Create the basic factor matrix in 2^r runs.
    A 2^r by r matrix where each column represent a basic factor in 2^r runs.
    The columns are ordered such that ith columns is a repetition of (N/2^(r-i)) zeros and (N/2^(r-i)) ones.

    :param int r: number of basic factors
    :returns array mat: basic factors matrix"""
    vec = np.array(range(int(2 ** r)), dtype=np.uint8, ndmin=2)
    mat = np.unpackbits(vec, axis=0, bitorder='little', count=r)
    return np.array(mat[::-1].T, dtype=int)


def b_mat(r):
    """Create the full-interaction matrix for r basic factors.
    A 2^r by (2^r)-1 matrix with the 2^r-1 interactions of the columns representing the r basic factors.

    :param int r: number of basic factors
    :returns array mat: full interaction matrix"""
    vec = np.array(range(int(2 ** r)), dtype=np.uint8, ndmin=2)
    mat = np.unpackbits(vec, axis=0, bitorder='little', count=r)
    bf_mat = mat[::-1].T
    fi_mat = mat[:, 1:]
    return np.array((bf_mat@fi_mat) % 2, dtype=int)


def g_mat(r):
    """Create the reduced interaction matrix for r basic factors.
    A r by 2^r-1 matrix where each column represents an interaction and each row represents a basic factors.
    An entry of 1 means that the ith basic factor is used in the jth interaction.

    :param int r: number of basic factors
    :returns array mat: reduced interaction matrix"""
    vec = np.array(range(1, int(2**r)), dtype=np.uint8, ndmin=2)
    mat = np.unpackbits(vec, axis=0, bitorder='little', count=r)
    return np.array(mat, dtype=int)
