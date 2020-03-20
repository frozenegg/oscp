# oscp
http://inaz2.hatenablog.com/entry/2014/07/06/163219
strcpy string copy

gcc -g -z exestack -no-pie -o bo1 -m32 bo1.c

gdb bo1
run A
info registers

see esp, ebp

x/40x $esp
(eXamine 40 heXadecimal words, starting at $esp)
