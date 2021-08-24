#بسمك ربي عبدناك و لم نحسن عبادتك فإغفر لنا و ثبتنا على الإيمان و العلم و الحكمة يارب العالمين

#------------------------ المرجع الشامل لمبادئ تحليل البيانات ---------------------------------
from numpy.core.fromnumeric import mean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''data = {"Microsoft Xbox 360":4200,"Microsoft Xbox One":5900,
            "Nvidia GTX 1050":2400,"Nvidia GTX 1060":2900,"Nvidia GTX 1070":3200,"Nvidia GTX 1080":3600}
'''
# @This_Method is used to get the key while the value is specified.
'''def getKey(valu):
    for key, value in data.items():
        if valu == value:
            return key
'''
#print("Price of {} is {}£.".format(getKey(4200),data["Nvidia GTX 1060"]))
'''file = pd.ExcelWriter("C:\\Users\\musta\\Documents\\Python Scripts\\Udacity_Data_Analysis\\PandasDataset__Test.xlsx",engine="xlsxwriter")
'''
# @Rename: columns we use a dictionary of each row {name} for the header & row {values} for each item.
            # We do the following....
'''dataFrame = pd.DataFrame({"Items":data.keys(),"Prices":data.values()})
'''
# @Convert the dataFrame from the form of dictionary using mapping into the form of compact data.
'''convertedFile = dataFrame.to_excel(file,sheet_name='Sheet1')
'''
# @Finally Saving the file...
'''file.save()
'''

# @NumPy_Array this case is used mainly to determine specific data required from 
#              the <array1> according to the data in the <array2>; while the determination 
#              is according to each index in the first array that matches the boolean value in
#              in the array2.
#arr1 = np.array([1,2,3,4,5,6])
#arr2 = np.array([True,True,False,True,True,False])
#print(arr1[arr2])


# @Imp_Note: mean() value calculated by {adding values together - then dividing by its count.} >> 
        # for instance [[10,11,12]] > 10 + 11 + 12 = 33 / 3<*COUNT OF NUMBERS> = 11. 


#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

# ------------------------------ @Explanation ---------------------------
# ----------------# Section A
# Change False to True for each block of code to see what it does
'''
# Using index arrays
if False:
    a = np.array([1, 2, 3, 4])
    b = np.array([True, True, False, False])
    
    print a[b]
    print a[np.array([True, False, True, False])]
    
# Creating the index array using vectorized operations
if False:
    a = np.array([1, 2, 3, 2, 1])
    b = (a >= 2)
    
    print a[b]
    print a[a >= 2]
    
# Creating the index array using vectorized operations on another array
if False:
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 2, 3, 2, 1])
    
    print b == 2
    print a[b == 2]
'''
'''
k = 0
for i in life_expectancy_values:
    k += i
print(k/20)
'''
'''
count = 0
for i in life_expectancy:
    if i >= life_expectancy.mean():
        count += 1
        print(i)
print("Count = {}".format(count))
count = 0
for n in gdp_values:
    if n >= gdp.mean():
        print(n)
        count += 1
print("Count = {}".format(count))
'''
'''
count = 0
for i in life_expectancy:
    if i > life_expectancy.mean():
        count += 1
print(count)
'''

# ----------------# Section B
# Accessing elements and slicing
'''
#if False:
#    print life_expectancy[0]
#    print gdp[3:6]

# Looping

#if False:
#    for country_life_expectancy in life_expectancy:
#        print 'Examining life expectancy {}'.format(country_life_expectancy)
    
# Pandas functions

##if False:
 #   print life_expectancy.mean()
#    print life_expectancy.std()
 #   print gdp.max()
 #   print gdp.sum()

# Vectorized operations and index arrays
#if False:
#    a = pd.Series([1, 2, 3, 4])
#    b = pd.Series([1, 2, 1, 2])
#  
#    print a + b
#    print a * 2
#    print a >= 3
#    print a[a >= 3]

'''
# ◘◘----------------# Section C <loc / iloc> Functions
#lst_countries = pd.Series(life_expectancy_values,index=countries)
#print(lst_countries)
#       @return an array like the following:
'''Andorra                83.4
Angola                 57.6
Antigua and Barbuda    74.6
Argentina              75.4
'''
# *@Note using <loc> method  {.loc() method} is used to return the value to the associated specified key.
'''print(lst_countries["Azerbaijan"]) # equals to
print(lst_countries.loc["Azerbaijan"])'''
# *@note using <iloc> method {.iloc() method} is used to return the value associated with the specified index.
'''print(lst_countries.iloc[0])'''
#------------------------------    @Reference     -------------------------
# Change False to True for each block of code to see what it does
'''valuePositive = (life_expectancy > life_expectancy.mean()) & (gdp > gdp.mean())
valueNegative = (life_expectancy < life_expectancy.mean()) & (gdp < gdp.mean())
count = 0'''


'''for i in range(len(life_expectancy)):
    if (life_expectancy[i] > life_expectancy.mean()) & \
            (gdp[i] > gdp.mean()) | (life_expectancy[i] < life_expectancy.mean()) & (gdp[i] < gdp.mean()) :
        count += 1
