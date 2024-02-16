import os
import json
import sys

def validate_inputs(inputs):
    errors = []

    # Check if token and tenant_id are provided
    if 'TOKEN' not in inputs:
        errors.append("Token is required.")
    if 'TENANT_ID' not in inputs:
        errors.append("Tenant ID is required.")

    # Check if repository_name is provided
    if 'REPOSITORY_NAME' not in inputs:
        errors.append("Repository name is required.")

    return errors

# def main():
#     # Read inputs from environment variables
#     inputs = {
#         'DOCKERFILE_CONTEXT': os.getenv('DOCKERFILE_CONTEXT', ''),
#         'ENDPOINT': os.getenv('ENDPOINT', ''),
#         'TOKEN': os.getenv('TOKEN', ''),
#        # 'TENANT_ID': os.getenv('TENANT_ID', ''),
#         'REPOSITORY_NAME': os.getenv('REPOSITORY_NAME', ''),
#         'TAG': os.getenv('TAG', ''),
#         'SEVERITY': os.getenv('SEVERITY', ''),
#         'CODE': os.getenv('CODE', '')
#     }

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

# if __name__ == "__main__":
#     main()
