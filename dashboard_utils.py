import pandas as pd
from tkinter import filedialog
from tkinter import ttk
import os
import tkinter as tk
from tkinter import messagebox
import csv


def open_csv_editor(csv_path, title="CSV Editor"):
    if not os.path.exists(csv_path):
        messagebox.showerror("Error", f"File '{csv_path}' does not exist.")
        return

    editor = tk.Toplevel()
    editor.title(title)
    editor.geometry("900x600")

    # Read CSV
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)

    if not data:
        messagebox.showinfo("Info", "The CSV file is empty.")
        return

    headers = data[0]
    rows = data[1:]

    # Treeview setup
    tree = ttk.Treeview(editor, columns=headers, show="headings")
    for col in headers:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    for row in rows:
        tree.insert("", tk.END, values=row)

    tree.pack(fill=tk.BOTH, expand=True)

    # Editing logic
    def on_double_click(event):
        selected_item = tree.identify_row(event.y)
        selected_column = tree.identify_column(event.x)
        if not selected_item or not selected_column:
            return

        col_index = int(selected_column.replace("#", "")) - 1
        item_values = tree.item(selected_item, "values")

        # Create entry box
        entry_popup = tk.Entry(editor)
        entry_popup.insert(0, item_values[col_index])
        bbox = tree.bbox(selected_item, column=selected_column)
        if not bbox:
            return
        x, y, width, height = bbox
        entry_popup.place(x=x, y=y + tree.winfo_y(), width=width, height=height)

        def save_edit(event):
            new_value = entry_popup.get()
            updated_values = list(item_values)
            updated_values[col_index] = new_value
            tree.item(selected_item, values=updated_values)
            entry_popup.destroy()

        entry_popup.bind("<Return>", save_edit)
        entry_popup.bind("<FocusOut>", lambda e: entry_popup.destroy())
        entry_popup.focus()

    tree.bind("<Double-1>", on_double_click)

    # Save CSV back
    def save_csv():
        updated_data = [headers]
        for row_id in tree.get_children():
            row_values = tree.item(row_id, "values")
            updated_data.append(row_values)

        with open(csv_path, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)

        messagebox.showinfo("Saved", "CSV saved successfully.")
        editor.destroy()

    save_btn = tk.Button(editor, text="💾 Save Changes", command=save_csv, bg="#4CAF50", fg="white", font=("Arial", 12))
    save_btn.pack(pady=10)
