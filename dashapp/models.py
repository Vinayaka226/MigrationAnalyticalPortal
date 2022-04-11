from django.db import models
import datetime
import os

# Create your models here.
class Dashboard_Info(models.Model):
    projectName = models.CharField(primary_key = True, max_length = 100)
    category = models.CharField(max_length = 3)
    dmName  = models.CharField(max_length = 100)
    completionZone = models.CharField(max_length = 10, default = "Green")
    projectStatus = models.CharField(max_length = 10, default = "New")
    dealValue = models.CharField(max_length = 15)
    #customer = models.TextField(default="Not Available")

    class Meta:
        db_table = "Dashboard_Info"

#This Model holds general information of projects listed in Dashboard_Info
class ProjectDetails(models.Model):
    ProjectId = models.CharField(primary_key = True, max_length = 20)
    projectName = models.ForeignKey(Dashboard_Info,
    on_delete = models.CASCADE,)
    category = models.CharField(max_length = 3)
    startDate = models.CharField(max_length = 25, default = "May 2020")
    endDate = models.CharField(max_length = 25, default = "June 2020")
    tenure = models.IntegerField()
    numberOfSitesPlanned = models.IntegerField()
    numOfDevicesPlannedForMigration = models.IntegerField(default = 3500)
    numberOfWindowsPlanned = models.IntegerField(default = 590)
    numberOfWindowsExecuted = models.IntegerField(default = 448)
    numOfWindowsExecutedWidOutRollback =  models.IntegerField(default = 448)
    numOfSitesMigrated = models.IntegerField(default = 447)
    numberOfDevicesMigrated = models.IntegerField()
    numberOfAgreedServices = models.IntegerField(default = 451)
    numberOfServicesUpPostMigration = models.IntegerField(default = 449)
    totalHoursAllocated = models.IntegerField()
    totalProjectEfforts = models.IntegerField()
    plannedResourceAllocation = models.IntegerField()
    summary = models.TextField()
    completionStatus = models.IntegerField()
    totalSites = models.IntegerField(default = 550)
    projectLead = models.CharField(max_length = 50, default = "Channabasava")
    projectManager = models.CharField(max_length = 50, default = "Anuj Kumar")
    projectDeliveryManager = models.CharField(max_length = 50, default = "Prasanna Bakthavatchalam")
    preSales = models.CharField(max_length = 10, default = "No")
    region = models.CharField(max_length = 50, default = "Americas")
    theater = models.CharField(max_length = 50, default = "Americas")
    segment = models.CharField(max_length = 10, default = "GET")
    competativeMigration = models.CharField(max_length = 10, default = "No")
    thirdPartyToCisco = models.CharField(max_length = 10, default = "Yes")
    migrationType =  models.CharField(max_length = 30, default = "Device Migration")
    dealValue = models.IntegerField(default = 5)
    modifiedBy = models.TextField(default="Not Available")
    dealId = models.TextField(default="Not Available")
    includeForBookings = models.CharField(max_length=12, default="No")
    bookingsComment = models.TextField(default="Not Available")
    repeatBusiness = models.CharField(max_length = 5, default = "Yes")
    technology = models.TextField(default="NA")
    projectType = models.CharField(max_length = 40, default = "Migration")
    projectClass = models.CharField(max_length = 50, default = "AS-Transactional")
    executiveSummary = models.TextField(default="Not Available")
    generalComments = models.TextField(default="Not Available")
    serviceDelivery = models.TextField(default="Not Available")
    source = models.TextField(default="Not Available")
    sourceRequesterName = models.TextField(default="Not Available")
    staffing = models.TextField(default="Not Available")
    repeatBusiness = models.TextField(default="Not Available")
    repeatBusinessRemark = models.TextField(default="Not Available")
    newProjectAudit = models.TextField(default="Not Available")
    pOneProject = models.TextField(default="Not Available")
    newProjectAuditDate = models.CharField(max_length = 25, default = "5/20/2020")
    pOneAudit = models.TextField(default="Not Available")
    pOneAuditDate = models.CharField(max_length = 25, default = "5/20/2020")
    modified = models.CharField(max_length = 25, default = "4/30/2020  3:02:01 PM")
    test = models.CharField(max_length = 35, default = "Shaurya Gupta")
    projectBookingYear = models.CharField(max_length = 25, default = "FY21")
    executionFY = models.CharField(max_length = 25, default = "FY21-22")
    startDate = models.CharField(max_length = 25,default="NA")
    endDate = models.CharField(max_length = 25,default="NA")
    executiveSummary = models.TextField(default="Not Available")
    customerSentiment = models.CharField(max_length = 10, default="NA")
    overallStatus = models.CharField(max_length = 10, default="NA")
    scheduleStatus = models.CharField(max_length = 10,default="NA")
    scheduleComments = models.TextField(default="Not Available")
    qualityStatus = models.CharField(max_length = 10,default="NA")
    qualityComments = models.TextField(default="Not Available")
    resourceStatus = models.CharField(max_length = 10,default="NA")
    resourceComments = models.TextField(default="Not Available")
    automationStatus = models.CharField(max_length = 10,default="NA")
    automationComments = models.TextField(default="Not Available")
    accomplishments = models.TextField(default="Not Available")
    goalsForNextMonth = models.TextField(default="Not Available")
    risksImpactAsks = models.TextField(default="Not Available")
    India_NCEs = models.TextField(default="Not Available")
    otherRegionNCEs = models.TextField(default="Not Available")
    preSalesActivity = models.CharField(max_length = 10, default="No")
    preSalesContributor = models.TextField(default="Not Available")
    preSalesEffort = models.TextField(default="Not Available")
    scheduleStatus = models.TextField(default="Not Available")
    qualityStatus = models.TextField(default="Not Available")
    resourceStatus = models.TextField(default="Not Available")
    automationStatus = models.TextField(default="Not Available")
    cbuCfuStatus = models.TextField(default="Not Available")
    CommentsOnScheduleResourcing = models.TextField(default="Not Available")

    class Meta:
        db_table = "projectdetails"

