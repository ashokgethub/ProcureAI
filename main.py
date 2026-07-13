import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class ProcureAI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("ProcureAI v0.3")
        self.geometry("1200x700")

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(
            self.sidebar,
            text="📦 ProcureAI",
            font=("Arial", 24, "bold")
        ).pack(pady=25)

        menu = [
            "🏠 Dashboard",
            "🏢 Vendors",
            "📨 RFQs",
            "💰 Quotations",
            "🛒 Purchase Orders",
            "🧾 Invoices",
            "💳 Payments",
            "📦 BOM Manager",
            "📊 Reports",
            "🤖 AI Assistant",
            "⚙ Settings"
        ]

        for item in menu:
            ctk.CTkButton(
                self.sidebar,
                text=item,
                width=180
            ).pack(pady=5)

        # Main Area
        self.main = ctk.CTkFrame(self)
        self.main.pack(side="right", fill="both", expand=True)

        ctk.CTkLabel(
            self.main,
            text="Dashboard",
            font=("Arial", 30, "bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            self.main,
            text="Welcome Ashok 👋",
            font=("Arial", 20)
        ).pack()

        cards = ctk.CTkFrame(self.main)
        cards.pack(pady=30)

        data = [
            ("Pending RFQs", "0"),
            ("Open POs", "0"),
            ("Pending Payments", "₹0"),
            ("Monthly Spend", "₹0")
        ]

        for title, value in data:
            card = ctk.CTkFrame(cards, width=180, height=120)
            card.pack(side="left", padx=10)
            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=title,
                font=("Arial", 15, "bold")
            ).pack(pady=(20, 5))

            ctk.CTkLabel(
                card,
                text=value,
                font=("Arial", 24)
            ).pack()


app = ProcureAI()
app.mainloop()