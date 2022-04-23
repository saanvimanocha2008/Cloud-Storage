import os
import dropbox
from dropbox.files import WriteMode
#
class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token
#
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    # construct the full local path
                local_path = os.path.join(root, filename)

                    # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BFbiem4lJeopuf1WamWGP0sU_3uG29hcPLhoBZg_PXUnjFF6OpjTuNxio3HDdZeIthcP_evo4vLcC3W_0qFUfxquSE53C-4hlXrMnpPZnmcOfNzXeGjH7AHbEZsJcM90rrfejzaU'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : -"))
    file_to = input("enter the full path to upload to dropbox:- ") 
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()


