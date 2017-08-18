from datetime import datetime, timedelta

def add_gigasecond(date):

    gig = date + timedelta(seconds=10**9)
    
    return gig
