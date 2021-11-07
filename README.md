# McGill-Physics-Hackathon
Created by Eve Wang and Jessica Zhu

We gauge the effectiveness of social distancing in preventing COVID19 transmission in this project.

Simulation of airborne COVID19 viruses using brownian motion and random walk concepts. 

From the simulation, the probability of infection for individual X distance away is calculated.

## Files
  - physics_hack.py: contents of our code to run the sim; currently runs a 2m distancing simulation. Can change the distance variable to run sims for desried distance
 
  - 2m_distancing_plot.png:  layered line plot of 1000 sims with 2m distancing
  
  - 2m_distancing_scatter.png:  scatter plot of the final positions of the airborne viruses with 2m distancing. See a gradient with highest concentration near the centre
  
  - probability_2m.png:  output of the graph along with the number of molecules in contact with a person, as well as the probability that the person if infected with covid while distancing 2m
  
  - probability_1m.png: output of graph with console for distancing of 1m


## Next Steps
  - Currently takes around 3 minutes to simulate 1000 molecules due to the nested loops. Make it more efficient
