#include <unistd.h>
#include <stdio.h>
int makeChildren(int (*function1)(), int (*function2)()){
	pid_t pid1=fork(),pid2;
	if(pid1<0){
		printf("\nCouldn't make 1st child");
		return -1;
	}
	else if(pid1==0)
		return function1();
	else{
		pid2 = fork();
		if(pid2<0){
			printf("\nCouldn't make 2nd child");
			return -1;
		}
		else if(pid2==0)
			return function2();
	}
	printf("pids: %d, %d", pid1, pid2);
	return 1;
}
int print(){
	printf("\nPrintFunction");
}
int foo(){
	printf("\nFooFunction");
}
int main(int argc, char const *argv[])
{	
	makeChildren(foo, print);
	printf("\n");
}