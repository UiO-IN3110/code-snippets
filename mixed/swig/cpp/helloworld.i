/* file: helloworld.i */
%module helloworld
%{
/* include C++ header files necessary to compile the interface */
#include "src/HelloWorld.h"
#include "src/HelloWorld2.h"
%}

%include "src/HelloWorld.h"

%include "typemaps.i"
%apply double* OUTPUT { double& s_ }
%include "src/HelloWorld2.h"

%extend HelloWorld {
    void print_() { self->message(std::cout); }
    }
