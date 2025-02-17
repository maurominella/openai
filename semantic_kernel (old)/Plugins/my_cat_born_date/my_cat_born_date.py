def my_cat_born_date():
    """ Returns my cat's born date """
    import datetime, random
    from dateutil.relativedelta import relativedelta
    
    if (random.uniform(0, 1)<failure_rate):
        raise Exception("Simulated error in my_cat_born_date for testing purpose")
        
    # Calculate the date as ten years ago  
    ten_years_ago = datetime.date.today() - relativedelta(years=10) 
    
    cat_born_date = {
        "cat_born_date": ten_years_ago.strftime("%Y-%m-%d")
    }
    return json.dumps(cat_born_date)