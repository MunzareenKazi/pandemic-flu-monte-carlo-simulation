import random
import matplotlib.pyplot as plt

random.seed(1000)
#part D - No vaccination
number_of_reps = 1000
len_of_each_outbreak = []
num_of_infections_until_now = []

for rep in range(number_of_reps):
    #there are 50 susceptible kids in the classroom
    all_kids = 50 * [0]

    #simulation starts with 1 infectious kid - Tommy
    all_kids.append(1)

    total_expected_num_of_infected_kids_by_day = [1]

    num_of_day = 1

    while any(1 <= kid <= 3 for kid in all_kids):
        #we will consider 0: Healthy, 1-3: Infectious, 4-Recovered
        currently_infectious = 0
        for kid in all_kids:
            if 1 <= kid <= 3:
                currently_infectious += 1

        #new infections today
        new_infections_today = []
        for i in range(len(all_kids)):
            if all_kids[i] == 0:
                prob_of_not_being_infected = 0.99 ** currently_infectious
                if prob_of_not_being_infected < random.random():
                    new_infections_today.append(i)

        #moving to the next day
        for i in range(len(all_kids)):
            if 1 <= all_kids[i] <= 3:
                all_kids[i] += 1

        #turning status of susceptible kids who have become infectious to 1
        for i in new_infections_today:
            all_kids[i] = 1

        #expected number of infected kids till now
        cumulative_total = 0
        for kid in all_kids:
            if kid > 0:
                cumulative_total += 1
        total_expected_num_of_infected_kids_by_day.append(cumulative_total)

        #moving to next day
        num_of_day += 1

    len_of_each_outbreak.append(num_of_day - 1)
    num_of_infections_until_now.append(total_expected_num_of_infected_kids_by_day)

#finding expected number of kids sick on day i
longest_outbreak = 0
for infection_list in num_of_infections_until_now:
    if len(infection_list) > longest_outbreak:
        longest_outbreak = len(infection_list)

#calculating average of every day of the outbreak in each simulation
result = []

for num in range(longest_outbreak):
    total = 0
    for infection_list in num_of_infections_until_now:
        if num < len(infection_list):
            total += infection_list[num]
        else:
            total += infection_list[-1]
    result.append(total/1000)

for day, num_of_inf in enumerate(result):
    print(f"Day {day+1}: {num_of_inf} infected on average")

#creating histogram of the duration of outbreak
plt.hist(len_of_each_outbreak)
plt.xlabel("Number of days")
plt.ylabel("Number of simulation runs")
plt.title("Duration of infection without immunization")
plt.show()











#part E: Each kid has 60% of being immunized
number_of_reps = 1000
len_of_each_outbreak = []
num_of_infections_until_now = []

#we will consider -1: Immune, 0: Healthy, 1-3: Infectious, 4-Recovered

for rep in range(number_of_reps):
    #there are 50 susceptible kids in the classroom
    all_kids = [1] #this is tommy

    #giving each kid 60% chance of being immunized
    for i in range(50):
        if random.random() > 0.60:
            all_kids.append(0)
        else:
            all_kids.append(-1)

    total_expected_num_of_infected_kids_by_day = [1]

    num_of_day = 1

    while any(1 <= kid <= 3 for kid in all_kids):
        currently_infectious = 0
        for kid in all_kids:
            if 1 <= kid <= 3:
                currently_infectious += 1

        #new infections today
        new_infections_today = []
        for i in range(len(all_kids)):
            if all_kids[i] == 0:
                prob_of_not_being_infected = 0.99 ** currently_infectious
                if prob_of_not_being_infected < random.random():
                    new_infections_today.append(i)

        #moving to the next day
        for i in range(len(all_kids)):
            if 1 <= all_kids[i] <= 3:
                all_kids[i] += 1

        #turning status of susceptible kids who have become infectious to 1
        for i in new_infections_today:
            all_kids[i] = 1

        #expected number of infected kids till now
        cumulative_total = 0
        for kid in all_kids:
            if kid > 0:
                cumulative_total += 1
        total_expected_num_of_infected_kids_by_day.append(cumulative_total)

        #moving to next day
        num_of_day += 1

    len_of_each_outbreak.append(num_of_day - 1)
    num_of_infections_until_now.append(total_expected_num_of_infected_kids_by_day)

#finding expected number of kids sick on day i
longest_outbreak = 0
for infection_list in num_of_infections_until_now:
    if len(infection_list) > longest_outbreak:
        longest_outbreak = len(infection_list)

#calculating average of every day of the outbreak in each simulation
result = []

for num in range(longest_outbreak):
    total = 0
    for infection_list in num_of_infections_until_now:
        if num < len(infection_list):
            total += infection_list[num]
        else:
            total += infection_list[-1]
    result.append(total/1000)

for day, num_of_inf in enumerate(result):
    print(f"Day {day+1}: {num_of_inf} infected on average")

#creating histogram of the duration of outbreak
plt.hist(len_of_each_outbreak)
plt.xlabel("Number of days")
plt.ylabel("Number of simulation runs")
plt.title("Duration of infection with 60% chance of being immunization")
plt.show()

























































