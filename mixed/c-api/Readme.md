
#Compile with:

```bash
gcc -Isrc -fPIC $(pkg-config --cflags --libs python3) -c src/hw.c hw_wrap.c
gcc -shared -fPIC -o hw.so hw.o hw_wrap.o
```

# Test with

```bash
python test.py
```
