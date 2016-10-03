#ifndef HELLOWORLD_H_
#define HELLOWORLD_H_

#include <iostream>

class HelloWorld
{
public:
    HelloWorld();
    ~HelloWorld();
 
    void set(double r1, double r2);
    inline double get() const { return s; }
    void message(std::ostream& out) const;

protected:
    double r1, r2, s;
    void compute();    // compute s=sin(r1+r2)
};

std::ostream& operator<<(std::ostream& out, const HelloWorld& hw);

#endif // HELLOWORLD_H_
