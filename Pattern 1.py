print("""
                          *
                         ***
                        *****
                       *******
                      *********
                     ***********
                    *************
                   ***************
                  *****************
                 *******************
                *********************
               ***********************
""")
a=27
for i in range(1,25,2):
    a-=1
    for x in range(a):
         print(" ",end="")
    print("*"*i,end="")

    print()