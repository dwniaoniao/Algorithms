#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_LENGTH(x) (sizeof(x) / sizeof(x[0]));

typedef enum {false, true} bool;

typedef struct list{
    int *element;
    int length;
} List; //表

typedef struct{
    int *element;
    int length;
} Heap; //堆

void PrintList(List l)
{
    //输出表l中的所有元素
    for (int i = 0; i < l.length; i++)
    {
        printf("%d ", *(l.element + i));
    }
    putchar('\n');
}
void PrintHeap(Heap h)
{
    //输出堆h中的所有元素
    for (int i = 0; i < h.length; i++)
    {
        printf("%d ", *(h.element + i));
    }
    putchar('\n');
}

void HeapPut(Heap *h, int x)
{
    //向堆h尾加入一个元素，并向上调整
    int son, tmp;
    h->element = (int *)realloc(h->element, (h->length + 1) * sizeof(int));
    *(h->element + h->length) = x; /*新元素加入堆尾*/
    h->length++;
    son = h->length - 1;
    while (*(h->element + (son / 2)) > *(h->element + son))
    {
        tmp = *(h->element + (son / 2));
        *(h->element + (son / 2)) = *(h->element + son);
        *(h->element + son) = tmp;
        son /= 2;
    }
}

int HeapGet(Heap *h)
{
    //取堆头元素
    int fa = 0, son = 1, tmp;
    bool stop = false;
    int get = *(h->element);                         /*堆头元素*/
    *(h->element) = *(h->element + (h->length - 1)); /*置堆头元素为堆尾元素的值*/
    h->element = (int *)realloc(h->element, (h->length - 1) * sizeof(int));
    h->length--; /*删去堆尾元素*/
    int len = h->length;
    while (((son < len) || (son + 1 < len)) && (stop == false))
    {
        if ((son + 1 > len - 1) || (*(h->element + son) < *(h->element + (son + 1))))
            ;
        else
            son += 1;
        if (*(h->element + fa) > *(h->element + son))
        {
            tmp = *(h->element + fa);
            *(h->element + fa) = *(h->element + son);
            *(h->element + son) = tmp;
            fa = son;
            son *= 2;
        }
        else
            stop = true;
    }
    return get;
}

void SortList(List *l)
{
    //对表l进行排序(冒泡排序法)
    int tmp;
    for (int i = 0; i < l->length - 1; i++)
    {
        for (int j = 0; j < l->length - 1 - i; j++)
        {
            if (*(l->element + (j + 1)) < *(l->element + j))
            {
                tmp = *(l->element + (j + 1));
                *(l->element + (j + 1)) = *(l->element + j);
                *(l->element + j) = tmp;
            }
        }
    }
}

int ListGet(List *l)
{
    //取表第一个元素，删去这个元素并返回其值
    int r = *(l->element);
    l->element++;
    l->length--;
    return r;
}

void KMerge(List l[], int k, int n, List *result)
{
    //归并k个有序表
    Heap h;
    h.element = NULL;
    h.length = 0;
    int *r = result->element;
    for (int i = 0; i < k; i++)
    {
        HeapPut(&h, ListGet(&l[i]));
    }
    while (h.length)
    {
        *r = HeapGet(&h);
        for (int i = 0; i < k; i++)
        {
            if (l[i].length && *(l[i].element - 1) == *r)
            {
                HeapPut(&h, ListGet(&l[i]));
                break;
            }
        }
        r++;
    }
}

int main(int argc, char const *argv[])
{
    freopen("kmerge.txt","r",stdin);
    printf("k = \n");
    int k, n, sum = 0;
    scanf("%d", &k);
    int *s[k];
    List l[k];
    for (int i = 0; i < k; i++)
    {
        printf("Element number of list %d: \n", i + 1);
        scanf("%d", &n);
        sum += n;
        s[i] = (int *)malloc(n * sizeof(int));
        srand((unsigned)time(NULL));
        for (int j = 0; j < n; j++)
            s[i][j] = rand() % 10000;
        l[i].element = s[i];
        l[i].length = n;
        SortList(&l[i]);
    }

    for (int i = 0; i < k; i++)
    {
        printf("List %d: ", i + 1);
        PrintList(l[i]);
    }
    printf("Total element number: %d\n", sum);

    List result;
    result.element = (int *)malloc(sum * sizeof(int));
    result.length = sum;

    clock_t start, end;
    start = clock();

    KMerge(l, k, sum, &result);
    end = clock();
    printf("The result list: ");
    PrintList(result);
    double second = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time used: %.8fs\n", s);
    return 0;
}
