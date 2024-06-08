
import pandas as pd

def load_data(data):
    df = pd.read_csv(data)
    # ------------------Head------------------
    head = df.head()
    # ------------------Describe------------------
    shape = df.shape 
    # ------------------Info------------------
    info = df.info()

    output = {'Head': head,
              'Shape': shape
              'info': info
             }

    return output
