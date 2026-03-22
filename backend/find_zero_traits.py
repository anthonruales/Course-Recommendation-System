"""Find and show the 0-trait options so we can fix them."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED

for q in QUESTIONS_POOL_ENHANCED:
    for opt in q['options']:
        if len(opt['trait_tags']) == 0:
            print(f"Q{q['question_id']} ({q['category']}): \"{q['question_text']}\"")
            print(f"  option {opt['option_id']}: \"{opt['option_text']}\"")
            print(f"  Other options in this question:")
            for o2 in q['options']:
                if o2['option_id'] != opt['option_id']:
                    print(f"    opt {o2['option_id']}: {len(o2['trait_tags'])} traits - {list(o2['trait_tags'].keys())[:3]}...")
            print()
