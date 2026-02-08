import urllib.request, json

try:
    resp = urllib.request.urlopen('http://localhost:8000/user/50/assessment-history')
    data = json.loads(resp.read())
    if data['history'] and data['history'][0]['recommended_courses']:
        course = data['history'][0]['recommended_courses'][0]
        print('✓ Score field returned from backend:')
        print('  Course:', course.get('course_name'))
        print('  Compatibility Score:', course.get('compatibility_score'))
    else:
        print('No courses in history')
except Exception as e:
    print('Error:', str(e)[:80])
