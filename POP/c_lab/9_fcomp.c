#include<stdio.h>
int f_comp(FILE *f1,FILE *f2){
	char ch1,ch2;
	ch1 = fgetc(f1);
	ch2 = fgetc(f2);
	while(ch1==ch2 && ch1!=EOF && ch2!=EOF){
		ch1 = fgetc(f1);
		ch2 = fgetc(f2);
	}
	ch1 = ch1==EOF?0:ch1;
	ch2 = ch2==EOF?0:ch2;
	return ch1-ch2;
}
int main(){
	FILE *f1,*f2;
	f1 = fopen("one","r");
	f2 = fopen("two","r");
	if(f1==NULL || f2==NULL){
		printf("File not found");
		return 1;
	}
	int res = f_comp(f1,f2);
	printf("fcomp('one','two') : %d\n",res);
	printf("'one' %c 'two'\n",res==0?'=':res<0?'<':'>');
	return 0;
}