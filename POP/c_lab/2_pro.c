struct Product{
	char name[20];
	float unit_cost;
}products[10];
void input(Product *pro){
	printf("Name : "); 
	scanf("%[^\n]",pro->name); 
	scanf("%*c");
	printf("Unit cost : "); 
	scanf("%f",&pro->unit_cost); 
}
int main(){
	int n;
	printf("Enter number of products : ");
	scanf("%d",&n);
	prod = (Product**)malloc(sizeof(Product*));
	for(int i=0;i<n;++i){
		prod[i] = (Product*)malloc(sizeof(Product));
		prod[i]->input();
	}
}