import time
import threading


titles     = ["Harry Potter", "Pride and Prejudice"]
pages      = [250, 430]
first_name = ["J.K.", "Jane"]
last_name  = ["Rowling", "Austen"]
location   = ["UK", "UK"]

def build_book_dict(titles, pages, first_name, last_name, locations):
    inputs = zip(titles, pages, first_name, last_name, locations)

    d = {}

    for title, pg, fn, ln, loc in inputs:
        d[title] = {
            "Pages": pg,
            "Author": {"First": fn, "Last": ln},
            "Publisher": {"Location": loc}
        }

    time.sleep(3)
    return d

def cancel_timer(timer):
    timer.cancel()
    print("Timer Cancelled")

if __name__ == "__main__":
    timer = threading.Timer(5, cancel_timer, args=(None,))  # 先预占一个位置
    # 立刻用正确实例替换 args
    timer.args = (timer,)
    timer.start()
    print("Timer started, will cancel in 5 seconds...")

    result = build_book_dict(titles, pages, first_name, last_name, location)
    print("Built book dictionary:")
    print(result)