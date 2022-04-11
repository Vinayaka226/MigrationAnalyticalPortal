from django.shortcuts import render, redirect
from django.http import HttpResponse
from dashapp.models import Issue,Lessons
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def main(request):
	return redirect('/account/login')
	
def getLessonLearntTable(request):
 	lessons = Lessons.objects.all()
 	regionsApac = Issue.objects.filter(Region = 'APAC')
 	regionsAmear = Issue.objects.filter(Region = 'AMEAR')
 	regionsEmea = Issue.objects.filter(Region = 'EMEA')
 	apacCount = regionsApac.count()
 	amearCount = regionsAmear.count()
 	emeaCount = regionsEmea.count()
 	
 	return render(request,'mainPage_KM.html',{'lessons':lessons, 'apacCount':apacCount,'amearCount':amearCount,'emeaCount':emeaCount})

def myLesson(request, firstName):
	#print(username)
	userLesson = Lessons.objects.filter(username=request.user)
	lessonCount = userLesson.count()
	return render(request, 'myLessons.html',{'userLesson':userLesson, 'lessonCount':lessonCount,'username':request.user,'firstName':firstName})
	#return redirect('/LLM/mainPage')

def showDetails(request,issueid):
	lesson = Lessons.objects.filter(IssueID_id =issueid)
	return render(request,'lessonDetails.html',{'lessons':lesson,'lessonId':issueid})

def deleteLesson(request, issueid):
	issue = Issue.objects.get(IssueID = issueid)
	issue.delete()
	messages.info(request, issueid)
	return redirect('getLessonLearntTable')

def addLesson(request,username, firstName):
	if request.method =='POST':
		#issueId = request.POST['issueId']
		region = request.POST['region']
		#recordedBy = request.POST.get['recorderBy']
		deviceOS = request.POST['deviceOS']
		tacID = request.POST['tacID']
		status = request.POST['status']
		title = request.POST['title']
		date = request.POST['date']
		activityType = request.POST['activityType']
		functionalBlock = request.POST['functionalBlock']
		description = request.POST['description']
		solution = request.POST['solution']
		learnt = request.POST['learnt']
		avoidance = request.POST['avoidance']
		project_name = request.POST['project']
		
		
		#if len(request.FILES['image']) !=0:
		image = request.FILES.get('image', False)
		model_Number = request.POST['modelNumber']

		if image == False:
			image = ""

		#print("*************")
		#print(type(image))
		issue = Issue.objects.all()
		lesson = Lessons.objects.all()
		print("*************")
		print(lesson.count())
		lastIndex = issue.count()-1
		lastIssue = issue[lastIndex]
		newIssueId = int(lastIssue.IssueID) + 1
		newIssueId = str(newIssueId)
	
		#if issueId == "":
		#	messages.info(request,"IssueID cannot be Blank!")
		#	return redirect('/LLM/addLesson/'+user.username)
		#else:
		issue = Issue(IssueID = newIssueId, IssueTitle=title,FunctionalBlock=functionalBlock,DeviceOS=deviceOS,
			TACID=tacID,Region=region)
		issue.save()
		lesson = Lessons(IssueID_id=newIssueId,username=username,Date_of_Migration=date,Activity_Type=activityType,
			Description=description,Solution=solution,Lesson=learnt,Avoidance=avoidance,Status=status,
			Recorded_By=firstName,project_id=project_name, image=image, modelNumber= model_Number)
			
		lesson.save()
		messages.success(request, newIssueId)
		return redirect('/LLM/myLesson/'+username)
		#return render(request,'LessonAdded.html')
	else:
		return render(request,'addLesson.html')

def editLesson(request,issueid,firstName):
	issue = Issue.objects.all()
	lastIndex = issue.count()-1
	lastIssue = issue[lastIndex]
	newIssueId = int(lastIssue.IssueID) + 1
	newIssueId = str(newIssueId)
	print(newIssueId)
	if request.method =='POST':
		'''
		issue = Issue.objects.get(IssueID=issueid)
		issue.IssueTitle = request.POST['title']
		issue.FunctionalBlock = request.POST['functionalBlock']
		issue.DeviceOS = request.POST['deviceOS']
		issue.TACID = request.POST['tacID']
		issue.Region = request.POST['region']
		issue.save()

		lesson = Lessons.objects.get(IssueID_id=issueid)
		lesson.Date_of_Migration = request.POST['date']
		lesson.Activity_Type = request.POST['activityType']
		lesson.Description = request.POST['description']
		lesson.Solution = request.POST['solution']
		lesson.Lesson = request.POST['learnt']
		lesson.Avoidance = request.POST['avoidance']
		lesson.Status = request.POST['status']
		lesson.save()
		'''
		region = request.POST['region']
		#recordedBy = request.POST.get['recorderBy']
		deviceOS = request.POST['deviceOS']
		tacID = request.POST['tacID']
		status = request.POST['status']
		title = request.POST['title']
		date = request.POST['date']
		activityType = request.POST['activityType']
		functionalBlock = request.POST['functionalBlock']
		description = request.POST['description']
		solution = request.POST['solution']
		learnt = request.POST['learnt']
		avoidance = request.POST['avoidance']
		project_name = request.POST['project']
		modelNumber = request.POST['modelNumber']

		print(newIssueId)
		issue = Issue(IssueID = newIssueId, IssueTitle=title,FunctionalBlock=functionalBlock,DeviceOS=deviceOS,
			TACID=tacID,Region=region)
		issue.save()

		lesson = Lessons(IssueID_id=newIssueId,username=request.user,Date_of_Migration=date,Activity_Type=activityType,
			Description=description,Solution=solution,Lesson=learnt,Avoidance=avoidance,Status=status,
			Recorded_By=firstName,project_id=project_name,modelNumber = modelNumber)
		lesson.save()
		msg = " "+issueid+" was updated and new Issues has been created with ID: "+newIssueId
		messages.success(request, msg)
		return redirect('/LLM/mainPage/')
	else:

		lesson = Lessons.objects.filter(IssueID_id =issueid)
		return render(request,'editLesson.html',{'lessons':lesson,'newIssueId':newIssueId,'firstName':firstName})

