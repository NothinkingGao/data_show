import requests
# download a file from url
def download(url,file_name = None):
    base_url, file_name = url.rsplit("/", 1)
    with open(file_name, "wb") as file:
        # use ssl to download the file
        response = requests.get(url, verify=True)
        file.write(response.content)


while True:
    try:
        # input the url of the file to be downloaded
        url = input("Enter the URL of the file to be downloaded: ")
        download(url, "file_name")
    except Exception as e:
        print("Error: ", e)
