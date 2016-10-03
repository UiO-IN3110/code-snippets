#include <stdio.h>
#include <math.h>

#include "hw.h"

void hw1(double r1, double r2, double *s)
{
    *s = sin(r1 + r2);
}

void hw2(double r1, double r2)
{
    double s;
    s = sin(r1 + r2);
    printf("sin(%f+%f)=%f\n", r1, r2, s);
}
