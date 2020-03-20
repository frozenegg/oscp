#include <stdio.h>

int main(){
  char buf[100];
  setlinebuf(stdout);
  gets(buf);
  puts(buf);
  return 0;
}
