#  إِلَهي لا تُعَذِّبني فَإِنّي مُقِرٌّ بِالَّذي قَد كانَ مِنّي فَما لي حِيلَةٌ إِلا رَجائي بِعَفوِكَ إِن عَفَوتَ وَحُسنِ ظَنّي فَكَم مِن زَلَّةٍ لِي في الخطايا عَضَضتُ أَناملي وَقَرَعتُ سِنّي يَظُّنُ الناسُ بي خَيراً وَإِنّي لَشَرُّ الخَلقِ إِن لَم تَعفُ عَنّي


import pandas as pd
import numpy as np



                                                                # ¶¶ ينوه هنا أنه يتوجب تحرير بيانات الجزء المطلوب قبل التجربة 

# ▐ Part I ▀ Numpy ▌



# ▐▌▌▌▌▌▐▌▌ Sector α ▐▌▌▌▌▌▐▌▌  Intoroduction to data analysis.

# implementing a new data frame for the provided data.
'''dataFrame = pd.DataFrame({"Items":["GTX 1650","RTX 2070","RTX 2080"],"Prices":[2900,3200,4500]})'''


# Function to get the least item on the dataFrame.
'''def get_least_cost_item(dataFrame):
    count = 0
    for i in dataFrame.Prices:
        if i < 3200:
            print(dataFrame.Items[count])
        count += 1

cities_data_frame = pd.DataFrame({"City":["Paris","London","Cairo","Dubai"],"Return_Flight_Cost":[200,250,370,450],"Hotel_Per_day_Cost":[20,30,15,10],"Weekly_Car_Rental_Price":[200,120,80,70]})
x = cities_data_frame.Hotel_Per_day_Cost
'''





# ▐▌▌▌▌▌▐▌▌ Sector α ▐▌▌▌▌▌▐▌▌  Numpy data manipulation


'''alexandria = np.array([73, 67, 43])
cairo = np.array([91, 88, 64])
giza = np.array([87, 134, 58])
aswan = np.array([102, 43, 37])
sina = np.array([69, 96, 70])

weights = np.array([0.3,0.1,0.5])'''




# ◘ To open a csv file in numpy
'''
climate_data = np.genfromtxt("C:\\Users\\Mustafa Muhammad\\Documents\\Python Scripts\\Data_Analysis\\climate.csv",delimiter = ",",skip_header = 1)

weights = np.array([0.3,0.1,0.5])
yields = climate_data * weights
'''
# ◘ » Concatenating 2 numpy arrays; merging the second array into a new column in the first numpy array
#     Implementing new dimension.
# هو المُعبر عن ذلك حيث  axis تُستخدم هذه الطريقة لدمج مصفوفتين مختلفتين حيث تنضم المصفوفة المُضافة إلى أعمدة المصفوفة الأولى أو إلى صفوفها و المتغير  
# axis = 0 >> rows صفوف
# axis = 1 >> columns أعمدة






# @Note: عند وضع إضافةالمصفوفتين إلى بعضهما في هذه الحالة يلزم إضافتهما على شكل 

#       (المصفوفة_1, المصفوفة_2) >> np.concatenate((المصفوفة_1, المصفوفة_2), axis = 0 OR 1)
'''climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis = 1)
'''






# ◘ » Saving the new array in csv file.
#  .CSV حيث يُحفظ الملف في هذه الحالة بصيغة  <Numpy> تُستخدم لحفظ بيانات المصفوفة من نوع 
'''np.savetxt("C:\\Users\\Mustafa Muhammad\\Documents\\Python Scripts\\Data_Analysis\\climate_results.csv",
            climate_results, fmt = "%.2f" ,
            header = "temperature, rainfall, humidity, yield_apples",
            comments = "")'''






# ◘ » Arithemetic Operations through same dimensional numpy arrays.
# العمليات الحسابية على المصفوفات المتامثلة في الأبعاد
#تُختلف من حيث التنفيذ عن المصفوفة العادية numpy يُلاحظ هاهنا أن إستخدام العمليات الحسابية مع المصفوفة من نوع 
# حيث أياً من العمليات الحسابية التي تتم عليها تتم على كل عنصر من عناصر المصفوفة أياً كان عددها أو أبعادها
'''arr_a = np.array([1,2,3,4,5])
array_plus = arr_a + 3
print(array_plus)
'''



# ◘ » Arithemetic Operations through different dimensional numpy arrays.
# العمليات الحسابية على المصفوفات المختلفة في الأبعاد
# يتوجب في هذه الحالة أن تتساوى قيم أبعاد المصفوفتين المجموعتين على بعضهما, يُذكر أن أبعاد المصفوفة تُحسب عدد الأعمدة
# حيث المثال أدناه تساوت فيه عدد أعمدة المصفوفةالأولى مع المصفوفة الثانية وهي 5 أعمدة
arr_b = np.array([[1,2,3,4,5],[7,8,9,10,11]])
arr_c = np.array([[1,2,3,4,5],[7,8,9,10,11]])


