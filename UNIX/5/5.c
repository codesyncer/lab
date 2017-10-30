#include <unistd.h>
#include <stdio.h>
int makeChildren(int (*function1)(), int (*function2)()){
	pid_t pid1=fork();
	if(pid1<0)
		printf("\nCouldn't make 1st child");
	else if(pid1==0)
		return function1();
	else{
		pid_t pid2 = fork();
		if(pid2<0)
			printf("\nCouldn't make 2nd child");
		else if(pid2==0)
			return function2();
	}
	return 1;
}
int print(){
	printf("PrintFunction\n");
}
int foo(){
	printf("FooFunction\n");
}
int main(int argc, char const *argv[])
{	
	makeChildren(&foo, &print);
}