void sort_me(int A[], int n){
	int t;
	for(int i=0; i<n-1;++i){
		for(int j=0; j<n-i-1; ++j){
			if(A[j]<A[j+1]){
				t= A[j];
				A[j]= A[j+1];
				A[j+1]= t;
			}
		}
	}
}
void merge_us(int A[],int *pna,int B[],int nb){
	int na = *pna;
	for(int i=0;i<nb;++i){
		A[na+i] = B[i];
	}
	*pna+=nb;
}
#include<stdio.h>
int main(){
	int A[50],B[50],na,nb;
	printf("Size of array A : "); scanf("%d",&na);
	printf("A : ");
	for(int i=0;i<na;++i){
		scanf("%d",A+i);
	}
	printf("Size of array B : "); scanf("%d",&nb);
	printf("B : ");
	for(int i=0;i<nb;++i){
		scanf("%d",B+i);
	}
	merge_us(A,&na,B,nb);
	sort_me(A,na);
	printf("\nArray : ");
	for(int i=0;i<na;++i){
		printf("%d ",A[i]);
	}
	printf("\n");
	return 0;
}