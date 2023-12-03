import numpy as np 
import matplotlib.pyplot as plt
import statistics
 
#set width of bar 
barWidth = 0.15 
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 14), sharex=True)

#set height of bar 
User1 = [6.35, 3.83, 30.3, 29.02, 9.78, 11.28, 2.48, 26.3] 
User2 = [9.22, 8.05, 48.27, 11.93, 10.12, 12.18, 31.88, 20.83] 
User3 = [4.79, 3.51, 12.78, 45.62, 9.94, 8.85, 21.45, 61.96]
User4 = [3.35, 7.53, 17.7, 31.27, 6.2, 11.44, 8.75, 25.33]
User5 = [13.83, 3.03, 18, 20.37, 3, 10.86, 14.52, 19.08]

#calculating averages
ave1 = (User1[0] + User2[0] + User3[0] + User4[0] + User5[0])/5
ave2 = (User1[1] + User2[1] + User3[1] + User4[1] + User5[1])/5
ave3 = (User1[2] + User2[2] + User3[2] + User4[2] + User5[2])/5
ave4 = (User1[3] + User2[3] + User3[3] + User4[3] + User5[3])/5
ave5 = (User1[4] + User2[4] + User3[4] + User4[4] + User5[4])/5
ave6 = (User1[5] + User2[5] + User3[5] + User4[5] + User5[5])/5
ave7 = (User1[6] + User2[6] + User3[6] + User4[6] + User5[6])/5
ave8 = (User1[7] + User2[7] + User3[7] + User4[7] + User5[7])/5

#calculating sd
task1 = [User1[0], User2[0], User3[0], User4[0], User5[0]]
task2 = [User1[1], User2[1], User3[1], User4[1], User5[1]]
task3 = [User1[2], User2[2], User3[2], User4[2], User5[2]]
task4 = [User1[3], User2[3], User3[3], User4[3], User5[3]]
task5 = [User1[4], User2[4], User3[4], User4[4], User5[4]]
task6 = [User1[5], User2[5], User3[5], User4[5], User5[5]]
task7 = [User1[6], User2[6], User3[6], User4[6], User5[6]]
task8 = [User1[7], User2[7], User3[7], User4[7], User5[7]]

sd1 = statistics.pstdev(task1)
sd2 = statistics.pstdev(task2)
sd3 = statistics.pstdev(task3)
sd4 = statistics.pstdev(task4)
sd5 = statistics.pstdev(task5)
sd6 = statistics.pstdev(task6)
sd7 = statistics.pstdev(task7)
sd8 = statistics.pstdev(task8)

#printing averages and sds
print("AVERAGE TIMES AND STANDARD DEVIATIONS FOR EACH TASK:")
print("Average time to complete Task 1: {:.3f}".format(ave1) + " and the standard deviation was: {:.3f}".format(sd1))
print()
print("Average time to complete Task 2: {:.3f}".format(ave2) + " and the standard deviation was: {:.3f}".format(sd2))
print()
print("Average time to complete Task 3: {:.3f}".format(ave3) + " and the standard deviation was: {:.3f}".format(sd3))
print()
print("Average time to complete Task 4: {:.3f}".format(ave4) + " and the standard deviation was: {:.3f}".format(sd4))
print()
print("Average time to complete Task 5: {:.3f}".format(ave5) + " and the standard deviation was: {:.3f}".format(sd5))
print()
print("Average time to complete Task 6: {:.3f}".format(ave6) + " and the standard deviation was: {:.3f}".format(sd6))
print()
print("Average time to complete Task 7: {:.3f}".format(ave7) + " and the standard deviation was: {:.3f}".format(sd7))
print()
print("Average time to complete Task 8: {:.3f}".format(ave8) + " and the standard deviation was: {:.3f}".format(sd8))
print()
print()
 
