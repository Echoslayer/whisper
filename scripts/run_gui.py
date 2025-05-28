import os
import sys
import tkinter as tk

# Add the scripts directory to the path so we can import the GUI
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from gui import TranscriptionGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = TranscriptionGUI(root)
    root.mainloop()
