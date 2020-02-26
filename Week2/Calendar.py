class calender:

    def month_starts_on(self,year,month,day=1):
        y = year
        m = month
        d = day
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = int((d + x + (31 * m0 // 12))) % 7                     #d0 stores day of week : 1 = Sunday
        return d0
    
    def days(self,year,month):                                      #cal number of days in the given month
        if month in (1,3,5,7,8,10,12):
            return 31
        elif month in (4,6,9,11):
            return 30
        elif month == 2:
            if calender.leap_year(self,year):
                return 29
            else:
                return 28
        else:
            print("wrong input of the month \n the month should be in range 01 to 12 \n you given ",month)
            exit()

    def leap_year(self,year):                                       #Checking leap year
        if  year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                  return True
        else:
            return False
    
    def month(self,year,month):                                     #prints calendar
        d = calender.month_starts_on(self,year,month)               #stores day when month starts
    
        days = calender.days(self,year,month)                       #number of days in the month
        month = []                                                  #list to store list of weeks
        day = 1
        week_days = ['Su','Mo','Tu','We','Th','Fr','Sa']            
        month.append(week_days)

        for i in range(0,6):                                        #i represent the week of the month
            if (days < day):                                        #track the counter day exceeds max days of month
               break
            temp = []                                               #temporary list to store the days of the a week
            
            for j in range(0,7):                                    #j stores day of the week
                if  (days < day):
                   temp.append("  ")
                   continue
                elif i == 0 and j < d:
                    temp.append("  ")
                    continue
                elif day < 10 :
                    temp.append(f'0{day}')
                else:
                    temp.append(f'{day}')
                day +=1
            month.append(temp)
        return month


cal = calender()                                #creating object for calender class
year = int(input("Enter the year"))
month = int(input("Enter the month"))
m = {1:"January",2:"February",3:"March",4:"Aprial",5:"May",6:"June",7:"July",8:"Auguest",9:"September",10:"Octomber",11:"November",12:"December"}

calen = cal.month(year,month)
print()
print("Calender ")
print()
print("year {} {}  ".format(year,m[month]))
# printing the calender
for i in calen:
    print(i)