import os
import PyPDF2
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

def get_first_page_text(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        if len(reader.pages) > 0:
            first_page = reader.pages[0]
            text = first_page.extract_text()
            text = text.replace('\n', ' ')
            text = text.replace('\r', ' ')  # Remove carriage returns
            text = text.replace(' ', '_')
            return text	
        
    return ""

def rename_pdf(old_path, new_name):
    directory = os.path.dirname(old_path)
    new_path = os.path.join(directory, new_name + ".pdf")
    os.rename(old_path, new_path)
    print(f"Renamed '{old_path}' to '{new_path}'")

def process_pdfs(folder_path):
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    for pdf_file in pdf_files:
        old_path = os.path.join(folder_path, pdf_file)
        first_page_text = get_first_page_text(old_path)
        
        # Tkinter GUI for user input
        def on_submit():
            new_name = entry.get()
            if not new_name:
                messagebox.showwarning("Warning", "No new name provided. File not renamed.")

        root = tk.Tk()
        root.title(f"Rename PDF: {pdf_file}")
        
        text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=5)
        text_box.insert(tk.END, first_page_text)
        text_box.config(state=tk.DISABLED)
        text_box.pack(pady=10)

        label = tk.Label(root, text="Enter new name (without .pdf):")
        label.pack(pady=5)

        entry = tk.Entry(root, width=50)
        entry.pack(pady=5)

        submit_button = tk.Button(root, text="OK", command=on_submit)
        submit_button.pack(pady=10)

        root.mainloop()

if __name__ == "__main__":
    folder_path = r"C:\Users\Hendr\OneDrive\Desktop\statistik"  # Replace with the path to your folder containing PDFs
    process_pdfs(folder_path)