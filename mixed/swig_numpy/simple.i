%module simple
%{
  #define SWIG_FILE_WITH_INIT
  #include "simple.h"
%}

%include "numpy.i"
%init %{
import_array();
%}

%apply (int DIM1, double* IN_ARRAY1) {(int n, double *a), (int m, double *b)};
%apply (int DIM1, double* ARGOUT_ARRAY1) {(int size, double *arr)};
%include "simple.h"
