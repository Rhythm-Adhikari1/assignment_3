def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    while True:
        date = input("date: ")
        
        try:
            # Try to handle the format MM/DD/YYYY
            m, d, y = date.split('/')
            m = int(m)
            d = int(d)
            y = int(y)
            if 1 <= m <= 12 and 1 <= d <= 31:
                break
        except ValueError:
            try:
                # Try to handle the format Month DD, YYYY
                m_str, d, y = date.split()
                d = int(d.strip(','))
                y = int(y)
                m_str = m_str.title().strip()
                
                if m_str in months:
                    m = months.index(m_str) + 1
                    if 1 <= d <= 31:
                        break
            except (ValueError, IndexError):
                pass  # If parsing fails, continue the loop to ask for input again

    print(f"{y}/{m:02}/{d:02}")

main()
