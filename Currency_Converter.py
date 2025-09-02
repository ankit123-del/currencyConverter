import requests

def currency_converter(amount, from_currency, to_currency):
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Error: Could not fetch exchange rates."

    data = response.json()
    if "rates" in data and to_currency in data["rates"]:
        return data["rates"][to_currency]
    else:
        return "Error: Conversion failed."

# ---- MAIN PROGRAM ----
if __name__ == "__main__":
    print("💱 Currency Converter 💱")

    amount = float(input("Enter amount: "))
    from_currency = input("From Currency (e.g., USD, INR, EUR): ").upper()
    to_currency = input("To Currency (e.g., USD, INR, EUR): ").upper()

    converted = currency_converter(amount, from_currency, to_currency)
    print(f"\n{amount} {from_currency} = {converted} {to_currency}")
