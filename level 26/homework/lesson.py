# def calculate_bmi(weight_kg, height_m):
#     # Calculate BMI
#     bmi = weight_kg / (height_m ** 2)
#     return bmi

# def interpret_bmi(bmi):
#     # Interpret BMI
#     if bmi < 18.5:
#         return "Underweight"
#     elif 18.5 <= bmi < 24.9:
#         return "Normal weight"
#     elif 25 <= bmi < 29.9:
#         return "Overweight"
#     else:
#         return "Obesity"

# # Input weight and height
# weight = float(input("Enter weight in kg: "))
# height = float(input("Enter height in meters: "))

# # Calculate and interpret BMI
# bmi = calculate_bmi(weight, height)
# # print(f"Your BMI is: {bmi:.2f}")
# print(f"Category: {interpret_bmi(bmi)}")



 # Define the maximum bid
# MAX_BID = 1000  # Set your maximum bid amount here

# def collect_bids():
#     bids = []
#     while True:
#         try:
#              Ask for a bid
#             bid = input("Enter your bid (or type 'done' to finish): ")
            
#              Allow the user to finish bidding
#             if bid.lower() == 'done':
#                 break
            
#              Convert the bid to an integer
#             bid = int(bid)
            
#              Check if the bid is within the allowed range
#             if 0 < bid <= MAX_BID:
#                 bids.append(bid)
#                 print(f"Bid of ${bid} accepted.")
#             else:
#                 print(f"Bid of ${bid} is out of range. Please enter a bid between $1 and ${MAX_BID}.")
        
#         except ValueError:
#             print("Invalid input. Please enter a numeric bid or 'done' to finish.")
    
#     return bids

# def determine_winner(bids):
#     if not bids:
#         return "No bids placed."
    
#     highest_bid = max(bids)
#     return f"The winning bid is ${highest_bid}."

#   Main auction program
# if __name__ == "__main__":
#     print("Welcome to the auction!")
#     bids = collect_bids()
#     result = determine_winner(bids)
#     print(result)


# import time

# def countdown_timer(seconds):
#     try:
#         seconds = int(seconds)
#         if seconds < 0:
#             raise ValueError("Please enter a positive number of seconds.")
#     except ValueError as e:
#         print(f"Invalid input: {e}")
#         return
    
#     while seconds > 0:
#         mins, secs = divmod(seconds, 60)
#         time_format = '{:02d}:{:02d}'.format(mins, secs)
#         print(time_format, end='\r')  # Print the timer in place
#         time.sleep(1)  # Wait for one second
#         seconds -= 1
    
#     print("00:00")  # Print the final countdown of 00:00
#     print("Time's up!")

#   Main program
# if __name__ == "__main__":
#     user_input = input("Enter the number of seconds for the countdown: ")
#     countdown_timer(user_input)