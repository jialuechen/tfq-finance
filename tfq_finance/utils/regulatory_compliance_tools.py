import pandas as pd

def check_compliance(data, rules):
    compliance_results = {}
    for rule, condition in rules.items():
        compliance_results[rule] = data.eval(condition).all()
    return compliance_results

if __name__ == "__main__":
    data = pd.DataFrame({
        'capital_ratio': [0.1, 0.12, 0.15, 0.11],
        'liquidity_ratio': [0.8, 0.85, 0.78, 0.82]
    })

    rules = {
        'Capital Adequacy': 'capital_ratio > 0.1',
        'Liquidity Coverage': 'liquidity_ratio > 0.75'
    }

    compliance_results = check_compliance(data, rules)
    print("Compliance Results:")
    for rule, result in compliance_results.items():
        print(f"{rule}: {'Compliant' if result else 'Non-compliant'}")