# print(arr_b + arr_c)



'''diff_dimensional_array = np.array([
    [[1,2,3,4,5],
    [6,7,8,9,10,11]],

    [[12,13,14,15,16],
    [17,18,19,20,21]],

    [[22,23,24,25,26],
    [27,28,29,30,31]]])
    '''
'''
◙ First Dimension  >> is the entire multi-dimensional array.
◙ Second Dimension >> is the first inside array.

array =
{[0]}    [[1,2,3,4,5],              {[0,0]}
        [6,7,8,9,10,11]],           {[0,1]} 

{[1]}        [[12,13,14,15,16],     {[1,0]}   
        [17,18,19,20,21]],          {[1,1]}

{[2]}        [[22,23,24,25,26],     {[2,0]}
        [27,28,29,30,31]]])         {[2,1]}
print(diff_dimensional_array[0,0])
'''


'''ranged_array = np.arange(10,90,3).reshape(3,3,3)
print(ranged_array)'''



#────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

# ▐ Part II ▀ Pandas ▌
# ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬


from  urllib.request import urlretrieve
retreived_file = urlretrieve("https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv",
                "C:\\Users\Mustafa Muhammad\\Documents\\Python Scripts\\Data_Analysis\\italy_covid_data.csv")

retreived_data_frame = pd.read_csv("C:\\Users\Mustafa Muhammad\\Documents\\Python Scripts\\Data_Analysis\\italy_covid_data.csv")


# » info()
# ◘ data frame تسترجع معلومات عن البيانات المعطاة ل 
#  و كذلك المساحة التي يشغلها الملف String حيث تعطي معلومات عن نوعية البيانات ما إذا كانت أعداداً صحيحة أو عشرية أو عبارة عن سلسلة من الحروف    
# 
'''print(retreived_data_frame.info())'''




#─────────────────
# » describe()
# ◘ في محتوى البيانات المُعطاة Column تُستخدم لعرض بيانات إحصائية كالوسط الحسابي و حساب الإنحراف المعياري و غيرها لكل عمود  
'''print(retreived_data_frame.describe())'''





#─────────────────
# initialise new pandas data frame || (pandas) إنشاء هيكل بيانات من نوع 
# dictionary   يتم إنشاؤه على هيئة  
data_frame = { "date":[2020,2019,2018,2017,2016,2015,2014,2013,2012,2011],
               "names":["Muhammad","Ahmad","Issa","Musa","Ibrahim","Ismael","Yunus","Yehia","Dhu-Kifl","Yakoup"]
}
# data frame ثم بعد ذلك تحويله إلى 
pd_data_frame = pd.DataFrame(data_frame)
'''print(pd_data_frame)'''




#─────────────────
# لتصدير بيانات معينة من هذه السلسلة
# ◘  index Number حيث يعطى لها رقم الخانة الدال عليها  iloc[] نستخدم دالة 
'''print(pd_data_frame.iloc[0])'''





#─────────────────
# ◘ إذا ما تم إدراج إسم العامود فذلك يستخدم لإسترجاع البيانات الخاصة به
'''print(pd_data_frame.names)'''
# -- OR --
'''print(pd_data_frame["names"])'''





#─────────────────
# ◘ كما يمكن إسترجاع بيانات معينة من العامود المطلوب 
'''print(pd_data_frame["names"][0])'''






#─────────────────
# ◘ إسترجاع بيانات من عدة أعمدة
'''print(pd_data_frame[["date","names"]])'''






# ▬▬ ◘ .at() method 
# ◘ row index number , column name تستخدم لإسترجاع البيانات من خلال رقم الصف و إسم العامود 
'''print(pd_data_frame.at[8,"names"])'''





#─────────────────
# ◘ تٌستخدم لنسخ هيكل البيانات إلى هيكل بيانات آخر و تجدر المُلاحظة هنا أن أي تغيير يطرأ على هيكل البيانات الجديد لا يُؤثر على الأصل
# » copy() بإستخدام الدالة 
'''new_data_frame = pd_data_frame.copy()
print(new_data_frame)'''





#─────────────────
# ◘  إسترجاع البيانات التي في الصفوف الاولى أو الأخيرة head() , tail()  يمكن من خلال الدالتين  
'''print(pd_data_frame.head(4))
print(pd_data_frame.tail(3))'''




#─────────────────
# ◘ dictionaryيمكن إضافة عامود جديد و يُلاحظ هنا أنها نفس طريقة إضافة بند جديد في ال 


