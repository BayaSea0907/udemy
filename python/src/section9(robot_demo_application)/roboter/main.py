import roboter

#csv_ctl.reader()

#row_dict['Name'] = 'test'
#row_dict['Restaurant'] = 'ebisu'
#row_dict['Status'] = 'y'

#csv_ctl.write(row_dict)

roboter = roboter.Roboter('ロボコン')
result = True

print('---- loop start ----\n')
while(result):
	result = roboter.start_up()

	if result == True:
		break


