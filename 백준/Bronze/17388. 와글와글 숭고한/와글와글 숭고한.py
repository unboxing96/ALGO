a, b, c = map(int, input().split())

if a + b + c >= 100:
    print("OK")

else:
    result = min(a, b, c)
    
    if result == a:
        print("Soongsil")
    elif result == b:
        print("Korea")
    else:
        print("Hanyang")