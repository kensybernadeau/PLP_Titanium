#include <stdio.h>
int main () {

    char str1[10];
    char str2[]="abcdefghijklmn";
    strcpy(str1,str2);


    char username[8];
    int allow = 0;
    printf external link("Enter your username, please: ");
    gets(username); // user inputs "malicious"

    if (grantAccess(username)) {
        allow = 1;
    }
    if (allow != 0) { // has been overwritten by the overflow of the username.
        privilegedAction();
        gets(username);
    }
    return 0;

    char *secret = "This is a secret!\n";
    printf(*secret)
}