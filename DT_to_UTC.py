import datetime
def convert_dt_to_utc(date_time): #time must be in "yyyy-mm-dd hh:mm:ss.xxxxxx" format, example : 2022-08-15 13:47:22.949504
#                                                                                                 2021-02-24 18:21:36.574231 
#                                                                                                 2018-07-14 19:57:13.478321
 
	date_time = datetime.datetime(int(date_time[0:4]),int(date_time[5:7]),int(date_time[8:10]),int(date_time[11:13]),int(date_time[14:16]),int(date_time[17:19]),int(date_time[20:-1]))
	date_time=(date_time-datetime.datetime(1970,1,1)).total_seconds()
	date_time-=0  #This should be corrected in seconds according to the local time of your location.
	date_time=int(date_time)
	date_time=str(date_time)
	return date_time

def main():
	date_time=input("Enter the date time:")
	utc_time=convert_dt_to_utc(date_time)
	print(utc_time)
if __name__=="__main__":
	main()
