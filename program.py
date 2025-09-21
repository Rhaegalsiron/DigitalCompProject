import tkinter as tk
from tkinter import messagebox, PhotoImage
import sqlite3
from tkinter import ttk
import os

class ECommerceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple E-Commerce program")
        self.root.geometry("800x600")
        
        # Set default background and foreground colors
        self.root.configure(bg='black')
        self.style = ttk.Style()
        self.style.configure('TFrame', background='black')
        self.style.configure('TLabel', background='black', foreground='white')
        self.style.configure('TButton', background='black', foreground='white')
        
        # Create images directory if it doesn't exist
        if not os.path.exists('images'):
            os.makedirs('images')
    
        # Initialize database
        self.init_database()
        
        # User state
        self.current_user = None
        self.cart = []
        self.current_total = 0.0  # Add this line
        self.discount_amount = 0.0  # Add this line
        
        # Show login page first
        self.show_login_page()

    def init_database(self):
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        
        # Create tables
        c.execute('''CREATE TABLE IF NOT EXISTS users
                    (username TEXT PRIMARY KEY, password TEXT)''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS products
                    (id INTEGER PRIMARY KEY, 
                     name TEXT, 
                     price REAL,
                     category TEXT,
                     image_path TEXT)''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS discount_codes
                    (code TEXT PRIMARY KEY, 
                     discount_type TEXT,
                     value REAL)''')
        
        # Check if products already exist
        c.execute("SELECT COUNT(*) FROM products")
        product_count = c.fetchone()[0]
        
        # Only insert sample data if the products table is empty
        if product_count == 0:
            try:
                # Electronics
                c.execute("INSERT INTO products (name, price, category, image_path) VALUES ('iPhone 17 Pro', 1299.99, 'Electronics', 'images/iphone17pro.png')")
                c.execute("INSERT INTO products (name, price, category, image_path) VALUES ('Logitech G Pro X Wireless', 149.99, 'Electronics', 'images/logitechg.png')")
                c.execute("INSERT INTO products (name, price, category, image_path) VALUES ('Gaming Monitor', 249.99, 'Electronics', 'images/monitor.png')")
                c.execute("INSERT INTO products (name, price, category, image_path) VALUES ('Laptop', 1199.99, 'Electronics', 'images/laptop.png')")
                
                # Accessories
                c.execute("INSERT INTO products (name, price, category, image_path) VALUES ('USB-C Charger', 39.99, 'Accessories', 'images/charger.png')")
                c.execute("INSERT INTO products (name, price, category, image_path) VALUES ('Mechanical Keyboard', 89.99, 'Accessories', 'images/keyboard.png')")
                c.execute("INSERT INTO products (name, price, category, image_path) VALUES ('Bluetooth Speaker', 59.99, 'Accessories', 'images/speaker.png')")
                
                # Storage
                c.execute("INSERT INTO products (name, price, category, image_path) VALUES ('External Hard Drive', 129.99, 'Storage', 'images/hdd.png')")
                c.execute("INSERT INTO products (name, price, category, image_path) VALUES ('USB Flash Drive', 29.99, 'Storage', 'images/usb.png')")
                
                # Toys
                c.execute("INSERT INTO products (name, price, category, image_path) VALUES ('Blahaj', 10.00, 'Toys', 'images/blahaj.png')")
                c.execute("INSERT INTO products (name, price, category, image_path) VALUES ('Plush Bear', 24.99, 'Toys', 'images/bear.png')")
                
                # Discount codes
                c.execute("INSERT INTO discount_codes (code, discount_type, value) VALUES ('SAVE10', 'PERCENT', 10)")
                c.execute("INSERT INTO discount_codes (code, discount_type, value) VALUES ('DISCOUNT10', 'PERCENT', 10)")
                c.execute("INSERT INTO discount_codes (code, discount_type, value) VALUES ('DISCOUNT01', 'FIXED', 1)")
                c.execute("INSERT INTO discount_codes (code, discount_type, value) VALUES ('FREESTUFF!!', 'FREE', 0)")
                
                conn.commit()
            except sqlite3.IntegrityError:
                pass
        
        conn.close()

    def create_logo(self, parent):
        """Create and return a new logo label"""
        logo_frame = tk.Frame(parent, bg='black')
        logo_label = tk.Label(logo_frame, 
                             text="E$", 
                             font=("Arial", 48, "bold"),
                             fg="#2ecc71",
                             bg='black')  # Keep logo green but with black background
        return logo_frame, logo_label

    def show_login_page(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Main frame with padding
        main_frame = tk.Frame(self.root, pady=50, bg='black')
        main_frame.pack(expand=True)
        
        # Create new logo for this page
        logo_frame, logo_label = self.create_logo(main_frame)
        logo_frame.pack(pady=(0, 30))
        logo_label.pack()
        
        # Login frame with modern styling and visible white border
        login_frame = tk.Frame(main_frame, 
                          relief=tk.SOLID,  # Changed from RAISED to SOLID
                          borderwidth=2,    # Increased from 1 to 2
                          bg='black',
                          highlightbackground='white',  # Add white border
                          highlightthickness=1)        # Border thickness
        login_frame.pack(padx=20, pady=20, ipadx=20, ipady=20)
        
        # Title
        tk.Label(login_frame, text="Login", font=("Helvetica", 16, "bold"), 
                bg='black', fg='white').pack(pady=(0, 20))
        
        # Username
        tk.Label(login_frame, text="Username:", font=("Helvetica", 10),
                bg='black', fg='white').pack()
        self.username_entry = tk.Entry(login_frame, width=30, bg='black', fg='white',
                                     insertbackground='white')
        self.username_entry.pack(pady=(0, 10))
        
        # Password
        tk.Label(login_frame, text="Password:", font=("Helvetica", 10),
                bg='black', fg='white').pack()
        self.password_entry = tk.Entry(login_frame, show="*", width=30, bg='black', 
                                     fg='white', insertbackground='white')
        self.password_entry.pack(pady=(0, 20))
        
        # Buttons
        button_frame = tk.Frame(login_frame, bg='black')
        button_frame.pack(pady=10)
        
        login_btn = tk.Button(button_frame, text="Login", command=self.login,
                             width=15, relief=tk.RAISED, bg='black', fg='white')
        login_btn.pack(side=tk.LEFT, padx=5)
        
        register_btn = tk.Button(button_frame, text="Create Account",
                               command=self.show_register_page, width=15,
                               bg='black', fg='white')
        register_btn.pack(side=tk.LEFT, padx=5)

    def show_register_page(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Main frame
        main_frame = tk.Frame(self.root, pady=50, bg='black')  # Added bg='black'
        main_frame.pack(expand=True)
        
        # Create new logo for this page
        logo_frame, logo_label = self.create_logo(main_frame)
        logo_frame.pack(pady=(0, 30))
        logo_label.pack()
        
        # Register frame with modern styling and visible white border
        register_frame = tk.Frame(main_frame, 
                            relief=tk.SOLID,
                            borderwidth=2,
                            bg='black',
                            highlightbackground='white',
                            highlightthickness=1)
        register_frame.pack(padx=20, pady=20, ipadx=20, ipady=20)
        
        # Title
        tk.Label(register_frame, text="Create Account", 
                font=("Helvetica", 16, "bold"),
                bg='black', fg='white').pack(pady=(0, 20))  # Added colors
    
        # Username
        tk.Label(register_frame, text="Username:", 
                font=("Helvetica", 10),
                bg='black', fg='white').pack()  # Added colors
        self.username_entry = tk.Entry(register_frame, width=30,
                                     bg='black', fg='white',
                                     insertbackground='white')  # Added colors
        self.username_entry.pack(pady=(0, 10))
        
        # Password
        tk.Label(register_frame, text="Password:", 
                font=("Helvetica", 10),
                bg='black', fg='white').pack()  # Added colors
        self.password_entry = tk.Entry(register_frame, show="*", width=30,
                                     bg='black', fg='white',
                                     insertbackground='white')  # Added colors
        self.password_entry.pack(pady=(0, 20))
        
        # Buttons
        button_frame = tk.Frame(register_frame, bg='black')  # Added bg='black'
        button_frame.pack(pady=10)
        
        register_btn = tk.Button(button_frame, text="Register",
                           command=self.register, width=15,
                           bg='black', fg='white')  # Added colors
        register_btn.pack(side=tk.LEFT, padx=5)
        
        back_btn = tk.Button(button_frame, text="Back to Login",
                       command=self.show_login_page, width=15,
                       bg='black', fg='white')  # Added colors
        back_btn.pack(side=tk.LEFT, padx=5)

    def show_store_page(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
    
        # Top frame for logo and welcome message
        top_frame = tk.Frame(self.root)
        top_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Welcome message on left
        tk.Label(top_frame, text=f"Welcome, {self.current_user}!",
                font=("Helvetica", 12, "bold")).pack(side=tk.LEFT)
        
        # Create new logo for this page
        logo_frame, logo_label = self.create_logo(top_frame)
        logo_frame.pack(side=tk.RIGHT)
        logo_label.pack()
        
        # Main store frame
        store_frame = tk.Frame(self.root)
        store_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Add category filter
        filter_frame = tk.Frame(store_frame)
        filter_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(filter_frame, text="Filter by category:", 
                font=("Helvetica", 10)).pack(side=tk.LEFT, padx=(0, 10))
        
        # Get unique categories
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        c.execute("SELECT DISTINCT category FROM products ORDER BY category")
        categories = [row[0] for row in c.fetchall()]
        
        # Category variable for radiobuttons
        self.selected_category = tk.StringVar(value="All")
        
        # All categories radio button
        tk.Radiobutton(filter_frame, text="All", variable=self.selected_category,
                      value="All", command=self.filter_products).pack(side=tk.LEFT)
        
        # Category specific radio buttons
        for category in categories:
            tk.Radiobutton(filter_frame, text=category, variable=self.selected_category,
                          value=category, command=self.filter_products).pack(side=tk.LEFT)
        
        # Products section
        products_frame = tk.LabelFrame(store_frame, text="Available Products",
                                     font=("Helvetica", 11))
        products_frame.pack(fill=tk.X, pady=10)
        
        # Create scrollable frame for products
        canvas = tk.Canvas(products_frame)
        scrollbar = ttk.Scrollbar(products_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Initial product loading
        self.filter_products()
        
        # Configure scrollbar
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_frame.bind("<Configure>", 
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Cart section
        cart_frame = tk.LabelFrame(store_frame, text="Shopping Cart",
                                 font=("Helvetica", 11))
        cart_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.cart_listbox = tk.Listbox(cart_frame, font=("Helvetica", 10))
        self.cart_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Bottom frame for discount and checkout
        bottom_frame = tk.Frame(store_frame, bg='black')
        bottom_frame.pack(fill=tk.X, pady=10)
        
        # Discount section
        discount_frame = tk.Frame(bottom_frame, bg='black')
        discount_frame.pack(side=tk.LEFT)
        
        tk.Label(discount_frame, text="Discount Code:",
                font=("Helvetica", 10), bg='black', fg='white').pack(side=tk.LEFT)
        self.discount_entry = tk.Entry(discount_frame, bg='black', fg='white',
                                 insertbackground='white')
        self.discount_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(discount_frame, text="Apply",
                 command=self.apply_discount,
                 bg='black', fg='white').pack(side=tk.LEFT)
        
        # Total price display frame
        total_frame = tk.Frame(bottom_frame, bg='black')
        total_frame.pack(side=tk.RIGHT, padx=10)
        
        self.total_label = tk.Label(total_frame, 
                               text="Total: $0.00",
                               font=("Helvetica", 12, "bold"),
                               bg='black', fg='white')
        self.total_label.pack(side=tk.TOP, pady=5)
        
        self.discount_label = tk.Label(total_frame,
                                 text="Discount: -$0.00",
                                 font=("Helvetica", 10),
                                 bg='black', fg='#2ecc71')  # Green color for discount
        self.discount_label.pack(side=tk.TOP)
        
        self.final_total_label = tk.Label(total_frame,
                                    text="Final Total: $0.00",
                                    font=("Helvetica", 12, "bold"),
                                    bg='black', fg='#2ecc71')
        self.final_total_label.pack(side=tk.TOP, pady=5)
        
        # Checkout button
        tk.Button(bottom_frame, text="Checkout",
                 command=self.checkout, width=20,
                 bg='black', fg='white').pack(side=tk.RIGHT)

    def filter_products(self):
        # Clear existing products
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        # Get filtered products
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        
        if self.selected_category.get() == "All":
            c.execute("SELECT * FROM products ORDER BY category, name")
        else:
            c.execute("SELECT * FROM products WHERE category=? ORDER BY name", 
                     (self.selected_category.get(),))
        
        products = c.fetchall()
        
        # Add products to scrollable frame
        current_category = None
        for product in products:
            if current_category != product[3]:  # New category
                current_category = product[3]
                tk.Label(self.scrollable_frame, text=current_category,
                        font=("Helvetica", 12, "bold")).pack(pady=(10, 5))
            
            product_frame = tk.Frame(self.scrollable_frame)
            product_frame.pack(pady=5, fill=tk.X)
            
            # Try to load and display product image
            try:
                img = PhotoImage(file=product[4])
                img = img.subsample(4, 4)  # Resize image
                img_label = tk.Label(product_frame, image=img)
                img_label.image = img  # Keep a reference!
            except:
                img_label = tk.Label(product_frame, text="[IMG]", width=5)
            img_label.pack(side=tk.LEFT, padx=5)
            
            tk.Label(product_frame, text=f"{product[1]}",
                    font=("Helvetica", 10)).pack(side=tk.LEFT)
            tk.Label(product_frame, text=f"${product[2]:.2f}",
                    font=("Helvetica", 10)).pack(side=tk.LEFT, padx=10)
            tk.Button(product_frame, text="Add to Cart",
                     command=lambda p=product: self.add_to_cart(p)).pack(side=tk.RIGHT)
        
        conn.close()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        
        if c.fetchone():
            self.current_user = username
            self.show_store_page()
        else:
            messagebox.showerror("Error", "Invalid credentials")
        
        conn.close()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")
        conn.close()

    def add_to_cart(self, product):
        self.cart.append(product)
        self.cart_listbox.insert(tk.END, f"{product[1]} - ${product[2]}")
        self.update_total_display()  # Update totals when adding items

    def update_total_display(self):
        # Calculate raw total
        self.current_total = sum(product[2] for product in self.cart)
        
        # Update labels
        self.total_label.config(text=f"Total: ${self.current_total:.2f}")
        self.discount_label.config(text=f"Discount: -${self.discount_amount:.2f}")
        final_total = max(0, self.current_total - self.discount_amount)
        self.final_total_label.config(text=f"Final Total: ${final_total:.2f}")

    def apply_discount(self):
        if not self.cart:
            messagebox.showerror("Error", "Cart is empty!")
            return
            
        code = self.discount_entry.get()
        conn = sqlite3.connect('ecommerce.db')
        c = conn.cursor()
        c.execute("SELECT discount_type, value FROM discount_codes WHERE code=?", (code,))
        result = c.fetchone()
        
        total = sum(product[2] for product in self.cart)
        
        if result:
            discount_type, value = result
            if discount_type == 'PERCENT':
                self.discount_amount = total * (value / 100)
                messagebox.showinfo("Success", f"Discount of {value}% applied!")
            elif discount_type == 'FIXED':
                self.discount_amount = value
                messagebox.showinfo("Success", f"Discount of ${value:.2f} applied!")
            elif discount_type == 'FREE':
                self.discount_amount = total
                messagebox.showinfo("Success", "Everything is free!")
            self.update_total_display()
        else:
            messagebox.showerror("Error", "Invalid discount code")
    
        conn.close()

    def checkout(self):
        if not self.cart:
            messagebox.showinfo("Info", "Cart is empty!")
            return
            
        final_total = max(0, self.current_total - self.discount_amount)
        messagebox.showinfo("Checkout", f"Final amount to pay: ${final_total:.2f}")
        self.cart = []
        self.cart_listbox.delete(0, tk.END)
        self.current_total = 0.0
        self.discount_amount = 0.0
        self.update_total_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = ECommerceApp(root)
    root.mainloop()