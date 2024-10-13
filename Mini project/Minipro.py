import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# ข้อมูลสถานี BTS สายสีเขียว
stations = [
    "คูคต", "แยก คปอ.", "พิพิธภัณฑ์กองทัพอากาศ", "โรงพยาบาลภูมิพลอดุลยเดช",
    "สะพานใหม่", "สายหยุด", "พหลโยธิน 59", "วัดพระศรีมหาธาตุ", 
    "บางบัว", "กรมป่าไม้", "มหาวิทยาลัยเกษตรศาสตร์", "เสนานิคม", 
    "รัชโยธิน", "พหลโยธิน 24", "ห้าแยกลาดพร้าว", "หมอชิต", 
    "สะพานควาย", "อารีย์", "สนามเป้า", "อนุสาวรีย์ชัยสมรภูมิ", 
    "พญาไท", "ราชเทวี", "สยาม","ชิดลม", "เพลินจิต", "นานา", "อโศก", 
    "พร้อมพงษ์", "ทองหล่อ", "เอกมัย", "พระโขนง", "อ่อนนุช", "บางจาก", 
    "ปุณณวิถี", "อุดมสุข", "บางนา", "แบริ่ง", "สำโรง", "ปู่เจ้า", 
    "ช้างเอราวัณ", "โรงเรียนนายเรือ", "ปากน้ำ", "ศรีนครินทร์", 
    "แพรกษา", "สายลวด", "เคหะสมุทรปราการ"
]

stations15Bath = [
    "คูคต", "แยก คปอ.", "พิพิธภัณฑ์กองทัพอากาศ", "โรงพยาบาลภูมิพลอดุลยเดช",
    "สะพานใหม่", "สายหยุด", "พหลโยธิน 59", "วัดพระศรีมหาธาตุ", 
    "บางบัว", "กรมป่าไม้", "มหาวิทยาลัยเกษตรศาสตร์", "เสนานิคม", 
    "รัชโยธิน", "พหลโยธิน 24", "ห้าแยกลาดพร้าว", "หมอชิต"
]

stationsNot15Bath = [
    "สะพานควาย", "อารีย์", "สนามเป้า", "อนุสาวรีย์ชัยสมรภูมิ", 
    "พญาไท", "ราชเทวี", "สยาม","ชิดลม", "เพลินจิต", "นานา", "อโศก", 
    "พร้อมพงษ์", "ทองหล่อ", "เอกมัย", "พระโขนง", "อ่อนนุช", "บางจาก", 
    "ปุณณวิถี", "อุดมสุข", "บางนา", "แบริ่ง", "สำโรง", "ปู่เจ้า", 
    "ช้างเอราวัณ", "โรงเรียนนายเรือ", "ปากน้ำ", "ศรีนครินทร์", 
    "แพรกษา", "สายลวด", "เคหะสมุทรปราการ"
]

class Ticket:
    def __init__(self, start_station, end_station, cash_received, price, many):
        self.start_station = start_station
        self.end_station = end_station
        self.cash_received = cash_received
        self.price = price  
        self.many = many

    def calculate_price(self):
        start_index = stations.index(self.start_station)
        end_index = stations.index(self.end_station)

        price = 0  

        if self.start_station in stations15Bath and self.end_station in stations15Bath:
            price = 15  
        elif (self.start_station in stations15Bath and self.end_station not in stations15Bath):
            price = 15 + self.calculate_priceNot15Bath(end_index - 15)
        elif (self.start_station not in stations15Bath and self.end_station in stations15Bath):
            price = 15 + self.calculate_priceNot15Bath(abs(start_index - 15))
        elif (self.start_station not in stations15Bath and self.end_station not in stations15Bath):
            price = self.calculate_priceNot15Bath(abs(start_index - end_index))

        return price

    def calculate_priceNot15Bath(self, intervalStation):
        if intervalStation == 1:
            priceSub = 17
        elif intervalStation == 2:
            priceSub = 25  
        elif intervalStation == 3:
            priceSub = 28      
        elif intervalStation == 4:
            priceSub = 32  
        elif intervalStation == 5:
            priceSub = 35    
        elif intervalStation == 6:
            priceSub = 40
        elif intervalStation == 7:
            priceSub = 43
        elif intervalStation >= 8:
            priceSub = 47
        return priceSub
    
    def get_change(self):
        price = self.calculate_price()
        many = int(many_entry.get())
        pricetotal = many * price
        change = self.cash_received - pricetotal
        return change, price, pricetotal

# ประกาศตัวแปรลิสต์สำหรับเก็บข้อมูล
ticket_tuple = []     
revenue_list = []     
change_list = []      