print(count)
differentNumbers = len(life_expectancy) - count
print("The total of different points count = {}".format(differentNumbers))
'''
#sameDirect = valuePositive | valueNegative
#print(sameDirect.sum())


# ••@Quiz         <Accomplished.>    {Using Vectorised Operations}
#       @Note While any operation occured on the entire array that will be reflected directly to each element.
'''
import numpy as np

# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

# Change this country name to change what country will be printed when you
# click "Test Run". Your function will be called to determine the standardized
# score for this country for each of the given 5 Gapminder variables in 2007.
# The possible country names are available in the Downloadables section.

country_name = 'United States'

def standardize_data(values):
    # ----------------------------Comment---------------------------------
    Fill in this function to return a standardized version of the given values,
    which will be in a NumPy array. Each value should be translated into the
    number of standard deviations that value is away from the mean of the data.
    (A positive number indicates a value higher than the mean, and a negative
    number indicates a value lower than the mean.)
    # ----------------------------*End*------------------------------------
    requiredData = (values - values.mean()) / values.std()
    return requiredData
print(standardize_data(employment))
'''


# ••Quiz  <mean() method> using (NumPy).
'''
import numpy as np
def mean_time_for_paid_students(time_spent, days_to_cancel):
    # ----------------------------Comment---------------------------------
    Fill in this function to calculate the mean time spent in the classroom
    for students who stayed enrolled at least (greater than or equal to) 7 days.
    Unlike in Lesson 1, you can assume that days_to_cancel will contain only
    integers (there are no students who have not canceled yet).
    
    The arguments are NumPy arrays. time_spent contains the amount of time spent
    in the classroom for each student, and days_to_cancel contains the number
    of days until each student cancel. The data is given in the same order
    in both arrays.
    # ----------------------------*End*-------------------------------------
    mean_time = (time_spent[days_to_cancel >= 7]).mean()
    return mean_time
     

# Time spent in the classroom in the first week for 20 students
time_spent = np.array([
       12.89697233,    0.        ,   64.55043217,    0.        ,
       24.2315615 ,   39.991625  ,    0.        ,    0.        ,
      147.20683783,    0.        ,    0.        ,    0.        ,
       45.18261617,  157.60454283,  133.2434615 ,   52.85000767,
        0.        ,   54.9204785 ,   26.78142417,    0.
])

# Days to cancel for 20 students
days_to_cancel = np.array([
      4,   5,  37,   3,  12,   4,  35,  38,   5,  37,   3,   3,  68,
     38,  98,   2, 249,   2, 127,  35
])
print(mean_time_for_paid_students(time_spent, days_to_cancel))
'''



#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# ••@Quiz <Using .Series() && .mean() methods> in Pandas.
'''
import pandas as pd

countries = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

life_expectancy_values = [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                          70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                          67.3,  70.6]

gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
              13495.1274663 ,   9388.68852258,   1424.19056199,  24765.54890176,
              27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
               3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]

# Life expectancy and gdp data in 2007 for 20 countries
life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)
#print(life_expectancy.mean())
'''


# ••@Quiz
'''
def variable_correlation(variable1, variable2):
    #------------------------------@Comment-------------------------------
    Fill in this function to calculate the number of data points for which
    the directions of variable1 and variable2 relative to the mean are the
    same, and the number of data points for which they are different.
    Direction here means whether each value is above or below its mean.
    
    You can classify cases where the value is equal to the mean for one or
    both variables however you like.
    
    Each argument will be a Pandas series.
    
    For example, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([4, 5, 6, 7]), then the output would be (4, 0).
    This is because 1 and 4 are both below their means, 2 and 5 are both
    below, 3 and 6 are both above, and 4 and 7 are both above.
    
    On the other hand, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([7, 6, 5, 4]), then the output would be (0, 4).
    This is because 1 is below its mean but 7 is above its mean, and
    so on.
    #------------------------------*End*-------------------------------

    
    num_same_direction = None        # Replace this with your code
    num_different_direction = None   # Replace this with your code
    count  = 0
    for i in range(len(variable1)):
        if (variable1[i] > variable1.mean()) & \
            (variable2[i] > variable2.mean()) | (variable1[i] < variable1.mean()) & (variable2[i] < variable2.mean()) :
                        count += 1
    num_same_direction = count 

    # @get the length of any specified arrays as both are to have the same length.
    num_different_direction = len(variable1) - count

    #                   ------------ @Reference_Solution -------------
    valuePositive = (life_expectancy > life_expectancy.mean()) & (gdp > gdp.mean())
    valueNegative = (life_expectancy < life_expectancy.mean()) & (gdp < gdp.mean())
    # @Note: {|} is considered as --OR-- in logical means but in pandas series it's typically manipulated like {+}.
    #num_same_direction = valuePositive | valueNegative
    #num_different_direction = len(variable1) - num_same_direction

    return (num_same_direction, num_different_direction)
