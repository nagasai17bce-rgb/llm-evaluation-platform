class Service:
    def run(self, value: str):
        actual = value.upper()
        score = float(actual == value)
        return {
            "samples": 1,
            "exact_match": score,
            "regression_gate": score >= 0.8,
            "expected": value,
            "actual": actual,
        }
