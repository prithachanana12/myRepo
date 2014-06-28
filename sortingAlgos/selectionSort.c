/*program for sorting a file containing up to 500 elements*/
#include<stdio.h>
#include<stdlib.h>
void main()
{
FILE *fp;
int i;
int p=0;int count=0;int j;int k;int smallest;int temp;
int final[500];
int unsorted[count];
char c[20];
fp=fopen("input.txt","r");
if (fp==NULL){
puts("cannot open file");
}
while (fgets(c,19,fp) != NULL){
i=atoi (c);
final[p]=i;
p++;count++;
}
fclose(fp);
/*for(p=0;p<count;p++){
printf("%d\t",final[p]);
}*/
for(j=0;j<count;j++){
unsorted[j]=final[j];
}
/*for(j=0;j<count;j++){
printf("\n%d\n",unsorted[j]);
}*/
for(j=0;j<count;j++)
{
smallest=j;
for(k=j+1;k<count;k++)
{
if (unsorted[k]<unsorted[j])
{
smallest=k;
temp=unsorted[j];
unsorted[j]=unsorted[k];
unsorted[k]=temp;
}}}
/*for(j=0;j<count;j++){
printf("\t%d\t",unsorted[j]);
}*/
fp=fopen("output.txt","w");
for(j=0;j<count;j++){
fprintf(fp, "%d\n",unsorted[j]);
}
fclose(fp);
}
