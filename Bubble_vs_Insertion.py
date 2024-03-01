"""
    Scott Quashen
    
    Created on Tuesday Feb 27 20:00 2024  
    
    Description: 
       Testing bubble sort verse insertion sort

    Dependencies: random, time, mathhplotlib.pyplot

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.3.1
"""




#----project imports section




import time, random
import matplotlib.pyplot as plt




#----function definitions section




#------------------------------------bubble sorting

#bubble sorting
def findAndSwapByOnePosition( someList ):
    """
    
    Description
    ----------
    findAndSwapByOnePosition() checks each item in list and swaps it with the next if the next is smaller.
    
    Parameters
    ----------
    someList : 
        List
        We keep passing in the same list that keeps updating each iteration
   
    Returns
    -------
    None.
    

    """
    for i in range( 0, len( someList ) - 1 ):
         if someList[ i + 1 ] <= someList[ i ]:        
             # then we found an item that needs to be swapped
             # swap items, holding one value in a new var
             c = someList [ i ]
             # swap right
             someList [ i ] = someList [ i + 1 ]
             # swap left
             someList [ i + 1 ] = c

# end of findAndSwapByOnePosition() function            


# bubble sorting
def callSwapAsManyTimesAsNeededUntilFinished( someList ):
    """
    
    Description
    ----------
    callSwapAsManyTimesAsNeededUntilFinished() does not stop calling our swap func until 
    all items in our list is 100% completely in ascending order, 
    at which point finished = true and the loop bails.
   
    Parameters
    ----------
    someList : 
        List  
        The List of random numbers we will be sorting
    
    Returns
    -------
    None.
   

    """
    finished = False
    while not finished:
        for i in range( len( someList ) ):
            # run through list one time, swapping values if needed
            if someList[ i - 1 ] > someList[ i ]:
                findAndSwapByOnePosition( someList )                
            else:
                # above, items were only swapped one time each, may need to move further left or right
                for i in range(len( someList )):
                    if i > 0:
                        if someList[ i - 1 ] > someList[ i ]:
                            # then we found an item out of order, sort again
                            findAndSwapByOnePosition( someList )
                        if i == len( someList ) - 1:
                            # we've reached the end of the list and all previous numberss in order
                            finished = True 
                                
# end of callSwapAsManyTimesAsNeededUntilFinished() function     

def getTimesBubble( someProblemSizes ) :
    
    """
    
    Description
    ----------    
    getTimesBubble() tracks how much time it takes to sort various amounts of random numbers using bubble sorting
    
    Parameters
    ----------
        someProblemSizes : 
            List of integers
            A value for each of problem sizes.
        
    Returns
    -------
        timeList : 
            List of floats
            The times that we will be plotting on the y-axis

    """
    
    timeListBubble = [ ]
    
    for i in range( len( someProblemSizes ) ):
        
        # define initial seed value
        random.seed( 22, int )
        
        # create list of random numbers
        L = [ random.randint(0, 999) for t in range( someProblemSizes[ i ]) ]
        
        # start timer
        startTimer = time.time()
        # sort
        callSwapAsManyTimesAsNeededUntilFinished( L )
        # end timer when sorting is complete
        endTimer = time.time()
        # measure & store time
        elapsedTime = endTimer - startTimer
        # y value of plot
        timeListBubble.append( elapsedTime )
        
        print( elapsedTime )
        print( checkSort( L ) )
        
 
        
        
    # return the list to plot
    print( "done timing" )
    return timeListBubble

# end getTimes() func


#------------------------------------insertion sorting

def insertionSort( someList ):
    
    """
    
    Description
    ----------
    The insertionSort() function inserts candidate to the left
    in ascending order. By the time we are at the last index, 
    all previous items are in order, and the final index can be
    placed anywhere that it belongs in the list, starting at the end,
    and walking down, we find where it belongs and insert it.
    
    Parameters
    ----------
        someList : 
            List of integers
            This is a list of random numbers for any problem size.

    Returns
    -------
    None.

    """
    
    for i in range( 1, len( someList ) ):
        
        # candidate will be the item we will be inserting where it belongs to its left
        candidate = someList[ i ]
        
        # the final j is where candidate will be inserted
        j = i - 1
        
        while ( j >= 0 and someList[ j ] > candidate ):
            
            # we have double values until we insert, at which point we replace the first of the two
            someList[ j + 1 ] = someList[ j ]
            
            j = j - 1
            
        someList[ j + 1 ] = candidate
        
        # do this for each index 

