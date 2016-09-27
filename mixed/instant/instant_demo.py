from instant import inline
source = """
double hw1(double r1, double r2)
{
return sin(r1 + r2);
}
"""
hw1 = inline(source)
x= 1.0
y =2.5
print("sin({0}+{1}) = {2}".format(x,y,hw1(x,y)))
