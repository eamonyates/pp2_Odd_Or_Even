#! usr/bin/env python3


def odd_even():
	user_number = int(input("Please enter a number: "))
	if (user_number % 4) ==0:
		print ("\nYou have chosen a number divisible by 4")
	elif (user_number % 2) == 0:
		print ("\nYou have chosen an even number")
	else:
		print ("\nYou have chosen an odd number")
	print ("\nNow lets check if a number is divisible by another.")
	num = int(input("Please enter a number to check: "))
	check = int(input("Now enter a number to divide it by: "))
	if num % check == 0:
		print ("\nWahey! The number " + str(num) + " is divisible by the number " + str(check))
	else:
		print ("\nSorry, the number " + str(num) + " is not divisible by the number " + str(check))

		
if __name__ == "__main__":
	odd_even()
