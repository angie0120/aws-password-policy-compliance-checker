def main():
    parser = argparse.ArgumentParser(
        description='AWS Password Policy Compliance Checker'
    )
    parser.add_argument('--profile', type=str, help='AWS profile to use')
    parser.add_argument('--region', type=str, default='us-east-1', help='AWS region')
    args = parser.parse_args()
    
    checker = PasswordPolicyChecker(profile_name=args.profile, region=args.region)
    success = checker.run_assessment()
    sys.exit(0 if success else 1)