# ฟังก์ชันสำหรับบันทึกสถิติการขายลงในไฟล์
def save_statistics():
    with open("Mini project//DB_BTS.txt", "w", encoding="utf-8") as file:
        for ticket in ticket_tuple:
            file.write(f"{ticket.start_station},{ticket.end_station},{ticket.price},{ticket.many}\n")
        total_revenue = sum(revenue_list)
        total_change = sum(change_list)
        file.write(f"total_revenue,{total_revenue}\n")
        file.write(f"total_change,{total_change}\n")

# ฟังก์ชันสำหรับโหลดข้อมูลสถิติจากไฟล์
def load_statistics():
    if os.path.exists("Mini project//DB_BTS.txt"):
        with open("Mini project//DB_BTS.txt", "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == "total_revenue":
                    revenue_list.append(int(data[1]))
                elif data[0] == "total_change":
                    change_list.append(int(data[1]))
                else:
                    start_station, end_station, price, many = data
                    ticket = Ticket(start_station, end_station, 0, int(price), int(many))
                    ticket_tuple.append(ticket)

# เรียกฟังก์ชันโหลดข้อมูลเมื่อเริ่มโปรแกรม
load_statistics()

def calculate_change_in_coins(change):
    change_details = []  # เก็บผลการทอนเป็น list   
    changesub = change
    if change == 0:
        return "ไม่มีเงินทอน"
    coin_denominations = [10, 5, 2, 1]  
    for coin in coin_denominations:
        if changesub >= coin:
            count = changesub // coin  # จำนวนเหรียญที่ทอน
            changesub = changesub % coin  # เหลือเงินทอนหลังจากทอนด้วยเหรียญนี้แล้ว
            change_details.append(f"เหรียญ {coin} บาท: {count} เหรียญ")
    
    return "\n".join(change_details)  # รวมข้อความเพื่อแสดงผลเป็นรายการ

def book_ticket():
    start_station = start_station_var.get()
    end_station = end_station_var.get()
    cash = cash_entry.get()
    many = many_entry.get()

    if not (start_station and end_station and cash):
        messagebox.showerror("Error", "กรุณากรอกข้อมูลให้ครบ")
        return
    
    if start_station == end_station:
        messagebox.showerror("Error", "สถานีต้นทางและปลายทางต้องแตกต่างกัน")
        return

    cash = int(cash)

    ticket = Ticket(start_station, end_station, cash, 0, many)

    change, price, pricetotal = ticket.get_change()  # อัพเดท change และ price

    ticket.price = price  # เก็บค่า price ใน ticket
    
    if change < 0:
        messagebox.showerror("Error", "เงินไม่พอสำหรับการซื้อบัตร")
        return
    
    change_details = calculate_change_in_coins(change)
    ticket_tuple.append(ticket)
    revenue_list.append(pricetotal)
    change_list.append(change)

    result_label.config(text=f"ราคาตั๋ว: {price} บาท  จำนวน: {many} ใบ \nทั้งหมด: {pricetotal} บาท เงินทอน: {change} บาท \nเงินทอน: {change_details}")

    save_statistics()  # บันทึกข้อมูลสถิติทุกครั้งที่จองตั๋ว

def show_statistics():
    if not ticket_tuple:
        messagebox.showinfo("สถิติการขายตั๋ว", "ยังไม่มีข้อมูลการขาย")
        return
        
    trips_text = "\n".join([f"จาก {ticket.start_station} ไป {ticket.end_station} ราคา {ticket.price} บาท จำนวน {ticket.many}" for ticket in ticket_tuple])
    total_revenue = sum(revenue_list)
    total_change = sum(change_list)
    messagebox.showinfo("สถิติการขายตั๋ว", f"{trips_text}\n\nรายได้รวม: {total_revenue} บาท\nทอนเงินรวม: {total_change} บาท")

root = tk.Tk()
root.title("BTS Ticket Booking")
root.geometry("800x600")
root.configure(bg="black")  # เปลี่ยนพื้นหลังของหน้าต่างเป็นสีดำ

# ปรับการจัดการแถวและคอลัมน์
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# ชื่อโปรแกรม
tk.Label(root, text="GUI ขายบัตร BTS สายสีเขียว", bg="black", fg="white", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20, pady=10)

# ส่วนข้อมูลอยู่ฝั่งซ้าย
left_frame = tk.Frame(root, bg="black")  # เปลี่ยนพื้นหลังของเฟรมซ้ายเป็นสีดำ
left_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)

