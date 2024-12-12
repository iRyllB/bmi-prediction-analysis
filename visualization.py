import matplotlib.pyplot as plt
import seaborn as sns

def visualize(data):
    print("\nChoose the independent variable you want to visualize:")
    print("1. X1_FCVC (Vegetables in meals)")
    print("2. X2_NCP (Number of main meals)")
    print("3. X3_CH2O (Water intake)")
    print("4. X4_FAF (Physical activity)")
    print("5. X5_TUE (Technology usage)")

    independent_choice = input("Please choose an independent variable (1-5): ")

    print("\nVisualizing the data with a regression line only...")

    if independent_choice == "1":
        # Regression plot with only the line: X1_FCVC vs Y_Obesity Level
        plt.figure(figsize=(10,6))
        sns.regplot(x='X1_FCVC', y='Y_Obesity level', data=data, scatter_kws={'color': 'white'}, line_kws={'color': 'red'})
        plt.title('Regression Line: X1_FCVC vs Y_Obesity Level')
        plt.xlabel('X1_FCVC: Vegetables in meals')
        plt.ylabel('Y_Obesity Level')
        plt.show()

    elif independent_choice == "2":
        # Regression plot with only the line: X2_NCP vs Y_Obesity Level
        plt.figure(figsize=(10,6))
        sns.regplot(x='X2_NCP', y='Y_Obesity level', data=data, scatter_kws={'color': 'white'}, line_kws={'color': 'red'})
        plt.title('Regression Line: X2_NCP vs Y_Obesity Level')
        plt.xlabel('X2_NCP: Number of main meals')
        plt.ylabel('Y_Obesity Level')
        plt.show()

    elif independent_choice == "3":
        # Regression plot with only the line: X3_CH2O vs Y_Obesity Level
        plt.figure(figsize=(10,6))
        sns.regplot(x='X3_CH2O', y='Y_Obesity level', data=data, scatter_kws={'color': 'white'}, line_kws={'color': 'red'})
        plt.title('Regression Line: X3_CH2O vs Y_Obesity Level')
        plt.xlabel('X3_CH2O: Water intake')
        plt.ylabel('Y_Obesity Level')
        plt.show()

    elif independent_choice == "4":
        # Regression plot with only the line: X4_FAF vs Y_Obesity Level
        plt.figure(figsize=(10,6))
        sns.regplot(x='X4_FAF', y='Y_Obesity level', data=data, scatter_kws={'color': 'white'}, line_kws={'color': 'red'})
        plt.title('Regression Line: X4_FAF vs Y_Obesity Level')
        plt.xlabel('X4_FAF: Physical activity')
        plt.ylabel('Y_Obesity Level')
        plt.show()

    elif independent_choice == "5":
        # Regression plot with only the line: X5_TUE vs Y_Obesity Level
        plt.figure(figsize=(10,6))
        sns.regplot(x='X5_TUE', y='Y_Obesity level', data=data, scatter_kws={'color': 'white'}, line_kws={'color': 'red'})
        plt.title('Regression Line: X5_TUE vs Y_Obesity Level')
        plt.xlabel('X5_TUE: Technology usage')
        plt.ylabel('Y_Obesity Level')
        plt.show()

    else:
        print("Invalid choice, please try again.")
