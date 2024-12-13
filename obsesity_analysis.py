import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder

def classify_bmi(bmi):
    """Classify BMI based on the given ranges."""
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
    else:
        return "Obesity III (BMI > 40)"

def predict_bmi_from_csv(csv_file):
    """Predict BMI for all rows in the CSV file and classify them."""
    # Load the dataset
    data = pd.read_csv(csv_file)

    # Check if required columns are present
    required_columns = ['Y_Obesity level', 'X1_FCVC', 'X2_NCP', 'X3_CH2O', 'X4_FAF', 'X5_TUE']
    if not all(col in data.columns for col in required_columns):
        raise ValueError("CSV file must contain columns: 'Y_Obesity level', 'X1_FCVC', 'X2_NCP', 'X3_CH2O', 'X4_FAF', 'X5_TUE'")

    # Apply the regression equation to predict BMI
    data['Predicted_BMI'] = 1.44 + 0.67 * data['X1_FCVC'] + 0.14 * data['X2_NCP'] + 0.29 * data['X3_CH2O'] - 0.39 * data['X4_FAF'] - 0.15 * data['X5_TUE']

    # Classify BMI
    data['BMI Classification'] = data['Predicted_BMI'].apply(classify_bmi)

    return data[['Y_Obesity level', 'X1_FCVC', 'X2_NCP', 'X3_CH2O', 'X4_FAF', 'X5_TUE', 'Predicted_BMI', 'BMI Classification']]

def browse_file():
    """Open a file dialog to select a CSV file and process it."""
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        try:
            # Predict BMI from the CSV file
            predicted_data = predict_bmi_from_csv(file_path)
            
            # Display predictions in the Treeview widget of Tkinter
            for row in predicted_data.itertuples():
                treeview.insert("", "end", values=row[1:])  # Insert each row into the Treeview widget
            
            messagebox.showinfo("Success", "BMI prediction completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create the main Tkinter window
root = tk.Tk()
root.title("BMI Prediction Tool")

# Create a frame for the file selection button
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Add a button to browse for a CSV file
browse_button = tk.Button(frame, text="Browse CSV File", command=browse_file)
browse_button.pack()

# Create a Treeview widget to display the data in a tabular format
columns = ['Y_Obesity level', 'X1_FCVC', 'X2_NCP', 'X3_CH2O', 'X4_FAF', 'X5_TUE', 'Predicted_BMI', 'BMI Classification']
treeview = ttk.Treeview(root, columns=columns, show='headings')

# Set column headings
for col in columns:
    treeview.heading(col, text=col)

# Set column width
for col in columns:
    treeview.column(col, width=150, anchor='center')

treeview.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