class RagDetails(models.Model):
    ProjectId = models.ForeignKey(ProjectDetails, on_delete = models.CASCADE,)
    month = models.IntegerField(default = 5)
    year = models.IntegerField(default = 2019)
    windowsPlanned = models.IntegerField()
    windowsCompleted = models.IntegerField()
    openIssues = models.CharField(max_length = 3)
    custSatisfaction = models.IntegerField()
    #custSatisfaction > 6, windowsCompleted = (90%)windowsPlanned => green
    #custSatisfaction > 6, windowsCompleted  (75-89%) windowsPlanned => Amber
    sitesCompleted = models.IntegerField()#Gives monthly data on sites completed.

    class Meta:
        db_table = "RAGDetails"

class ProjectReview(models.Model):
    projectName = models.ForeignKey(Dashboard_Info,
    on_delete = models.CASCADE,)
    projectPID = models.CharField(max_length = 30)
    dealValue = models.CharField(max_length = 8)
    cxDMName = models.CharField(max_length = 100)
    SDEName = models.CharField(max_length = 100)
    teamName = models.CharField(max_length = 100)
    reviewMonth = models.CharField(max_length = 25)
    startDate = models.CharField(max_length = 25)
    endDate = models.CharField(max_length = 25)
    executiveSummary = models.TextField(default="NA")
    customerSentiment = models.CharField(max_length = 10,default="NA")
    overallStatus = models.CharField(max_length = 10,default="NA")
    scheduleStatus = models.CharField(max_length = 10,default="NA")
    scheduleComments = models.TextField(default="NA")
    qualityStatus = models.CharField(max_length = 10,default="NA")
    qualityComments = models.TextField(default="NA")
    resourceStatus = models.CharField(max_length = 10,default="NA")
    resourceComments = models.TextField(default="NA")
    automationStatus = models.CharField(max_length = 10,default="NA")
    automationComments = models.TextField(default="NA")
    accomplishments = models.TextField(default="NA")
    goalsForNextMonth = models.TextField(default="NA")
    risksImpactAsks = models.TextField(default="NA")
    India_NCEs = models.TextField(default="NA")
    otherRegionNCEs = models.TextField(default="NA")
    preSalesActivity = models.CharField(max_length = 10, default="No")
    preSalesContributor = models.TextField(default="NA")
    preSalesEffort = models.TextField(default="NA")
    scheduleStatus = models.TextField(default="NA")
    qualityStatus = models.TextField(default="NA")
    resourceStatus = models.TextField(default="NA")
    automationStatus = models.TextField(default="NA")
    cbuCfuStatus = models.TextField(default="NA")
    CommentsOnScheduleResourcing = models.TextField(default="NA")

    class Meta:
        db_table = "project_review"

