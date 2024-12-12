import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from visualization import visualize

#load dataset
file_path = 'statsdata.xlsx' 
data = pd.read_excel(file_path)

#predict obsesity from linear regression
def predict_obesity():
    while True:  
        try:
            X1_FCVC = float(input("Enter frequency of vegetable consumption (1-5): "))
            if X1_FCVC < 1 or X1_FCVC > 5:
                print("Error: X1_FCVC should be between 1 and 5. Please try again.")
                continue

            X2_NCP = float(input("Enter number of main meals per day (1-5): "))
            if X2_NCP < 1 or X2_NCP > 5:
                print("Error: X2_NCP should be between 1 and 5. Please try again.")
                continue

            X3_CH2O = float(input("Enter water consumption (1-5): "))
            if X3_CH2O < 1 or X3_CH2O > 5:
                print("Error: X3_CH2O should be between 1 and 5. Please try again.")
                continue

            X4_FAF = float(input("Enter physical activity frequency (0-5): "))
            if X4_FAF < 0 or X4_FAF > 5:
                print("Error: X4_FAF should be between 0 and 5. Please try again.")
                continue

            X5_TUE = float(input("Enter time spent on technology (0-5): "))
            if X5_TUE < 0 or X5_TUE > 5:
                print("Error: X5_TUE should be between 0 and 5. Please try again.")
                continue

            break

        except ValueError:
            print("Error: Please enter a valid integer value.") 

    #Regression Equation from our data
    y_pred = 1.44 + (0.67 * X1_FCVC) + (0.14 * X2_NCP) + (0.29 * X3_CH2O) - (0.39 * X4_FAF) - (0.15 * X5_TUE)

    print(f"Predicted Obesity Level: {y_pred:.2f}")

    # Classification based on the predicted obesity level (1-6)
    if y_pred <= 1.5:
        classification = "Underweight (BMI < 18.5)"
    elif 1.5 < y_pred <= 2.5:
        classification = "Normal weight (BMI 18.5 - 24.9)"
    elif 2.5 < y_pred <= 3.5:
        classification = "Overweight (BMI 25.0 - 29.9)"
    elif 3.5 < y_pred <= 4.5:
        classification = "Obesity I (BMI 30.0 - 34.9)"
    elif 4.5 < y_pred <= 5.5:
        classification = "Obesity II (BMI 35.0 - 39.9)"
    elif y_pred > 5.5:
        classification = "Obesity III (BMI > 40)"

    print(f"Classification: {classification}")

#Main
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. See Data in Graph")
        print("2. Input Your Data for Prediction")
        print("3. Exit")

        choice = input("Please choose an option: ")

        if choice == "1":
            try:
                visualize(data) 
            except Exception as e:
                print(f"Error in visualization: {e}")
        elif choice == "2":
            predict_obesity()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

main_menu()
