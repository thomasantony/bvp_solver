.. currentmodule:: scikits.bvp_solver

Welcome
=====================================

:mod:`scikits.bvp_solver` is a python package for solving two point boundary value problems which is based on a modified version of the `BVP_SOLVER <http://cs.stmarys.ca/~muir/BVP_SOLVER_Webpage.shtml>`_ Fortran package. If you have any questions, comments or suggestions about this tutorial, the examples or bvp_solver itself, please e-mail them to the mailing list or to me at jsalvati@u.washington.edu.

To join the mailing list send an e-mail to scikits-bvp_solver+subscribe@googlegroups.com

Installing and learning to use :mod:`scikits.bvp_solver`
--------------------------------------------------------
:mod:`scikits.bvp_solver` is available through `PyPi <http://pypi.python.org/pypi/scikits.bvp_solver>`_. The easiest way to learn how to install and use :mod:`scikits.bvp_solver` is to read the :doc:`tutorial <tutorial>`. It is also helpful to look at the :doc:`examples <examples/examples>`, and to read about the :doc:`template generator <scikits.bvp_solver.get_template>`, which will generate a code skeleton for a boundary value problem which can then be filled in. Using the template generator reduces the busywork of solving a boundary value problem. 

Documentation
-------------

.. toctree::
   :maxdepth: 1

   tutorial
   examples/examples
   core

The `BVP_SOLVER webpage <http://cs.stmarys.ca/~muir/BVP_SOLVER_Webpage.shtml>`_ has several more Fortran examples which should translate easily as well as a `paper <http://cs.stmarys.ca/~muir/JNAIAM_Shampine_Muir_Xu2006.pdf>`_ on the solver which describes its usage and capabilities in greater detail.  

Source
------
The source can be found on GitHub `here <https://github.com/jsalvatier/scikits.bvp_solver>`_.

Compilation Help
-----------------
:mod:`scikits.bvp_solver` requires the gfortran compiler; it may work with other f90 compilers, but this has not been tested.

Compiling on Windows
---------------------
To install on Windows (tested on Windows 7):

#. Get MinGW with gfortran `here <http://www.equation.com/servlet/equation.cmd?fa=fortran>`_

#. Compile from source using ``python setup.py config --compiler=mingw32 build --compiler=mingw32 install``

Changes to BVP_SOLVER
---------------------
The modified version of the BVP_SOLVER package replaces the linear system solver COLROW (`Díaz, G. Fairweather, and P. Keast, 1983 <http://dl.acm.org/citation.cfm?id=356054>`_) with a related  linear system solver `LAMPAK <http://www.mscs.dal.ca/~keast/research/leq/lampak.f>`_. This modified version of BVP_SOLVER is BSD licsense compatible. COLROW employs row elimination with row pivoting alternated with column elimination with column pivoting to avoid fill-in in the structured matrices that arise. LAMPAK employs alternate row and column interchanges (i.e., pivoting) to avoid fill-in but performs only row elimination to reduce the matrices. The authors report that LAMPAK gives essentially the same results as COLROW in all the numerical experiments they considered.

Acknowledgments
---------------
Many thanks to Lawrence Shampine, Paul Muir, and H. Xu for writing the original Fortran software, BVP_SOLVER. Additional thanks to Paul Muir for the development of a BSD compliant version of BVP_SOLVER and for consultation during the development of  the Python wrapper for BVP_SOLVER.

Bug Reports
----------
Please make bug reports on GitHub `here <https://github.com/jsalvatier/scikits.bvp_solver/issues>`_. 
