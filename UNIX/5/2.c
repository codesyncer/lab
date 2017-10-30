#include <unistd.h>
#include <stdio.h>
void childRun(){
	for(char i='A';i<'F';++i){
		printf("%c", i);
	}
	printf("\n");
}
void main(int argc, char const *argv[])
{	
	printf("\nxStartinggggggggggggggggggg");
	pid_t myPid = fork();
	if(myPid<0)
		printf("\nCouldn't create child");
	else if(myPid==0){
		printf("Starting Child : ");
		return childRun();
	}
	for(int i=0;i<400;++i){
		if(!(i%10))
			printf("\n");
		printf("%d", i%10);
	}
	printf("\n");
}