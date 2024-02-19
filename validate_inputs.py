import os
import json
import sys

def validate_inputs(inputs):
    errors = []

    # Check if token and tenant_id are provided and not empty
    if 'TOKEN' not in inputs or not inputs['TOKEN']:
        errors.append("Token is required.")
    if 'TENANT_ID' not in inputs or not inputs['TENANT_ID']:
        errors.append("Tenant ID is required.")

    # Check if repository_name is provided and not empty
    if 'REPOSITORY_NAME' not in inputs or not inputs['REPOSITORY_NAME']:
        errors.append("Repository name is required.")
    if 'SEVERITY' in inputs:
        valid_severities = {'UNKNOWN', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL'}
        severity = inputs['SEVERITY'].upper()
        if severity not in valid_severities:
            errors.append("Invalid severity level provided.")

    # Check if code is provided and valid
    if 'CODE' in inputs:
        code = inputs['CODE']
        if code not in {'0', '1'}:
            errors.append("Invalid code value provided.")
    return errors

def main():
    # Read inputs from environment variables
    inputs = {
        'DOCKERFILE_CONTEXT': os.getenv('DOCKERFILE_CONTEXT', ''),
        'ENDPOINT': os.getenv('ENDPOINT', ''),
        'TOKEN': os.getenv('TOKEN', ''),
        'TENANT_ID': os.getenv('TENANT_ID', ''),
        'REPOSITORY_NAME': os.getenv('REPOSITORY_NAME', ''),
        'TAG': os.getenv('TAG', ''),
        'SEVERITY': os.getenv('SEVERITY', ''),
        'CODE': os.getenv('CODE', '')
    }

    # Validate inputs
    errors = validate_inputs(inputs)

    # Print validation result
    if errors:
        print("Input validation failed:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    else:
        print("Input validation passed.")
        sys.exit(0)

if __name__ == "__main__":
    main()
