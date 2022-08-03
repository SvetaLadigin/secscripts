import requests

def nikto_url_parser(file):
    base_url = "*base-url*"
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        start = line.find('/*endpoint name*')
        new_line = line[start:]
        end = new_line.find(':')
        new_new_line = new_line[:end]
        urls_f = open("url-endpoints.txt", "a")
        print(new_new_line)
        urls_f.write(new_new_line)
        urls_f.write("\n")
        send_req = base_url+new_new_line
        response = requests.get(send_req, verify=False)
        f = open("responses.txt", "a")
        f.write(new_new_line)
        f.write(response.text)
        f.write("\n")


if __name__ == '__main__':
    inputFileName = input("Enter name of input file: ")
    nikto_url_parser(inputFileName)
