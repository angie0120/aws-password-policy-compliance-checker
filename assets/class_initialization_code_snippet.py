def __init__(self, profile_name=None, region='us-east-1'):
    self.profile_name = profile_name
    self.region = region
    self.session = None
    self.iam_client = None
    self.account_id = None
    self.compliance_standards = {
        'minimum_password_length': 12,
        'require_symbols': True,
        'require_numbers': True,
        'require_uppercase': True,
        'require_lowercase': True,
        'max_password_age': 90,
        'password_reuse_prevention': 12,
        'allow_users_to_change_password': True,
        'hard_expiry': False
    }