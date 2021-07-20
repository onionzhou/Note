#include<stdio.h>
#include<time.h>

long absdiff(long x,long y)
{
    long result ;
    if (x < y)
        result = y -x ;
    else
        result = x -y;

    return  result ;

}


long cmovdiff(long x,long y )
{
    long rval = y - x;
    long eval = x - y;
    long ntest = x >= y;

    if (ntest) rval = eval ;

    return rval;
}


void main(){
    long x,y;
    x=1;
    y=2;
    clock_t start_t,finish_t;
    double total_t = 0;
    int i = 0;
    start_t = clock();
    for(;i<100000;++i)
    {
      absdiff(x,y);
    }
    finish_t = clock();
    total_t = (double)(finish_t - start_t) / CLOCKS_PER_SEC;//将时间转换为秒

    printf("CPU 占用的总时间：%f\n", total_t);
    return 0;

}