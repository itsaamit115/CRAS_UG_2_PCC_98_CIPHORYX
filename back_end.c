#include "cras.h"
//cras system pbl project by amitsingh,sarthaksingh,krishnauniyal.
void addre(int id,char nam[]){
FILE *fp=fopen("source.dat","ab");
FILE *out=fopen("output.txt","w");
if(fp==NULL){fprintf(out,"fahhhhh!!!! file error\n"); fclose(out); return;}
struct res r;r.id=id;strcpy(r.naam,nam);r.inuse=0;fwrite(&r,sizeof(r),1,fp);
fprintf(out,"resource added successfully\n");
fclose(fp); fclose(out);}
void viewresre(){
FILE *fp=fopen("source.dat","rb");
FILE *out=fopen("output.txt","w");struct res r;
if(fp==NULL){fprintf(out,"no resources\n"); fclose(out); return;}
fprintf(out,"id\tname\tresource status\n");
while(fread(&r,sizeof(r),1,fp)){
fprintf(out,"%d\t%s\t\t%s\n",r.id,r.naam,r.inuse?"Allocated":"Available");}
fclose(fp); fclose(out);}
void allocre(int id,char usern[],char userole[]){
FILE *fp=fopen("source.dat","rb+");
FILE *afp=fopen("inuse.dat","ab");
FILE *out=fopen("output.txt","w");
struct res r; int fo=0;
if(fp==NULL){fprintf(out,"NO FILE\n"); fclose(out); return;}
while(fread(&r,sizeof(r),1,fp)){
if(r.id==id){fo=1;if(r.inuse==0){r.inuse=1;
fseek(fp,-sizeof(r),SEEK_CUR);
fwrite(&r,sizeof(r),1,fp);
struct aloc a;a.resid=id;strcpy(a.usern,usern);strcpy(a.userole,userole);fwrite(&a,sizeof(a),1,afp);
fprintf(out,"allocated successfully\n");}
else{fprintf(out,"in use\n");}break;}}
if(!fo)fprintf(out,"not found\n");
fclose(fp); fclose(afp); fclose(out);}
void relresre(int id){
FILE *fp=fopen("source.dat","rb+");
FILE *out=fopen("output.txt","w");
struct res r; int fo=0;
if(fp==NULL){fprintf(out,"NO FILE\n"); fclose(out); return;}
while(fread(&r,sizeof(r),1,fp)){
if(r.id==id){fo=1;r.inuse=0;
fseek(fp,-sizeof(r),SEEK_CUR);
fwrite(&r,sizeof(r),1,fp);
fprintf(out,"RELEASED\n"); break;}}
if(!fo)fprintf(out,"NOT FOUND\n");
fclose(fp); fclose(out);}
void delre(int id){
FILE *fp=fopen("source.dat","rb");
FILE *temp=fopen("temp.dat","wb");
FILE *out=fopen("output.txt","w");
struct res r; int fo=0;
if(fp==NULL){fprintf(out,"NO FILE\n"); fclose(out); return;}
while(fread(&r,sizeof(r),1,fp)){
if(r.id==id){fo=1;
if(r.inuse==1){
fprintf(out,"cannot delete\n");
fclose(fp); fclose(temp); fclose(out);
remove("temp.dat");return;}continue;}
fwrite(&r,sizeof(r),1,temp);}
fclose(fp); fclose(temp);
remove("source.dat");
rename("temp.dat","source.dat");
if(fo)fprintf(out,"deleted\n");
else fprintf(out,"not found\n");fclose(out);}
int main(){
FILE *ip=fopen("input.txt","r");
if(!ip)return 0;int ch;
fscanf(ip,"%d",&ch);
switch(ch){
case 1:{int id; char name[30];
fscanf(ip,"%d%s",&id,name); addre(id,name); break;}
case 2:{viewresre(); break;}
case 3:{int id; char usern[30],userole[15];
fscanf(ip,"%d%s%s",&id,usern,userole); allocre(id,usern,userole); break;}
case 4:{int id;
fscanf(ip,"%d",&id); relresre(id); break;}
case 5:{int id;
fscanf(ip,"%d",&id); delre(id); break;}
default: break;}
fclose(ip); return 0;}
// backend program by AMIT SINGH.