def searchData(request):
	print(request)
	fb = request.GET['fblock']
	os = request.GET['do']
	reg = request.GET['region']

	if(len(fb) !=0 and len(os) != 0 and len(reg) != 0):
		issues = Issue.objects.filter(FunctionalBlock = fb, DeviceOS = os, Region = reg)
		#Create a set data object
		lessons = set()
		for issue in issues:		
			lesson = Lessons.objects.filter(IssueID = issue.IssueID)
			#If Multiple Queryset objects are returned, add one object at a time to lessons set
			for l in lesson:
				lessons.add(l)			
		return render(request,'searchPage.html',{'lessons': lessons,'FunctionalBlock':fb,
			'DeviceOS':os,'Region':reg})

	elif(len(fb) !=0 and len(os) != 0 and len(reg) == 0):
		issues = Issue.objects.filter(FunctionalBlock = fb, DeviceOS = os)
		#Create a set data object
		lessons = set()
		for issue in issues:		
			lesson = Lessons.objects.filter(IssueID = issue.IssueID)
			#If Multiple Queryset objects are returned, add one object at a time to lessons set
			for l in lesson:
				lessons.add(l)			
		return render(request,'searchPage.html',{'lessons': lessons,'FunctionalBlock':fb,
			'DeviceOS':os,'Region':"null"})

	elif(len(fb) !=0 and len(os) == 0 and len(reg) != 0):
		issues = Issue.objects.filter(FunctionalBlock = fb, Region = reg)
		#Create a set data object
		lessons = set()
		for issue in issues:		
			lesson = Lessons.objects.filter(IssueID = issue.IssueID)
			#If Multiple Queryset objects are returned, add one object at a time to lessons set
			for l in lesson:
				lessons.add(l)			
		return render(request,'searchPage.html',{'lessons': lessons,'FunctionalBlock':fb,
			'DeviceOS':"null",'Region':reg})
	elif(len(fb) ==0 and len(os) != 0 and len(reg) != 0):
		issues = Issue.objects.filter( DeviceOS = os, Region = reg)
		#Create a set data object
		lessons = set()
		for issue in issues:		
			lesson = Lessons.objects.filter(IssueID = issue.IssueID)
			#If Multiple Queryset objects are returned, add one object at a time to lessons set
			for l in lesson:
				lessons.add(l)			
		return render(request,'searchPage.html',{'lessons': lessons,'FunctionalBlock':"null",
			'DeviceOS':os,'Region':reg})

	elif(len(fb) !=0 and len(os) == 0 and len(reg) == 0):
		issues = Issue.objects.filter(FunctionalBlock = fb)
		#Create a set data object
		lessons = set()
		for issue in issues:		
			lesson = Lessons.objects.filter(IssueID = issue.IssueID)
			#If Multiple Queryset objects are returned, add one object at a time to lessons set
			for l in lesson:
				lessons.add(l)			
		return render(request,'searchPage.html',{'lessons': lessons,'FunctionalBlock':fb,
			'DeviceOS':"null",'Region':"null"})
	elif(len(fb) ==0 and len(os) != 0 and len(reg) == 0):
		issues = Issue.objects.filter(DeviceOS = os)
		#Create a set data object
		lessons = set()
		for issue in issues:		
			lesson = Lessons.objects.filter(IssueID = issue.IssueID)
			#If Multiple Queryset objects are returned, add one object at a time to lessons set
			for l in lesson:
				lessons.add(l)			
		return render(request,'searchPage.html',{'lessons': lessons,'FunctionalBlock':"null",
			'DeviceOS':os,'Region':"null"})
	elif(len(fb) ==0 and len(os) == 0 and len(reg) != 0):
		issues = Issue.objects.filter(Region = reg)
		#Create a set data object
		lessons = set()
		for issue in issues:		
			lesson = Lessons.objects.filter(IssueID = issue.IssueID)
			#If Multiple Queryset objects are returned, add one object at a time to lessons set
			for l in lesson:
				lessons.add(l)			
		return render(request,'searchPage.html',{'lessons': lessons,'FunctionalBlock':"null",
			'DeviceOS':"null",'Region':reg})
	else:
		return HttpResponse("<h2> OOPS! Please enter atleast 1 field to filter!")