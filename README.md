# bran-survival-analysis
This project is a second attempt to estimate the survival function of the brancher-annihilator process, a continuation of work done at the HWS 2021 REU under Dr. Hao.

The purpose of this repository is to estimate the survival function of the brancher-annihilator process, a particular stochastic cellular automaton (SCA) (also known as an interacting partical system) first introduced to me by Dr. Yan Hao at Hobart and William Smith Colleges during their summer 2021 mathematics REU.

With a partner (Jack Reever), I developed simulations of this SCA in Python. We were able to produce some preliminary visualizations, but we did not succeed in analyzing the survival function of messages. After that summer, I took a theoretical approach to the problem, which was able to generate some minor insights into the structure of the SCA, but not enough to calculate the survival function.

This time, I am taking a statistical approach; furthermore, I plan to do a much better job of keeping this respository organized, so that if anyone wants/needs to follow my thought process (perhaps future REU students at HWS), they will have a better understanding of my thought process. The plan is to use survival analysis to estimate the survivor function, and use various local and global network parameters as explanatory variables. 

In the event that I find something interesting, I also plan to write an article from this work, submit it for publication, and then share it with Dr. Hao and her collaborators. This write up will also be useful for anyone who wants to see my work, although it will likely be in a more academic than data-analytic style. To fill that gap, I may also produce a brief write up in the latter style.
