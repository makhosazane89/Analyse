### START FUNCTION
def five_num_summary(items):
    """
    Calculates the five number summary 
    
    Args:
        list (containing non-string items)
    
    Returns:
        dict: {max, median, min, q1, q3} all rounded to 2 decimal places
    
    Example:
        >>> five_num_summ([1, 2, 3, 4, 5])
        {'max': 5.0, 'median': 3.0, 'min': 1.0, 'q1': 2.0, 'q3': 4.0}   
    """
    try:
        items_length, sum_of_items = 0, 0
        for item in items:
            sum_of_items += item   # Calculating the sum of the items in a list 
            items_length += 1  # Calculating the length of a list  

        # Sorting out the list
        for i in range(items_length):
            for j in range(1,items_length):
                if items[j-1] > items[j]:
                    (items[j-1], items[j]) = (items[j], items[j-1]) 
                    
        max_num = items[-1] 
        min_num = items[0] 
        
        def median(items):
            items_length, sum_of_items = 0, 0 # initialising length and sum of items
            for item in items:
                sum_of_items += item   # Calculating the sum of the items in a list 
                items_length += 1  # Calculating the length of a list  

            mid = items_length // 2  # uses the floor division to have integer returned
            if (items_length % 2 == 0):
                # even
                return (items[mid-1] + items[mid]) / 2.0
            else:
                # odd
                return int(items[mid] * 100) / 100
      
        mid = items_length // 2 # uses the floor division to have integer returned
        
        # Calculating the lower and upper quartiles
        if (items_length % 2 == 0):
            # even
            q1 = median(items[:mid])
            q3 = median(items[mid:])
        else:
            # odd
            q1 = median(items[:mid])
            q3 = median(items[mid+1:])

        return {'max':float('%.2f' % max_num), 'median':float('%.2f' % median(items)), 'min':float('%.2f' % min_num), 'q1':float('%.2f' % q1),'q3':float('%.2f' % q3)}
    
    except TypeError:
        return 'Enter a valid argument: argument must be a list of --> int or floats'
        
### END FUNCTION