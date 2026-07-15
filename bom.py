import customtkinter as ctk
from tkinter import ttk, filedialog, messagebox
import openpyxl


class BOMPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(
            self,
            text="📦 BOM Manager",
            font=("Arial", 30, "bold")
        ).pack(pady=20)

        ctk.CTkButton(
            self,
            text="📂 Import Excel BOM",
            command=self.import_bom
        ).pack(pady=10)

        self.table = ttk.Treeview(
            self,
            columns=("MPN", "Qty"),
            show="headings"
        )

        self.table.heading("MPN", text="MPN")
        self.table.heading("Qty", text="Quantity")

        self.table.column("MPN", width=400)
        self.table.column("Qty", width=120)

        self.table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def import_bom(self):

        file = filedialog.askopenfilename(
            filetypes=[("Excel Files", "*.xlsx")]
        )

        if not file:
            return

        workbook = openpyxl.load_workbook(file)

        sheet = workbook.active

        for row in self.table.get_children():
            self.table.delete(row)

        for row in sheet.iter_rows(min_row=2, values_only=True):

            mpn = row[0]
            qty = row[1]

            self.table.insert(
                "",
                "end",
                values=(mpn, qty)
            )

        messagebox.showinfo(
            "Success",
            "BOM Imported Successfully"
        )