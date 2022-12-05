from flask import Flask, request, jsonify
from model import Applicant, Education, Skill, Reference, Work_experience, dbconnect
from create import addApplicant, addEducation, addReference, addSkill, addWorkExperience
from read import get_applicant
import json

app = Flask(__name__)

session = dbconnect()

# defining endpoints
@app.route('/cv', methods = ['POST', 'GET'])    
def Cv():
    if request.method == 'GET':
        return jsonify(get_applicant(session)) 
  
    if request.method == 'POST': 
        applicantInstance = addApplicant(request.json['personal_details']) 
        session.add(applicantInstance)
        for educationDict in request.json['Education']:          
            educationInstance = addEducation(educationDict)
            educationInstance.applicant = applicantInstance
            session.add(educationInstance)

        for skillDict in request.json['Skills']:          
            skillInstance = addSkill(skillDict)
            skillInstance.applicant = applicantInstance
            session.add(skillInstance)

        for work_experienceDict in request.json['Work_experience']:          
            work_experienceInstance = addWorkExperience(work_experienceDict)
            work_experienceInstance.applicant = applicantInstance
            session.add(work_experienceInstance)

        for referenceDict in request.json['References']:  
            print(referenceDict)           
            referenceInstance = addReference(referenceDict)
            referenceInstance.applicant = applicantInstance
            session.add(referenceInstance)
        session.commit()
    return 'Succesful'

@app.route('/healthz', methods=['GET'])
def healthz():
    return "ok"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