'''
#print(variable_correlation(life_expectancy,gdp))


#   ••@Quiz  <Using .loc() && /.argmax()> in pandas.

#employment = pd.Series(employment_values, index=countries)
'''
def max_employment(employment):
    #-----------------------@Comment----------------------
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    
    The input will be a Pandas series where the values
    are employment and the index is country names.
    
    Try using the Pandas idxmax() function. Documention can
    be found here:
    http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.idxmax.html  
    #---------------------- @End---------------------------
    max_country = employment.argmax()      # Replace this with your code
    max_value = employment.loc[max_country]   # Replace this with your code

    return (max_country, max_value)
'''
#print(max_employment(employment))
#           ------------- @Test -------------
#array = pd.Series([1,2,3,4,5,6],["A","B","C","D","E","F"])
# @return that will return the specified array with matching indecies.
 # @Note we can access array elements by normal loop.

#count = 0
#print(array)

#while count < array[len(array)-1]:
#    print(array[count])
#    count += 1
#lst = [1,2,3,4,5,6]

'''
                                                  ◘◘@Writing data on excel sheet.
'''
'''
# ◙ TODO > import pandas series into a new xlsx file.
items = {"GTX 1650": 2900,"GTX 1660": 3500, "GTX 2060":5600,"GTX 2060 TI":6200,"GTX 2070":6600,"GTX 2080": 7400}
itemsDict = pd.Series(items.values(),index = items.keys())
#print(itemsDict)
excelFile = pd.ExcelWriter("C:\\Users\\musta\\Documents\\Python Scripts\\Udacity_Data_Analysis\\Test.xlsx",engine="xlsxwriter")
itemsFrame = pd.DataFrame({"Items":itemsDict.keys(),"Prices":itemsDict.values})
itm = itemsDict.iloc[itemsDict.argmax()]
writtenFile = itemsFrame.to_excel(excelFile,sheet_name="Sheet1")
excelFile.save()'''
#print(itemsDict < 5000)

#print("{} Price is: {}.".format(returnKey(itm),itm))
'''def returnKey (price,dictItems):
    count = 0
    for key , value in dictItems.items:
        for i in dictItems < price:
            if i == True:
        #if value == iteratable:
                count += 1
            return key
'''

#count = 0
#count = 0

# ◙ r = itemsDict < 5000
#print(r.items)
#print(itemsDict < 5000)
#for i in itemsDict < 5000:
    #returnKey(count,5000,i)
#    print(i)
    #print()
    #if i == True:
    #    count+=1
        
        #print(returnKey(itemsDict.iloc[count]))
    #print()
#print(returnItems(itemsDict))

#print(itemsFrame)



#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬


#            ◘◘--------------- Sector Pandas main contents --------------------
# Calculating Correlation coeffecient (Pearson's R)....
'''
Correlation Coeffecient is meant to get the convariance between the variable (x or y) and its mean value.

    in the lesson example > it considered both value of (x and y) are >> Above the mean.
                                                        (x and y) are >> Below the mean.
                                                        (x and y) one below and the other above the mean value.

    # ↔ ↔ @Note: ▬ Note that for each covariance occured in (considering {x-value}) and follwed by a positively proportional covariance in {y} That's
                 called {Positive Correlation} and different conditions applied to ({x} and {y}).
                    ◙ for example > for increasing of Piety <التقوى> the person becomes more wiser. <increase and increase>


                 ▬ For Negative Correlation > means that for each increase in one variable [x or y] There is a negative decrease in the other variable.
                    ◙ for example > for increasing of speed the time to reach the destination decreases. <increase and decrease>


                 ▬ for zero correlation > means that for each increase in any variable; there is no increasing or decreasing on the other.
                    ◙ for example > for the current that first passes through the conductor it begun with variable rate; then , it becomes constant or semi-constant..

                          σXY
                 •ρX,Y= ▬▬▬▬▬▬▬▬    > as {ρX,Y} is the pearson correlation coeffecient value for [x and y]; 
                          σXσY        <Correlation Coefficient> {معامل الإرتباط أي نسبة الإرتباط و التغير  ما بين قيمة س وقيمة ص} 
                                      also {σXσY} is standard deviations between both {x and y} values... 

    # ↔ ↔ @Note: ▬ To calculate the <Standard Deviation> of any pandas [Series]
              • ▬ Calculate the mean value of the entire list {Represented by μ}...
              • ▬ Calculate (xi - μ)  and Square the result. where {xi is each number in the list; x1,x2,x3,..}.
              • ▬ Sum each result to others means getting (Σ] of the numbers and multiplying them to the [1/N]. 
                  where {N} is the count of numbers on the list.     
              • ▬ Finally get the root value of the result...                       

    @def ▬▬ of {Standard Deviation} >>  Standard deviation is considered to be the despersion<التباين> between a variable and its mean value.
      Then get the pearson's r variable...



    # •• @imp__Note: While ¶[.std()] function is used with Pandas Series. 
                           ¶[.corroef()] function is used to get the the same Correlation Coeffecient in Numpy Arrays...



    > ◙ Example to calculate the standard deviation and get Pearson R value:
            def correlation(x,y):
                std_x = (x - x.mean()) / x.std(ddof = 0)
                std_y = (y - y.mean()) / y.std(ddof = 0)
                return (std_x * std_y) .mean()
