import sys
import json

def validate_inputs(inputs):
    errors = []

    # Check if token and tenant_id are provided
    if 'token' not in inputs:
        errors.append("Token is required.")
    if 'tenant_id' not in inputs:
        errors.append("Tenant ID is required.")

    # Check if repository_name is provided
    if 'repository_name' not in inputs:
        errors.append("Repository name is required.")

    # Check if tag is provided and if it matches the required format
    if 'tag' in inputs and not inputs['tag'].startswith('v'):
        errors.append("Tag should start with 'v'.")

    return errors

def main():
    # Read inputs from stdin
    inputs_json = sys.stdin.read()
    inputs = json.loads(inputs_json)

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
