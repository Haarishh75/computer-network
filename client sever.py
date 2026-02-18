import urllib.request

try:
    file_name = "digital_image_processing.jpg"
    website = "http://tutorialspoint.com/java_dip/images/" + file_name

    print("Downloading File From:", website)

    # Open URL
    with urllib.request.urlopen(website) as response:
        with open(file_name, 'wb') as output_file:
            buffer_size = 2048
            
            while True:
                data = response.read(buffer_size)
                if not data:
                    break
                print("Buffer Read of length:", len(data))
                output_file.write(data)

    print("Download Complete!")

except Exception as e:
    print("Exception:", str(e))
