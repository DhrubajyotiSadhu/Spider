import os

# Make a directory for crawled and queued files:
def create_project_directory(project_name):
    if not os.path.exists(project_name):
        print "Creating Directory - "+ project_name
        os.makedirs(project_name)

# Create 2 file for crawled and queued files:
def create_data_files(project_name, base_url):
    crawled = project_name + "/crawled.txt"
    queued = project_name + "/queued.txt"
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isfile(queued):
        write_file(queued, base_url)

# Writting data into queued and crawler file:
def write_file(file, data):
    try:
        f = open(file,'w')
        f.write(data + '\n')
        f.close()
    except IOError:
        print "Error Writting file." + file

# Append data to an existing file:
def append_data_into_file(file, data):
    try:
        f = open(file, 'a')
        f.write(data + '\n')
        f.close()
    except IOError:
        print "Error Appending file."+ file

# Deleting the content of the file:
def delete_data_from_file(file):
    try:
        open(file, 'w')
        pass # Open the file and do nothing
    except IOError:
        print "File does not exists - " + file

# Write the content of the file to a set
def file_to_set(file):
    links = set()
    with open(file, 'rt') as f: # 'rt' - read text file
        for line in f:
            links.add(line.replace('\n',''))
    return links

# Write the content of the set to a file
def set_to_file(links, file):
    delete_data_from_file(file)
    for urls in links:
        append_data_into_file(urls)


# create_project_directory("Thenewboston")
# create_data_files("Thenewboston", "https://www.thenewboston.com")
# delete_data_from_file("/home/osboxes/my_git/Spider/src/Thenewboston/queued.txt")
# append_data_into_file("/home/osboxes/my_git/Spider/src/Thenewboston/queued.txt", "Apple_India")
# append_data_into_file("/home/osboxes/my_git/Spider/src/Thenewboston/queued.txt", "Apple_Suchandra")