#Set position of bar on x-axis 
tasks = ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5', 'Task 6', 'Task 7', 'Task 8']
br1 = np.arange(len(tasks)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 
br4 = [x + barWidth for x in br3]
br5 = [x + barWidth for x in br4]  

#Plot average times
for i, user in enumerate([User1, User2, User3, User4, User5]):
    axes[0].bar(eval(f'br{i+1}'), user, color=f'C{i}', width=barWidth,
                edgecolor='grey', label=f'User {i+1}')

U1 = [0, 0, 0, 1, 0, 0, 0, 1]
U2 = [0, 0, 2, 1, 0, 1, 0, 1]
U3 = [0, 0, 0, 1, 0, 0, 0, 4]
U4 = [0, 0, 0, 0, 0, 0, 0, 1]
U5 = [1, 0, 0, 0, 0, 0, 0, 0]

#calculating averages
av1 = (U1[0] + U2[0] + U3[0] + U4[0] + U5[0])/5
av2 = (U1[1] + U2[1] + U3[1] + U4[1] + U5[1])/5
av3 = (U1[2] + U2[2] + U3[2] + U4[2] + U5[2])/5
av4 = (U1[3] + U2[3] + U3[3] + U4[3] + U5[3])/5
av5 = (U1[4] + U2[4] + U3[4] + U4[4] + U5[4])/5
av6 = (U1[5] + U2[5] + U3[5] + U4[5] + U5[5])/5
av7 = (U1[6] + U2[6] + U3[6] + U4[6] + U5[6])/5
av8 = (U1[7] + U2[7] + U3[7] + U4[7] + U5[7])/5

#calculating sd
t1 = [U1[0], U1[0], U3[0], U4[0], U5[0]]
t2 = [U1[1], U2[1], U3[1], U4[1], U5[1]]
t3 = [U1[2], U2[2], U3[2], U4[2], U5[2]]
t4 = [U1[3], U2[3], U3[3], U4[3], U5[3]]
t5 = [U1[4], U2[4], U3[4], U4[4], U5[4]]
t6 = [U1[5], U2[5], U3[5], U4[5], U5[5]]
t7 = [U1[6], U2[6], U3[6], U4[6], U5[6]]
t8 = [U1[7], U2[7], U3[7], U4[7], U5[7]]

s1 = statistics.pstdev(t1)
s2 = statistics.pstdev(t2)
s3 = statistics.pstdev(t3)
s4 = statistics.pstdev(t4)
s5 = statistics.pstdev(t5)
s6 = statistics.pstdev(t6)
s7 = statistics.pstdev(t7)
s8 = statistics.pstdev(t8)

#printing averages and sds
print("AVERAGE MISTAKES AND STANDARD DEVIATIONS FOR EACH TASK:")
print("Average time to complete Task 1: {:.3f}".format(av1) + " and the standard deviation was: {:.3f}".format(s1))
print()
print("Average time to complete Task 2: {:.3f}".format(av2) + " and the standard deviation was: {:.3f}".format(s2))
print()
print("Average time to complete Task 3: {:.3f}".format(av3) + " and the standard deviation was: {:.3f}".format(s3))
print()
print("Average time to complete Task 4: {:.3f}".format(av4) + " and the standard deviation was: {:.3f}".format(s4))
print()
print("Average time to complete Task 5: {:.3f}".format(av5) + " and the standard deviation was: {:.3f}".format(s5))
print()
print("Average time to complete Task 6: {:.3f}".format(av6) + " and the standard deviation was: {:.3f}".format(s6))
print()
print("Average time to complete Task 7: {:.3f}".format(av7) + " and the standard deviation was: {:.3f}".format(s7))
print()
print("Average time to complete Task 8: {:.3f}".format(av8) + " and the standard deviation was: {:.3f}".format(s8))

#Set position of bar on x-axis 
br1 = np.arange(len(tasks)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 
br4 = [x + barWidth for x in br3]
br5 = [x + barWidth for x in br4]

#Plot average mistakes
for i, user in enumerate([U1, U2, U3, U4, U5]):
    axes[1].bar(eval(f'br{i+1}'), user, color=f'C{i}', width=barWidth,
                edgecolor='grey', label=f'User {i+1}')

#Adding x-axis labels
axes[1].set_xlabel('Task Number', fontweight='bold', fontsize=15)
axes[0].set_ylabel('Amount of Time the Task Took', fontweight='bold', fontsize=15)
axes[1].set_ylabel('Number of Mistakes', fontweight='bold', fontsize=15)
axes[1].set_xticks([r + 2 * barWidth for r in range(len(tasks))])
axes[1].set_xticklabels(tasks)

#Display legends
axes[0].legend()
axes[1].legend()

#Display the plot
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



