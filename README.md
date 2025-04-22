This is a simple GUI application that allows users to explore isopsephy (letter-to-number conversion) based on the Futhark rune system, applied to English-Old Norse word pairs.

This tool is useful for students of ancient languages, cryptographers, or anyone interested in historical linguistics and numerological systems.
📜 What is Isopsephy?

Isopsephy is the practice of assigning numerical values to letters and calculating the total value of a word. This concept is similar to gematria in Hebrew or Greek isopsephy, and this app applies it to reconstructed Old Norse using a Futhark-inspired system.
🛠 Features

    Load a custom English ↔ Old Norse dictionary (CSV file).

    Convert English words to Norse equivalents and get their isopsephy value.

    Input Norse words directly and:

        View their isopsephy values.

        Find all matching English translations (if available).

    Enter a numerical value to find all English words whose Norse equivalent equals that value.

📁 CSV Dictionary Format

The program accepts a .csv file with the following columns:

English,Norse
hello,heill
war,bardagi
...

Make sure headers are included, and that both values are lowercase or properly formatted.
🔢 Futhark Letter Values

The program uses a custom septimal (1–7) value system for runes:

Row 1: f=1, u=2, t=3, h=4, a=5, r=6, k=7  
Row 2: g=1, w=2, n=3, i=4, j=5, y=6, ei=7  
Row 3: p=1, z=2, s=3, b=4, m=5, l=6, d=7  
Row 4: o=1, th=2, c=3, q=4, x=5, v=6, ng=7  

Multi-letter rune combinations (th, ei, ng) are treated as atomic units when parsing.
🖥 How to Use
🏃‍♂️ Run the App

    Ensure you have Python installed.

    Required libraries: tkinter (built-in), pandas

    Run the script:

    python isopsephy_gui.py

🧰 Interface Breakdown

    Load Dictionary
    Click this first to import your English↔Norse CSV dictionary.

    Convert English Word
    Enter an English word → find its Norse equivalent → calculate isopsephy.

    Convert Norse Word
    Enter a Norse word directly → calculate its isopsephy → list any matching English terms.

    Find Words by Value
    Input a number to retrieve all English words whose Norse forms match that isopsephy value.

    Output Box
    Displays results, values, and messages.

🚨 Notes

    Words not found in the dictionary will prompt an error.

    The matching logic is case-insensitive.

    The system skips unknown letters (those not defined in futhark_values).

📦 Dependencies

    Python 3.6+

    pandas library

Install pandas if you haven’t already:

pip install pandas

📄 License

MIT License. Use it freely in personal or academic projects. Attribution appreciated!
✍️ Author

Created by 23.777 via AI
Feel free to contribute, fork, or submit issues and enhancements.
