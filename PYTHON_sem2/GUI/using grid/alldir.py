import os

def list_directories(drive_path):
    directories = [d for d in os.listdir(drive_path) if os.path.isdir(os.path.join(drive_path, d))]
    return directories

drive_path = "C:"  # Replace with the drive you want to explore
directories_in_drive = list_directories(drive_path)

print("Directories in {}: {}".format(drive_path, directories_in_drive))
