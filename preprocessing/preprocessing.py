import os
files = [name for name in os.listdir("/content/PlantVillage-Dataset/raw/color")]
print(len(sorted(files)))

arr=["PlantVillage-Dataset/raw/color/Tomato___Tomato_Yellow_Leaf_Curl_Virus","PlantVillage-Dataset/raw/color/Tomato___Target_Spot","PlantVillage-Dataset/raw/color/Tomato___Spider_mites Two-spotted_spider_mite","PlantVillage-Dataset/raw/color/Tomato___Septoria_leaf_spot","PlantVillage-Dataset/raw/color/Tomato___Early_blight",
"PlantVillage-Dataset/raw/color/Blueberry___healthy","PlantVillage-Dataset/raw/color/Corn_(maize)___Northern_Leaf_Blight","PlantVillage-Dataset/raw/color/Grape___Black_rot","PlantVillage-Dataset/raw/color/Orange___Haunglongbing_(Citrus_greening)","PlantVillage-Dataset/raw/color/Potato___healthy","PlantVillage-Dataset/raw/color/Raspberry___healthy","PlantVillage-Dataset/raw/color/Soybean___healthy","PlantVillage-Dataset/raw/color/Squash___Powdery_mildew","PlantVillage-Dataset/raw/color/Tomato___Leaf_Mold","PlantVillage-Dataset/raw/color/Tomato___Tomato_mosaic_virus"]
print(len(arr))
for i in arr:
    #!rm -rf "{i}"
    print(i)

root_dir=r'PlantVillage-Dataset/raw/color'
files = [name for name in os.listdir(root_dir)]
print(files)

for file in files:
  newpath = r'PlantVillage-Dataset/raw/test/'+file
  if not os.path.exists(newpath):
      os.makedirs(newpath)
import os
import shutil
import random

root_dir = r'PlantVillage-Dataset/raw/color/'
output_dir =r'PlantVillage-Dataset/raw/test/'
ref = 1
files = [name for name in os.listdir(root_dir)]

for name in files:
    print(root_dir+name)
    print('hi')
    for root, dirs, files in os.walk(root_dir+name):
        print(root)
        print(dirs)
        print(files)
        number_of_files = len(os.listdir(root))
        if number_of_files > ref:
            ref_copy = int(round(0.2 * number_of_files))
            for i in range(ref_copy):
                chosen_one = random.choice(os.listdir(root))
                file_in_track = root
                file_to_copy = file_in_track + '/' + chosen_one
                if os.path.isfile(file_to_copy) == True:
                    shutil.move(file_to_copy,output_dir+name)
                    print(file_to_copy)
        else:
            for i in range(len(files)):
                track_list = root
                file_in_track = files[i]
                file_to_copy = track_list + '/' + file_in_track
                if os.path.isfile(file_to_copy) == True:
                    shutil.move(file_to_copy,output_dir+name)
                    print(file_to_copy)
print('Finished !')