'''
'''
items = ["GTX 1650", "Ryzen 5 3500X" ,"AMD R9 280X","AMD R9 270X"]
prices = [2900, 2900, 1900, 1450]
lst = pd.Series(prices, index= items)
print(lst.std(ddof=0)) #getting the standard deviation value. <Rememberance: standard deviation means to get the value of difference between any point {x or y} and the mean value.>
'''
#%%
#                                                             ~~<Sector DataFrame and vectorised operations...>~~
# Adding DataFrames with the column names
'''if False:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]})
    print df1 + df2
    '''
# ◘@Note Properly that will return a new dataFrame with each element accumulated to the other...
'''df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]})
print(df1 + df2)'''



# Adding DataFrames with overlapping column names 
'''if False:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'d': [10, 20, 30], 'c': [40, 50, 60], 'b': [70, 80, 90]})
    print df1 + df2
'''
# ◘@Note Also that will return new dataFrame with each column name <indicated with "a", "b", "c", "d"> accumulated with the same name in the second provided array 
#           {df2} while individual provided array such as {a , d} will return null or NaN in the result array. 
'''df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
df2 = pd.DataFrame({'d': [10, 20, 30], 'c': [40, 50, 60], 'b': [70, 80, 90]})
print(df1 + df2)
'''


# Adding DataFrames with overlapping row indexes
'''if False:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]},
                       index=['row1', 'row2', 'row3'])
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]},
                       index=['row4', 'row3', 'row2'])
    print df1 + df2
'''
# ◘@Note that "a", "b", ..... considered as Columns titles; while index listed elements considered as row names.
# as {row1 , row4} are not existed in both arrays; it will return NaN in the resulted array. 
'''df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]},
                       index=['row1', 'row2', 'row3'])
df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]},
                       index=['row4', 'row3', 'row2'])
print(df1 + df2)
'''


# ••--- Quiz ---
# Cumulative entries and exits for one station for a few hours.
'''entries_and_exits = pd.DataFrame({
    'ENTRIESn': [3144312, 3144335, 3144353, 3144424, 3144594,
                 3144808, 3144895, 3144905, 3144941, 3145094],
    'EXITSn': [1088151, 1088159, 1088177, 1088231, 1088275,
               1088317, 1088328, 1088331, 1088420, 1088753]
})
print(entries_and_exits - entries_and_exits.shift(1))
'''

# ◘@Note: that periods <that passed as a parameter> in the {.shift} method; indicates how much indices will be dislodged from the array;
#  ▬ While passing (8) it dislodged the array for (8) indices. first element becomes the 9th. 





# •• @Quiz  <mean() method> using (NumPy).
'''
entries_and_exits = pd.DataFrame({
    'ENTRIESn': [3144312, 3144335, 3144353, 3144424, 3144594,
                 3144808, 3144895, 3144905, 3144941, 3145094],
    'EXITSn': [1088151, 1088159, 1088177, 1088231, 1088275,
               1088317, 1088328, 1088331, 1088420, 1088753]
})

def get_hourly_entries_and_exits(entries_and_exits):
    # ◘◘ in this example it desired to get the difference and compare each row with the previous one; •• while that will result new dataFrame with data differences between 
    # -------------------------Comment------------------------------
    Fill in this function to take a DataFrame with cumulative entries

    and exits (entries in the first column, exits in the second) and
    return a DataFrame with hourly entries and exits (entries in the
    first column, exits in the second).
    # --------------------------------------------------------------
    result = entries_and_exits - entries_and_exits.shift(1)
    return result

print(get_hourly_entries_and_exits(entries_and_exits))
'''

# DataFrame applymap()
# ◘◘@Note : <.applymap()> is used to apply specific method into the dataFrame...
'''
if False:
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [10, 20, 30],
        'c': [5, 10, 15]
    })
  
    def add_one(x):
        return x + 1
        
    print df.applymap(add_one)
'''
'''df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [10, 20, 30],
        'c': [5, 10, 15]
    })
