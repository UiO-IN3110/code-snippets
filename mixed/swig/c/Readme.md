#Generate swig interface with:

swig -python -Isrc hw.i

#Look at generated wrapper in hw_wrap.c


#Compile with:

gcc -Isrc -fPIC $(pkg-config --cflags --libs python3) -c src/hw.c hw_wrap.c

gcc -shared -fPIC -o _hw.so hw.o hw_wrap.o
