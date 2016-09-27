#Generate swig interface with:

swig -python -I.. hw.i

#Look at generated wrapper in hw_wrap.c


#Compile with:

gcc -I.. -fPIC -I/usr/include/python3.5 -c ../hw.c hw_wrap.c

gcc -shared -fPIC -o _hw.so hw.o hw_wrap.o
