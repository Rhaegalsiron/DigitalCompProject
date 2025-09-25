````markdown
# 🛒 Simple E-Commerce Program (Tkinter + SQLite)

**Authors:** HERBERT & Woon (B1u3_)  

A desktop E-Commerce application built with **Python Tkinter** (GUI) and **SQLite** (database).  
Features secure user authentication, product browsing by category, shopping cart, discount codes, and checkout.

---

## ✨ Features

- 🔐 **User Authentication**
  - Register with bcrypt-hashed passwords
  - Login with validation

- 🛍️ **Product Store**
  - Browse by category (Electronics, Accessories, Storage, Toys, etc.)
  - Display product images (PNG)
  - Add to cart

- 🛒 **Shopping Cart**
  - Real-time list of selected products
  - Dynamic total calculation

- 🎟️ **Discount Codes**
  - **PERCENT** – apply % discount (e.g. `SAVE10`)
  - **FIXED** – fixed discount in currency (e.g. `DISCOUNT01`)
  - **FREE** – make everything free (e.g. `FREESTUFF!!`)

- 💳 **Checkout**
  - Calculates final amount after discount
  - Empties cart after confirming checkout

- 🎨 **Dark Theme UI**
  - Black background with white text
  - Green highlight for discount amounts

---

## 🛠️ Requirements & Setup

### Prerequisites

- Python 3.8 or newer  
- `bcrypt` library  

Install dependencies:

```bash
pip install bcrypt
````

### Running the App

1. Clone the repository:

   ```bash
   git clone https://github.com/Rhaegalsiron/DigitalCompProject.git
   cd DigitalCompProject
   ```

2. Run the main script (adjust file name if different):

   ```bash
   python program.py
   ```

   The app will auto-create `ecommerce.db` and the `images/` folder if they don’t exist.

---

## 📁 Project Layout

```
DigitalCompProject/
│
├── program.py           # Main application logic
├── ecommerce.db         # SQLite database (auto-generated)
├── images/              # Product image files (e.g., pngs)
└── README.md            # Project description
```

---

## 🔧 How It Works (Brief)

1. On first launch:

   * Creates SQLite database `ecommerce.db`
   * Builds tables: `users`, `products`, `discount_codes`
   * Inserts sample products and discount codes (if the products table is empty)
   * Ensures `images/` folder exists

2. The app starts at the **login screen**. You may choose to **register** if you don’t have an account.

3. Once logged in, you’re presented with the **store interface**:

   * Filter products by category
   * View images, names, and prices
   * Add to cart

4. In the cart section:

   * View the list of added items
   * Enter a discount code and apply it
   * See updated totals

5. Click **Checkout** to finalize:

   * Displays final amount
   * Clears the cart for a new session

---

## 📋 Sample Discount Codes

| Code          | Type    | Value | Description                |
| ------------- | ------- | ----- | -------------------------- |
| `SAVE10`      | PERCENT | 10    | 10% off the total          |
| `DISCOUNT10`  | PERCENT | 10    | 10% off the total          |
| `DISCOUNT01`  | FIXED   | 1     | \$1 off the total          |
| `FREESTUFF!!` | FREE    | —     | Everything becomes free 🎉 |

---

## ⚠️ Notes & Caveats

* Ensure that product images (PNG) are placed correctly inside the `images/` folder for them to display.
* Sample products & discount codes are only inserted when the `products` table is empty.
* This app is intended for **demonstration / educational use**, not production use.

---

## 📜 License (MIT)

MIT License

Copyright (c) 2025 HERBERT & Woon (B1u3\_)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

Thank you for trying out our app!

— *HERBERT & Woon (B1u3\_)*

```

Do you also want me to **add installation screenshots / UI preview images section** (so your GitHub looks more visual), or keep it clean text-only?
```
