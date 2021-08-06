from django.shortcuts import render,redirect
from .models import Faculty_Department  
from django.http import HttpResponse
import xlwt

# Create your views here.
def export_excel(request):
       
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Faculty.xls' 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Faculty')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bolld = True
    columns = ['IT', 'Mechanical', 'Electrical', 'Teachers']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Faculty_Department.objects.filter().values_list('IT', 'Mechanical', 'Electrical', 'Teachers')
    for i in rows:
        row_num +=1
        for col_num in range(len(rows)):
            ws.write(row_num, col_num, str(rows[col_num]),font_style)
    wb.save(response)
    return response

def home(request): 	

	if request.method=="POST":
		name=request.POST['name']
		dep_type1=request.POST['name1']
		dep_type2=request.POST['name2']
		print(dep_type2)
		if dep_type1:
			if dep_type1=="IT":
				val = Faculty_Department(IT=name)
				val.save()
			elif dep_type1=="Mechanical":
				val = Faculty_Department(Mechanical=name)
				val.save()
			elif dep_type1=="Electrical":
				val = Faculty_Department(Electrical=name)
				val.save()
			elif dep_type1=="Teachers":
				val = Faculty_Department(Teachers=name)
				val.save()
		if dep_type2:
			if dep_type2=="IT":
				val = Faculty_Department(IT=name)
				val.save()
			elif dep_type2=="Mechanical":
				val = Faculty_Department(Mechanical=name)
				val.save()
			elif dep_type2=="Electrical":
				val = Faculty_Department(Electrical=name)
				val.save()
			elif dep_type2=="Teachers":
				val = Faculty_Department(Teachers=name)
				val.save()
	return render(request,'index.html')


