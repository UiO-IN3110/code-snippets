#include "Python.h"
#include "src/hw.h"

static PyObject *_wrap_hw3(PyObject *self, PyObject *args) {
  PyObject *resultobj;
  double arg1, arg2, result;

  PyArg_ParseTuple(args, (char *)"dd:hw3", &arg1, &arg2);

  hw3(arg1, arg2, &result);

  resultobj = PyFloat_FromDouble(result);
  return resultobj;
}

static PyMethodDef HwMethods[] = {
    {"hw3", _wrap_hw3, METH_VARARGS, "Hello world."},
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
