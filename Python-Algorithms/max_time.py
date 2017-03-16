#Program to find the max time in 24hr clock from given integes. Ex: given ints(2,0,5,3), should output 23:50
def solution(A, B, C, D):
    # write your code in Python 2.7
    time = [A,B,C,D]
    
    maxTime = [-1,-1] #Initialize max as hh, mm
    
    for i in range(len(time)-1):
        for j in range(i+1,len(time)): #checks all possible combinations of hh and mm
           
            hours = [time[i],time[j]]
            minutes = [time[ind] for ind in range(len(time)) if ind != i and ind != j ] #takes all other values not present in hours
            hour1 = hours[0]*10+ hours[1]
            hour2 = hours[1]*10+ hours[0]
            hour1 = hour1 if hour1 < 24 else -1 #ensure the hour(hh) is less than 24. since the max can only be 23 hrs
            hour2 = hour2 if hour2 < 24 else -1
            maxHours = max(hour1,hour2)
           
            
            min1 = minutes[0]*10+ minutes[1]
            min2 = minutes[1]*10+ minutes[0]
            min1 = min1 if min1 < 60 else -1  #ensure the minutes(mm) is less than 60. since the max can only be 59 mins
            min2 = min2 if min2 < 60 else -1
            maxMin = max(min1,min2)
           
            if maxHours > -1 and maxMin > -1:
                if maxTime[0] < maxHours:
                    maxTime[0] =  maxHours
                    maxTime[1] = maxMin
                elif maxTime[0] == maxHours and maxMin > maxTime[1]:
                    maxTime[1] = maxMin
                    
    if -1 in maxTime:
        return "NOT POSSIBLE"
    else:
        for ind in range(2):
            if maxTime[ind] < 10:
                maxTime[ind] = "0"+str(maxTime[ind])
        return str(maxTime[0])+":"+str(maxTime[1])
    pass

if __name__ == '__main__':
    print(solution(2,0,5,3))