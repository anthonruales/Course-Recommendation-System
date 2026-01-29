#!/usr/bin/env python3
"""Find and replace emoji with text in Python files"""
import re
import os

def fix_emojis_in_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Define emoji to text mapping - includes ALL emoji variations
    replacements = {
        '✓': '[OK]',
        '✅': '[OK]',
        '❌': '[ERROR]',
        '⚠️': '[WARN]',
        '💾': '[DATA]',
        '🌱': '[SEED]',
        '🧹': '[CLEAN]',
        '🎯': '[TARGET]',
        '📊': '[STATS]',
        '🔌': '[DB]',
        '🔍': '[DEBUG]',
        '📝': '[NOTE]',
        '📋': '[FORM]',
        '🚫': '[REJECT]',
        '🟢': '[OK_GREEN]',
        '🔵': '[BLUE]',
        '🔴': '[RED]',
        '🟡': '[YELLOW]',
        '🧠': '[BRAIN]',
    }
    
    original_content = content
    
    # Apply replacements
    for emoji, text in replacements.items():
        content = content.replace(emoji, text)
    
    # Also replace common Unicode escapes for emojis
    emoji_unicode = {
        '\\U0001f4cd': '[BRAIN]',  # 🧠
        '\\U0001f4cb': '[FORM]',   # 📋
        '\\U0001f535': '[BLUE]',   # 🔵
        '\\U0001f4dd': '[NOTE]',   # 📝
        '\\U0001f6ab': '[REJECT]', # 🚫
        '\\U0001f7e2': '[OK_GREEN]',  # 🟢
        '\\U0001f534': '[RED]',    # 🔴
        '\\U0001f7e1': '[YELLOW]', # 🟡
        '\\U0001f6ab': '[REJECT]', # 🚫
    }
    
    for escape_seq, text in emoji_unicode.items():
        content = content.replace(escape_seq, text)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")
    else:
        print(f"No changes needed: {filepath}")

if __name__ == "__main__":
    files = [
        'main.py',
        'database.py',
        'test_adaptive_rec.py',
        'recommendation_engine.py',
        'seed_data.py',
        'adaptive_assessment.py',
        'assessment_service.py',
    ]
    
    for f in files:
        try:
            fix_emojis_in_file(f)
        except Exception as e:
            print(f"Error processing {f}: {e}")
