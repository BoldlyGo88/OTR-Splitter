import json
import os
import shutil
import math

manifest = "manifest.json"
current_directory = os.getcwd()
combineable = []
cthresh = 0
cmb_manifest = {}

print("OTR-Splitter v1.2\n")
print("1. You can't put a value lower than 1000, doing so will just make it 1000\n2. Default and tested value is 1350\n3. Values <1350 could result in the Misc folder filling and more parts being made todo: fix this one day")
print("4. Files that are split and converted to .otr with Retro will probably take a lot more space, so plan for that\n")
print("How many files will be in each partition, for fat32 and to be safe use <=1400")
split_amount = input("Enter the max amount of files per split: ")

try:
    split_amount = int(split_amount)
except ValueError:
    split_amount = 1350
    
if split_amount < 1000: split_amount = 1000

def manifest_path(path):
    return os.path.splitext(path.replace("\\", "/"))[0]

def copy_structure(root, file, destination):
    directories = os.path.dirname(file).split(os.sep)
    os.makedirs(os.path.join(destination, *directories[directories.index(root):]), exist_ok=True)

def ine_create(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_dir_size(directory):
    count = 0
    
    for a, b, files in os.walk(directory):
        for f in files:
            count += 1
    
    return count

def dir_partition(directory, mdata, combined=False):
    parts = 1
    count = 0
    tmp = {}
    tmp_manifest = {}
    dir_size = get_dir_size(directory)
    
    if not combined:
        ine_create(f"OTR-Splitter-{directory}_{parts}")
    
        for source, sd, files in os.walk(directory):
            for f in files:
                path = os.path.join(source, f)
            
                if count % split_amount == 0 and count > 0:
                    ine_create(f"OTR-Splitter-{directory}_{parts}")
                    with open(f"OTR-Splitter-{directory}_{parts}/manifest.json", "w") as newman:
                        json.dump(tmp_manifest, newman, indent=2)
                    
                    tmp_manifest = {}
                    count = 0
                    parts += 1
                                
                if count == 0:
                    tmp[f"OTR-Splitter-{directory}_{parts}"] = { "paths": [], "names": []}
                
                if parts == math.ceil(dir_size/split_amount):
                    if "OTR-Splitter-Misc" not in tmp:
                        tmp[f"OTR-Splitter-Misc"] = { "paths": [], "names": []}
                    tmp["OTR-Splitter-Misc"]["paths"].append(path)
                    tmp["OTR-Splitter-Misc"]["names"].append(os.path.splitext(f)[0])
                else:
                    tmp[f"OTR-Splitter-{directory}_{parts}"]["paths"].append(path)
                    tmp[f"OTR-Splitter-{directory}_{parts}"]["names"].append(os.path.splitext(f)[0])
             
                if manifest_path(path) in mdata:
                    print(f"Adding {os.path.splitext(f)[0]} to manifest...")
                    if parts == math.ceil(dir_size/split_amount):
                        cmb_manifest[manifest_path(path)] = mdata[manifest_path(path)]
                    else:
                        tmp_manifest[manifest_path(path)] = mdata[manifest_path(path)]
                    
                count += 1
    
        if len(tmp_manifest) > 0:
            ine_create(f"OTR-Splitter-{directory}_{parts}")
            with open(f"OTR-Splitter-{directory}_{parts}/manifest.json", "w") as newman:
                json.dump(tmp_manifest, newman, indent=2)
   
        for key, data in tmp.items():
            for i, name in enumerate(data["names"]):
                print(f"Copying {name}...")
                copy_structure(directory, data["paths"][i], key)
                shutil.copy2(f"{data['paths'][i]}", f"{key}/{data['paths'][i]}")
    else:
        ine_create("OTR-Splitter-Misc")
        
        for source, sd, files in os.walk(directory):
            for f in files:
                path = os.path.join(source, f)
            
                if count == 0:
                    tmp["OTR-Splitter-Misc"] = { "paths": [], "names": []}
            
                tmp["OTR-Splitter-Misc"]["paths"].append(path)
                tmp["OTR-Splitter-Misc"]["names"].append(os.path.splitext(f)[0])
             
                if manifest_path(path) in mdata:
                    print(f"Adding {os.path.splitext(f)[0]} to manifest...")
                    cmb_manifest[manifest_path(path)] = mdata[manifest_path(path)]
                
                count += 1
                        
        for i, name in enumerate(tmp["OTR-Splitter-Misc"]["names"]):
            print(f"Copying {name}...")
            copy_structure(directory, tmp["OTR-Splitter-Misc"]["paths"][i], "OTR-Splitter-Misc")
            shutil.copy2(f"{tmp['OTR-Splitter-Misc']['paths'][i]}", f"OTR-Splitter-Misc/{tmp['OTR-Splitter-Misc']['paths'][i]}")

if not os.path.exists(manifest):
    raise FileNotFoundError("manifest.json could not be found!")
    
with open(manifest, "r") as man:
    mandata = json.load(man)

for dir in [di for di in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, di))]:
    if get_dir_size(dir) <= split_amount and (get_dir_size(dir) + cthresh) <= split_amount:
        combineable.append(dir)
        cthresh += get_dir_size(dir)
    dir_partition(dir, mandata, True) if dir in combineable else dir_partition(dir, mandata)

if len(cmb_manifest) > 0:
    ine_create("OTR-Splitter-Misc")
    with open("OTR-Splitter-Misc/manifest.json", "w") as newman:
        json.dump(cmb_manifest, newman, indent=2)

print(f"Split successful and ready to be built with Retro!")
input("Press Enter to exit...")