#print(df)
def add(x):
    return x + 1
print(df.applymap(add))
'''
'''
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)
'''
# ◘◘@Note that while the method is manipulating with numbers; then it will be used with numrical values through the dateFrame.
# --------------------------------------- @Solution........
'''
def returnLetterForGrade(degree):
    if degree>= 90:
        return("A")
    elif degree>= 80:
        return("B")
    elif degree>= 70:
        return("C")
    elif degree>= 60:
        return ("D")
    else:
        return ("F")
#print(grades_df.iloc[0].apply(returnLetterForGrade))
#print(grades_df.applymap(returnLetterForGrade))

    
def convert_grades(grades):
   
    Fill in this function to convert the given DataFrame of numerical
    grades to letter grades. Return a new DataFrame with the converted
    grade.
    
    The conversion rule is:
        90-100 -> A
        80-89  -> B
        70-79  -> C
        60-69  -> D
        0-59   -> F
    
    return None
'''
#  •→ @Test <DataFrame {.applymap()} method>.
'''
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)
def addValue(x):
    return x + 5
'''


# •• @Quiz  <using .apply() method> through the NumPy array...
'''grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)
'''

#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

# Change False to True for this block of code to see what it does

# DataFrame apply()
#if False:
'''def convert_grades_curve(exam_grades):
        # Pandas has a built-in function that will perform this calculation
        # This will give the bottom 0% to 10% of students the grade 'F',
        # 10% to 20% the grade 'D', and so on. You can read more about
        # the qcut() function here:
        # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html
    return pd.qcut(exam_grades,
                    [0, 0.1, 0.2, 0.5, 0.8, 1],
                    labels=['F', 'D', 'C', 'B', 'A'])
        
    # qcut() operates on a list, array, or Series. This is the
    # result of running the function on a single column of the
    # DataFrame.
    '''
#print (convert_grades_curve(grades_df['exam1']))
#print(pd.qcut(range(5),3,labels=["bad","Medium","good"]))
    
    # qcut() does not work on DataFrames, but we can use apply()
    # to call the function on each column separately
#print (grades_df.apply(convert_grades_curve))
# ◘◘@Note: to directly convert single array numircal values into alphabetical array...
'''print(convert_grades_curve(grades_df['exam1']))'''
'''convert_grades_curve(grades_df['exam2'])'''
#print(grades_df.apply(convert_grades_curve))
#print(convert_grades_curve(grades_df['exam1']))



# ◘ ◙ @Methods to get the the standard deviation firstly then to apply this method into the entire arrays by the second method...
# ◘◘@Note: Rememberance >> Standard Deviation is defined to be the difference between the variable and its {mean value}. 
# ◘◘@Note: that <.apply() method> is used mainly to be applied through a 1D Array on the dataFrame, while <.applymap()> is used to be applied into the entire dataFrame.
'''
def stdDeviation(x):
    return (x - x.mean()) / x.std()
def standardize(df):
    
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    

    return df.apply(stdDeviation)
print(standardize(grades_df))
'''


#--------------Test--------------------
#print(grades_df.apply(addValue,axis=0))
#print(grades_df.index)
#print(grades_df.values[0,1])
x = 0
y = 0
#print(grades_df.values[0,1] == 24)
#print(grades_df['exam2'].argmax())
#print(grades_df.index[grades_df['exam2'].argmax()])
#print(grades_df.index[grades_df['exam1'].argmax()],grades_df['exam1'].max())
#print(grades_df.index[grades_df['exam2'].argmax()],grades_df['exam2'].max())

'''if grades_df.values[0,0] == 43 and grades_df.values[0,1] == 24:
    print("True")
'''
#--------------End--------------------

df = pd.DataFrame({
    'a': [4, 5, 3, 1, 2],
    'b': [20, 10, 40, 50, 30],
    'c': [25, 20, 5, 15, 10]
})

# Change False to True for this block of code to see what it does

# DataFrame apply() - use case 2
#if False:   
#print (df.apply(np.mean))
#print (df.apply(np.max))

lst = [7,5,2,6,47,5,9,4,2,0,22,26,27,89]

'''
══Solution 1══
count = 0
for i in lst:
    
    if (lst[count]<max(lst)):
        count = i
    if count == len(lst) -1:
        break
    count += 1
print(count)
'''
'''
══Solution 2══
count = 0
for i in lst:
    if i < max(lst):
        count = i
print(count)
'''
'''def getSecond(number):
    count = 0
    if number < max(df['a']):
        count = number
    return count
'''

'''def secondLargestColumnNumber(column):
    sortedData = column.sort_values(ascending = False)
    return sortedData.iloc[1]
'''


#══Quiz Solution══
'''
def second_largest(df):
    
    Fill in this function to return the second-largest value of each 
    column of the input DataFrame.
    

    return df.apply(secondLargestColumnNumber)
