import linux_cmds
import aws_cli
import partitioner


print("""          ________________________
         |                       |
         |One-For-All Interface  |
         |_______________________|                   """)


print("""         Press 1 for performing Linux Commands
         Press 2 for Hadoop Setup
         Press 3 for partioning
         Press 4 for AWS CLI configuration
         Press 0 to exit
         """)
a=input()
while a!='0':
    if a=='1':
        linux_cmds.clear_screen_linux()
    if a=='3':
        partitioner.clear_screen_partition()
    if a=='4':
        aws_cli.clear_screen_aws()

print("\n\n\nthanks for visiting  : )")

