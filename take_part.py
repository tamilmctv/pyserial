def enable(ser):
    print("Enable function activated")
    counts = {
        10: 0,
        20: 0,
        50: 0,
        100: 0,
        200: 0
    }
    
    while True:
        byte_read = ser.read()
        if byte_read == b'\x41':
            counts[10] += 1
            print("Amount rupees 10 received")
            ser.write(b'\x02')
            print(counts[10])
            calculate(counts)
            
        elif byte_read == b'\x42':
            counts[20] += 1
            print("Amount rupees 20 received")
            ser.write(b'\x02')
            print(counts[20])
            calculate(counts)
            
        elif byte_read == b'\x43':
            counts[50] += 1
            print("Amount 50 received")
            ser.write(b'\x02')
            print(counts[50])
            calculate(counts)
            
        elif byte_read == b'\x44':
            counts[100] += 1
            print("Amount 100 received")
            ser.write(b'\x02')
            print(counts[100])
            calculate(counts)
            
        elif byte_read == b'\x45':
            counts[200] += 1
            print("Amount 200 received")
            ser.write(b'\x02')
            print(counts[200])
            calculate(counts)

def calculate(counts):
    total = 0
    for i, j in counts.items():
        amount=i * j
        print(f"{i} * {j} = {amount}")
        total += j * i

    
    print(f"Total amount: {total}")

