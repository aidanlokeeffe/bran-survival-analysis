import numpy as np
import pandas as pd

class BrancherAnnihilator(object):
    # Constructor
    def __init__(self, adjacency_matrix, injection_probability, num_messages):
        self.A = adjacency_matrix
        self.n = self.A.shape[0]
        self.p = injection_probability
        self.Alpha = num_messages
    
    # Uniformly distributed initial state
    def get_x0(self):
        return np.array( [np.random.choice([complex("0"),complex("1")]) for i in range(self.n)] )
    
    # Injection vector whose L1 norm follows a Binomial(n,p) distribution
    def get_b(self):
        return np.array( [np.random.choice([complex("0"),complex("1")], p=[1-self.p, self.p]) for i in range(self.n)] )
    
    # Uniformly chooses an incoming message to track (will throw an error if b is the 0 vector)
    def inject_tracker(self, b):
        support = [i for i in range(self.n) if b[i,]]
        node = np.random.choice(support)
        b[node,] = complex("j")
    
    # Multiply each component by the indicator that the total number of messages (tracked or untracked) is exactly 1
    def collide(self, y):
        return np.array( [ y[i,]*(y[i,].real + y[i,].imag == 1) for i in range(self.n) ] )
    
    # Carry out the simulation. The output is a dictionary whose keys are the message labels and whose entries are the corresponding survival times
    def simulate(self):
        # These are variables related to message tracking, not the dynamics per se
        survival_times = dict()
        alpha = 0
        need_injection = True

        # This will be the initial state x_0
        x = self.get_x0()

        # Now, carry out the process until Alpha messages have been tracked
        while alpha < self.Alpha:
            # Get b_t
            b = self.get_b()

            # If it is necessary and possible to inject a tracker, then do so, and update tracking variables accordingly
            if need_injection and np.sum(b) > 0:
                self.inject_tracker(b)
                need_injection = False
                alpha += 1
                survival_times[alpha] = 1
            
            # Calculate the next state
            x = self.collide(np.matmul( self.A, x) + b)

            # Check if message alpha has survived or not, and update accordingly
            if complex("j") in x:
                survival_times[alpha] += 1
            else:
                need_injection = True
        
        survival_times = pd.DataFrame(survival_times.items())
        survival_times.columns = ["MESSAGE_ID", "SURVIVAL_TIME"]
        
        return survival_times


