# 💰 Expense Tracker API

<p align="center">
  <strong>A secure, RESTful Expense Tracker API built with Flask, SQLite, and JWT authentication.</strong><br>
  This system allows users to securely manage personal expenses, including adding, viewing, updating, deleting, and filtering financial records.
</p>

---

# 📖 Project Description

The Expense Tracker API is a backend web service designed to help users manage their personal finances in a structured and secure way.

Each user can create an account, log in securely, and manage their own set of expenses. Every expense is linked directly to the user who created it, ensuring complete data privacy and separation between users.

This project was built as part of the <a href="https://roadmap.sh/projects/expense-tracker-api" target="_blank">**roadmap.sh Python Projects roadmap**</a> and demonstrates essential backend development concepts including:

- REST API design principles
- User authentication using JWT (JSON Web Tokens)
- Secure password hashing using Argon2
- Relational database design using SQLite
- CRUD (Create, Read, Update, Delete) operations
- Data filtering and pagination
- Input validation and error handling

---

# 🧠 What This API Does (Simple Explanation)

Think of this API as a digital notebook where:

- You can write down your expenses (like shopping, bills, etc.)
- You can log in securely so only you can see your data
- You can search your expenses by date or category
- You can update or delete any entry at any time

Everything is stored safely in a database and linked to your account only.

---

# ✨ Features

## 👤 User System

- Register a new user account
- Secure login system
- Passwords are encrypted (not stored in plain text)
- JWT token authentication for secure access

---

## 💸 Expense Management

- Add a new expense
- View all your expenses
- Update existing expenses
- Delete expenses
- Each expense belongs only to its owner

---

## 🔍 Filtering & Search

You can filter expenses by:

- A specific date
- A date range
- Last week, month, or 3 months
- Category (e.g. Groceries, Health, etc.) - You can insert whatever category you would like

---

## 📄 Pagination

Expenses are displayed in pages:

- You can choose how many results per page
- You can move between pages
- Helps manage large sets of data efficiently

---

# 🛠 Technology Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Core programming language       |
| Flask         | Web framework for API           |
| SQLite        | Lightweight database            |
| PyJWT         | Token-based authentication      |
| Argon2        | Secure password hashing         |
| python-dotenv | Environment variable management |

---

# 🏗 Project Structure

The project is organised into service-based modules:

```text
Expense-Tracker-API/
|
├── instance/
│   └── expense.db      # Creates on first launch
├── services/
│   ├── auth.py
│   ├── config.py
│   ├── db.py
│   ├── expenses.py
│   ├── users.py
│   └── validator.py
├── app.py
├── .env                # Creates on first launch
├── LICENSE
└── README.md

```

---

## 📦 File Breakdown (Important Functions Explained)

### 🔹 app.py (Main Application File)

This is the entry point of the API.

It:

- Starts the Flask server
- Defines all API routes (endpoints)
- Handles incoming requests
- Returns responses to users

---

### 🔹 services/auth.py

Handles all authentication logic:

- `login_required()`
  Protects routes so only logged-in users can access them.

- `create_token(user_id)`
  Generates a JWT token for authenticated users.

- `decode_token(token)`
  Extracts user information from a JWT token.

- `hash_password(password)`
  Encrypts user passwords securely.

- `check_password(stored, entered)`
  Checks if a password is correct during login.

---

### 🔹 services/users.py

Handles user management:

- `user_register(data)`
  Creates a new user account in the database.

- `find_user(data)`
  Finds a user by email.

- `user_login(data)`
  Authenticates a user and returns a JWT token.

---

### 🔹 services/expenses.py

Handles all expense-related logic:

- `add_expense(data)`
  Adds a new expense to the database.

- `all_expenses(...)`
  Retrieves all expenses for a user with filtering and pagination.

- `update_expense(...)`
  Updates an existing expense.

- `delete_expense(...)`
  Deletes an expense from the database.

---

### 🔹 services/db.py

Handles all database operations:

- `execute()` → Runs SQL queries that modify data
- `fetch_one()` → Retrieves a single record
- `fetch_all()` → Retrieves multiple records
- `delete_one()` → Deletes a record

---

### 🔹 services/config.py

Handles system configuration:

- Creates `.env` file if missing with the secret key or token generated
- Connects to SQLite database
- Creates required tables (`users`, `expenses`)

---

### 🔹 services/validator.py

Handles input validation:

- Validates email format
- Validates date format (DD-MM-YYYY)
- Ensures correct data input before saving to database

---

# 🚀 Getting Started (Installation Guide)

## 1. Download the Project

Clone the repository:

```bash
git clone https://github.com/sheikh-h/expense-tracker-api.git
cd expense-tracker-api
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac / Linux

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
python app.py
OR
flask run
```

