/* hw.i */
%module hw
%{
#include "hw.h"
%}

%include "typemaps.i"

/* list functions to be interfaced: */
/*void hw3(double r1, double r2, double *s);*/

/*void hw3(double r1, double r2, double *OUTPUT);*/

%apply double *OUTPUT { double* s }
void hw3(double r1, double r2, double *s);


