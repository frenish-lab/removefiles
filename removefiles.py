import time
import os
import shutil
def main():
    path="/PATH_TO_DELETE"
    days=30
    deleted_folders_count=0
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            folder_path=os.path.join(root_folder,folders)
            if seconds>=get_file_or_folder_age(folder_path):
                remove_folder(folder_path)
                deleted_folders_count+=1
def get_file_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime            
def remove_folder(path):
    if not os.remove(path):
        print("path is removed successfully")
    else:
        print("unable to delete")    
if __name__=='__main__':
    main()          