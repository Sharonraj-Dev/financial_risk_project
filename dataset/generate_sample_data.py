"""Generate a synthetic financial risk dataset as CSV."""
import argparse
import pandas as pd
import numpy as np


def generate(n_rows=2000, out_path='dataset/sample_risk_data.csv', random_state=42):
    """
    Generates and saves a synthetic financial risk dataset.
    
    Args:
        n_rows (int): Number of rows to generate.
        out_path (str): Path to save the output CSV file.
        random_state (int): Seed for the random number generator.
    """
    rng = np.random.RandomState(random_state)
    
    # --- Feature Generation ---
    # features: income, age, loan_amount, loan_term_months, 
    # credit_score, num_of_defaults, employment_years
    
    income = rng.normal(50000, 20000, size=n_rows).clip(5000, 500000)
    age = rng.randint(18, 75, size=n_rows)
    loan_amount = rng.normal(15000, 10000, size=n_rows).clip(500, 200000)
    loan_term_months = rng.choice(
        [12, 24, 36, 48, 60], 
        size=n_rows, 
        p=[0.1, 0.15, 0.4, 0.25, 0.1]
    )
    credit_score = rng.normal(650, 70, size=n_rows).clip(300, 850)
    num_of_defaults = rng.poisson(0.2, size=n_rows)
    employment_years = rng.exponential(5, size=n_rows).clip(0, 50).round(1)

    # --- Risk Label Generation (Synthetic) ---
    # 1 = high risk, 0 = low risk
    risk_prob = (
        (loan_amount / (income + 1)) * 0.6
        + (1 - (credit_score - 300) / 550) * 0.4
        + (num_of_defaults * 0.2)
        - (employment_years * 0.02)
    )
    
    # Normalize probability score between 0 and 1
    risk_prob = (risk_prob - risk_prob.min()) / (risk_prob.max() - risk_prob.min())
    label = (risk_prob > 0.5).astype(int)

    # --- Create DataFrame and Save ---
    df = pd.DataFrame({
        'income': income,
        'age': age,
        'loan_amount': loan_amount,
        'loan_term_months': loan_term_months,
        'credit_score': credit_score,
        'num_of_defaults': num_of_defaults,
        'employment_years': employment_years,
        'risk': label,
    })

    df.to_csv(out_path, index=False)
    print(f"Generated {n_rows} rows to {out_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Generate a synthetic financial risk dataset."
    )
    parser.add_argument(
        '--rows', 
        type=int, 
        default=2000,
        help="Number of rows to generate."
    )
    parser.add_argument(
        '--out', 
        type=str, 
        default='dataset/sample_risk_data.csv',
        help="Output CSV file path."
    )
    args = parser.parse_args()
    
    # Ensure the output directory exists (optional, but good practice)
    # import os
    # os.makedirs(os.path.dirname(args.out), exist_ok=True)
    
    generate(n_rows=args.rows, out_path=args.out)