# เลือกสถานีต้นทาง
tk.Label(left_frame, text="สถานีต้นทาง", font=("Arial", 14), fg="white", bg="black").grid(row=0, column=0, sticky="e", padx=20, pady=10)
start_station_var = tk.StringVar(left_frame)
start_station_var.set(stations[0])  
start_station_menu = tk.OptionMenu(left_frame, start_station_var, *stations)
start_station_menu.config(width=20, font=("Arial", 12), fg="black")  # ตั้งค่าสีตัวอักษรของ OptionMenu
start_station_menu.grid(row=0, column=1, sticky="w")

# เลือกสถานีปลายทาง
tk.Label(left_frame, text="สถานีปลายทาง", font=("Arial", 14), fg="white", bg="black").grid(row=1, column=0, sticky="e", padx=20, pady=10)
end_station_var = tk.StringVar(left_frame)
end_station_var.set(stations[0])  
end_station_menu = tk.OptionMenu(left_frame, end_station_var, *stations)
end_station_menu.config(width=20, font=("Arial", 12), fg="black")  # ตั้งค่าสีตัวอักษรของ OptionMenu
end_station_menu.grid(row=1, column=1, sticky="w")

# จำนวนบัตร
tk.Label(left_frame, text="จำนวนบัตรที่ต้องการ", font=("Arial", 14), fg="white", bg="black").grid(row=2, column=0, sticky="e", padx=20, pady=10)
many_entry = tk.Entry(left_frame, width=20, font=("Arial", 12), fg="black", bg="white")  # ตั้งค่าสีตัวอักษรของ Entry
many_entry.grid(row=2, column=1, sticky="w")

# จำนวนเงินที่จ่าย
tk.Label(left_frame, text="จำนวนเงิน (บาท)", font=("Arial", 14), fg="white", bg="black").grid(row=3, column=0, sticky="e", padx=20, pady=10)
cash_entry = tk.Entry(left_frame, width=20, font=("Arial", 12), fg="black", bg="white")  # ตั้งค่าสีตัวอักษรของ Entry
cash_entry.grid(row=3, column=1, sticky="w")

# ปุ่มจองตั๋ว
book_button = tk.Button(left_frame, text="ชำระเงิน", command=book_ticket, bg="#4CAF50", fg="white", font=("Arial", 14))
book_button.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

# ปุ่มแสดงสถิติ
stats_button = tk.Button(left_frame, text="แสดงสถิติ", command=show_statistics, bg="#2196F3", fg="white", font=("Arial", 14))
stats_button.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

# ป้ายผลลัพธ์
result_label = tk.Label(left_frame, text="", font=("Arial", 12), fg="white", bg="black")
result_label.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

# ส่วนคู่มือการใช้งานอยู่ฝั่งขวา
right_frame = tk.Frame(root, bg="black")  # เปลี่ยนพื้นหลังของเฟรมขวาเป็นสีดำ
right_frame.grid(row=1, column=1, sticky="nsew", padx=0, pady=0)


# ใส่รูปภาพ (เปลี่ยน path ของรูปภาพตามต้องการ)
try:
    image = Image.open("C:\\Users\\lenovo\\Desktop\\dsadsad\\software lap\\Mini project\\yellow-map.jpg")# แทนที่ด้วย path ของรูปภาพจริง
    image = image.resize((200, 200), Image.LANCZOS)  # ปรับขนาดรูป
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(right_frame, image=photo, bg="#F0F0F0")
    image_label.image = photo  
    image_label.pack(pady=10)
except Exception as e:
    print("ไม่สามารถโหลดรูปภาพได้:", e)
    tk.Label(right_frame, text="ไม่พบรูปภาพ", bg="#F0F0F0").pack(pady=10)

# เพิ่มคู่มือการใช้งาน
tk.Label(right_frame, text="คู่มือการใช้งาน", bg="Black", font=("Arial", 16), fg="white").pack(pady=5)
tk.Label(right_frame, text="1.เลือกสถานีต้นทางและปลาบทาง", bg="Black", font=("Arial", 10), fg="white").pack(pady=1)
tk.Label(right_frame, text="2.เลือกจำนวนบัตรที่ต้องการซื้อ", bg="Black", font=("Arial", 10), fg="white").pack(pady=1)
tk.Label(right_frame, text="3.กรองจำนวนเงินที่ต้องการจ่าย", bg="Black", font=("Arial", 10), fg="white").pack(pady=1)
tk.Label(right_frame, text="4.เสร็จสิ้นแล้วกดชำระเงิน", bg="Black", font=("Arial", 10), fg="white").pack(pady=1)

root.mainloop()
