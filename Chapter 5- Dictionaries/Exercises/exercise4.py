rivers={ 'Nile' :'Egypt',
        'Amazon':'Brazil',
        'yangtze':'china'
       }

# a sentance about the rivers
for river ,country in rivers.items():
    print (f"The beautiful {river} river runs through {country}.")

# prrinting rivers
print("\n rivers")
for river in rivers.keys():
    print(river)


#printing countries
print("\n countries")
for country in rivers.values():
    print (country)