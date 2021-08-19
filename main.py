# block sites
from datetime import datetime
end_time = datetime(2021, 1, 1, 20)
sites_to_block = ["www.facebook.com", "facebook.com"]
host_path = '/etc/hosts'

redirect = "127.0.0.1"
def block_website():
    if datetime.nov() < end_time:
        print("Block Sites")
        with open(host_path, 'r+') as hostfile:
            hosts_contect = hostfile.read()
            for site in sites_to_block:
                if site not in hosts_contect:
                    hostfile.write(redirect + ' ' + site + '\n')
    else:
        print("Unblock Sites")
        with open(host_path, 'r+') as hostfile:
            lines = hostfile.redlines()
            hostfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostfile.write(line)
                hostfile.truncate()
                
if __name__ == '__main__':
    block_website()
