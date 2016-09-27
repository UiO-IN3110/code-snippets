#Generate swig interface with:

swig -python -I.. hw.i

#Look at generated wrapper in hw_wrap.c


#Compile with:

gcc -I.. -fPIC $(pkg-config --cflags --libs python3) -c ../hw.c hw_wrap.c

gcc -shared -fPIC -o _hw.so hw.o hw_wrap.o
