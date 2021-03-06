
import sys
import numpy as np
import pressiotools.linalg as ptla

np.set_printoptions(linewidth=140)

def run(comm):
  '''
  this demo shows how to compute the parallel QR factorization
  over N ranks of a block-row distributed random matrix A.

  Suppose A is a 100x5 matrix such that it is
  block-row distributed over multiple MPI ranks.

  For example, suppose have 4 ranks:

       0     j        4
  i=0  ----------------
          rank=0
  24   ----------------
          rank=1
  49   ----------------
          rank=2
  74   ----------------
          rank=3
  i=99 ----------------

  Each rank owns 25 rows and all columns of A.
  '''
  rank = comm.Get_rank()

  # fix seed for reproducibility
  np.random.seed(312367)

  # create the local piece for each rank:
  # here for simplicity we use random numbers, but one can
  # fill each piece by reading a file or some other way.
  # Note: the layout MUST be fortran such that
  # pressiotools can view it without copying data.
  # This is important to reduced the memory footprint
  # especially for large matrices.
  myLocalRandPiece = np.asfortranarray(np.random.rand(25,5))

  # use the local piece to create a distributed multivector
  # the multivector is an abstraction that allows us
  # to easily perform all the computations behind the scenes
  # in native C++ without performance hit
  A = ptla.MultiVector(myLocalRandPiece)

  # construct a Tsqr object
  qrO = ptla.Tsqr()
  # comptue the QR factorization of A
  qrO.computeThinOutOfPlace(A)

  # the R factor (5x5 upper tridiagonal matrix) is replicated on all ranks
  # R is a numpy array that you can use as you want.
  # Note that R is owned by the qr object.
  R = qrO.viewR()

  # the Q matrix is block-row distributed in the same way A is
  # so viewing the LocalQ here means that you only access
  # the rows of Q that belong to this rank
  # Q is a numpy array that you can use as needed.
  # Note that Q is owned by the qr object.
  Q = qrO.viewQLocal()
  print("Rank = {}, Q.shape = {}, R.shape = {}".format(rank, Q.shape, R.shape))

  if rank==0: print("R = {}".format(R))

  # note: the above methods are called "view" because NO copy is made


if __name__ == '__main__':
  '''
  run with:  mpirun -np 4 python3 qr.py
  '''
  from mpi4py import MPI
  comm = MPI.COMM_WORLD
  if (comm.Get_size() != 4):
    print("Rerun with 4 ranks")
    sys.exit()

  run(comm)
