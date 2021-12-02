import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
    
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A9bvgWfk0EtgCaBZ-tt2vHRa6BquzZZgGHWUEDFgLdV7G60rZ8ZWW8Mn61LLVmaE4azhGOiBClPCgsGGJ9ksBedxmyugHMzIHiv4YVyumkPB0KxZjOzV9JJ-SC-Dc0iIswmZaFU'
    transferData = TransferData(access_token)
    
    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("The file has been moved")

main()