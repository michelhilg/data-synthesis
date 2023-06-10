"""
Custom Dataset

Implementation

Deifne a custom PyTorch dataset for data manipulation.
"""

from PIL import Image
import os
from PIL import Image
import pandas as pd
import torch
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self, labels_file, root_dir, transforms=None):
        self.annotations = pd.read_csv(labels_file, header=None)
        self.root_dir = root_dir
        self.transform = transforms

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, index):
        img_path = os.path.join(self.root_dir, self.annotations.iloc[index, 0])
        image = Image.open(img_path)
        label = torch.tensor(int(self.annotations.iloc[(index, 2)]))

        if self.transform:
            image = self.transform(image)

        return(image, label)
    
    def __getlabel__(self, index):
        label = self.annotations.iloc[(index, 1)]      

        return(label)