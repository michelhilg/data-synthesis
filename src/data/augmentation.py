"""
Conventional Augmentation Pipeline

Implementation

The purpose of this notebook is to implement the conventional augmentation pipeline as outlined in sections 3.3.0 of the bachelor thesis.

The augmentation pipeline applies basic spatial and color transformations on the raw dataset.
"""

import torchvision.transforms as transforms
import os
from torchvision.utils import save_image
from labels import general_csv, class_csv
from custom_dataset import CustomDataset

#Data Structure
discrete_class = {1 : "0_punching_hole",
                  2 : "1_welding_line",
                  3 : "2_crescent_gap",
                  4 : "3_water_spot",
                  5 : "4_oil_spot",
                  6 : "5_silk_spot",
                  7 : "6_inclusion",
                  8 : "7_rolled_pit",
                  9 : "8_crease",
                  10 : "9_waist_folding"}

#Transformation Pipeline
aug_transforms = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomVerticalFlip(p=0.5),
    transforms.RandomChoice([transforms.RandomRotation((0, 0)), 
                             transforms.RandomRotation((180, 180)), 
                             ]),
    transforms.RandomApply([transforms.ColorJitter(brightness=((0.75, 1.25)))], p=0.75),
    transforms.RandomApply([transforms.ColorJitter(contrast=((0.75, 1.25)))], p=0.75),
    transforms.RandomApply([transforms.ColorJitter(saturation=((0.75, 1.25)))], p=0.75),
    transforms.RandomApply([transforms.GaussianBlur(kernel_size=(3, 3), sigma=(0.1, 2.0))], p=0.25)])

#Creating the datasets class specific
labels_file = []
root_dir = []
datasets = []

for i in range(1,11):
    labels_file.append('path/to/raw/training/root/folder' + discrete_class[i] + '.csv')
    root_dir.append('path/to/raw/training/images' + discrete_class[i])
    datasets.append(CustomDataset(labels_file=labels_file[i-1], root_dir=root_dir[i-1]))
    
#Appling the augmentation
def applyAugmentation(dataset, root_path, aug_tranforms, to_tensor, num_instances):
    """Apply augmentation until match a defined number of instances in each class"""
    img_num = 0
    for _ in range(num_instances // dataset.__len__()):
        for image, label in dataset:
            image = aug_tranforms(image)
            image = to_tensor(image)
            if img_num < (num_instances-dataset.__len__()):
                save_image(image, os.path.join(root_path, dataset.__getlabel__(0),'img_augmented_'+str(img_num)+'.jpg'))
                img_num += 1
            else:
                break
    return print('Done!')

to_tensor = transforms.ToTensor()
augmented_path = '/root/path/to/augmented/images'
num_instances = 1000

for i in range(10):
    applyAugmentation(datasets[i], augmented_path, aug_transforms, to_tensor, num_instances)

#Generating labels
general_csv(discrete_class=discrete_class, data_path=augmented_path)
class_csv(discrete_class=discrete_class, data_path=augmented_path)