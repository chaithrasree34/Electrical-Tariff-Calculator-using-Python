# Electrical-Tariff-Calculator-using-Python
# Electrical Tariff Calculator

print("===== ELECTRICAL TARIFF CALCULATOR =====")

units = float(input("Enter electricity units consumed (kWh): "))

# Tariff slabs
if units <= 100:
    energy_charge = units * 1.50

elif units <= 200:
    energy_charge = (100 * 1.50) + ((units - 100) * 2.50)

elif units <= 500:
    energy_charge = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

else:
    energy_charge = (100 * 1.50) + (100 * 2.50) + \
                    (300 * 4.00) + ((units - 500) * 6.00)

# Fixed charge
fixed_charge = 50

# Total bill
total_bill = energy_charge + fixed_charge

print("\n===== ELECTRICITY BILL =====")
print("Units Consumed :", units, "kWh")
print("Energy Charge  : ₹", round(energy_charge, 2))
print("Fixed Charge   : ₹", fixed_charge)
print("Total Bill     : ₹", round(total_bill, 2))
