import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
from tkinter import messagebox

def classify_bmi(bmi):
    if bmi <= 1.5:
        return "Underweight (BMI < 18.5)"
    elif 1.5 < bmi <= 2.5:
        return "Normal weight (BMI 18.5 - 24.9)"
    elif 2.5 < bmi <= 3.5:
        return "Overweight (BMI 25.0 - 29.9)"
    elif 3.5 < bmi <= 4.5:
        return "Obesity I (BMI 30.0 - 34.9)"
    elif 4.5 < bmi <= 5.5:
        return "Obesity II (BMI 35.0 - 39.9)"
    elif bmi > 5.5:
        return "Obesity III (BMI > 40)"

def predict_bmi_from_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        if "Y_Obesity level" in data.columns:
            data = data.drop(columns=["Y_Obesity level"])
        required_columns = ["X1_FCVC", "X2_NCP", "X3_CH2O", "X4_FAF", "X5_TUE"]
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            messagebox.showerror("Error", f"CSV file is missing the following required columns: {', '.join(missing_columns)}. Accepted columns are: {', '.join(required_columns)}.")
            return None
        coefficients = [0.67, 0.14, 0.29, -0.39, -0.15]
        intercept = 1.44
        data["Predicted_BMI"] = intercept + sum(coeff * data[col] for coeff, col in zip(coefficients, required_columns))
        data["Classification"] = data["Predicted_BMI"].apply(classify_bmi)
        return data
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return None

def display_predictions(data):
    for widget in output_frame.winfo_children():
        widget.destroy()
    tree = ttk.Treeview(output_frame)
    tree.pack(fill=tk.BOTH, expand=True)
    scrollbar_x = ttk.Scrollbar(output_frame, orient="horizontal", command=tree.xview)
    scrollbar_y = ttk.Scrollbar(output_frame, orient="vertical", command=tree.yview)
    tree.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    tree["columns"] = list(data.columns)
    tree["show"] = "headings"
    for col in data.columns:
        tree.heading(col, text=col, command=lambda c=col: sort_column(tree, c, False))
        tree.column(col, width=120, anchor="center")
    for _, row in data.iterrows():
        tree.insert("", "end", values=list(row))
    tree.pack(fill=tk.BOTH, expand=True)

def sort_column(tree, col, reverse):
    data = [(tree.set(k, col), k) for k in tree.get_children("")]
    data.sort(reverse=reverse)
    for index, (_, k) in enumerate(data):
        tree.move(k, "", index)
    tree.heading(col, command=lambda: sort_column(tree, col, not reverse))

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        data = predict_bmi_from_csv(file_path)
        if data is not None:
            display_predictions(data)

root = tk.Tk()
root.title("BMI Prediction")
root.geometry("1000x600")
file_button = tk.Button(root, text="Select CSV File", command=select_file, font=("Arial", 14))
file_button.pack(pady=20)
output_frame = tk.Frame(root)
output_frame.pack(fill=tk.BOTH, expand=True)
root.mainloop()
