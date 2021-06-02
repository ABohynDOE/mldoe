mldoe module
=============

Design classes
--------------

This section describes the two main classes of the module:

* Two-Level Design class (TLD)
* Mixed-Level Design class (MLD)

In both classes the design is defined by its run size (it must be a power of two) and the numbers of the columns used
for its factors.

Each column numbers uniquely defines a generator, by the factors it used.
Powers of two are independent factors while other numbers are combinations of independent factors.
To known which factor are used in a generator, simply decompose it into powers of 2.
For example :math:`7=3+2+1` so the generator represented by column 7 is composed of the independent factors 1, 2 and 3, and we can write :math:`7=123`.
All the possible generators formed by :math:`r` basic factors can be summarized by the :math:`r \times 2^{r}-1` matrix called the **reduced design matrix**.
Below is the reduced design matrix for four basic factors.

.. math::

    \begin{array}{l|cccccccc}
     & \mathbf{1} & \mathbf{2} & 3 & \mathbf{4} & 5 & 6 & 7 & \mathbf{8} \\
    \hline
    a & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 \\
    b & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 \\
    c & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 0 \\
    d & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
    \end{array}


Here is how we create a four-level factor

.. math::

    \begin{array}{rrrrcr}
    a & b & ab & & A \ \
    \hline
    0 & 0 & 0 & \rightarrow & 0 \ \
    0 & 1 & 1 & \rightarrow & 1 \ \
    1 & 0 & 1 & \rightarrow & 2 \ \
    1 & 1 & 0 & \rightarrow & 3
    \end{array}

.. TODO: refactor the explanation of columns more correctly and clearly

.. TODO: add explanation for the type-specific WLP matrix and for the type of words.

.. automodule:: src.mldoe.design
    :members:
    :undoc-members:
    :show-inheritance:

Matrix functions
----------------

.. automodule:: src.mldoe.matrix
    :members:
    :undoc-members:
    :show-inheritance:

Tools functions
---------------

.. automodule:: src.mldoe.tools
    :members:
    :undoc-members:
    :show-inheritance:

References
----------
.. [2009] Xu, H. (2009). Algorithmic construction of efficient fractional factorial designs with large run sizes. Technometrics, 51(3), 262-277.
.. [1989] Wu, C. F. J. (1989). Construction of 2m4 n designs via a grouping scheme. The Annals of Statistics, 1880-1885.