'''
#print(second_largest(df))


#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

#SubSector (α)  ~~ ⌠⌠<DataFrame with Series> Vectorised Operations.  
# Adding a Series to a square DataFrame
#if False:
'''◘◘@Note: while vectorised operation between (Series and DataFrame); each number on the Series will be applied into a row in order.
   # ◙ for example> number (1) in the Series  s; will be accumulated to the {row [0]} in the DataFrame (df).
'''
'''s = pd.Series([1, 2, 3, 4])
df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
#print (df)
print (df + s)
   ''' 
# Adding a Series to a one-row DataFrame 
'''if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10], 1: [20], 2: [30], 3: [40]})
    
    print df
    print '' # Create a blank line between outputs
    print df + s
'''


# Adding a Series to a one-column DataFrame
'''if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10, 20, 30, 40]})
    
    print df
    print '' # Create a blank line between outputs
    print df + s
  '''
#   ◘◘@Note: when attempting to add a Series to 1D DataFrame array; the first element on the data series will be added into the dataFrame array; 
#         and the rest will be not added into...which means return NaN...
    
s = pd.Series([1, 2, 3, 4])
df = pd.DataFrame({0: [10, 20, 30, 40]})
#print(df + s)


#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬    
# Adding when DataFrame column names match Series index
'''if False:
    s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
 '''

'''s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    }) 
print(df + s)
'''

# Adding when DataFrame column names don't match Series index
'''if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
    
    print df
    print '' # Create a blank line between outputs
    print df + s
'''

'''◘◘ @imp__Note : because the default indexing is [0,1,2,3,4,5,.....] then if ["a","b","c","d",...] is replaced with [0,1,2,3,.... ] the accumulation process will be executed;
              but while the indecies are name in different names; then the vectorisation process will not be applied...
'''
'''s = pd.Series([1, 2, 3, 4])
df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
print(s + df)
'''


#if False:
# ◘◘@Note: iterated...
'''s = pd.Series([1, 2, 3, 4])
df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
print (df)
print (df + s)
'''  
# Adding with axis='index'

#if False:
# ◘◘ ◙ ◙@imp___Note: <.add()> with specifying the 'index' as the (axis); then oppositely each element in the Series will be added to the row {rather than the column};
#                while normally manipulating with (+,-,*,/) will be applied into the column rather than the row...
s = pd.Series([1, 2, 3, 4])
df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })   
#print df
#print(df.add(s, axis='index'))

    # The functions sub(), mul(), and div() work similarly to add()
    
# Adding with axis='columns'
'''if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print df
    print '' # Create a blank line between outputs
    print df.add(s, axis='columns')
    # The functions sub(), mul(), and div() work similarly to add()
'''  



'''
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def standardize(df):
    
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    
    This time, try to use vectorized operations instead of apply().
    You should get the same results as you did before.
    
    return None

def standardize_rows(df):
    
    Optional: Fill in this function to standardize each row of the given
    DataFrame. Again, try not to use apply().
    
    This one is more challenging than standardizing each column!
    
    return None'''






#x = df.div(df.std())
'''mean_value = grades_df.mean()

standard_value = grades_df['exam1'] - mean_value[0]

standard_deviation = standard_value / mean_value[0]
print(standard_deviation)
'''


# ◘◘ ◙◙@imp__Note: to return the mean of the column rather than the entire dataFrame; then using (axis = 'columns').....
                  # Also using {axis = rows} will be used to get the mean value for each [row]....

# ◘◘ @Note >> to calculate the standard deviation.....
'''mean_valu = grades_df.mean(axis = 'columns')
standardise_opt = grades_df.sub(grades_df.mean(axis = 'columns'))
standard_deviation = grades_df.std(axis = 'columns')
total_for_standard_deviation = mean_valu.div(standard_deviation,axis='index')
print(total_for_standard_deviation)
'''


#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

# ¶SubSector (ß) Pandas <.groupby()> function....


values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for each block of code to see what it does


# Examine DataFrame
'''#if False:
#print (example_df)
'''


# Examine groups
#if False:
# ◘◘@imp__Note: to arrange and group the elements on the dataFrame based on the specified determinant; Here the result dataFrame is based on ("even") values...
'''grouped_data = example_df.groupby('even')
# The groups attribute is a dictionary mapping keys to lists of row indexes
print (grouped_data.groups)'''


# Group by multiple columns
# ◘◘@imp__Note: also the dataFrame could be grouped by double columns value or multiple column values...
'''grouped_data = example_df.groupby(['even', 'above_three'])
print (grouped_data.groups)
'''  
# Get sum of each group
#if False:
'''grouped_data = example_df.groupby('even')
print (grouped_data.sum())'''
    
# Limit columns in result
#if False:
grouped_data = example_df.groupby('even')
'''
    # You can take one or more columns from the result DataFrame
