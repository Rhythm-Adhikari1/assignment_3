def main():
    months= [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
     
    while True:
    
        date=input("date:" )
        try: 
            m,d,y=date.split('/')
            m=int(m)
            d=int(d)
            y=int(y)
            if m>12 or m<1 or d<1 or d>31 :
                pass  
            else :
                break
        except ValueError:
            try:
                m,d,y=date.split()
                y=int(y)
                d=int(d)
                i=0
                flag=0
                while i<12 :
                    if months[i]==m.title().strip():
                        m=i+1
                        flag=1
                        break
                    i+=1
                    
                if flag==1 and 1<=d<=31:
                    break
                
            except(ValueError,IndexError):
                pass

    print(f"{y}/{m:02}/{d:02}")
    
main()