'''retreived_data_frame["positive_rate"] = retreived_data_frame.new_cases / retreived_data_frame.new_tests

print(retreived_data_frame)'''





#─────────────────
# ◘ drop() يمكن حذف عامود من خلال دالة 

'''retreived_data_frame.drop(columns = ["positive_rate"],inplace = True)
print(retreived_data_frame)'''




# ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# ▄▄ α) Specified basic analysis for cases.


'''rate = retreived_data_frame.new_deaths.sum() / retreived_data_frame.new_cases.sum()
print("Total rate: {:.2f} %".format(rate))'''




# ◘ ينوه هنا أنه يمكن إستخدام علامات المقارنة الجبرية في  هيكل البيانات و ذلك لتحديد القيم المطلوبة فقط و تجاهل الأخرى
# و ينتج من ذلك قيم منطقية تعبر عن ما إذا الكانت البيانات الواردة تطبق الشرط أم لا




'''print(retreived_data_frame.new_cases > 1000)
# ▬▬ OR ▬▬
print(retreived_data_frame["new_cases"] > 1000)'''





# ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# ▌▌ ß) Specified analysis using some propablities.


'''
positive_rate = 0.05206657
ratio = retreived_data_frame[retreived_data_frame.new_cases / retreived_data_frame.new_tests > positive_rate]
print(ratio)
'''


#─────────────────
# ◘ Sorting values on data frame and apply analysis on it.
# ◘ ترتيب هيكل البيانات تصاعدياً أو تنازلياً حسب القيم المدرجة كمعاملات في الدالة, حيث يتم إدراج إسم العامود ليكون القيمة المُراد ترتيبها
'''sorted_data_frame = retreived_data_frame.sort_values("new_cases",ascending = False)
print(sorted_data_frame)'''




#─────────────────
# ▬▬ ◘ يُلاحظ أن البيان رقم 172 في بند الحالات الجديدة يحمل الرقم -148 و هذا غير منطقي لذا يتوجب حل هذه المشكلة بإحدى الخطوات التالية
#   1_ تجاهل الصف بأكمله
#   2_ إستبداله بالوسيط الحسابي للبيان التالي له و السابق له
#   3_ إستبداله بصفر 
#   4_ إستبداله بالوسيط الحسابي لبيانات العامود بأكمله

'''
retreived_data_frame.at[172,"new_cases"] = (retreived_data_frame.at[171,"new_cases"] + retreived_data_frame.at[173,"new_cases"]) / 2
print(retreived_data_frame.iloc[172])'''




#─────────────────
# ◘ to_datetime() بطريقة مباشرة لذا يزم تحويلها إلى صيغة يمكن التعرف عليها وذلك عن طريق الدالة  pandas بيانات التاريخ وغيرها لا يتعرف عليها 




retreived_data_frame["date"] = pd.to_datetime(retreived_data_frame.date)
#print(retreived_data_frame["date"])






# ◘ و بعد التحويل إلى صيغة التاريخ يمكن تحديد البيانات حسب السنة و الشهر و اليوم 
# » يتم هنا إضافة عامود جديد للبيانات و يتم تخصيصه لبيانات العام
'''retreived_data_frame["year"] = pd.DatetimeIndex(retreived_data_frame["date"]).year
print(retreived_data_frame["year"])
'''





# » للشهر
retreived_data_frame["month"] = pd.DatetimeIndex(retreived_data_frame["date"]).month
#print(retreived_data_frame["month"])






# » لليوم
'''retreived_data_frame["day"] = pd.DatetimeIndex(retreived_data_frame["date"]).day
print(retreived_data_frame["day"])
'''






# » وحينها إذا ما كان يُراد إستخراج بيانات لشهر بعينه 
'''data_for_july = retreived_data_frame[retreived_data_frame.month == 7] 
#print(data_for_july)
'''






# » أو سنة بعينها 
'''data_for_2021 = retreived_data_frame[retreived_data_frame.year == 2020]
print(data_for_2021)'''







# ◘ للحصول على ناتج إجمالي لكل عامود أو عدة أعمدة
'''data_for_july[["new_cases","new_tests"]]
total_data_for_july = data_for_july.sum()
print(total_data_for_july)'''






# ◘ للحصول على الوسيط الحسابي لبيانات الأعمدة
'''mean_value_of_july_data = data_for_july.mean()
print(mean_value_of_july_data)'''







#─────────────────
# ◘ لهذا الغرض groupby() لترتيب البيانات وفقاً لمعيار معين تستخدم دالة 
# » وحينها يتم إستخراج بيانات وفقاً للشهر و كذلك حساب مجملها ليتم ترتيبها في ما بعد وفقاً لكل شهر على حدى
'''grouped_data_frame = retreived_data_frame.groupby("month")[["new_cases","new_tests"]]
print(grouped_data_frame.sum())
'''





