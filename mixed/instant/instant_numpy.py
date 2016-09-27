import numpy
from instant import inline_with_numpy
c_code = """
double sum (int n1, double* array1){
        double tmp = 0.0;
        for (int i=0; i<n1; i++) {
            tmp += array1[i];
        }
        return tmp;
    }
    """

sum_func = inline_with_numpy(c_code,  arrays = [['n1', 'array1']])
a = numpy.arange(10000000); a = numpy.sin(a)
sum_func(a)
