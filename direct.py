import os
a = [
    0, 0, 0
    ]
    def fun(str):
            nod = 0
            nof = 0
            for root, dirs, files in os.walk(str):
                            for name in files:
                                print(os.path.join(root, name))
                                nof += 1
                                a[1] = nof
                            for name in dirs:
                                print(os.path.join(root, name))
                                nod += 1
                                a[2] = nod
path = input("Enter the ath of the drive")
fun(path)
print("No of files is :%s" % a[1])
print("No of flders/sub directories is:%s" % a[2])
