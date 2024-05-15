# import tkinter as tk
# from tkinter import filedialog, messagebox
# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import StandardScaler

# def load_data():
#     file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
#     if file_path:
#         diabetes_dataset = pd.read_csv(file_path)
#         return diabetes_dataset
#     else:
#         return None

# def preprocess_data(diabetes_dataset):
#     X = diabetes_dataset.drop('Outcome', axis=1)
#     y = diabetes_dataset['Outcome']

#     scaler = StandardScaler()
#     X_scaled = scaler.fit_transform(X)

#     return X_scaled, y, scaler

# def train_model(X_scaled, y):
#     model = LogisticRegression()
#     model.fit(X_scaled, y)
#     return model

# def on_predict_click(X_scaled, scaler):
#     input_data = [float(entry.get()) for entry in entry_fields]
#     input_scaled = scaler.transform([input_data])
#     prediction = model.predict(input_scaled)
#     result_label.config(text=f"Prediction: {'Diabetic' if prediction[0] == 1 else 'Not Diabetic'}")

# def on_load_data_click():
#     global model, scaler, X_scaled
#     diabetes_dataset = load_data()
#     if diabetes_dataset is not None:
#         X_scaled, y, scaler = preprocess_data(diabetes_dataset)
#         model = train_model(X_scaled, y)
#         messagebox.showinfo("Info", "Data loaded and model trained successfully.")

# def main():
#     global entry_fields, result_label, model, scaler, X_scaled
#     root = tk.Tk()
#     root.title("Diabetes Prediction")

#     entry_fields = []
#     attributes = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#                   'BMI', 'DiabetesPedigreeFunction', 'Age']
#     for i, attribute in enumerate(attributes):
#         label = tk.Label(root, text=attribute)
#         label.grid(row=i, column=0, padx=10, pady=5)
#         entry = tk.Entry(root)
#         entry.grid(row=i, column=1, padx=10, pady=5)
#         entry_fields.append(entry)

#     predict_button = tk.Button(root, text="Predict", command=lambda: on_predict_click(X_scaled, scaler))
#     predict_button.grid(row=len(entry_fields), columnspan=2, pady=10)

#     load_button = tk.Button(root, text="Load Data", command=on_load_data_click)
#     load_button.grid(row=len(entry_fields)+1, columnspan=2, pady=10)

#     result_label = tk.Label(root, text="")
#     result_label.grid(row=len(entry_fields)+2, columnspan=2, pady=10)

#     root.mainloop()

# if __name__ == "__main__":
#     main()

import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        diabetes_dataset = pd.read_csv(file_path)
        return diabetes_dataset
    else:
        return None

def preprocess_data(diabetes_dataset):
    X = diabetes_dataset.drop('Outcome', axis=1)
    y = diabetes_dataset['Outcome']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler

def train_model(X_scaled, y):
    model = LogisticRegression()
    model.fit(X_scaled, y)
    return model

def on_predict_click(X_scaled, scaler, entry_fields, result_label):
    input_data = [float(entry.get()) for entry in entry_fields]
    input_scaled = scaler.transform([input_data])
    prediction = model.predict(input_scaled)
    result_label.config(text=f"Prediction: {'Diabetic' if prediction[0] == 1 else 'Not Diabetic'}", fg="red")

def on_load_data_click():
    global model, scaler, X_scaled
    diabetes_dataset = load_data()
    if diabetes_dataset is not None:
        X_scaled, y, scaler = preprocess_data(diabetes_dataset)
        model = train_model(X_scaled, y)
        messagebox.showinfo("Info", "Data loaded and model trained successfully.")

def main():
    global entry_fields, result_label, model, scaler, X_scaled
    root = tk.Tk()
    root.title("Diabetes Prediction")
    root.configure(bg="lightgray")

    entry_fields = []
    attributes = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                  'BMI', 'DiabetesPedigreeFunction', 'Age']
    for i, attribute in enumerate(attributes):
        label = tk.Label(root, text=attribute, bg="lightgray")
        label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(root)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry_fields.append(entry)

    predict_button = tk.Button(root, text="Predict", command=lambda: on_predict_click(X_scaled, scaler, entry_fields, result_label), bg="blue", fg="white")
    predict_button.grid(row=len(entry_fields), columnspan=2, pady=10)

    load_button = tk.Button(root, text="Load Data", command=on_load_data_click, bg="green", fg="white")
    load_button.grid(row=len(entry_fields)+1, columnspan=2, pady=10)

    result_label = tk.Label(root, text="", bg="lightgray")
    result_label.grid(row=len(entry_fields)+2, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
