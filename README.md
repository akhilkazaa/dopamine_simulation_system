Dopamine Simulation System report documentation
Introduction
This project explores the simulation of decision-making processes in the brain by modelling the dopamine reward system. Inspired by the brain’s mechanism of prioritizing actions that maximize dopamine release, I aimed to understand how decision-making can be optimized using computational models. The focus of the project is on the intersection of learning, prediction, and rewards, with applications to neuroscience and artificial intelligence.
Objective
The objective of this project was to create a simulation that mimics the way the brain rewards certain actions through dopamine release. I aimed to simulate how these reward signals are processed using the Rescorla-Wagner Model, which focuses on learning associations between stimuli and responses, and Thompson Sampling, a decision-making algorithm used for reinforcement learning.
Stimuli and Reward Probabilities
In this project, three common activities were chosen, each given a predefined probability of generating a positive dopamine reward:
•	Exercise (0.1) – Associated with physical well-being and long-term rewards.
•	Gaming (0.57) – Provides instant and frequent gratification.
•	Reading (0.03) – Represents intellectual stimulation, with slower, more gradual rewards.
These probabilities reflect the hypothesis that gaming, being an addictive activity, generates more frequent dopamine rewards compared to exercise or reading, which have less immediate effects. This infrastructure allows the model to simulate how activities with different dopamine triggers might influence an individual's behaviour and preferences over time.
Reward Prediction Error:
The simulation incorporates the concept of reward prediction error, a key mechanism by which the brain adjusts its expectations based on actual outcomes. This is calculated by determining the difference between the actual reward and the expected reward:
Positive feedback occurs when the actual reward exceeds the expected reward, resulting in a positive reward prediction error.
Negative feedback occurs when the actual reward is lower than the expected reward, leading to a negative reward prediction error.
This process mirrors how the brain learns from experience, continuously adjusting future behaviour based on previous outcomes.
Methodology
1. Rescorla-Wagner Model: This model updates the expected reward variable by computing the difference between the expected reward and the actual reward to derive the prediction error, while applying the learning rate to determine the weight given to new data. In this simulation I used the equation:
ΔV=α (Actual Reward−Expected Reward)
where:
•	V(t) represents the expected reward.
•	α is the learning rate (set between 0 and 1), controlling the weight given to new information when updating expected reward variable.
•	δ symbolises the prediction error.
The value of the prediction error was calculated each iteration to update the expected reward variable, thereby simulating how the brain learns from reward-based experiences.
Thompson Sampling was incorporated into the model to address the exploration-exploitation trade-off in decision-making. This algorithm selects actions based on the probability of maximizing rewards, making it ideal for problems involving uncertainty. Thompson Sampling uses Bayesian inference to update its understanding of each action’s potential reward as more data becomes available.
In this model, Bayesian inference is implemented through a Beta distribution, which estimates the probability of receiving a reward for each action. The Beta distribution is updated with two parameters:
•	Alpha: Represents the number of positive outcomes (rewards).
•	Beta: Represents the number of negative outcomes (no reward).
At each iteration, the model:
1.	Samples from the Beta distribution for each action using the current values of alpha (positive rewards) and beta (negative rewards). This step estimates the likelihood of each action yielding a reward based on past experiences.
2.	Selects an action that maximizes the expected reward, with a bias toward choosing actions that have historically provided rewards. This demonstrates exploitation bias, where the system prefers the options that offer immediate and predictable rewards over exploring less certain alternatives. 
3.	Updates the beta distribution based on the observed outcome:
o	If a reward is received, alpha for that action is incremented, reinforcing the belief that the action will yield positive rewards.
o	If no reward is received, beta is incremented, indicating a higher likelihood of failure for that action.
Over time, the system increasingly favours actions that provide immediate gratification, showing how the exploitation bias drives behaviour. The simulation mirrors how real-life decision-making often defaults to repeatedly indulging in known rewards, even at the expense of exploring new or potentially better options. Bayesian inference continuously updates the probability distribution for each action, ensuring that the model becomes more focused on exploiting reliable rewards as more data is gathered.
By combining Thompson Sampling with the Rescorla Wagner Model, I simulated both the learning process (how the brain learns which actions are rewarding) and the decision-making process (how the brain chooses actions to maximize future rewards.)
Implementation
The simulation was coded in Python, utilizing libraries such as NumPy for handling the mathematical computations and arrays. The Rescorla-Wagner model was implemented to track how dopamine release changes with each action and how this influences future decisions. Thompson Sampling was applied to ensure the system continued exploiting safe reward options over exploring new actions.
Initialization: 
Stimuli Selection - Three stimuli are defined, each with their own fixed reward probability: exercise (0.1), gaming (0.57), and reading (0.03.) These probabilities simulate how likely a given stimulus will provide a dopamine release.
Iteration Setup: The simulation runs for 50,000 iterations, with each stimulus evaluated in each run.
Dataset Creation – A zero matrix X was created to track actual reward outcomes across all runs. If a random number generated between 0 and 1 fell below the stimulus’ reward probability, the corresponding element in the matrix becomes 1, marking a reward.
Initial Reward Values and Parameters:
Initial expected rewards (V) are assigned to each stimulus. These represent the brain's prior expectations of reward, inspired by the hypothesis of a video game addict brain. Video games had a high expected reward of 0.7, followed by exercise at 0.2 and reading at 0.1.
Two parameters, alpha (positive rewards) and beta (negative rewards), are initialized for each stimulus to facilitate updating future action choices based on observed rewards.
Thompson Sampling for Action Selection:
During each iteration, the model samples from a Beta distribution (based on the current values of alpha and beta for each stimulus) to determine which stimulus has the highest potential reward.
The Thompson Sampling strategy picks the action with the highest likelihood of providing the largest dopamine release, factoring in both the current expected reward (V) and the Beta-distributed sample.
Prediction Error and Reward Update:
Once a stimulus is selected, the actual reward is obtained from the dataset X for that stimulus during the current iteration.
The prediction error is calculated as the difference between the actual reward and the current expected reward (V) for that stimulus.
Using the Rescorla-Wagner model, the expected reward (V) is updated according to the learning rate and the prediction error. This step allows the model to adjust future expectations of reward based on past experiences.
Bayesian Update of Alpha and Beta:
After observing whether the selected stimulus provided a reward (1) or no reward (0), the model updates alpha (positive feedback) and beta (negative feedback) for that stimulus.
This allows the model to dynamically adjust how frequently each stimulus is selected in future iterations, aiming to maximize dopamine release over time.
Output:
After completing all iterations, the model outputs the number of positive feedback (rewards) received for each stimulus.
The stimulus that received the highest positive feedback is declared as the one most capable of stimulating dopamine release.
Testing
I conducted 5 test runs to see how my model performed:
Test NO:	Socialising reward	Gaming reward	Exercise reward	Reward ratio
1	0	1976	8	0: 271 :1
2	5	2127	1	5: 2127 :1
3	3	2154	0	3: 2154 :0
4	3	2154	2	3: 2154 :2
5	7	2141	1	7: 2141 :1

