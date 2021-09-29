my_list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]

for item in my_list:
    item_split = item.split(".")
    print(item_split[len(item_split)-1])