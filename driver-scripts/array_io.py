import pathlib, sys
file_path = pathlib.Path(__file__).parent.absolute()
sys.path.append(str(file_path) + "/../..")

import numpy as np
from mpi4py import MPI
import pressiotools as pt
import math

# Binary IO
def read_binary_array(fileName,nCols):
  # read a numpy array from a binary file "fileName".bin
  if nCols==1:
    return np.fromfile(fileName)
  else:
    array = np.fromfile(fileName)
    nRows = int(len(array) / float(nCols))
    return array.reshape((nCols,nRows)).T

def write_binary_array(arr,fileName):
  # write numpy array arr to a binary file "fileName"
  f = open(fileName,'w')
  arr.T.tofile(f)
  f.close()

# Ascii IO
def read_ascii_array(fileName,nCols):
  # read a numpy array from an ascii file "fileName"
  return np.asfortranarray(np.loadtxt(fileName))

def write_ascii_array(arr,fileName):
  # write numpy array arr to an ascii file "fileName"
  np.savetxt(fileName,arr)

# Optional IO
def read_array(fileName,nCols,isBinary=True):
  if isBinary:
    return read_binary_array(fileName,nCols)
  else:
    return read_ascii_array(fileName,nCols)

def write_array(arr,fileName,isBinary=True):
  if isBinary:
    return write_binary_array(arr,fileName)
  else:
    return write_ascii_array(arr,fileName)

# Distributed IO
def read_array_distributed(fileName,nCols,isBinary=True):
  # Read an array from binary  or ascii files with the name specified by the string fileName
  # Each local array segment will be written to a file fileName.XX.YY, 
  # where XX is the number of ranks and YY is the local rank
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  size = comm.Get_size()

  nDigit = int(math.log10(size)) + 1

  # write array portion on each processor
  myFileName = "{}.{}.{:0{width}d}".format(fileName,size,rank,width=nDigit)
  myArr = read_array(myFileName,nCols,isBinary)
  
  if nCols==1:
    return pt.Vector(myArr)    
  else:
    return pt.MultiVector(myArr)

def write_array_distributed(arr,fileName,isBinary=True):
  # Write array arr to binary or ascii files with the name specified by the string fileName
  # Each local array segment will be written to a file fileName.XX.YY, 
  # where XX is the number of ranks and YY is the local rank
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  size = comm.Get_size()

  nDigit = int(math.log10(size)) + 1

  # write BaseVector portion on each processor
  myFileName = "{}.{}.{:0{width}d}".format(fileName,size,rank,width=nDigit)
  myArr = arr.data()
  write_array(myArr,myFileName,isBinary)
