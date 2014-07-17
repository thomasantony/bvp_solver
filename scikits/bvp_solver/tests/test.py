### Small example file that shows the problem with relative error. Please not this BVP will not actually solve.

import scikits.bvp_solver
import numpy
import pylab
from scipy import special
def function (t,x):
    #dxdt=numpy.array([numpy.log(special.gamma(x[0])),1]) 
    dxdt=numpy.array([1e50*special.psi(x[0]),1])   
    return dxdt
def boundary_conditions(Begin,End):
    return numpy.array([Begin[0]-0]), numpy.array([End[0]-0])
def function_derivative( t, x):
    Deriv = numpy.array([[1e50*special.polygamma(1,x[0])     ,0       ],
                  [0      ,0      ]])
    return Deriv

problem=scikits.bvp_solver.ProblemDefinition(num_ODE=2,
                                             num_parameters=0,
                                             num_left_boundary_conditions = 1,
                                             boundary_points = (0,10),
                                             function=function,
                                             function_derivative = function_derivative,
                                             boundary_conditions= boundary_conditions)
solution=scikits.bvp_solver.solve(problem,
                                  solution_guess=[1,1],
                                  trace=1,
                                  max_subintervals = 100000)

A=numpy.linspace(0,10,10)
X=solution(A)
pylab.plot(A,X[0,:],'x')


