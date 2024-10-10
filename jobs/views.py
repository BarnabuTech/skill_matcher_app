# Create your views here.

from django.utils.timezone import now
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Job, JobAlert
import requests

def fetch_jobs_view(request):
    if request.method == 'POST':
        skills = request.POST.get('skills').split(',')
        # Assuming we have an API endpoint to fetch jobs by skills
        url = 'https://tabiya.api/jobs?skills=' + ','.join(skills)
        response = requests.get(url)
        jobs = response.json()

        # Optionally, save jobs to the database
        for job_data in jobs:
            Job.objects.create(
                title=job_data['title'],
                description=job_data['description'],
                location=job_data['location'],
                company=job_data['company'],
                skills_required=job_data['skills']
            )

        return render(request, 'jobs/job_list.html', {'jobs': jobs})
    return render(request, 'jobs/job_search.html')

def check_new_jobs():
    alerts = JobAlert.objects.all()
    for alert in alerts:
        skills = alert.skills.split(',')
        jobs = Job.objects.filter(skills_required__icontains=skills, posted_date__gt=alert.last_checked)
        if jobs.exists():
            # Send notification email
            send_mail(
                'New Job Alerts',
                f"Hi {alert.user.username}, new jobs matching your skills are available!",
                'from@example.com',
                [alert.user.email],
                fail_silently=False,
            )
            # Update the last checked time
            alert.last_checked = now()
            alert.save()
            
def job_list(request):
    # Fetch jobs from your database or other source
    jobs = {'jobs': jobs} # Your logic to get job data
    context = {'jobs': jobs}
    return render(request, 'job_list.html', context)  # Render job list template


def job_search(request):
    # Fetch jobs from your database or other source
    jobs = {'jobs': jobs} # Your logic to get job data
    context = {'jobs': jobs}
    return render(request, 'job_search.html', context)  # Render job list template