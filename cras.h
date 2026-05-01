#ifndef cras_h
#define cras_h
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct res{
    int id;
    char naam[30];
    int inuse;};
struct aloc{
    int resid;
    char usern[30];
    char userole[15];};
void add(int id,char name[]);
void viewres();
void alloc(int id,char usern[],char userole[]);
void relres(int id);
void delr(int id);
#endif
// header file for cras system by AMIT SINGH.