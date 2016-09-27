class HelloWorld
{
    protected:
        double r1, r2, s;
        void compute();  // compute s=sin(r1+r2)
    public:
        HelloWorld();
        ~HelloWorld();

        void set(double r1, double r2);
        double get() const { return s; }
        void message(std::ostream& out) const;
};
