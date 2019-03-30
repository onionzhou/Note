#include <stdio.h>
#include <stdlib.h> 



typedef struct LNode
{
    int data ;
    struct LNode *next ;

}LinkNode;

//头插 
LinkNode *createLinklistByhead (int n)
{
    //int num ;
    int i ;
    LinkNode *head = NULL;
    LinkNode *p;

    head =(LinkNode*)malloc(sizeof(LinkNode));
    head->next =NULL;
    

    for( i=0;i<n;i++)
    {
        //scanf("输入插入的值 %d",&num);

        p = (LinkNode *)malloc(sizeof(LinkNode));
        p ->data = i;
        //头插入法
        p->next = head->next;
        
        head->next = p ;

    }

    return head;

}
//尾插
LinkNode *createLinklistBytail(int n)
{
    int i ;
    LinkNode *p ;
    
    p = (LinkNode *)malloc(sizeof(LinkNode));
    p->next = NULL;

    for( i=0;i<n;i++)
    {
        p = (LinkNode *)malloc(sizeof(LinkNode));
        p->data = i ;

        p->next = q ;
    }

}
void display ( LinkNode *L)
{
    LinkNode *tmp ;
    tmp = L;
    while (tmp->next)
    {
        tmp = tmp->next;
        printf("%d ",tmp->data);
    }
    printf("\n");
}

void destory(LinkNode L)
{
    free(L);
}

int staticChar(int n )
{
    printf("%d\n",n);
}
int main(int argc, char const *argv[])
{
    int c[20] = 0;
    printf("输入任意数字: \n");
    scanf("%d",&c);
    staticChar(*c);

    return 0;
}