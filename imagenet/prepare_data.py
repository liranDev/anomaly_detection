import splitfolders
import os

input_folder = 'dataset/raw_data'
print(os.path.isdir(input_folder))
output = 'dataset/'

splitfolders.ratio(input_folder, output=output, ratio=(.7, .15, .15))
