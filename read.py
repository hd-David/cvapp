from model import Applicant, dbconnect, Education
import pprint

session = dbconnect()
pp = pprint.PrettyPrinter(indent=4)

def get_applicant(session):
# Execute a SELECT query on JOINed tables
    applicants = session.query(Applicant).join(Education, Education.Applicant_id == Applicant.id).all()
    #Loop through applicants
    applicants_list =[]
    for applicant in applicants:
        applicantObject = {
            'name': applicant.name,
            'phone_number': applicant.phone_number,
            'email': applicant.email,
            'linked_in': applicant.linked_in,
            'location': applicant.location,
            'education': []
        }
        for education in applicant.education:
            education = {
                'school': education.school,
                'qualification':  education.qualification,
                'duration':  education.duration,
            }
            applicantObject['education'].append(education)
            applicants_list.append(applicantObject)
            pprint.pprint(applicants_list)
    return applicants_list