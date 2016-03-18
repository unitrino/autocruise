import xlwt

data = [ 
{'id':1,'data':'10-10-2016','empty':'','from':'s1','full_name':'Egor Egor','numb':'3','tel':'+38099999','to':'d1','note':'TEXTTEXT'},
{'id':2,'data':'11-11-2016','empty':'','from':'s2','full_name':'Egor Egor2','numb':'33','tel':'+380999991','to':'d12','note':'TEXTTEXT2'},
{'id':3,'data':'12-12-2016','empty':'','from':'s3','full_name':'Egor Egor3','numb':'34','tel':'+380999992','to':'d13','note':'TEXTTEXT3'},
{'id':4,'data':'12-13-2016','empty':'','from':'s1','full_name':'Egor Egor4','numb':'35','tel':'+380999993','to':'d14','note':'TEXTTEXT4'},
{'id':5,'data':'12-14-2016','empty':'','from':'s2','full_name':'Egor Egor5','numb':'36','tel':'+380999994','to':'d15','note':'TEXTTEXT5'},
{'id':6,'data':'12-15-2016','empty':'','from':'s3','full_name':'Egor Egor6','numb':'37','tel':'+380999995','to':'d16','note':'TEXTTEXT6'}
]

wb = xlwt.Workbook()

work_sheets_groups = dict()
for i in data:
	if i["from"] not in work_sheets_groups:
		work_sheets_groups[i["from"]] = [i['id']]
	else:
		work_sheets_groups[i["from"]].append(i['id'])

print work_sheets_groups


for i in work_sheets_groups:
	ids = work_sheets_groups[i]
	ws = wb.add_sheet(i)
	row_numb = 0
	for j in ids:
		for ii in data:
			if ii['id'] == j:
				ws.write(row_numb,0,ii["data"])
				ws.write(row_numb,1,ii["empty"])
				ws.write(row_numb,2,ii["from"])
				ws.write(row_numb,3,ii["full_name"])
				ws.write(row_numb,4,ii["numb"])
				ws.write(row_numb,5,ii["tel"])
				ws.write(row_numb,6,ii["to"])
				ws.write(row_numb,7,ii["note"])
				row_numb += 1

wb.save('example.xls')