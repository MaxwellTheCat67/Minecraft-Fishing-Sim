from tkinter import *
import random
win = Tk()
win.title("Fishing in Minecraft")
win.geometry("475x500")
current_window1 = None
current_window2 = None
current_window3 = None
current_window4 = None

def center_window(window, width, height):
    win.update_idletasks()
    root_x = win.winfo_rootx()
    root_y = win.winfo_rooty()
    root_width = win.winfo_width()
    root_height = win.winfo_height()
    x = root_x + (root_width - width) // 2
    y = root_y + (root_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def close_open_popups():
    global current_window1, current_window2, current_window3, current_window4

    for window in (current_window1, current_window2, current_window3, current_window4):
        if window is not None and window.winfo_exists():
            window.destroy()

    current_window1 = None
    current_window2 = None
    current_window3 = None
    current_window4 = None

def direction():
    global current_window1

    close_open_popups()

    current_window1 = Toplevel(win)
    current_window1.title("Directions")
    center_window(current_window1, 200, 100)
    label = Label(current_window1, text="Click the fishing rod to\nfish for unknown loot!", font=("Arial", 12))
    label.pack(pady=20)

def loot():
    global current_window2

    close_open_popups()

    current_window2 = Toplevel(win)
    current_window2.title("Loot")
    center_window(current_window2, 300, 550)
    loot_label = Label(current_window2, text="Loot")
    loot_label.grid(row=0,column=1,pady=20)
    rarity_label = Label(current_window2, text="Rarity")
    rarity_label.grid(row=0,column=2,pady=20)

    x = 1
    for i in minecraft_fishing_loot:
        Label(current_window2, text=i).grid(row=x,column=1,padx=10)
        x+=1

    y = 1
    for i in minecraft_fishing_rarity_pct:
        Label(current_window2,text=i).grid(row=y,column=2)
        y += 1

def current_loots():
    global current_window3

    close_open_popups()

    current_window3 = Toplevel(win)
    current_window3.title("Loot Found")
    center_window(current_window3, 300, 550)
    x = 1
    for i in minecraft_fishing_loot:
        Label(current_window3, text=i).grid(row=x,column=1,padx=10)
        x+=1

def clicks():
    global raw_cod, raw_salmon, tropical_fish, pufferfish, lily_pad, bone, bowl
    global leather, leather_boots, rotten_flesh, water_bottle, tripwire_hook, stick
    global string, fishing_rod_damaged, ink_sac, bow_enchanted, fishing_rod_enchanted
    global enchanted_book, name_tag, nautilus_shell, saddle, clicked

    loot = random.choice(minecraft_fishing_loot_for_rarity)
    label3.config(text=f"You got: {loot}")

    if loot == "Raw Cod":
        raw_cod += 1
    elif loot == "Raw Salmon":
        raw_salmon += 1
    elif loot == "Tropical Fish":
        tropical_fish += 1
    elif loot == "Pufferfish":
        pufferfish += 1
    elif loot == "Lily Pad":
        lily_pad += 1
    elif loot == "Bone":
        bone += 1
    elif loot == "Bowl":
        bowl += 1
    elif loot == "Leather":
        leather += 1
    elif loot == "Leather Boots":
        leather_boots += 1
    elif loot == "Rotten Flesh":
        rotten_flesh += 1
    elif loot == "Water Bottle":
        water_bottle += 1
    elif loot == "Tripwire Hook":
        tripwire_hook += 1
    elif loot == "Stick":
        stick += 1
    elif loot == "String":
        string += 1
    elif loot == "Fishing Rod (Damaged)":
        fishing_rod_damaged += 1
    elif loot == "Ink Sac":
        ink_sac += 1
    elif loot == "Bow (Enchanted)":
        bow_enchanted += 1
    elif loot == "Fishing Rod (Enchanted)":
        fishing_rod_enchanted += 1
    elif loot == "Enchanted Book":
        enchanted_book += 1
    elif loot == "Name Tag":
        name_tag += 1
    elif loot == "Nautilus Shell":
        nautilus_shell += 1
    elif loot == "Saddle":
        saddle += 1
    clicked += 1
    label2.config(text=f"{clicked}")
        
def loot_gotten():
    global current_window4

    close_open_popups()

    current_window4 = Toplevel(win)
    current_window4.title("LOOT GOTTEN")
    center_window(current_window4, 300, 550)
    loot_label = Label(current_window4, text="Loot")
    loot_label.grid(row=0,column=1,pady=20)
    rarity_label = Label(current_window4, text="Amount")
    rarity_label.grid(row=0,column=2,pady=20)
    x=1
    for i in minecraft_fishing_loot:
        Label(current_window4, text=i).grid(row=x,column=1,padx=10)
        x+=1
    Label(current_window4, text=raw_cod).grid(row=1,column=2)
    Label(current_window4, text=raw_salmon).grid(row=2,column=2)
    Label(current_window4, text=tropical_fish).grid(row=3,column=2)
    Label(current_window4, text=pufferfish).grid(row=4,column=2)
    Label(current_window4, text=lily_pad).grid(row=5,column=2)
    Label(current_window4, text=bone).grid(row=6,column=2)
    Label(current_window4, text=bowl).grid(row=7,column=2)
    Label(current_window4, text=leather).grid(row=8,column=2)
    Label(current_window4, text=leather_boots).grid(row=9,column=2)
    Label(current_window4, text=rotten_flesh).grid(row=10,column=2)
    Label(current_window4, text=water_bottle).grid(row=11,column=2)
    Label(current_window4, text=tripwire_hook).grid(row=12,column=2)
    Label(current_window4, text=stick).grid(row=13,column=2)
    Label(current_window4, text=string).grid(row=14,column=2)
    Label(current_window4, text=fishing_rod_damaged).grid(row=15,column=2)
    Label(current_window4, text=ink_sac).grid(row=16,column=2)
    Label(current_window4, text=bow_enchanted).grid(row=17,column=2)
    Label(current_window4, text=fishing_rod_enchanted).grid(row=18,column=2)
    Label(current_window4, text=enchanted_book).grid(row=19,column=2)
    Label(current_window4, text=name_tag).grid(row=20,column=2)
    Label(current_window4, text=nautilus_shell).grid(row=21,column=2)
    Label(current_window4, text=saddle).grid(row=22,column=2)



img = PhotoImage(file="fishing_rod.png")
img = img.subsample(2, 2)

minecraft_fishing_loot = [
    "Raw Cod",
    "Raw Salmon",
    "Tropical Fish",
    "Pufferfish",
    "Lily Pad",
    "Bone",
    "Bowl",
    "Leather",
    "Leather Boots",
    "Rotten Flesh",
    "Water Bottle",
    "Tripwire Hook",
    "Stick",
    "String",
    "Fishing Rod (Damaged)",
    "Ink Sac",
    "Bow (Enchanted)",
    "Fishing Rod (Enchanted)",
    "Enchanted Book",
    "Name Tag",
    "Nautilus Shell",
    "Saddle",
]


minecraft_fishing_loot_for_rarity = [
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Cod",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Raw Salmon",
    "Tropical Fish",
    "Tropical Fish",
    "Tropical Fish",
    "Tropical Fish",
    "Tropical Fish",
    "Tropical Fish",
    "Tropical Fish",
    "Tropical Fish",
    "Pufferfish",
    "Pufferfish",
    "Pufferfish",
    "Pufferfish",
    "Lily Pad",
    "Lily Pad",
    "Lily Pad",
    "Lily Pad",
    "Bone",
    "Bone",
    "Bone",
    "Bone",
    "Bowl",
    "Bowl",
    "Bowl",
    "Bowl",
    "Leather",
    "Leather",
    "Leather",
    "Leather",
    "Leather Boots",
    "Leather Boots",
    "Leather Boots",
    "Leather Boots",
    "Rotten Flesh",
    "Rotten Flesh",
    "Rotten Flesh",
    "Rotten Flesh",
    "Water Bottle",
    "Water Bottle",
    "Water Bottle",
    "Water Bottle",
    "Tripwire Hook",
    "Tripwire Hook",
    "Tripwire Hook",
    "Tripwire Hook",
    "Stick",
    "Stick",
    "Stick",
    "String",
    "String",
    "String",
    "Fishing Rod (Damaged)",
    "Fishing Rod (Damaged)",
    "Ink Sac",
    "Ink Sac",
    "Ink Sac",
    "Ink Sac",
    "Bow (Enchanted)",
    "Fishing Rod (Enchanted)",
    "Enchanted Book",
    "Name Tag",
    "Name Tag",
    "Name Tag",
    "Nautilus Shell",
    "Nautilus Shell",
    "Nautilus Shell",
    "Saddle",
]

minecraft_fishing_rarity_pct = [
    "51.0%",
    "21.3%",
    "1.7%",
    "11.1%",
    "1.7%",
    "1.0%",
    "1.0%",
    "1.0%",
    "1.0%",
    "1.0%",
    "1.0%",
    "1.0%",
    "0.5%",
    "0.5%",
    "0.2%",
    "0.1%",
    "0.8%",
    "0.8%",
    "0.8%",
    "0.8%",
    "0.8%",
    "0.8%",
]

raw_cod = 0
raw_salmon = 0
tropical_fish = 0
pufferfish = 0
lily_pad = 0
bone = 0
bowl = 0
leather = 0
leather_boots = 0
rotten_flesh = 0
water_bottle = 0
tripwire_hook = 0
stick = 0
string = 0
fishing_rod_damaged = 0
ink_sac = 0
bow_enchanted = 0
fishing_rod_enchanted = 0
enchanted_book = 0
name_tag = 0
nautilus_shell = 0
saddle = 0


frame = Frame()
frame.pack(fill=X)
label = Label(frame, text="Welcome to Fishing in Minecraft!", font=("Arial", 16))
label.pack(pady=20)
label2 = Label(frame, text="0", font=("Arial", 12))
label2.pack(pady=(0, 10))
clicked = 0
click = Button(frame, image = img,command=clicks)
click.pack(pady=10)
label3 = Label(frame, text="Loot: ", font=("Arial", 12))
label3.pack(pady=(0, 10))

frame2 = Frame()
frame2.pack(fill=X, pady=10)
possible_loot = Button(frame2,text="POSSIBLE LOOT",command=loot)
directions = Button(frame2, text="DIRECTIONS",command=direction)
current_loot = Button(frame2,text="LOOT NOW",command=loot_gotten)
exit = Button(frame2, text="Exit",command=win.destroy)

possible_loot.grid(row=1,column=1,padx=20)
directions.grid(row=1,column=2,padx=20)
current_loot.grid(row=1,column=3,padx=20)
exit.grid(row=2,column=2)

win.mainloop()
