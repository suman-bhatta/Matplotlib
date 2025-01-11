"Creating Pie Charts"

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 


"Labels"

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Python", "Pandas", "Numpy", "Matplotlib"]

plt.pie(y, labels = mylabels)
plt.show() 


"Start Angle"

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Python", "Java", "JavaScript", "PHP"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 


"Explode"

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Django", "Express", "Spring Boot", "Laravel"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 


"Shadow"

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Python", "Pandas", "Numpy", "Matplotlib"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 


"Colors"

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Python", "Pandas", "Numpy", "Matplotlib"]
mycolors = ["Red", "Green", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()


"Legend"

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Python", "Pandas", "Numpy", "Matplotlib"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 



"Legend With Header"

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Scikit-learn", "Pandas", "Numpy", "Matplotlib"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Libraries:")
plt.show()