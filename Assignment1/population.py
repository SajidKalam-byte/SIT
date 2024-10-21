
''' In a town, the percentage of men is 52. The percentage of total literacy is 48. If total percentage
of literate men is 35 of the total population, write a program to find the total number of
illiterate men and women if the population of the town is 80,000'''


population = 80000


men_percent = 52
literate_percent = 48
literate_men_percent = 35


men = (men_percent / 100) * population
women = population - men


literate_men = (literate_men_percent / 100) * population
total_literate = (literate_percent / 100) * population
literate_women = total_literate - literate_men


illiterate_men = men - literate_men
illiterate_women = women - literate_women

print(f"Illiterate Men: {int(illiterate_men)}")

print(f"Illiterate Women: {int(illiterate_women)}")


