#include<stdio.h>
#include<stdlib.h>
void quicksort(int A[],int p,int r);
int partition(int A[],int p,int r);
void main(int argc, char* argv[])
{
int i;char c[20];
int index=0;
int k;
int A[9000];
FILE *fp;
FILE *fout;
if (argc<2)
	printf("ERROR!Enter input file name at the command prompt\n");
else if (argc>2)
{
	fp=fopen(argv[1],"r");
	if (fp==NULL)
	{
		puts("cannot open file\n");
	}
	while (fgets(c,20,fp) != NULL)
	{
		i=atoi(c);
		A[index]=i;
		index++;
	}
}
fclose(fp);
quicksort(A,0,index-1);
fout=fopen(argv[2],"w");
for (k=0;k<index;k++)
{
	fprintf(fout,"%d\n",A[k]);
}
fclose(fout);	
}

void quicksort(int A[],int p, int r)
{
while (p<r)
{
	int q=(partition(A,p,r));
	quicksort(A,p,q-1);
	p=q+1;
}
}

int partition(int A[],int p,int r)
{
int x=A[r];
int i=p-1;
int j,temp;
for(j=p;j<r;j++)
{
	if (A[j]<=x)
	{
		i++;
		temp=A[j];
		A[j]=A[i];
		A[i]=temp;
	}
}
temp=A[i+1];
A[i+1]=A[r];
A[r]=temp;
return(i+1);
}
	
