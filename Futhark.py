import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

# Define Futhark values in a septimal system
futhark_values = {
    'f': 1, 'u': 2, 't': 3, 'h': 4, 'a': 5, 'r': 6, 'k': 7,
    'g': 1, 'w': 2, 'n': 3, 'i': 4, 'j': 5, 'y': 6, 'ei': 7, 
    'p': 1, 'z': 2, 's': 3, 'b': 4, 'm': 5, 'l': 6, 'd': 7, 
    'o': 1, 'th': 2, 'c': 3, 'q': 4, 'x': 5, 'v': 6, 'ng':7,
}

def load_dictionary():
    """Load the English-Old Norse dictionary from a CSV file."""
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return
    
    global dictionary, reverse_dictionary
    dictionary = {}
    reverse_dictionary = {}
    
    try:
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            english, norse = str(row["English"]).strip().lower(), str(row["Norse"]).strip().lower()
            dictionary[english] = norse
            
            if norse in reverse_dictionary:
                reverse_dictionary[norse].add(english)
            else:
                reverse_dictionary[norse] = {english}
        
        messagebox.showinfo("Success", "Dictionary loaded successfully from CSV!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load dictionary: {e}")

def calculate_isopsephy(norse_word):
    """Calculate the isopsephy value for a given Norse word."""
    total = 0
    word = norse_word.lower()
    i = 0
    while i < len(word):
        if i < len(word) - 1 and word[i:i+2] in futhark_values:
            total += futhark_values[word[i:i+2]]
            i += 2
        elif word[i] in futhark_values:
            total += futhark_values[word[i]]
            i += 1
        else:
            i += 1
    return total

def process_english_word():
    """Find Norse equivalent and calculate its isopsephy value."""
    english_word = entry_english.get().lower()
    if not dictionary:
        messagebox.showerror("Error", "Please load the dictionary first!")
        return
    
    if english_word not in dictionary:
        messagebox.showerror("Error", "Word not found in dictionary!")
        return
    
    norse_word = dictionary[english_word]
    isopsephy_value = calculate_isopsephy(norse_word)
    
    result_text.insert(tk.END, f"English: {english_word} -> Norse: {norse_word} -> Isopsephy: {isopsephy_value}\n")

def process_norse_word():
    """Find English equivalents and calculate isopsephy value."""
    norse_word = entry_norse.get().lower()
    if not norse_word:
        messagebox.showerror("Error", "Please enter a Norse word!")
        return
    
    isopsephy_value = calculate_isopsephy(norse_word)
    matching_english_words = reverse_dictionary.get(norse_word, [])
    
    if matching_english_words:
        result_text.insert(tk.END, f"Norse: {norse_word} -> English: {', '.join(matching_english_words)} -> Isopsephy: {isopsephy_value}\n")
    else:
        result_text.insert(tk.END, f"Norse: {norse_word} -> No English words found -> Isopsephy: {isopsephy_value}\n")

def process_numerical_value():
    """Find words that match the entered numerical value."""
    try:
        num_value = int(entry_numerical.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numerical value!")
        return
    
    matching_words = [word for word, norse in dictionary.items() if calculate_isopsephy(norse) == num_value]
    if matching_words:
        result_text.insert(tk.END, f"Words matching {num_value}: {', '.join(matching_words)}\n")
    else:
        result_text.insert(tk.END, f"No words found with isopsephy value {num_value}\n")

# GUI Setup
root = tk.Tk()
root.title("English-Old Norse Isopsephy Calculator")
root.geometry("600x400")

dictionary = {}
reverse_dictionary = {}

btn_load = tk.Button(root, text="Load Dictionary", command=load_dictionary)
btn_load.pack(pady=5)

label_english = tk.Label(root, text="Enter English word:")
label_english.pack()
entry_english = tk.Entry(root)
entry_english.pack()
btn_convert_english = tk.Button(root, text="Convert", command=process_english_word)
btn_convert_english.pack(pady=5)

label_norse = tk.Label(root, text="Enter Norse word:")
label_norse.pack()
entry_norse = tk.Entry(root)
entry_norse.pack()
btn_convert_norse = tk.Button(root, text="Convert", command=process_norse_word)
btn_convert_norse.pack(pady=5)

label_numerical = tk.Label(root, text="Enter Numerical Value:")
label_numerical.pack()
entry_numerical = tk.Entry(root)
entry_numerical.pack()
btn_find_number = tk.Button(root, text="Find Words", command=process_numerical_value)
btn_find_number.pack(pady=5)

result_text = tk.Text(root, height=10, width=70)
result_text.pack()

root.mainloop()