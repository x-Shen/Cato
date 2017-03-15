import json
import json_extraction
from django.core.management.base import BaseCommand, CommandError

from CatoApp.models import Job
from CatoApp.models import JobNeedSkill
from CatoApp.models import Skill



class Command(BaseCommand):

    def handle(self, *args, **options):
        text=open('finalpart.json')
        text = text.readlines()[1:-2]
        for i in range(len(text)):
            ctext = text[i][:-2]
            jdata = json.loads(ctext)
            j = Job(company=json_extraction.get_company(jdata), title = json_extraction.get_title(jdata),url = json_extraction.get_url(jdata))
            print(j)
            j.save()

        for i in range(len(text)):
            ctext = text[i][:-2]
            jdata = json.loads(ctext)
            q = Job.objects.filter(title = json_extraction.get_title(jdata))
            q0 = q[0]
            skills = json_extraction.get_skills(jdata)
            for s in skills:
                qs = Skill.objects.filter(name = s)
                s0 = qs[0]
                q_object = Job.objects.get(id = q0.id)
                s_object = Skill.objects.get(id = s0.id)
                jns = JobNeedSkill(job = q_object,skill = s_object)
                jns.save()
    
    



    
