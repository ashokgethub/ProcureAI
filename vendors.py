import customtkinter as ctk
from tkinter import ttk, messagebox
import openpyxl


class VendorsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.vendors = []

        # Title
        ctk.CTkLabel(
            self,
            text="🏢 Vendor Management",
            font=("Arial", 30, "bold")
        ).pack(pady=20)

        # Form Frame
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

            label = ctk.CTkLabel(
                form,
                text=field
            )
            label.grid(
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


        # Buttons

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=15)


        ctk.CTkButton(
            button_frame,
            text="➕ Add Vendor",
            command=self.add_vendor
        ).pack(
            side="left",
            padx=10
        )


        ctk.CTkButton(
            button_frame,
            text="📤 Export Excel",
            command=self.export_excel
        ).pack(
            side="left",
            padx=10
        )


        # Table

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
            self.table.heading(
                col,
                text=col
            )


        self.table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )


    def add_vendor(self):

        data = {}

        for field, entry in self.fields.items():
            data[field] = entry.get()


        if data["Vendor Name"] == "":
            messagebox.showwarning(
                "Missing Information",
                "Vendor Name is required"
            )
            return


        self.vendors.append(data)


        self.table.insert(
            "",
            "end",
            values=(
                data["Vendor Name"],
                data["Category"],
                data["Contact Person"],
                data["Phone Number"],
                data["Payment Terms"]
            )
        )


        for entry in self.fields.values():
            entry.delete(0, "end")


        messagebox.showinfo(
            "Success",
            "Vendor Added Successfully"
        )


    def export_excel(self):

        workbook = openpyxl.Workbook()

        sheet = workbook.active
        sheet.title = "Vendors"


        headers = list(self.fields.keys())

        sheet.append(headers)


        for vendor in self.vendors:
            sheet.append(
                list(vendor.values())
            )


        workbook.save(
            "Vendor_List.xlsx"
        )


        messagebox.showinfo(
            "Export Complete",
            "Vendor_List.xlsx created"
        )