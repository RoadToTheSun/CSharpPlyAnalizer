from cTreeParser import *
import os

s = '''
        bool a = true;
        int b ;
        /* comment 1

        */

        b = a + a * 10;;

        for (int i = 0; i < 5; i = i + 2)
            i = 0;

        while (true){
            if (a > b + 1 & x) {
                  // comment 2
                a = 0;
            }
            else
                if (8 > 9)
                    i = 1;
                else {
                    a=9;}

            a = 90;
        }

        do{
    
            a = a - b;
        } while (!a != (1 + 9) * b / 8);

    '''

s1 = '''public static class Main
        {
            int a = 0;
        }
         '''

with open("input.txt", 'r') as opened:
    cs_input = opened.read()

if __name__ == '__main__':
    print(*build_tree(s), sep=os.linesep)
