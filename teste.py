import numpy as np
import matplotlib.pyplot as plt

data = np.array([[[70, 19, 2],
                  [[70, 19, 2],
                   [70, 19, 2],
                   [135, 46, 28],
                   [135, 46, 28],
                   [137, 48, 30]],
                  [[70, 19, 2],
                   [70, 19, 2],
                   [70, 19, 2],
                   [135, 46, 28],
                   [135, 46, 28],
                   [136, 47, 29]],
                  [[71, 18, 2],
                   [70, 19, 2],
                   [70, 19, 2],
                   [135, 46, 28],
                   [135, 46, 28],
                   [134, 45, 27]],
                  [[90, 117, 36],
                   [91, 118, 37],
                   [90, 119, 37],
                   [116, 129, 57],
                   [116, 129, 57],
                   [116, 129, 57]],
                  [[92, 117, 36],
                   [90, 117, 36],
                   [91, 118, 37],
                   [117, 130, 58],
                   [116, 129, 57],
                   [116, 130, 55]],
                  [[92, 117, 36],

                   [93, 118, 37],
                   [118, 131, 59],
                   [116, 130, 55],
                   [115, 129, 54]]]])

plt.plot(data)
plt.show()
