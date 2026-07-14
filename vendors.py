import customtkinter as ctk
from tkinter import ttk, messagebox
import openpyxl

from app.service.vendor_service import (
    add_vendor,
    get_all_vendors
)


class VendorsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(
            self,
            text="🏢 Vendor Management",
            font=("Arial", 30, "bold")
        ).pack(pady=20)

        form = ctk.CTkFrame(self)
        form.pack(pady=10)

        self.fields = {}

        fields = [
            "Vendor Name",
            "Contact Person",
            "Phone Number",
            "Email",
            "GST Number",
            "PAN Number",
            "Address",
            "Payment Terms",
            "Category",
            "Currency",
            "Bank Details"
        ]

        for i, field in enumerate(fields):

            ctk.CTkLabel(
                form,
                text=field
            ).grid(
                row=i,
                column=0,
                padx=10,
                pady=5,
                sticky="w"
            )

            entry = ctk.CTkEntry(
                form,
                width=250
            )

            entry.grid(
                row=i,
                column=1,
                padx=10,
                pady=5
            )

            self.fields[field] = entry

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=15)

        ctk.CTkButton(
            button_frame,
            text="➕ Add Vendor",
            command=self.add_vendor
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            button_frame,
            text="📤 Export Excel",
            command=self.export_excel
        ).pack(side="left", padx=10)

        self.table = ttk.Treeview(
            self,
            columns=(
                "Name",
                "Category",
                "Contact",
                "Phone",
                "Payment"
            ),
            show="headings"
        )

        for col in self.table["columns"]:
            self.table.heading(col, text=col)

        self.table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.load_vendors()

    def add_vendor(self):

        data = {}

        for field, entry in self.fields.items():
            data[field] = entry.get().strip()

        if data["Vendor Name"] == "":
            messagebox.showwarning(
                "Missing Information",
                "Vendor Name is required"
            )
            return

        # Save to database
        add_vendor(
            data["Vendor Name"],
            data["Contact Person"],
            data["Phone Number"],
            data["Email"],
            data["GST Number"],
            data["PAN Number"],
            data["Address"],
            data["Payment Terms"],
            data["Category"],
            data["Currency"],
            data["Bank Details"]
        )

        # Clear form
        for entry in self.fields.values():
            entry.delete(0, "end")

        # Refresh table
        self.load_vendors()

        messagebox.showinfo(
            "Success",
            "Vendor Added Successfully"
        )

    def load_vendors(self):

        # Remove old rows
        for row in self.table.get_children():
            self.table.delete(row)

        vendors = get_all_vendors()

        for vendor in vendors:
            self.table.insert(
                "",
                "end",
                values=(
                    vendor[1],   # Vendor Name
                    vendor[9],   # Category
                    vendor[2],   # Contact Person
                    vendor[3],   # Phone
                    vendor[8]    # Payment Terms
                )
            )

    def export_excel(self):

        workbook = openpyxl.Workbook()

        sheet = workbook.active
        sheet.title = "Vendors"

        headers = [
            "Vendor Name",
            "Contact Person",
            "Phone Number",
            "Email",
            "GST Number",
            "PAN Number",
            "Address",
            "Payment Terms",
            "Category",
            "Currency",
            "Bank Details"
        ]

        sheet.append(headers)

        vendors = get_all_vendors()

        for vendor in vendors:
            sheet.append(vendor[1:])

        workbook.save("Vendor_List.xlsx")

        messagebox.showinfo(
            "Export Complete",
            "Vendor_List.xlsx created successfully."
        )