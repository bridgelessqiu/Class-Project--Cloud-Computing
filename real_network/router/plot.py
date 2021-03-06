import matplotlib.pyplot as plt

x = [0, 0.01, 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.19, 0.21, 0.23, 0.25]

# [, , , , , , , , , , , , , ]

y_mine_naive = [0.998945, 0.99804, 0.996984, 0.992913, 0.995024, 0.992159, 0.992612, 0.986882, 0.983414, 0.979343, 0.980097, 0.975724, 0.97301, 0.968034]

y_mine_advanced = [1, 1, 0.999246, 0.998492, 0.997286, 0.997286, 0.99427, 0.994119, 0.991707, 0.991104, 0.990501, 0.986279, 0.982509, 0.985374]

y_netal = [1, 0.998794, 0.995326, 0.990048, 0.988691, 0.983414, 0.971954, 0.968486, 0.96547, 0.974065, 0.952503, 0.964113, 0.972708, 0.89611]

y_hubalign = [1, 0.99608, 0.891586, 0.951297, 0.876659, 0.419029, 0.818758, 0.852232, 0.357961, 0.388571, 0.447829, 0.400633, 0.371381, 0.372738]

y_isorank = [0.998191, 0.128922, 0.128329, 0.123792, 0.112938, 0.091827, 0.172635, 0.098371, 0.112927, 0.134628, 0.153628, 0.128601, 0.137892, 0.122534]

plt.xlabel("Noise level")
plt.ylabel("EC")
plt.ylim((0, 1.1))

plt.title("Router network")

plt.plot(x, y_mine_naive, 'o--', label='Naive_alignment')
plt.plot(x, y_mine_advanced, 'o--', label='Seed_alignment')
plt.plot(x, y_hubalign, 'o--', label='HubAlign')
plt.plot(x, y_netal, 'o--', label='NETAL')
plt.plot(x, y_isorank, 'o--', label='IsoRank')
plt.legend()

plt.show()
