#include <string.h>

void do_something(char *Buffer)
{
     char MyVar[128];
     strcpy(MyVar,Buffer);
}

int main (int argc, char **argv)
{
     do_something(argv[1]);
}
