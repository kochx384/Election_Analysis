voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "registered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}]

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for counties_dict in voting_data:
    print(f"{counties_dict['county']} has {counties_dict['registered_voters']:,} registered voters")
