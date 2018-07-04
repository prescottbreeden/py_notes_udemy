# mileage calculator for terminal
print("program running... \n")

kms = input('How many kilometers did you cycle today? ')
miles = float(kms)/1.60934
miles = round(miles, 2)

# return answer and round to 2 decimals
print(f'Your {kms}km ride is equal to {miles} miles')
