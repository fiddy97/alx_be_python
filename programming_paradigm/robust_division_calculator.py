def safe_divide(numerator, denominator):
    try:
        # Convert input values to floats
        num = float(numerator)
        denom = float(denominator)

        # Perform division and handle division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        else:
            return f"The result of the division is {num / denom}"

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."