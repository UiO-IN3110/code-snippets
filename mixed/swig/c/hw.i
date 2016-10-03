/* file: hw.i */
%module hw
%{
/* Everything in the %{ }% block will be copied in the wrapper file.
   Here, we include C header files necessary to compile the interface
*/
#include "hw.h"
%}

%include "typemaps.i"

/* list functions to be interfaced: */
void hw1(double r1, double r2, double *OUTPUT); /* OUTPUT indicates an return variable */

/* Alternative: */
/* %apply double *OUTPUT { double* s }  */ /* apply rule that defines the argument *s as an output variable */
/* void hw1(double r1, double r2, double *s); */

void hw2(double r1, double r2);