print (grouped_data.sum()['value'])
    
    # You can also take a subset of columns from the grouped data before 
    # collapsing to a DataFrame. In this case, the result is the same.
print (grouped_data['value'].sum())
'''   
#filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
#subway_df = pd.read_csv(filename)


#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

# ¶SubSector (Γ) Applying on Pandas <.groupby()> function....
values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# ◘◘@imp_method {to sort data based on specified determinant.}
#print(example_df.sort_values(inplace=False, by='value'))



# Change False to True for each block of code to see what it does

# Standardize each group
#if False:
'''def standardize(xs):
    return (xs - xs.mean()) / xs.std()
grouped_data = example_df.groupby('even')
print (grouped_data['value'].apply(standardize))
'''   
# Find second largest value in each group
#if False:
'''
def second_largest(xs):
    sorted_xs = xs.sort(inplace=False, by='value')
    return sorted_xs.iloc[1]
grouped_data = example_df.groupby('even')
#print (grouped_data['value'].apply(second_largest))
'''

# --- Quiz ---
# DataFrame with cumulative entries and exits for multiple stations
ridership_df = pd.DataFrame({
    'UNIT': ['R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051'],
    'TIMEn': ['00:00:00', '02:00:00', '04:00:00', '06:00:00', '08:00:00', '10:00:00', '12:00:00', '14:00:00', '16:00:00'],
    'ENTRIESn': [3144312, 8936644, 3144335, 8936658, 3144353, 8936687, 3144424, 8936819, 3144594],
    'EXITSn': [1088151, 13755385,  1088159, 13755393,  1088177, 13755598, 1088231, 13756191,  1088275]
})

def get_hourly_entries_and_exits(entries_and_exits):
    '''
    Fill in this function to take a DataFrame with cumulative entries
    and exits and return a DataFrame with hourly entries and exits.
    The hourly entries and exits should be calculated separately for
    each station (the 'UNIT' column).
    
    Hint: Take a look at the `get_hourly_entries_and_exits()` function
    you wrote in a previous quiz, DataFrame Vectorized Operations. If
    you copy it here and rename it, you can use it and the `.apply()`
    function to help solve this problem.
    '''
    return None

# @------------------------------------------------------__@ Classes__-----------------------------------------
# --------------@ Imp_Methods.....
# @Method to get value while specifying a key.
items = {"GTX 1650": 2900,"GTX 1660": 3500, "GTX 2060":5600,"GTX 2060 TI":6200,"GTX 2070":6600,"GTX 2080": 7400}
itemsDict = pd.Series(items.values(),index = items.keys())
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

class RetrieveValue(object):
    def __init__(self) -> None:
        super().__init__()

    def returnKey (self,valu):
        for key , value in itemsDict.items():
            if value == valu:
                return key

# @Method to get value while specifying items Dictionary and price.
    def returnKeyFromPrice(self,dictItems,price):
        count = 0
        for i in itemsDict < 5000:
            if i == True:
                print(self.returnKey(itemsDict.iloc[count]))
                count += 1
# @Method to get the highest value from 2D NumPy Array; with the specified names and grade....
    def getNameFromIndex(self,grades_df,array,array2):
        return (grades_df.index[grades_df[array].argmax()],grades_df[array].max(), grades_df.index[grades_df[array2].argmax()],grades_df[array2].max())
# --- @Test
#obk = RetrieveValue()
#obk.returnKeyFromPrice(itemsDict,5000)


#print(4)


#%%
# ¶SubSector (γ) Pandas Data Merge {Merge Multiple DataFrames together}.

'''subway_df = pd.DataFrame({
    'UNIT': ['R003', 'R003', 'R003', 'R003', 'R003', 'R004', 'R004', 'R004',
             'R004', 'R004'],
    'DATEn': ['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
              '05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11'],
    'hour': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'ENTRIESn': [ 4388333,  4388348,  4389885,  4391507,  4393043, 14656120,
                 14656174, 14660126, 14664247, 14668301],
    'EXITSn': [ 2911002,  2911036,  2912127,  2913223,  2914284, 14451774,
               14451851, 14454734, 14457780, 14460818],
    'latitude': [ 40.689945,  40.689945,  40.689945,  40.689945,  40.689945,
                  40.69132 ,  40.69132 ,  40.69132 ,  40.69132 ,  40.69132 ],
    'longitude': [-73.872564, -73.872564, -73.872564, -73.872564, -73.872564,
                  -73.867135, -73.867135, -73.867135, -73.867135, -73.867135]
})



