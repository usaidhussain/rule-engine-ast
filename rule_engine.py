from src.database import load_sample_data, get_data_by_id

class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def evaluate(self, data):
        results = []
        for rule in self.rules:
            result = rule.evaluate(data)
            results.append(result)
        return results