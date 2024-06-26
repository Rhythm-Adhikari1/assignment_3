def main():
    items_count = {}
    while True:
        try:
            item = input().strip().lower()  
            if item in items_count:
                items_count[item] += 1
            else:
                items_count[item] = 1
        except EOFError:
            break

    for item in sorted(items_count):
        print(f"{items_count[item]} {item.upper()}")

main()
