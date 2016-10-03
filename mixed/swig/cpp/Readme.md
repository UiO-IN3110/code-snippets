# Run swig:

swig -python -c++ helloworld.i

# Compile with

g++ -std=c++0x -fPIC -O -c $(pkg-config --cflags --libs python3)\
         HelloWorld.cpp HelloWorld2.cpp helloworld_wrap.cxx
g++ -std=c++0x -shared -o _helloworld.so HelloWorld.o HelloWorld2.o helloworld_wrap.o

# Test new module
python test.py
