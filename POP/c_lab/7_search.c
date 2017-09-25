#include<stdio.h>
int main(){
	char str[50],ch;
	printf("String : ");
	scanf("%[^\n]",str);
	scanf("%*c");
	printf("Char : ");
	scanf("%c",&ch);
	int count= 0, pos= -1;
	for(int i=0;str[i];++i){
		if(str[i]==ch){
			if(pos==-1){
				pos = i+1;
			}
			count++;
		}
	}
	if(pos==-1){
		printf("\n%c not found in string\n",ch);
		return 0;
	}
	printf("\nPosition of %c in string : %d",ch,pos);
	printf("\nRepeation of %c in string : %d\n",ch,count);
	return 0;
}