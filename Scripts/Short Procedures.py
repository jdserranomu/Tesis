##

import os
import numpy as np
import pandas as pd
import glob

##
# Join trainLabels.csv and testLabels.csv and create labels.csv. All annotation should appear in this file even if some
# images are damaged and preprocessing operations do not apply to them, in case this happens this should be noted in the
# file corresponding the preprocessing made.

labels_folder = os.path.join("Database", "labels")

df_train_labels = pd.read_csv(os.path.join(labels_folder, "trainLabels.csv"))
df_test_labels = pd.read_csv(os.path.join(labels_folder, "testLabels.csv"))

df_labels = pd.concat([df_test_labels.drop(columns=["Usage"]), df_train_labels])

print(f'Todas los nombres de imagenes son unicos: {len(pd.unique(df_labels["image"])) == len(df_labels)}')

df_labels.to_csv(os.path.join(labels_folder, "labels.csv"), index=False)

