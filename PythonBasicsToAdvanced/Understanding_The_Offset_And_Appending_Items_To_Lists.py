"""

List is what would call a data structure

Data structure, as the name is self-explanatory, is just a way of organizing and storing data in Python.

"""

states_of_america = ["Delaware","Pennsylvania","New Jersei","Georgia","Connecticut","Massachusetts","Maryland","South Carolina","New Hampshire","Virginia","New York","North Carolina","Rhode Island","Vermont","Kentucky","Tennessee","Ohio","Louisiana","Indiana","Mississippi","Illinois","Alabama","Maine","Missouri","Arkansas","Michigan","Florida","Texas","Iowa","Wisconsin","California","Minnesota","Oregon","Kansas","West Virginia","Nevada","Nebraska","Colorado","North Dakota","South Dakota","Montana","Washington","Idaho","Wyoming","Utah","Oklahoma","New Mexico","Arizona","Alaska","Hawaii"]

# Delaware is at the beginning of the list, so it has an offset or a shift of 0.
state_delaware = states_of_america[0]
print(state_delaware)

state_hawaii = states_of_america[-1]
print(state_hawaii)

states_of_america[2] = "New Jersey"
states_of_america.append("La La Land")
states_of_america.extend(["Jurassic Park", "Disney Land"])

print("States list in the US are: "+ str(states_of_america))