weather_df = pd.DataFrame({
    'DATEn': ['05-01-11', '05-01-11', '05-02-11', '05-02-11', '05-03-11',
              '05-03-11', '05-04-11', '05-04-11', '05-05-11', '05-05-11'],
    'hour': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'latitude': [ 40.689945,  40.69132 ,  40.689945,  40.69132 ,  40.689945,
                  40.69132 ,  40.689945,  40.69132 ,  40.689945,  40.69132 ],
    'longitude': [-73.872564, -73.867135, -73.872564, -73.867135, -73.872564,
                  -73.867135, -73.872564, -73.867135, -73.872564, -73.867135],
    'pressurei': [ 30.24,  30.24,  30.32,  30.32,  30.14,  30.14,  29.98,  29.98,
                   30.01,  30.01],
    'fog': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'rain': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'tempi': [ 52. ,  52. ,  48.9,  48.9,  54. ,  54. ,  57.2,  57.2,  48.9,  48.9],
    'wspdi': [  8.1,   8.1,   6.9,   6.9,   3.5,   3.5,  15. ,  15. ,  15. ,  15. ]
})


newsDataFrame = subway_df.merge(weather_df, on=['DATEn','hour','latitude','longitude'],
how='left')

def combine_dfs(subway_df, weather_df):

    
    Fill in this function to take 2 DataFrames, one with subway data and one with weather data,
    and return a single dataframe with one row for each date, hour, and location. Only include
    times and locations that have both subway data and weather data available.
    

    return subway_df.merge(weather_df, on=['DATEn','hour','latitude','longitude'],how='left')
print(combine_dfs(subway_df,weather_df))
'''



# ◘◘@Note: to merge multiple dataFrame with different columns names that desired to be merged; Use 

#       ▬▬ firstDataFrame.merge(secondDataFrame, left_on = ['DATEn','HOURs'],
#       ▬▬                                       right_on = ['date','hours'],
#       ▬▬                                       how = 'inner')





values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])



subway_df = pd.DataFrame({
    'UNIT': ['R003', 'R003', 'R003', 'R003', 'R003', 'R004', 'R004', 'R004',
             'R004', 'R004'],
    'DATEn': ['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
              '05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11'],
    'hour': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'ENTRIESn': [ 4388333,  4388348,  4389885,  4391507,  4393043, 14656120,
                 14656174, 14660126, 14664247, 14668301],
    'EXITSn': [ 2911002,  2911036,  2912127,  2913223,  2914284, 14451774,
               14451851, 14454734, 14457780, 14460818],
    'latitude': [ 40.689945,  40.689945,  40.689945,  40.689945,  40.689945,
                  40.69132 ,  40.69132 ,  40.69132 ,  40.69132 ,  40.69132 ],
    'longitude': [-73.872564, -73.872564, -73.872564, -73.872564, -73.872564,
                  -73.867135, -73.867135, -73.867135, -73.867135, -73.867135]
})



weather_df = pd.DataFrame({
    'DATEn': ['05-01-11', '05-01-11', '05-02-11', '05-02-11', '05-03-11',
              '05-03-11', '05-04-11', '05-04-11', '05-05-11', '05-05-11'],
    'hour': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'latitude': [ 40.689945,  40.69132 ,  40.689945,  40.69132 ,  40.689945,
                  40.69132 ,  40.689945,  40.69132 ,  40.689945,  40.69132 ],
    'longitude': [-73.872564, -73.867135, -73.872564, -73.867135, -73.872564,
                  -73.867135, -73.872564, -73.867135, -73.872564, -73.867135],
    'pressurei': [ 30.24,  30.24,  30.32,  30.32,  30.14,  30.14,  29.98,  29.98,
                   30.01,  30.01],
    'fog': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'rain': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'tempi': [ 52. ,  52. ,  48.9,  48.9,  54. ,  54. ,  57.2,  57.2,  48.9,  48.9],
    'wspdi': [  8.1,   8.1,   6.9,   6.9,   3.5,   3.5,  15. ,  15. ,  15. ,  15. ]
})


data_by_location = subway_df.groupby(['latitude', 'longitude'], as_index=False).mean()

print(data_by_location)


# ◘◘Plotting the dataFrame: 
plt.scatter(weather_df['latitude'],weather_df['longitude'])


#print(example_df.groupby(['value']).mean())
# Change False to True for this block of code to see what it does

# groupby() without as_index
if False:
    first_even = example_df.groupby('even').first()
    print (first_even)
    print (first_even['even']) # Causes an error. 'even' is no longer a column in the DataFrame
    
# groupby() with as_index=False
if False:
    first_even = example_df.groupby('even', as_index=False).first()
    print (first_even)
    print (first_even['even']) # Now 'even' is still a column in the DataFrame

#filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
#subway_df = pd.read_csv(filename)

## Make a plot of your choice here showing something interesting about the subway data.
## Matplotlib documentation here: http://matplotlib.org/api/pyplot_api.html
## Once you've got something you're happy with, share it on the forums!




# ◘◘@Note: Regarding Multiple Dimension dataFrame (3D DataFrame); commonly that
#          data Structure known as <Panel>.





