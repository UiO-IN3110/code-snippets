swig -python -Isrc hw.i

gcc -Isrc -fPIC $(pkg-config --cflags --libs python3) -c src/hw.c hw_wrap.c
gcc -shared -fPIC -o _hw.so hw.o hw_wrap.o

python -c "import hw" # test
