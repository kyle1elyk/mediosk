# Kyle Stead kstead2016@my.fit.edu
from sys import stdin, stdout

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

class Drivers_License:
    def __init__(self, data_in):
        self.first_name = None
        self.last_name = None
        self.middle_name = None
        
        self.state_abbrv = None
        self.city = None
        
        self.address = None
        
        self.license_number = None
        self.expiration_year = None
        
        self.birth_month = None
        self.birth_year = None
        self.birth_day = None
        
        self.version = None
        
        split_index = data_in.index("?")
        first_part = data_in[1:split_index]
        
        first_part = [" ".join(segment.split("$")) for segment in first_part.split("^")]
        
        self.state_abbrv = first_part[0][:2]
        self.city = first_part[0][2:].title()
        
        self.last_name = first_part[1].split(" ")[0].title()
        self.first_name = first_part[1].split(" ")[1].title()
        if (len(first_part[1].split(" ")) >= 3):
            self.middle_name = first_part[1].split(" ")[2].title()
        
        self.address = first_part[2].title()
        
        split_index_2 = data_in.index("=") + 1
        
        second_part = data_in[split_index_2:split_index_2 + 12]
        
        self.expiration_year = 2000 + int(second_part[0:2])
        self.birth_month = int(second_part[2:4]) - 1
        self.birth_year = int(second_part[4:8])
        self.birth_day = int(second_part[10:])
        
        self.version = int(second_part[8:10])
        
    
    def display_nice(self):
        month = months[self.birth_month]
        ret = "Hello {} {} {}\r\n".format(self.first_name, self.middle_name, self.last_name)
        ret += "from {}, {}, {}\r\n".format(self.address, self.city, self.state_abbrv)
        ret += "Your birthday is {} {}, {}".format(month, self.birth_day, self.birth_year)
        stdout.write(ret + "\r\n")
        return True
if __name__ == "__main__":
    for line in stdin:
        lic = Drivers_License(line)
        print("Hey there " + lic.first_name + ", your birthday is in " + months[lic.birth_month])