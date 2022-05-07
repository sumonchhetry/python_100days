print("Welcome to tip calculator")

amount = input("How much is the total amount ? \n")
tip_percent = input("Select how much % you want to tip for ? 10, 12 or 15 ? \n")

tip = (int(amount) / 100) * int(tip_percent)

amount = int(amount)
tip = int(tip)

total_amount = amount + tip

print(f"Your total amount after tip is {total_amount}")

devided_amount = input(f"How many people you want {total_amount} to be devided in ? \n")
devided_amount = int(devided_amount)

final_amount = total_amount / devided_amount
final_amount = int(final_amount)

print(f"So after spilitting the {total_amount} in {devided_amount} the final amount is {final_amount} each")