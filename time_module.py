# time module
import time
#time.sleep() for time between two statemant

# print("this is for while loop")
initial1 = time.time()
k = 0
while(k<45):
    print("hello ansh")

    # time.sleep(2)

    k+=1
print("while loop ran in", time.time() -initial1, "seconds")

# print("\nthis is for for loop")
initial2 = time.time()
for i in range(45):
    print("hello ansh")
print("for loop ran in", time.time() -initial2, "seconds")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)