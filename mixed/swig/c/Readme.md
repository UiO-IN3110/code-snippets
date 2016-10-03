Building with distutils
-----------------------

```bash
python setup.py build_ext
```

Test with

```bash
python test.py
```


Building manually
-----------------

#Generate swig interface with:

```bash
swig -python -Isrc hw.i
```

#Look at generated wrapper in hw_wrap.c


#Compile with:

```bash
gcc -Isrc -fPIC $(pkg-config --cflags --libs python3) -c src/hw.c hw_wrap.c
gcc -shared -fPIC -o _hw.so hw.o hw_wrap.o
```
