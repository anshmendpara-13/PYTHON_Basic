f1 = open("ansh.txt")

try:
    f = open("done1.txt")

except Exception as e:
    print(e)
except EOFError as i:
    print("print eof error aa gaya hai",i)
except IOError as j:
    print("print io errror aa gaya hai",j)

else:
    print("this will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()
    print("important stuff")

# final else use above

