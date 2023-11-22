total_money = 50  
usb_cost = 6  

num_usb_sticks = total_money // usb_cost
money_left = total_money % usb_cost

print(f"The girl can buy {num_usb_sticks} USB sticks and will have £{money_left} left.")

