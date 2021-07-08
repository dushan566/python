from datetime import datetime
from datetime import timedelta

def main():
    ## Get now time in Year-Month-Date-Hour-Minute
    now_time = datetime.now() 
    print(now_time.strftime("%Y-%m-%d-%H-%M")) 

    ## Get today in YYYY-MM-DD
    today = datetime.now() 
    print(today.strftime("%Y-%m-%d")) 
    
    ## Get yesterday in YYYY-MM-DD
    yesterday = datetime.now() - timedelta(days=1)
    print(yesterday.strftime("%Y-%m-%d")) 

    ## Get tomorrow in Year-Month-Date
    tomorrow = datetime.now() + timedelta(days=1)
    print(tomorrow.strftime("%Y-%m-%d"))
    
    ## Get last month MM
    lastmonth = datetime.today().replace(day=1) - timedelta(days=1)
    print(lastmonth.strftime("%m")) 

    ## Get last year in YYYY
    today = datetime.now()
    lastyear = today.year -1 
    print(lastyear)

if __name__  == "__main__":
    main()