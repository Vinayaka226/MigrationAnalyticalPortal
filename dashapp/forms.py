from django import forms
from dashapp.models import Dashboard_Info,ProjectReview

class Dashboard_InfoForm(forms.ModelForm):
    class Meta:
        model = Dashboard_Info
        fields = "__all__"

class ProjectReviewForm(forms.ModelForm):
    class Meta:
        model = ProjectReview
        fields = ['projectName','projectPID','dealValue','cxDMName','SDEName','teamName','reviewMonth','startDate','endDate','executiveSummary','customerSentiment','scheduleStatus','scheduleComments','qualityStatus','qualityComments','resourceStatus','resourceComments','automationStatus','automationComments','accomplishments','goalsForNextMonth','risksImpactAsks']
