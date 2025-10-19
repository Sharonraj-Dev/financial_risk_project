"""
Train a scikit-learn model for risk prediction and save it using joblib.
"""
import argparse
import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


def main(input_csv: str = 'dataset/sample_risk_data.csv',
        output_model: str = 'models/saved_model.joblib',
        random_state: int = 42):
    """
    Loads data, trains a RandomForestClassifier, evaluates it, 
    and saves the model.
    
    Args:
        input_csv (str): Path to the input CSV dataset.
        output_model (str): Path to save the output model file (.joblib).
        random_state (int): Seed for reproducibility.
    """
    
    # --- 1. Setup and Data Loading ---
    print(f"Starting model training process...")
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_model), exist_ok=True)
    
    print(f"Loading data from {input_csv}...")
    try:
        df = pd.read_csv(input_csv)
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_csv}")
        return

    # --- 2. Feature and Target Preparation ---
    target = 'risk'
    if target not in df.columns:
        print(f"Error: Target column '{target}' not in dataset.")
        return
        
    X = df.drop(columns=[target])
    y = df[target]
    features = list(X.columns)

    # --- 3. Train/Test Split ---
    print("Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_state, stratify=y
    )

    # --- 4. Model Training ---
    print("Training RandomForestClassifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=random_state)
    model.fit(X_train, y_train)
    print("Model training complete.")

    # --- 5. Model Evaluation ---
    print("\n--- Model Evaluation (on Test Set) ---")
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    print(f"Accuracy: {acc:.4f}")
    print("\nClassification Report:")
    print(report)
    print("----------------------------------------")

    # --- 6. Model Saving ---
    print(f"Saving model and features to {output_model}...")
    # Bundle the model and the feature list together for later use
    model_payload = {
        'model': model,
        'features': features
    }
    joblib.dump(model_payload, output_model)
    print(f"Successfully saved model to {output_model}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Train and save a risk prediction model."
    )
    parser.add_argument(
        '--input', 
        type=str, 
        default='dataset/sample_risk_data.csv',
        help="Path to the input training data CSV file."
    )
    parser.add_argument(
        '--output', 
        type=str, 
        default='models/saved_model.joblib',
        help="Path to save the output .joblib model file."
    )
    args = parser.parse_args()
    
    main(input_csv=args.input, output_model=args.output)