import json

#text = open("jobs_internsupply.json").readlines()[1:-1]
#print(text[-1])
#text2 = text[2][:-2]
#print(text2)
#jdata = json.loads(text2)
#print(type(jdata))
#print(jdata['title'])
#jdata2 = json.loads(jdata['description'])
#print(jdata2)

def parse_jfile(filename):
    text = open("jobs_internsupply.json").readlines()[1:-1]
    for line in text:
        line = line[:-2]
    return text

def get_company(jdata):
    try:
        return jdata['company']
    except:
        return ''

def get_title(jdata):
    try:
        return jdata['title']
    except:
        return ''

def get_url(jdata):
    try:
        return jdata["application_url"]
    except:
        return ''

def get_skills(jdata):
    try:
        return jdata["skills"]
    except:
        return ''
    

#jdata3 = jdata2['content']
#print(jdata3)

#all_des = ''
#for i in range(len(text)):
#    ctext = text[i][:-2]
#    jdata = json.loads(ctext)
#    j = Job(company=json_extraction.get_company(jdata), title = json_extraction.get_title(jdata),url = json_extraction.get_url(jdata))  


    