#─────────────────
# ▬▬ ◘◘ Merging data from multiple sources. دمج بيانات من عدة مصادر
location_df_file_url = "https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv"
location_data_frame_retreived_file = urlretrieve(location_df_file_url,"C:\\Users\\Mustafa Muhammad\\Documents\\Python Scripts\\Data_Analysis\\Locations.csv")
locations_df = pd.read_csv("C:\\Users\\Mustafa Muhammad\\Documents\\Python Scripts\\Data_Analysis\\Locations.csv")


#print(locations_df[locations_df.location == "Egypt"]["population"])


# » إنشاء عامود جديد لهيكل البيانات 
retreived_data_frame["location"] = "Egypt"





#◘» يُستخدم هنا لتبيان العامود المشترك بين هيكلي البيانات لدمجهما على أساسه on المعامل 
''''merged_data_frame = retreived_data_frame.merge(locations_df,on = "location").head(3)

#print(merged_data_frame)
'''





# ▬ والناتج يكون على هذا الشكل
'''
        date  new_cases  new_deaths  new_tests  month location continent   population  life_expectancy  hospital_beds_per_thousand  gdp_per_capita
0 2019-12-31        0.0         0.0        NaN     12    Egypt    Africa  102334403.0            71.99                         1.6       10550.206
1 2020-01-01        0.0         0.0        NaN      1    Egypt    Africa  102334403.0            71.99                         1.6       10550.206
2 2020-01-02        0.0         0.0        NaN      1    Egypt    Africa  102334403.0            71.99                         1.6       10550.206
'''




# ▬▬ Some other basic analysis executed over the data frame and added in a new columns.
# 1e6 يجدر التنويه هنا أن 
# تعني 10 مرفوعة لأس 6 
'''merged_data_frame["cases_per_million"] = merged_data_frame.new_cases * 1e6 / merged_data_frame.population
print(merged_data_frame.cases_per_million)'''






#────────────────────────────────────important──────────────────────────────────────
# α)
# ◘ Calculate the total cost for the entire provided costs
'''
number = 0
count = 0
for i in cities_data_frame.Return_Flight_Cost,cities_data_frame.Hotel_Per_day_Cost,cities_data_frame.Weekly_Car_Rental_Price:
    for j in range(4):
        number += i[j]

    count += 1
'''


# ß)
# ◘ Get the least cost on the data frame
'''
def get_least_vacation_cost(cities_data_frame):
    count = 0
    vacation_weekly_cost = cities_data_frame.Hotel_Per_day_Cost * 14
    number = vacation_weekly_cost[1]
    for i in vacation_weekly_cost:
        if number > vacation_weekly_cost[count]:
            number = vacation_weekly_cost[count]
        count += 1
    return cities_data_frame.iloc[count - 1]
'''


# Γ)
# ◘ Get the total cost for data frame integer values provided.
'''
def calc_total_cost(cities_data_frame):
    number = 0
    count = 0
    costs_list = [[],[],[],[]]
    for data_sector in cities_data_frame.Return_Flight_Cost, cities_data_frame.Hotel_Per_day_Cost, cities_data_frame.Weekly_Car_Rental_Price:
        for j in range(4):
            costs_list[j].append(data_sector[j])
        number += 1
    for k in range(len(costs_list)):
        if sum(costs_list[k]) < 1000:
            return cities_data_frame.iloc[count]
        count += 1
'''

# Σ) 
# ◘ return total of each element on both arrays to be multiplied to each other.
'''
def calc_total (region, weights):
    result = 0
    for x,y in zip(region, weights):
        result += x * y
    return result
'''

# σ)
# ◘ return the same result as above function; rather that retreiving each element from both of arrays,
#   Numpy takes the entire required to be multiplied arrays; using <.dot()> method
'''
alexandria_result = np.dot(alexandria,weights)
                ---- OR ----
alexandria_result = sum(alexandria * weights)
'''


# µ)
# ◘ implement new axis of the specified arrays.
'''
a = np.array([1,2])
b = np.array([5,6])
x = np.stack((a,b),1)
'''


# τ)
# ◘ insert new elemenent in the specified array; and in dedicated position.
'''new_array = np.array([1,2,3,4])'''
# » (<Specified_array>,[required_position],<the required array to be inserted>).
'''a = np.insert(new_array,4,[5,6])'''


# Φ)
# ◘ matrix multiplication on numpy.
'''
matrix_mul_value = np.matmul(alexandria,cairo)
                ---- OR ----

» Using [@] sign to indicate matrix multiplication.

matrix_mul_value = alexandria @ cairo
'''

count = 0
l = [1,2,3,4,5]
for i in l:
    if i == 4:
        print(count)
    count += 1
print(l[3])