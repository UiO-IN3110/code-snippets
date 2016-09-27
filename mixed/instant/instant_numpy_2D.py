import numpy
from instant import inline_with_numpy

# Example 2: two array, both inout and of same size
# Cannot avoid specifying all dimensions for both arrays
c_code = """
double sum (int x1, int y1, double* array1, int x2, int y2, double* array2){
  double tmp = 0.0;
  for (int i=0; i<x1; i++)
    for (int j=0; j<y1; j++){
      tmp = array1[i*y1 + j];
      array1[i*y1 + j] = array2[i*y1 + j];
      array2[i*y1 + j] = tmp;
    }
  return tmp;
}
"""

sum_func = inline_with_numpy(c_code, arrays = [['x1', 'y1', 'array1'],
                                               ['x2', 'y2', 'array2']],
                             cache_dir="test_ex2_cache")

a = numpy.ones(4)
a.shape = (2, 2)
b = a.copy()
a *= 2
print(sum_func(a, b))