class Resources(models.Model):
    cecID = models.CharField(primary_key= True, max_length=10)
    name = models.CharField(max_length=50)
    empId = models.IntegerField()
    projectRole = models.CharField(max_length=30)
    phoneNum = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    badge = models.CharField(max_length=5)
    assignedProject = models.CharField(max_length=50, default='Not Assigned')
    entOrSp = models.CharField(max_length=50, default='ENT')
    leadCapable = models.CharField(max_length=5, default='No')
    manager = models.CharField(max_length=50, default= 'Anuj Kumar')

    class Meta:
        db_table = "Resources"

class resourceSkills(models.Model):
    cecId = models.ForeignKey(Resources, on_delete= models.CASCADE)
    #assignedProject = models.CharField(max_length=50)
    #technology = models.CharField(max_length=20)
    certiDevnet = models.CharField(max_length=3)
    certiCcna = models.CharField(max_length=3)
    certiCcnp = models.CharField(max_length=3)
    certiSdwan = models.CharField(max_length=3)
    certiSda = models.CharField(max_length=3)
    certiCcie = models.CharField(max_length=3)

    class Meta:
        db_table = "resourceSkills"

class EntTechnologies(models.Model):
    cecId = models.ForeignKey(Resources, on_delete=models.CASCADE)
    entRouting = models.CharField(max_length=100)
    entSwitching = models.CharField(max_length=100)
    itilFoundation = models.CharField(max_length=50)
    entOperationsTools = models.CharField(max_length=100)
    entDesign = models.CharField(max_length=100)
    entDnaSDA = models.CharField(max_length=100)
    entMulticast = models.CharField(max_length=100)
    entQos = models.CharField(max_length=100)
    entDmvpn = models.CharField(max_length=100)
    entMeraki = models.CharField(max_length=100)
    entMultiCloud = models.CharField(max_length=100)
    entSdn = models.CharField(max_length=100)
    entIpv6 = models.CharField(max_length=100)

    class Meta:
        db_table = "EntTechnologies"

class SpTechnologies(models.Model):
    cecId = models.ForeignKey(Resources,on_delete=models.CASCADE)
    spRoutingSwitching = models.CharField(max_length=100)
    spMplsL2L3Vpn = models.CharField(max_length=100)
    spMplste = models.CharField(max_length=100)
    spMulticastMultiCastVpn = models.CharField(max_length=100)
    spXrHardwarePlatformsOs = models.CharField(max_length=100)
    spNexusHardwarePlatformsOs = models.CharField(max_length=100)
    spAccessPlatforms = models.CharField(max_length=100)
    spSegmentRouting = models.CharField(max_length=100)
    spSegmentRoutingSdnBgpPcep = models.CharField(max_length=100)
    spSegmentRoutingTE = models.CharField(max_length=100)
    spEvpnPbBEvpn = models.CharField(max_length=100)
    spVxlan = models.CharField(max_length=100)
    spNso = models.CharField(max_length=100)

    class Meta:
        db_table = "SpTechnologies"

class ScriptingSkills(models.Model):
    cecId = models.ForeignKey(Resources,on_delete=models.CASCADE)
    python = models.CharField(max_length=20)
    vbaScripting = models.CharField(max_length=20)
    restApi = models.CharField(max_length=20)
    jsonXml = models.CharField(max_length=20)
    netconfRestconfYang = models.CharField(max_length=20)

    class Meta:
        db_table = "ScriptingSkills"
  

