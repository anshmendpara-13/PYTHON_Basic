def searcher():
    import time
    # some 4 seconds time consuming task
    book = "this is a book on ansh and code with ansh and good"
    time.sleep(3)

    while True:
        text = (yield)
        if text in book:
            print("your text is in this book")
        else:
            print("text is not in this book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("ansh")

input("press any key")
search.send("ansh")

search.close()
# stop itresion error
search.send("your text")