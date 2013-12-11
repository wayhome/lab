#include "apue.h"
#include <dirent.h>

int main(int argc, char argv[])
{
    DIR *dp;
    struct direct *dirp;

    if(argc !=2)
        err_quit("Usage: ls directory_name");

}