class Automation1(models.Model):
    projectName = models.ForeignKey(Dashboard_Info, on_delete=models.CASCADE,)
    offer = models.CharField(max_length=10)
    amiFunction = models.CharField(max_length=15)
    architecture = models.CharField(max_length=30)
    #technoDomain = models.CharField(max_length=10)
    subDomain = models.CharField(max_length=15)
    technology = models.CharField(max_length=30)
    qtr = models.CharField(max_length=10)
    lifeCycleStage = models.CharField(max_length=50)
    serviceDescription = models.CharField(max_length=50)
    solutionTemplateDocument = models.CharField(max_length=50)
    frequencyofdelivery = models.CharField(max_length=50)
    effortBaseline = models.IntegerField()
    nwDiagUpdatesAutomatable = models.CharField(max_length=5)
    mwPrePostChecksAutomatable = models.CharField(max_length=5)
    configPushAutomatable = models.CharField(max_length=5)
    validationCorporateAppAutomatable = models.CharField(max_length=5)
    validationPublicAppAutomatable = models.CharField(max_length=5)
    nwDiagUpdatesCurrentManualEffortMin = models.IntegerField()
    mwPrePostChecksCurrentManualEffortMin = models.IntegerField()
    configPushCurrentManualEffortMin = models.IntegerField()
    validationCorporateAppCurrentManualEffortMin = models.IntegerField()
    validationPublicAppCurrentManualEffortMin = models.IntegerField()
    nwDiagUpdatesCurrentFinalEffortMin = models.IntegerField()
    mwPrePostChecksCurrentFinalEffortMin = models.IntegerField()
    configPushCurrentFinalEffortMin = models.IntegerField()
    validationCorporateAppFinalManualEffortMin = models.IntegerField()
    validationPublicAppFinalManualEffortMin = models.IntegerField()
    nwDiagUpdatesDeliverableCount = models.IntegerField()
    mwPrePostChecksDeliverableCount = models.IntegerField()
    configPushDeliverableCount = models.IntegerField()
    validationCorporateAppDeliverableCount = models.IntegerField()
    validationPublicAppDeliverableCount = models.IntegerField()
    #devicesPerDeliverable = models.IntegerField()

    class Meta:
        db_table = "Automation1"


#############################################################################################
#############################################################################################


class Issue(models.Model):
    IssueID = models.CharField(primary_key=True, max_length = 10)
    IssueTitle = models.CharField(max_length = 50)
    FunctionalBlock = models.CharField(max_length = 30)
    DeviceOS = models.CharField(max_length = 20)
    TACID = models.CharField(max_length = 10)
    Region = models.CharField(max_length = 5)    

    class Meta:
        db_table = "Issue"


class Project_Names(models.Model):
    project_ID = models.CharField(primary_key=True, max_length=10)
    project_Name = models.CharField(max_length=150)

    class Meta:
        db_table = "Project_Names"

def filepath(request,filename):
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    oldFilname = filename
    filename = "%s%s"%(timeNow,oldFilname)
    return os.path.join("uploads/", filename)

class Lessons(models.Model):
    IssueID = models.ForeignKey(Issue, on_delete = models.CASCADE,)
    username = models.CharField(max_length=150, default= "not available")
    Date_of_Migration = models.CharField(max_length = 25)
    Activity_Type = models.CharField(max_length = 50)
    Description = models.CharField(max_length = 900)
    Solution = models.CharField(max_length = 900)
    Lesson = models.CharField(max_length = 900)
    Avoidance = models.CharField(max_length = 900)
    Status = models.CharField(max_length = 10)
    Recorded_By = models.CharField(max_length = 150)
    project = models.ForeignKey(Project_Names, on_delete=models.CASCADE, default = "0")
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    modelNumber = models.CharField(max_length = 15, default="NA")

    class Meta:
        db_table = "Lessons"

'''
class projectTracker(models.Model):



    class Meta:
        db_table = "projectTracker"
'''

