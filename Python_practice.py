from multiprocessing import Value


counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
print(voting_data)


for county_dict in voting_data:
    for registered_voters in county_dict.items():
        print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")


print(county_dict)
