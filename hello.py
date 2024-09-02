
rate = [None, 1500, 4540, 7090]

for index, value in enumerate(rate):
    if index == 0:
        continue  # ข้ามตำแหน่งที่ 0
    print(f"Index {index}: {value}")