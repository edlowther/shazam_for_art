from glob import glob
import os
from shutil import copyfile

index = 0
print(len(glob('./images/easier/rembrandt*')))
# for filename in glob('./images/backup_all/rembrandt*'):
#     print(filename)
#     copyfile(filename, filename.replace("backup_all", "easier").split("_")[0] + "_" + str(index) + '.jpg')
#     index += 1
