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
            columns=("MPN", "Qty", "Unit Price", "Total"),
            show="headings"
        )

        self.table.heading("MPN", text="MPN")
        self.table.heading("Qty", text="Quantity")
        self.table.heading("Unit Price", text="Unit Price")
        self.table.heading("Total", text="Total")

        self.table.column("MPN", width=350)
        self.table.column("Qty", width=100)
        self.table.column("Unit Price", width=120)
        self.table.column("Total", width=120)

        self.table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.total_label = ctk.CTkLabel(
            self,
            text="Grand Total: ₹0",
            font=("Arial", 18, "bold")
        )

        self.total_label.pack(pady=10)
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

            if qty is None:
                qty = 0

            unit_price = 0
            total = qty * unit_price

            self.table.insert(
                "",
                "end",
                values=(
                    mpn,
                    qty,
                    unit_price,
                    total
                )
            )

        self.calculate_total()            

        messagebox.showinfo(
            "Success",
            "BOM Imported Successfully"
        )

    def calculate_total(self):

        grand_total = 0

        for row in self.table.get_children():

            values = self.table.item(row)["values"]

            if len(values) >= 4:
                grand_total += float(values[3])

        self.total_label.configure(
            text=f"Grand Total: ₹{grand_total:,.2f}"
        )