The API will run at:

```
http://127.0.0.1:5000
OR
localhost:5000
```

---

# 🌍 Environment Variables

The `.env` file is created itself anyway and gets the port from your local machine on application run:

```env
SECRET_KEY=your_secret_key_here
```

---

# 📬 API Usage Guide (Postman + Curl)

For the projects, I have been using an application called postman which is opensourced and available to use online and would recommend that you download it and install it from their website to use with this project of mine for viewability and ease of use.

---

# 🔐 1. Register a New User

### Endpoint:

```
POST /register
```

### Body (JSON):

```json
{
  "name": "Sheikh",
  "email": "sheikh@example.com",
  "password": "password123"
}
```

### Using cURL:

```bash
curl -X POST http://127.0.0.1:5000/register \
-H "Content-Type: application/json" \
-d '{"name":"Sheikh","email":"sheikh@example.com","password":"password123"}'
```

### Response:

```json
{
  "success": "your_jwt_token"
}
```

---

# 🔑 2. Login

### Endpoint:

```
POST /login
```

### Body:

```json
{
  "email": "sheikh@example.com",
  "password": "password123"
}
```

---

### cURL:

```bash
curl -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{"email":"sheikh@example.com","password":"password123"}'
```

### Response:

```json
{
  "success": "your_jwt_token"
}
```

---

# 💸 3. Add Expense

### Endpoint:

```
POST /expenses
```

### Headers:

```
Authorization: Bearer <your_token>
```

### Body:

```json
{
  "title": "Groceries",
  "category": "Groceries",
  "amount": 45.99,
  "date": "14-06-2026"
}
```

---

### cURL:

```bash
curl -X POST http://127.0.0.1:5000/expenses \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <YOUR_TOKEN>" \
-d '{"title":"Groceries","category":"Groceries","amount":45.99,"date":"14-06-2026"}'
```

---

# 📄 4. Get Expenses

### Endpoint:

```
GET /expenses
```

### Optional Filters:

- page
- limit
- category
- on
- from
- to

### Example:

```
GET /expenses?page=1&limit=5
```

---

### cURL:

```bash
curl http://127.0.0.1:5000/expenses \
-H "Authorization: Bearer YOUR_TOKEN"
```

---

# ✏️ 5. Update Expense

### Endpoint:

```
PUT /expenses/<id>
```

### Example Body:

```json
{
  "amount": 60
}
```

---

### cURL:

```bash
curl -X PUT http://127.0.0.1:5000/expenses/1 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_TOKEN" \
-d '{"amount":60}'
```

---

# ❌ 6. Delete Expense

### Endpoint:

```
DELETE /expenses/<id>
```

### cURL:

```bash
curl -X DELETE http://127.0.0.1:5000/expenses/1 \
-H "Authorization: Bearer YOUR_TOKEN"
```

---

# ⚠ Error Responses

### Missing Fields

```json
{
  "error": "Missing fields in request"
}
```

### Invalid Token

```json
{
  "denied": "Invalid Token"
}
```

### Not Found

```json
{
  "error": "Unable to find email"
}
```

---

# 🔐 Security Features

- Passwords hashed using Argon2
- JWT-based authentication
- Token expiry (1 hour)
- Protected routes
- User-specific data isolation

---

# 🔮 Future Improvements

- Add refresh tokens
- Improve validation layer structure
- Add logging system
- Add Swagger API documentation
- Docker support
- Move to PostgreSQL for scalability

---

# 🎯 Roadmap.sh Project

This project is part of the following roadmap.sh task:

👉 https://roadmap.sh/projects/expense-tracker-api

---

# 📄 Licence

```text
MIT Licence

Copyright (c) 2026 Sheikh Hussain

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
```

---

# 🤝 Connect With Me

<div align="center">

<a href="https://github.com/Sheikh-H">
<img src="https://img.shields.io/badge/GitHub-376e00?style=flat&logo=github&logoColor=white" alt="GitHub">
</a>

<a href="https://www.linkedin.com/in/sheikh-hussain/">
<img src="https://img.shields.io/badge/LinkedIn-376e00?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>

<a href="mailto:sheikh.hussain1155@gmail.com">
<img src="https://img.shields.io/badge/Gmail-376e00?style=flat&logo=gmail&logoColor=white" alt="Gmail">
</a>

<a href="https://sheikh-h.github.io/">
<img src="https://img.shields.io/badge/Portfolio-376e00?style=flat&logo=github&logoColor=white" alt="Portfolio">
</a>

</div>

---

<p align="center">
Built with Python, Flask and SQLite by <strong>Sheikh Hussain</strong> 💚
</p>

<p align="center">
⭐ If you found this project useful, consider giving it a star on GitHub.
</p>
