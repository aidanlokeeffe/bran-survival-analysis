# bran-survival-analysis
This project uses a statistical approach to solve a problem in mathematics. 

To give a short description of the problem, we have a directed network, and every second, three rules are applied:
  1) Every message already on the network sends a copy of itself to all available neighbors of their current node,
  2) Some number of additional messages are injected into the network, and
  3) Any messages sent/injected to the same node collide, and those copies are deleted from the network.

This project seeks to use survival analysis to understand how the structure of the network affects the number of seconds that pass until all copies of a particular message are deleted.

The intended audience of this project is twofold:
  1) Employers who want to see a demonstration of skills relevant to data science, and 
  2) Mathematicians, especially my former collaborators, who may want to understand this work.

This is a challenging project, and when it is complete, is will demonstrate several skills:
  1) Experience with Python libraries used in data science, namely numpy and scikit.learn,
  2) The ability to handle network data,
  3) Study design and the generation of synthetic data,
  3) Survival analysis,
  4) Research skills, and
  5) Persistence, in that I have continually come back to this project despite getting stuck many times.