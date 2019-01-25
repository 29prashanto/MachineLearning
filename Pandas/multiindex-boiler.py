import numpy as np
import pandas as pd

myIndex = [('Slot1', 1), ('Slot1', 2), ('Slot1', 3), ('Slot2', 1), ('Slot2', 2), ('Slot2', 3)]
myIndex = pd.MultiIndex.from_tuples(myIndex)

dataFrame = pd.DataFrame(np.random.randn(6,2), index=myIndex, columns=['Res1', 'Res2'])