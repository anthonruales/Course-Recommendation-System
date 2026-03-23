import sys; sys.path.insert(0, '.')
from dotenv import load_dotenv; load_dotenv()
from core.database import SessionLocal
from core import models
from core.security import create_access_token
import requests

db = SessionLocal()
user = db.query(models.User).filter(models.User.user_id == 1).first()
db.close()

token = create_access_token({'user_id': user.user_id, 'username': user.username, 'email': user.email, 'is_admin': getattr(user, 'is_admin', False)})
headers = {'Authorization': 'Bearer ' + token}
r = requests.get('http://localhost:8000/user/1/assessment-history', headers=headers)
data = r.json()
print('Status:', r.status_code, 'total_attempts:', data.get('total_attempts'))
for item in data.get('history', []):
    aq_count = len(item.get('answered_questions', []))
    print('  attempt_id=' + str(item['attempt_id']) + ', taken_at=' + str(item.get('taken_at')) + ', aq=' + str(aq_count))
