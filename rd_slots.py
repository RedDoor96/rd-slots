import tkinter as tk
import ttkbootstrap as ttk
import numpy as np
import os

root = tk.Tk()
root.title('slots')
root.geometry('700x700')
base_dir = os.path.dirname(__file__)
image_path = os.path.join(base_dir, "rd_slots_logo.png")
icon = tk.PhotoImage(file=image_path)
root.iconphoto(True, icon)
rng = np.random.default_rng()

slots_data = np.array([
'🍒',
'💎','💎',
'👑','👑','👑',
'🍉','🍉','🍉','🍉',
'💸','💸','💸','💸','💸',
'🍇','🍇','🍇','🍇','🍇','🍇',
'🍓','🍓','🍓','🍓','🍓','🍓','🍓',
'🍌','🍌','🍌','🍌','🍌','🍌','🍌','🍌'])

tk_slots_data = tk.StringVar()
score_data = tk.IntVar(value=100)
betting_amount = tk.IntVar(value=10)

def score():
    try:
        if score_data.get() - betting_amount.get() >= 0:
            score_data.set(score_data.get() - betting_amount.get())
            current_value = rng.choice(slots_data, size=(3,3))
            diag1 = np.diag(current_value)
            diag2 = np.diag(np.fliplr(current_value))

            def scoring_data(emoji, score):
                if np.any(np.all(current_value == emoji, axis=1)) or np.any(np.all(current_value == emoji, axis=0)) or np.all(diag1 == emoji) or np.all(diag2 == emoji):        
                    score_data.set(score_data.get() + score)

            scoring_data('🍌',betting_amount.get() * 2)
            scoring_data('🍓',betting_amount.get() * 3)
            scoring_data('🍇',betting_amount.get() * 5)
            scoring_data('💸',betting_amount.get() * 10)
            scoring_data('🍉',betting_amount.get() * 15)
            scoring_data('👑',betting_amount.get() * 20)
            scoring_data('💎',betting_amount.get() * 30)
            scoring_data('🍒',betting_amount.get() * 50)

            tk_slots_data.set('\n'.join(' '.join(row) for row in current_value))    
    except TypeError:
        pass



slot_dispaly = ttk.Label(root,textvariable=tk_slots_data, font='FreeMono 50 bold')
betting_entry = ttk.Entry(root, textvariable=betting_amount)
reroll_button = ttk.Button(root, text='play', command=score)
score_display = ttk.Label(root,textvariable=score_data, font='FreeMono 100 bold')

score_display.pack()
slot_dispaly.pack(anchor='center', expand=True)
betting_entry.pack()
reroll_button.pack(pady=10)


root.mainloop()
