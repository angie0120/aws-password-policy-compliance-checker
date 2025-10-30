def evaluate_policy_compliance(self, policy):
    print("Evaluating password policy against compliance standards...")
    evaluation = {
        'compliant_controls': [],
        'non_compliant_controls': [],
        'missing_controls': [],
        'compliance_score': 0,
        'soc2_cc6_2_status': 'UNKNOWN',
        'nist_ia_5_status': 'UNKNOWN',
        'overall_status': 'UNKNOWN',
        'policy_type': 'unknown'
    }

    if policy is None:
        evaluation['missing_controls'] = list(self.compliance_standards.keys())
        evaluation['overall_status'] = 'NON_COMPLIANT'
        return evaluation

# Analysis logic continues... (truncated for brevity)

    total_controls = len(self.compliance_standards)
    compliant_count = 0
    for control, required_value in self.compliance_standards.items():
        current_value = policy.get(control)
        if current_value is None:
            evaluation['missing_controls'].append(control)
        elif self._is_control_compliant(control, current_value, required_value):
            evaluation['compliant_controls'].append(control)
            compliant_count += 1
        else:
            evaluation['non_compliant_controls'].append(control)

    evaluation['compliance_score'] = round((compliant_count / total_controls) * 100, 2)
    evaluation['overall_status'] = 'COMPLIANT' if evaluation['compliance_score'] >= 90 else 'NON_COMPLIANT'

    return evaluation