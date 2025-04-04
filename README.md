# 📝 Sentence Aligner App

A simple web application to compare two text files **line by line**, let users **approve** or **delete** sentence pairs, and **save approved lines** to an Excel file.

Built using **React** (frontend) and **Flask** (backend), with support for **Unicode/Devanagari** text.

---

## 📁 Features

- Upload two `.txt` files with aligned sentences.
- View and approve line pairs one-by-one.
- Delete all uploaded content with a click.
- Save only the approved sentence pairs to an Excel file (`approved_data.xlsx`).

---

## 🔧 Setup Instructions

### 📌 Requirements

- Python 3.9+
- Node.js and npm

---

## 🐍 Backend Setup (Flask)

1. **Clone or download this repo**, then open the backend folder.

2. **Install required Python packages**:
   ```bash
   pip install flask pandas openpyxl flask-cors
Create a file named server.py and paste this:

python
Copy
Edit
from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/save", methods=["POST"])
def save_to_excel():
    data = request.json
    approved_pairs = data.get("approvedPairs", [])
    if not approved_pairs:
        return jsonify({"message": "No approved lines to save"}), 400

    df = pd.DataFrame(approved_pairs)
    df.to_excel("approved_data.xlsx", index=False, engine="openpyxl")
    return jsonify({"message": "Approved data saved successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
Run the backend:

bash
Copy
Edit
python server.py
⚛️ Frontend Setup (React)
Create React app:

bash
Copy
Edit
npx create-react-app text-compare-app
cd text-compare-app
Install Axios:

bash
Copy
Edit
npm install axios
Replace src/App.js with this:

[Paste full App.js code from above here, or link to it]

Start the React app:

bash
Copy
Edit
npm start
It will launch at http://localhost:3000

✅ How to Use
Run both the backend and frontend.

Open the app in your browser.

Upload two .txt files – one in each input.

Review line pairs and approve by checking the boxes.

Click “Approve & Save Selected Lines” to export the approved lines to approved_data.xlsx.

Use “Delete All” to reset the interface.

🔤 Unicode / Devanagari Support
This app fully supports Unicode, so you can upload and view content in Hindi, Konkani, or any other script including Devanagari.

📂 Output
The approved sentence pairs will be saved in:

Copy
Edit
approved_data.xlsx
With columns:

file1	file2
Sentence 1 line	Sentence 2 line
...	...
🛠️ Customization Ideas
Add "Next" / "Previous" navigation for better review.

Add multi-language support in UI.

Export to CSV as an alternative to Excel.

Add file name display and validation.

💬 Questions?
Feel free to open an issue or reach out if you need help setting it up or customizing it further.

👨‍💻 Author
Anup Borker – MSc AI Student 🧠
