def calculate_total(price, quantity):
    return price * quantity


def ai_suggestion(total):
    if total >= 3000:
        return "Your cart total is high. Check for discounts."
    else:
        return "Your cart total is reasonable."


price = 100
quantity = 3

total = calculate_total(price, quantity)

print("Total:", total)
print("AI Suggestion:", ai_suggestion(total))