# end insertion sort func

def getTimesInsertion( someProblemSizes ) :
    
    """
    
    Description
    ----------    
    getTimesInsertion() tracks how long it takes to sort various counts of random numbers using insertion sorting
    
    Parameters
    ----------
        someProblemSizes : 
            List of integers
            A value for each of problem sizes.
        
    Returns
    -------
        timeList : 
            List of floats
            The times that we will be plotting on the y-axis

    """
    
    timeListInsertion = [ ]
    
    for i in range( len( someProblemSizes ) ):
        
        # define initial seed value
        random.seed( 22, int )
        
        # create list of random numbers
        L = [ random.randint(0, 999) for t in range( someProblemSizes[ i ]) ]
        
        # start timer
        startTimer = time.time()
        # sort
        insertionSort( L )
        # end timer when sorting is complete
        endTimer = time.time()
        # measure & store time
        elapsedTime = endTimer - startTimer
        # y value of plot
        timeListInsertion.append( elapsedTime )
        
        print( elapsedTime )
        print( checkSort( L ) )
        
 
        
        
    # return the list to plot
    print( "done timing" )
    return timeListInsertion

# end getTimes() func


#------- shared definitions


def checkSort( someList ):
    
    """
    
    Description
    ----------
    checkSort() loop can ends by returning true or false, depending on item order of the passed-in list
   
    Parameters
    ----------
        someList : 
            List of random integers
            The List of random numbers we will be sorting
    
    Returns
    -------
        bool
            True if the list is in ascending order, False if not.

    """
    
    print( "Is the List sorted?" )
    
    for i in range( 1, len( someList ) ): 
            
        if someList[ i - 1 ] > someList[ i ]:
        # search for values that are out of order, if found, list not in order
            return False
        
        if i == len( someList ) - 1:
        # We've reached the end of list, all previous numbers in order 
            return True
            
# end of checkSort() function


def createPlot( xData, yDataBubble, yDataInsertion ):
    
    """
    
    Description
    ----------  
    createPloat() uses mathPlot to create a chart representing the time taken to sort our given problem sizes.

    Parameters
    ----------
        
        xData : 
            List of integers
            Our problem sizes
            
        yData : 
            List of floats
            Our y-axis values for plotting

    Returns
    -------
    None.

    """
    
    width = 100
    # string values for x ticks
    Ns = [ str( t ) for t in xData ]
    plt.title( "Bubble Sorting vs. Insertion Sorting" )
    plt.xlabel( 'Random Numbers in List' )
    plt.ylabel( 'Seconds to Sort' )
    plt.xscale( "log" )
    plt.xticks( xData, Ns )
    plt.scatter( xData, yDataBubble, width, label='Bubble' )
    plt.scatter( xData, yDataInsertion, width, label='Insertion' )
    plt.plot( xData, yDataBubble, xData, yDataInsertion )
    plt.legend( ["Bubble", "Insertion"], loc=2 )
    #plt.plot( xData, yDataInsertion )
    plt.savefig( "Scott Quashen_Project_4.png", dpi=600 )
    plt.show()

# end createPlot() func




#--------------------------main code section

# dev name
print( "Scott Quashen..." + time.asctime() )

# define the problem sizes
problemSizes = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]

# 8192, 16384

# create lists, sort them, measure elapsed time, and return our lists of data for use in plotting
InsertionTimes = getTimesInsertion( problemSizes )

BubbleTimes = getTimesBubble( problemSizes )

# handle the plotting of previously gathered data
createPlot( problemSizes, BubbleTimes, InsertionTimes )




#------end 
















