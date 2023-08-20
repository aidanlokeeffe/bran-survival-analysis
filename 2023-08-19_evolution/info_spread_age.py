import numpy as np
import pandas as pd

class info_spread_age(object):
    # Constructor
    def __init__(self, adj, inj_p, num_msg):
        self.adj = adj
        self.N = self.adj.shape[0]
        self.inj_p = inj_p
        self.num_msg = num_msg
    
    # Uniformly distributed initial state
    def get_x0(self):
        return self.get_b(inj_p=0.5)
    
    # Injected vector
    def get_b(self, inj_p):
        return np.random.choice([complex("0"), complex("1")], size=self.N, p=[1-inj_p, inj_p], replace=True)
    
    # Modify b in-place by adding a message tracker 
    def inject_tracker(self, b):
        support = [i for i in range(self.N) if b[i]]
        choice = np.random.choice(support)
        b[choice] = complex("j")
    
    # Execute collisions. Note that we have to use a more complicated
    # formula because if we use the easy one, we'll always lose the
    # tracker
    def collide(self, z):
        return z * np.array(z.real + z.imag == 1, dtype=int)

    # Carry out the simulation. The output is the mean message age
    def simulate(self):
        # The summed ages approach is for a streamlined calculation
        # The dictionary approach is the old one. We know it works, and
        # we'll use it to test the results of this new approach

        survival_times = dict()

        summed_ages = 0
        curr_msg = -1
        need_inj = True
        
        x = self.get_x0()
        while curr_msg < self.num_msg - 1:
            b = self.get_b(self.inj_p)
            if need_inj and np.sum(b) > 0:
                self.inject_tracker(b)
                need_inj = False
                curr_msg += 1
                summed_ages += 1
                survival_times[curr_msg] = 1
                
            x = self.collide(np.matmul(self.adj, x) + b)

            if complex("j") in x:
                summed_ages += 1
                survival_times[curr_msg] += 1
            else:
                need_inj = True
        
        survival_times = pd.DataFrame(survival_times.items())
        survival_times.columns = "MESSAGE_ID", "SURVIVAL_TIME"

        return summed_ages / self.num_msg, survival_times