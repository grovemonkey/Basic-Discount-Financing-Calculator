# Simple calculator in Python

# Get user input
msrp_input = input("Enter the MSRP: ")
add_promotions_input = input("Would you like to add promotion discounts? (y/n): ")

# Convert input to float or set default value if no input is provided
msrp = float(msrp_input) if msrp_input else 0.0

# Perform calculations without promotions
promotion1_amount = 0.0
promotional_price1 = msrp

if add_promotions_input.lower() == "y":
    # Ask for promotion 1 input
    promotion1_percent_input = input("Enter the percentage for Promotion 1: ")
    promotion1_percent = float(promotion1_percent_input) if promotion1_percent_input else 0.0

    # Perform calculations with promotion 1
    promotion1_amount = msrp * (promotion1_percent / 100)
    promotional_price1 = msrp - promotion1_amount

    # Print results for promotion 1
    print("Promotion 1: $", promotion1_amount)
    print("Promotional Price 1: $", promotional_price1)

    # Ask for promotion 2 input
    promotion2_input = input("Would you like to add Promotion 2? (y/n): ")
    if promotion2_input.lower() == "y":
        promotion2_percent_input = input("Enter the percentage for Promotion 2: ")
        promotion2_percent = float(promotion2_percent_input) if promotion2_percent_input else 0.0

        # Perform calculations with promotion 2
        promotion2_amount = promotional_price1 * (promotion2_percent / 100)
        promotional_price2 = promotional_price1 - promotion2_amount

        # Print results for promotion 2
        print("Promotion 2: $", promotion2_amount)
        print("Promotional Price 2: $", promotional_price2)

        # Ask for promotion 3 input
        promotion3_input = input("Would you like to add Promotion 3? (y/n): ")
        if promotion3_input.lower() == "y":
            promotion3_percent_input = input("Enter the percentage for Promotion 3: ")
            promotion3_percent = float(promotion3_percent_input) if promotion3_percent_input else 0.0

            # Perform calculations with promotion 3
            promotion3_amount = promotional_price2 * (promotion3_percent / 100)
            promotional_price3 = promotional_price2 - promotion3_amount

            # Print results for promotion 3
            print("Promotion 3: $", promotion3_amount)
            print("Promotional Price 3: $", promotional_price3)

            final_promotional_price = promotional_price3

        else:
            final_promotional_price = promotional_price2

    else:
        final_promotional_price = promotional_price1

else:
    final_promotional_price = msrp

# Print final promotional price
print("\nFinal Price: $", final_promotional_price)

# Calculate monthly payments if financing is selected
financing_input = input("\nWould you like to finance your purchase? (y/n): ")
if financing_input.lower() == "y":
    downpayment_input = input("\nEnter the downpayment amount: ")

    # Convert input to float or set default value if no input is provided
    downpayment = float(downpayment_input) if downpayment_input else 0.0

    # Perform calculation
    loan_amount = final_promotional_price - downpayment

    # Print downpayment result
    print("Loan Amount: $", loan_amount)
    financing_percent_input = input("Enter the financing percentage: ")
financing_term_input = input("Enter the financing term (in months): ")

# Convert input to floats or set default values if no input is provided
financing_percent = float(financing_percent_input) if financing_percent_input else 0.0
financing_term = float(financing_term_input) if financing_term_input else 0.0

# Perform calculations
monthly_interest_rate = financing_percent / 1200  # 12 months per year, 100 to convert percentage to decimal
monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-financing_term))

# Print monthly payment amount
print("Monthly Payment: $", round(monthly_payment, 2))
print("Disclaimer: Monthly Payments are generated without any lender-specific fees added. Final monthly payments will vary.")
