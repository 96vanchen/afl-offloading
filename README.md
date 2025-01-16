
Folders named "batch_size", "chi-bound", "fed_interval", "learning-rate", and "reward-para" are simulations of the algorithm with different parameters. Folders named "bs_ability", "converge-k", "fed_interval", "mt-size", and "task_size" are simulations of the algorithm in different environments.

You can refer to "6ue-fl-adaptive-3" in folder "learning-rate" for our proposed algorithm.

When running the program, please note the following:
1.	First, open the "ddpg.py" file in the "ddpg" folder, and modify the relevant path in the line of code "sys.path.append(xxx)" according to the location where you saved the files.
2.	Run "main.py" to execute the algorithm.
3.	Files named "plot" contain the visualization of the running results. In the lines of code "io.loadmat(xxx)", you should modify the path according to the location where the simulation results are saved.
