#include <unistd.h>
#include <stdio.h>
void childRun(){
	for(char i='A';i<'F';++i)
		printf("%c", i);
	printf("\n");
}
void main(int argc, char const *argv[])
{	
	printf("\nBefore fork() 1");
	printf("\nBefore fork() 2");
	// fflush(stdout);
	pid_t myPid = fork();
	if(myPid<0)
		printf("\nCouldn't create child");
	else if(myPid==0){
		printf("\nStarting Child : ");
		return childRun();
	}
	for(int i=0;i<400;++i){
		if(!(i%10))
			printf("\n%d: ", i);
		printf("%d", i%10);	
	}
	printf("\n");
}