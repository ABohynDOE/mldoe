=====
Usage
=====

Here is a code example:

The column are taken from the full-interaction matrix :math:`\mathbf{B}` that can be obtained
by multiplying the matrices :math:`\mathbf{R}` and :math:`\mathbf{G}`, taken from
the article of Xu [2009]_

.. [2009] Xu, H. (2009). Algorithmic construction of efficient fractional factorial designs with large run sizes. Technometrics, 51(3), 262-277.

..
    TODO: add explanation of the columns number of the pseudo-factor triplets

.. code-block:: python

    import mldoe

    # Generate a two-level design by specifying columns number
    D = mldoe.TLdesign(16,[1,2,4,8,6])

    # Print the design matrix
    print(D.array)

    # Compute its word-length pattern
    print(D.wlp())