import customtkinter as ctk
from vendors import VendorsPage


# -----------------------------
# App Settings
# -----------------------------
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


# -----------------------------
# Dashboard Page
# -----------------------------
class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=30)

        welcome = ctk.CTkLabel(
            self,
            text="Welcome Ashok 👋",
            font=("Arial", 20)
        )
        welcome.pack()

        cards_frame = ctk.CTkFrame(self)
        cards_frame.pack(pady=40)

        cards = [
            ("Pending RFQs", "0"),
            ("Open POs", "0"),
            ("Pending Payments", "₹0"),
            ("Monthly Spend", "₹0")
        ]

        for name, value in cards:
            card = ctk.CTkFrame(
                cards_frame,
                width=180,
                height=120
            )
            card.pack(side="left", padx=10)
            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=name,
                font=("Arial", 15, "bold")
            ).pack(pady=(20, 5))

            ctk.CTkLabel(
                card,
                text=value,
                font=("Arial", 25)
            ).pack()


# -----------------------------
# Simple Module Pages
# -----------------------------
class ModulePage(ctk.CTkFrame):

    def __init__(self, parent, title):
        super().__init__(parent)

        ctk.CTkLabel(
            self,
            text=title,
            font=("Arial", 30, "bold")
        ).pack(pady=50)

        ctk.CTkLabel(
            self,
            text="Module coming soon 🚀",
            font=("Arial", 18)
        ).pack()


# -----------------------------
# Main Application
# -----------------------------
class ProcureAI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("ProcureAI v0.4")
        self.geometry("1200x700")

        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )
        self.sidebar.pack(
            side="left",
            fill="y"
        )

        ctk.CTkLabel(
            self.sidebar,
            text="📦 ProcureAI",
            font=("Arial", 24, "bold")
        ).pack(pady=25)


        # Main area
        self.main = ctk.CTkFrame(self)
        self.main.pack(
            side="right",
            fill="both",
            expand=True
        )


        # Menu buttons
        menu = [
            ("🏠 Dashboard", self.show_dashboard),
            ("🏢 Vendors", self.show_vendors),
            ("📨 RFQs", self.show_rfqs),
            ("💰 Quotations", self.show_quotations),
            ("🛒 Purchase Orders", self.show_po),
            ("🧾 Invoices", self.show_invoices),
            ("💳 Payments", self.show_payments),
            ("📦 BOM Manager", self.show_bom),
            ("📊 Reports", self.show_reports),
            ("🤖 AI Assistant", self.show_ai),
            ("⚙ Settings", self.show_settings)
        ]


        for text, command in menu:

            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                width=180,
                height=40,
                command=command
            )

            btn.pack(pady=5)


        # Start page
        self.show_dashboard()


    # Clear current page
    def clear_page(self):

        for widget in self.main.winfo_children():
            widget.destroy()


    # Pages

    def show_dashboard(self):
        self.clear_page()
        DashboardPage(self.main).pack(
            fill="both",
            expand=True
        )


    def show_vendors(self):
        self.clear_page()

        VendorsPage(self.main).pack(
            fill="both",
            expand=True
        )


    def show_rfqs(self):
        self.clear_page()
        ModulePage(
            self.main,
            "📨 RFQ Management"
        ).pack(fill="both", expand=True)


    def show_quotations(self):
        self.clear_page()
        ModulePage(
            self.main,
            "💰 Quotations"
        ).pack(fill="both", expand=True)


    def show_po(self):
        self.clear_page()
        ModulePage(
            self.main,
            "🛒 Purchase Orders"
        ).pack(fill="both", expand=True)


    def show_invoices(self):
        self.clear_page()
        ModulePage(
            self.main,
            "🧾 Invoice Tracker"
        ).pack(fill="both", expand=True)


    def show_payments(self):
        self.clear_page()
        ModulePage(
            self.main,
            "💳 Payments"
        ).pack(fill="both", expand=True)


    def show_bom(self):
        self.clear_page()
        ModulePage(
            self.main,
            "📦 BOM Manager"
        ).pack(fill="both", expand=True)


    def show_reports(self):
        self.clear_page()
        ModulePage(
            self.main,
            "📊 Reports"
        ).pack(fill="both", expand=True)


    def show_ai(self):
        self.clear_page()
        ModulePage(
            self.main,
            "🤖 AI Assistant"
        ).pack(fill="both", expand=True)


    def show_settings(self):
        self.clear_page()
        ModulePage(
            self.main,
            "⚙ Settings"
        ).pack(fill="both", expand=True)



# Run App
app = ProcureAI()
app.mainloop()