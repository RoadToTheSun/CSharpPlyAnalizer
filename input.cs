class Program
    {
        static void Main()
        {
            Box box = new Box(); //default constructor
            Function( box);
        }
        private static void Function( Box box)
        {
            Console.WriteLine(box);

            double a, b, c;
            Console.WriteLine("Enter parameters for new box:");
            Console.Write("a=");
            a = Convert.ToDouble(Console.ReadLine());
            Console.Write("b=");
            b = Convert.ToDouble(Console.ReadLine());
            Console.Write("c=");
            c = Convert.ToDouble(Console.ReadLine());

            for (var i = 0; i < 5; i++, a++)
            {
                Box temp = new Box(a, b, c);
                temp.SetA(a+10);
                temp.SetB(a-10);
                temp.SetC(b+15);
                b++;
                c++;
                Console.Write("Volume of temp" + temp + "=" + temp.GetVolume());
                Console.WriteLine("; S of surface of temp" + temp + "=" + temp.GetSurface());
            }


            /* a=-123;
             Box
             before
             "while"
              loop*/
            Box before = new Box(a, b, c);
            Console.WriteLine("Before loop: " + before);

            int count = 5;
            while (count-- > 0)
            {
                if (a < b)
                {
                    a += b - a + 1;
                    before.SetA(a);
                }
                else if (b < a)
                {
                    b += a - b + 1;
                    before.SetB(b);
                }

                if (a < b && b < c)
                {
                    while (b <= c)
                    {
                        b += 1;
                        before.SetB(b);
                    }
                }
                else if (b < a || c > 10)
                {
                    // return;
                }
            }

            ref Box after = ref before; // i don`t know about "ref"
            Console.WriteLine("After loop: " + after); // after changes
        }
    }

    class Box
    {
        private double _a;
        private double _b;
        private double _c;
        private static int _counter;

        public Box()
        {
            _counter++;
        }

        public Box(double a, double b, double c)
        {
            _a = a;
            _b = b;
            _c = c;
            _counter++;
        }

        public double GetA()
        {
            return _a;
        }

        public double GetB()
        {
            return _b;
        }

        public double GetC()
        {
            return _c;
        }

        public void SetA(double a)
        {
            _a = a;
        }

        public void SetB(double b)
        {
            _b = b;
        }

        public void SetC(double c)
        {
            _c = c;
        }

        public double GetVolume()
        {
            return _a * _b * _c;
        }

        public double GetSurface()
        {
            return 2 * (_a * _b + _a * _c + _b * _c);
        }

        public override string ToString()
        {
            var s = "Box(" + _a + ", " + _b + ", " + _c+")";
            return s;
        }

        public override int GetHashCode()
        {
            return _counter;
        }

        public static int GetCounter()
        {
            return _counter;
        }
    }
