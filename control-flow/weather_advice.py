user_input = input("What's the weather like today? (sunny/rainy/cold): ")
if user_input == "sunny":
    print("Recommendation: Wear a t-shirt and sunglasses.")
elif user_input == "rainy":
    print("Recommendation: Don't forget your umbrella and a raincoat.")
elif user_input == "cold":
    print("Recommendation: Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")