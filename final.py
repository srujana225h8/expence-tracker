import customtkinter as ctk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    database="expense_tracker"
)
cursor = db.cursor()

ctk.set_appearance_mode("light")
root = ctk.CTk()
root.geometry("950x600")
root.title("Expense Tracker")
root.configure(bg="#d5c4bc")

image = Image.open("bgImage.webp")
image = image.resize((250, 600), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

items_list = []

def add_item():
    item = item_box.get()
    cost = cost_box.get()
    quantity = quantity_box.get()
    date = date_picker.get_date().strftime("%Y-%m-%d")
    total = int(quantity) * int(cost)

    item_label = ctk.CTkLabel(frame_heading, text=item, text_color="#5b3952", font=("Arial", 15, "bold"))
    item_label.grid(row=len(items_list) + 1, column=0, padx=(10, 20), pady=5, sticky="w")

    quantity_label = ctk.CTkLabel(frame_heading, text=quantity, text_color="#5b3952", font=("Arial", 15, "bold"))
    quantity_label.grid(row=len(items_list) + 1, column=1, padx=(10, 20), pady=5, sticky="w")

    cost_label = ctk.CTkLabel(frame_heading, text=cost, text_color="#5b3952", font=("Arial", 15, "bold"))
    cost_label.grid(row=len(items_list) + 1, column=2, padx=(10, 20), pady=5, sticky="w")

    total_label = ctk.CTkLabel(frame_heading, text=str(total), text_color="#5b3952", font=("Arial", 15, "bold"))
    total_label.grid(row=len(items_list) + 1, column=3, padx=(10, 20), pady=5, sticky="w")
    
    date_label = ctk.CTkLabel(frame_heading, text=date, text_color="#5b3952", font=("Arial", 15, "bold"))
    date_label.grid(row=len(items_list) + 1, column=4, padx=(10, 20), pady=5, sticky="w")
    cursor.execute("INSERT INTO expenses (item, quantity, cost, total, date) VALUES (%s, %s, %s, %s, %s)",
                   (item, int(quantity), int(cost), total, date))
    db.commit()

    single_item_info = {"Item": item, "Quantity": int(quantity), "Cost": int(cost), "Total Amount": total, "Date": date}
    items_list.append(single_item_info)

def clear_item():
    item_box.delete(0, "end")
    quantity_box.delete(0, "end")
    cost_box.delete(0, "end")
    date_picker.set_date(pd.Timestamp.today())

from datetime import datetime

def analyze():
    cursor.execute("SELECT item, SUM(total) as total_amount, MONTH(date) as month FROM expenses WHERE MONTH(date) = MONTH(CURRENT_DATE()) GROUP BY item, MONTH(date)")
    db_data = cursor.fetchall()
    
    db_df = pd.DataFrame(db_data, columns=['Item', 'Total Amount', 'Month'])
    
    current_df = pd.DataFrame(items_list)
    combined_df = pd.concat([db_df, current_df], ignore_index=True)
    
    current_month = datetime.now().month
    current_year = datetime.now().year
    combined_df = combined_df[(combined_df['Month'] == current_month)]
    
    items = combined_df['Item']
    total = combined_df['Total Amount']
    colors = ['#e1bee7', '#ce93d8', '#ba68c8', '#ab47bc', '#9c27b0', '#8e24aa', '#7b1fa2', '#6a1b9a', '#4a148c']
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    ax1.pie(total, labels=items, autopct='%1.1f%%', startangle=90, colors=colors)
    ax1.set_title(f"Expense Tracker Analysis - Total Expenses for {datetime.now().strftime('%B %Y')} by Item")
    monthly_totals = combined_df.groupby('Item')['Total Amount'].sum().reset_index()
    ax2.bar(monthly_totals['Item'], monthly_totals['Total Amount'], color='purple', alpha=0.7)
    ax2.set_xlabel('Item')
    ax2.set_ylabel('Total Expenses')
    ax2.set_title(f"Monthly Expenses for {datetime.now().strftime('%B %Y')} by Item")

    plt.tight_layout()
    plt.show()




button_bg_color = "#5b3952"

left_frame = ctk.CTkFrame(root, width=250, height=600)
left_frame.grid(row=0, column=0, sticky="nsew")

image_label = ctk.CTkLabel(left_frame, image=photo, text="")
image_label.place(relwidth=1, relheight=1)

right_frame = ctk.CTkFrame(root, width=700, height=600, bg_color="#d5c4bc")
right_frame.grid(row=0, column=1, sticky="nsew")

title_label = ctk.CTkLabel(right_frame, text="Expense Tracker", text_color="#5b3952", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

container_frame = ctk.CTkScrollableFrame(right_frame, bg_color="transparent", border_color=button_bg_color, border_width=2, orientation="vertical", scrollbar_button_color=button_bg_color)
container_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)

item_label = ctk.CTkLabel(container_frame, text="Item", text_color="#5b3952", font=("Arial", 15, "bold"))
item_label.pack(pady=(10, 5), anchor="w")
item_box = ctk.CTkEntry(container_frame, font=("Arial", 15), height=40, width=300, corner_radius=50)
item_box.pack(padx=10, pady=(10, 5), anchor="w")

quantity_label = ctk.CTkLabel(container_frame, text="Quantity", text_color="#5b3952", font=("Arial", 15, "bold"))
quantity_label.pack(pady=(10, 5), anchor="w")
quantity_box = ctk.CTkEntry(container_frame, font=("Arial", 15), height=40, width=300, corner_radius=50)
quantity_box.pack(padx=10, pady=(10, 5), anchor="w")

cost_label = ctk.CTkLabel(container_frame, text="Cost Per Unit", text_color="#5b3952", font=("Arial", 15, "bold"))
cost_label.pack(pady=(10, 5), anchor="w")
cost_box = ctk.CTkEntry(container_frame, font=("Arial", 15), height=40, width=300, corner_radius=50)
cost_box.pack(padx=10, pady=(10, 5), anchor="w")

date_label = ctk.CTkLabel(container_frame, text="Date", text_color="#5b3952", font=("Arial", 15, "bold"))
date_label.pack(pady=(10, 5), anchor="w")
date_frame = ctk.CTkFrame(container_frame, corner_radius=10, height=40, width=300)
date_frame.pack(padx=10, pady=(10, 5), anchor="w")
date_picker = DateEntry(date_frame, width=25, background='#5b3952', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
date_picker.pack(fill="both", expand=True, padx=5, pady=5)

frame_buttons = ctk.CTkFrame(container_frame)
frame_buttons.pack(pady=10)

add_button = ctk.CTkButton(frame_buttons, text="Add Item", fg_color=button_bg_color, font=("Arial", 15, "bold"), command=add_item, hover_color="#965f8f")
add_button.pack(side=ctk.LEFT, padx=10)

clear_button = ctk.CTkButton(frame_buttons, text="Clear", fg_color=button_bg_color, font=("Arial", 15, "bold"), command=clear_item, hover_color="#965f8f")
clear_button.pack(side=ctk.LEFT)

display_label = ctk.CTkLabel(container_frame, text="Expenses", text_color="#5b3952", font=("Arial", 15, "bold"))
display_label.pack(pady=(10, 5), anchor="w")

frame_heading = ctk.CTkFrame(container_frame, bg_color="transparent", border_width=2, border_color=button_bg_color)
frame_heading.pack()

heading_labels = ["Item", "Quantity", "Unit Cost", "Total", "Date"]
for col, heading in enumerate(heading_labels):
    heading_label = ctk.CTkLabel(frame_heading, text=heading, text_color="#5b3952", font=("Arial", 15, "bold"))
    heading_label.grid(row=0, column=col, padx=(10, 20), pady=5, sticky="w")

analyze_button = ctk.CTkButton(container_frame, text="Analyze", fg_color=button_bg_color, font=("Arial", 15, "bold"), command=analyze, hover_color="#965f8f")
analyze_button.pack(pady=10)

root.grid_columnconfigure(0, weight=1, minsize=250)
root.grid_columnconfigure(1, weight=3, minsize=700)
root.grid_rowconfigure(0, weight=1)

root.mainloop()
