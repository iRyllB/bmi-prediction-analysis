from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Fetch dataset
data = fetch_ucirepo(id=544)
X = data.data.features
y = data.data.targets

# Step 2: Handle categorical variables
categorical_columns = X.select_dtypes(include=['object']).columns  
label_encoders = {}

for column in categorical_columns:
    le = LabelEncoder()
    X.loc[:, column] = le.fit_transform(X[column])  
    label_encoders[column] = le  

# Step 3: Scale numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

y_le = LabelEncoder()
y_encoded = y_le.fit_transform(y.values.ravel()) 

# Step 4: Split the data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Step 5: Train the model
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Step 6: Evaluate the model
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=y_le.classes_)

# Plot the confusion matrix with adjusted label rotation
plt.figure(figsize=(10, 7))
disp.plot(cmap=plt.cm.Blues)
plt.xticks(rotation=45, ha='right')  
plt.title('Confusion Matrix')
plt.tight_layout() 
plt.show()
