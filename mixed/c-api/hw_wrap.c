#include "Python.h"
#include "src/hw.h"

static PyObject *_wrap_hw1(PyObject *self, PyObject *args) {
  PyObject *resultobj;
  double arg1, arg2, result;

  PyArg_ParseTuple(args, (char *)"dd:hw1", &arg1, &arg2);

  hw1(arg1, arg2, &result);

  resultobj = PyFloat_FromDouble(result);
  return resultobj;
}

static PyMethodDef HwMethods[] = {
    {"hw1", _wrap_hw1, METH_VARARGS, "Hello world."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef hwmodule = {
   PyModuleDef_HEAD_INIT,
   "hw",   /* name of module */
   NULL,   /* module documentation, may be NULL */
   -1,     /* size of per-interpreter state of the module,
              or -1 if the module keeps state in global variables. */
   HwMethods
};


PyMODINIT_FUNC
PyInit_hw(void)
{
    return PyModule_Create(&hwmodule);
}
