# interpolate

import pandas as pd
data = {
    "time":[1,2,4,None,16],
    "value":[3,6,None,None,15]
}
df = pd.DataFrame(data)
print(df)
print()
df[["time","value"]] = df[["time","value"]].interpolate(method="linear")
print(df)