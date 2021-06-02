import tocm_reference_data as ref
import matplotlib.pyplot as plt

for line in ref.Hestand_2015.figure7.lines:
    plt.plot(line.x, line.y, label=line.label)

plt.legend()
plt.show()

print(ref.Hestand_2015.metadata)