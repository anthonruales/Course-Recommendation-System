"""Sync questions_enhanced.py data into the database:
  - Update categories for all questions
  - Add missing options to questions that have < 6
  - Add any questions that exist in file but not DB
Then reset the adaptive engine cache.
"""
from database import SessionLocal
from models import Question, Option
from questions_enhanced import QUESTIONS_POOL_ENHANCED

def main():
    db = SessionLocal()
    
    # Build lookup of file questions
    file_qs = {q['question_id']: q for q in QUESTIONS_POOL_ENHANCED}
    
    # Get all DB questions
    db_qs = {q.question_id: q for q in db.query(Question).all()}
    
    # Get all DB options grouped by question
    db_opts = {}
    for opt in db.query(Option).all():
        db_opts.setdefault(opt.question_id, {})[opt.option_id] = opt
    
    updated_cats = 0
    added_opts = 0
    added_qs = 0
    updated_opts = 0
    
    for qid, fq in file_qs.items():
        if qid not in db_qs:
            # Question doesn't exist in DB - add it
            new_q = Question(
                question_id=qid,
                question_text=fq['question_text'],
                category=fq.get('category', '')
            )
            db.add(new_q)
            db.flush()
            added_qs += 1
            
            # Add all its options
            for opt in fq['options']:
                trait_tags = opt.get('trait_tags', {})
                # Get the primary trait (highest weight)
                primary_trait = max(trait_tags, key=trait_tags.get) if trait_tags else ''
                new_opt = Option(
                    option_id=opt['option_id'],
                    question_id=qid,
                    option_text=opt['option_text'],
                    trait_tag=primary_trait
                )
                db.add(new_opt)
                added_opts += 1
        else:
            # Update category if different
            db_q = db_qs[qid]
            file_cat = fq.get('category', '')
            if db_q.category != file_cat and file_cat:
                db_q.category = file_cat
                updated_cats += 1
            
            # Check and add missing options
            existing_opt_ids = set(db_opts.get(qid, {}).keys())
            for opt in fq['options']:
                opt_id = opt['option_id']
                if opt_id not in existing_opt_ids:
                    trait_tags = opt.get('trait_tags', {})
                    primary_trait = max(trait_tags, key=trait_tags.get) if trait_tags else ''
                    new_opt = Option(
                        option_id=opt_id,
                        question_id=qid,
                        option_text=opt['option_text'],
                        trait_tag=primary_trait
                    )
                    db.add(new_opt)
                    added_opts += 1
    
    db.commit()
    
    print(f"Updated categories: {updated_cats}")
    print(f"Added questions: {added_qs}")
    print(f"Added options: {added_opts}")
    
    # Verify
    total_qs = db.query(Question).count()
    null_cats = db.query(Question).filter(Question.category == None).count()
    
    from collections import Counter
    opt_counts = Counter()
    low = 0
    for q in db.query(Question).all():
        n = db.query(Option).filter(Option.question_id == q.question_id).count()
        opt_counts[n] += 1
        if n < 6:
            low += 1
    
    print(f"\nDB now has {total_qs} questions")
    print(f"NULL categories: {null_cats}")
    print(f"Questions with < 6 options: {low}")
    print(f"Option distribution: {dict(sorted(opt_counts.items()))}")
    
    db.close()

if __name__ == "__main__":
    main()
