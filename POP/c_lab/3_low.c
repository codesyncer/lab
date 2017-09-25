#include<stdio.h>
int main(){
	int mat[10][10];
	int r,c;
	printf("Row size and column size : ");
	scanf("%d %d",&r,&c);
	printf("Matrix\n\n");
	for(int i=0;i<r;++i){
		printf(" ");
		for(int j=0;j<c;++j){
			scanf("%d",&mat[i][j]);
		}
	}
	printf("\nLower triangle\n");
	for(int i=0;i<r;++i){
		for(int j=0;j<c;++j){
			if(j>=i){
				printf("\n");
				break;
			}
			printf(" %d", mat[i][j]);
		}
	}
	return 0;
}