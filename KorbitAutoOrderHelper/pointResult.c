#include <stdio.h>
#include <math.h>
#include <stdlib.h>
 
int main(int argc, char **argv){
    char operator;
    double num1, num2, result;
    if (argc != 3) {
      printf ("USAGE: enter \n");
      return 1;
    } 
	num1 = atof(argv[1]);// alternative strtod
	num2 = atof(argv[2]);//alternative strtod
	result = num1 / num2;
	printf("%5.9f",result);
}
