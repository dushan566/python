"""
# Method 1 - (Assign global variable and call in oher functions)
#-------------------------------------------------------------------------------
def get_status():
    global status
    status = 'running'

def main():
    get_status()
    print(status)

if __name__ == "__main__":
    main()
"""

"""
# Method 2 - (Assign variable inside function and call them in oher functions)
#-------------------------------------------------------------------------------
def get_status():
    get_status.x = 'stopped'

def main():
    get_status()
    print(get_status.x)

if __name__ == "__main__":
    main()
"""

# Method 3 - (Call variables withing the class)
# This is an example schenario if the ec2 trsffic is stopped, then RDS maintenance will be performed
#---------------------------------------------------------------------------------------------------
class myclass:
    def traffic(self):
        self.traffic_status = "stopped"
        return self.traffic_status

    def rds(self):
        self.rds_status = "running"
        return self.rds_status

    def maintenance(self,mode):
        # Randomly get function 1 value
        print("this is traffic status variable from function 1 , traffic is " + self.traffic_status)
        # Randomly get function 2 value
        print("This is another variable form funcion 2 used in function 3, RDS is " + self.rds_status)        
        if mode == "godtogo":
            print("RDS maintenance will be performed")
        else:
            print("RDS maintenance will be skipped, because traffic is not stopped") 
               
def main():
    c = myclass()
    traffic = c.traffic()
    rds = c.rds()
    # Example call where you can use a variable defined in a function inside a class
    print("This is traffic status of myclass you can call from main function, it's " + traffic)
    print("This is rds status of myclass you can call from main function, it's " + rds)

    # Do some random stuff with function in a class
    if traffic == "stopped":
        c.maintenance("godtogo")
    else:
        c.maintenance("skipping")

if __name__ == "__main__":
    main()
   
