def main():
    while True:
        a=input("fraction: ")
        x,y=a.split('/')
        try: 
            if y==0:
                raise ZeroDivisionError
            if x>y: 
                raise ValueError
            else:
                b=int(x)/int (y) *100
                b=round(b)
                if b<=1:
                    print("E")
                elif b>=99:
                    print("F")
                else: 
                    print(f"{b}%")
                break

        except(ValueError,ZeroDivisionError):
            pass

main()



    