Reading, Gaming and Exercise average reward ratio – 3.6 : 2150.4 : 2.4
Based on this observation, it can be concluded that my model effectively simulates the brain of a video game addict and demonstrates how rewarding gaming can be to the brain. The degree of positive reward reaped by gaming, compared to other activities like exercise and reading, illustrates the power instant gratification in the form of gaming has over the brain’s decision-making process. This continuous positive feedback loop creates a reinforcement mechanism, making it difficult for individuals to break away from such activities, and highlights the exploration – exploitation bias in the human brain, whereby the brain chooses to exploit and repeat activities stimulating dopamine receptors, instead of exploring new stimuli, providing reasoning behind the origin of addiction.
The tests show that frequent dopamine rewards lead to stronger associations between the stimulus (gaming) and the reward, reinforcing the behaviour over time. This insight aligns with real-world addiction, where the brain prioritizes behaviours that trigger higher dopamine release, making it harder to shift focus toward less immediately rewarding activities like exercise or reading. Ultimately, the simulation provides a clear understanding of how addiction to highly rewarding stimuli, such as gaming, can become deeply ingrained in the brain, explaining why overcoming such addictions poses significant challenges.
Optimization to consider
From a critical perspective, there are a few improvements that can be made to the model:
Lack of scientific research
Considering the predefined reward probabilities at the very start of the program are fundamental to the performance of the model, these should have been determined with research. Instead, the probabilities were assumed based on the hypothesis, therefore decreasing the validity and accuracy of the model’s results.
Dynamic learning rate
A dynamic learning rate for the Rescorla Wagner equation which adapts over time would further improve accuracy, preventing fluctuations in expected reward once the model stabilizes. For example, I could begin by implementing a higher learning rate to adjust initial predictions before gradually decreasing this, which could lead to more refined reward predictions.
Incorporating a forgetting mechanism
To bolster the realism of the model, I could include the possibility the brain “forgets” or devalues stimuli over time, by introducing a decay factor as a forgetting mechanism to gradually reduce the strength of associations when stimuli are not encountered for a while. This would simulate the fading importance of activities which haven’t been engaged in which would make the model more biologically realistic. For example, when stimuli have not provided reward for a set number of iterations, the decay factor will reduce the strength of associations.


