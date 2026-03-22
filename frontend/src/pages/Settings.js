import React, { useState, useEffect, useRef } from 'react';
import { authFetch, getTokenPayload } from '../api';
import Toast from '../components/Toast';
import NavBar from '../components/NavBar';

// Bad words filter list
const BAD_WORDS = [
  'fuck', 'shit', 'ass', 'bitch', 'damn', 'crap', 'bastard', 'dick', 'pussy', 'cock',
  'asshole', 'motherfucker', 'nigger', 'nigga', 'faggot', 'slut', 'whore', 'cunt',
  'retard', 'idiot', 'stupid', 'dumb', 'moron', 'loser', 'gay', 'homo', 'lesbian',
  'puta', 'gago', 'tangina', 'taena', 'bobo', 'tanga', 'putangina', 'ulol', 'lintik',
  'peste', 'punyeta', 'leche', 'hayop', 'animal', 'pokpok', 'malandi'
];

const capitalizeName = (name) => {
  if (!name) return '';
  return name.toLowerCase().split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
};

const containsBadWords = (name) => {
  if (!name) return false;
  const lowerName = name.toLowerCase().replace(/[^a-z\s]/g, '');
  const words = lowerName.split(/\s+/);
  return words.some(word => BAD_WORDS.includes(word));
};

// Predefined options for Academic Interests
const INTEREST_OPTIONS = [
  // Science & Research
  { id: 'science', label: 'Science & Research', category: 'Science' },
  { id: 'biology', label: 'Biology & Life Sciences', category: 'Science' },
  { id: 'chemistry', label: 'Chemistry', category: 'Science' },
  { id: 'physics', label: 'Physics', category: 'Science' },
  { id: 'environment', label: 'Environment & Nature', category: 'Science' },
  { id: 'earth_science', label: 'Earth Science & Geology', category: 'Science' },
  { id: 'marine_science', label: 'Marine Science & Oceanography', category: 'Science' },
  { id: 'biotechnology', label: 'Biotechnology & Genetics', category: 'Science' },
  { id: 'meteorology', label: 'Weather & Atmospheric Science', category: 'Science' },
  { id: 'statistics', label: 'Statistics & Probability', category: 'Science' },
  { id: 'food_science', label: 'Food Science & Safety', category: 'Science' },
  { id: 'forensic_science', label: 'Forensic Science', category: 'Science' },
  { id: 'env_planning', label: 'Environmental Planning & Sustainability', category: 'Science' },
  // Technology
  { id: 'programming', label: 'Programming & Coding', category: 'Technology' },
  { id: 'computer', label: 'Computers & IT', category: 'Technology' },
  { id: 'data', label: 'Data & Analytics', category: 'Technology' },
  { id: 'ai', label: 'AI & Machine Learning', category: 'Technology' },
  { id: 'cybersecurity', label: 'Cybersecurity', category: 'Technology' },
  { id: 'robotics', label: 'Robotics & Automation', category: 'Technology' },
  { id: 'game_dev', label: 'Game Development', category: 'Technology' },
  { id: 'web_tech', label: 'Web & Mobile Technologies', category: 'Technology' },
  { id: 'multimedia', label: 'Multimedia & Digital Entertainment', category: 'Technology' },
  { id: 'networking', label: 'Computer Networking', category: 'Technology' },
  { id: 'software_eng', label: 'Software Engineering', category: 'Technology' },
  { id: 'database', label: 'Database & Information Systems', category: 'Technology' },
  { id: 'health_info', label: 'Health Information Technology', category: 'Technology' },
  // Engineering
  { id: 'engineering', label: 'Engineering (General)', category: 'Engineering' },
  { id: 'mechanical', label: 'Mechanical Systems', category: 'Engineering' },
  { id: 'electrical', label: 'Electrical & Electronics', category: 'Engineering' },
  { id: 'civil', label: 'Civil & Construction', category: 'Engineering' },
  { id: 'architecture', label: 'Architecture & Interior Design', category: 'Engineering' },
  { id: 'industrial', label: 'Industrial & Manufacturing', category: 'Engineering' },
  { id: 'aeronautical', label: 'Aeronautical & Aerospace', category: 'Engineering' },
  { id: 'geodetic', label: 'Geodetic & Surveying', category: 'Engineering' },
  { id: 'landscape', label: 'Landscape Architecture', category: 'Engineering' },
  { id: 'industrial_design', label: 'Product & Industrial Design', category: 'Engineering' },
  { id: 'aircraft_maint', label: 'Aircraft Maintenance & Avionics', category: 'Engineering' },
  { id: 'marine_eng', label: 'Marine Engineering', category: 'Engineering' },
  // Business & Finance
  { id: 'business', label: 'Business & Entrepreneurship', category: 'Business' },
  { id: 'finance', label: 'Finance & Banking', category: 'Business' },
  { id: 'marketing', label: 'Marketing & Advertising', category: 'Business' },
  { id: 'accounting', label: 'Accounting', category: 'Business' },
  { id: 'economics', label: 'Economics', category: 'Business' },
  { id: 'management', label: 'Management & Administration', category: 'Business' },
  { id: 'real_estate', label: 'Real Estate & Property', category: 'Business' },
  { id: 'human_resource', label: 'Human Resource Management', category: 'Business' },
  { id: 'operations', label: 'Operations & Supply Chain', category: 'Business' },
  { id: 'customs', label: 'Customs & International Trade', category: 'Business' },
  { id: 'agribusiness', label: 'Agribusiness', category: 'Business' },
  { id: 'office_admin', label: 'Office Administration', category: 'Business' },
  { id: 'startup', label: 'Startup & Innovation', category: 'Business' },
  // Arts & Creative
  { id: 'art', label: 'Arts & Design', category: 'Arts' },
  { id: 'music', label: 'Music & Performance', category: 'Arts' },
  { id: 'film', label: 'Film & Media Production', category: 'Arts' },
  { id: 'writing', label: 'Writing & Literature', category: 'Arts' },
  { id: 'photography', label: 'Photography & Visual Arts', category: 'Arts' },
  { id: 'animation', label: 'Animation & Multimedia', category: 'Arts' },
  { id: 'fashion', label: 'Fashion & Textile Design', category: 'Arts' },
  { id: 'theater', label: 'Theater & Performing Arts', category: 'Arts' },
  { id: 'advertising_arts', label: 'Advertising & Graphic Arts', category: 'Arts' },
  { id: 'music_production', label: 'Music Production & Audio', category: 'Arts' },
  { id: 'fine_arts', label: 'Fine Arts & Painting', category: 'Arts' },
  { id: 'clothing_tech', label: 'Clothing & Textile Technology', category: 'Arts' },
  // Healthcare
  { id: 'medical', label: 'Medicine & Healthcare', category: 'Healthcare' },
  { id: 'nursing', label: 'Nursing & Patient Care', category: 'Healthcare' },
  { id: 'psychology', label: 'Psychology & Mental Health', category: 'Healthcare' },
  { id: 'pharmacy', label: 'Pharmacy & Pharmaceutical Science', category: 'Healthcare' },
  { id: 'physical_therapy', label: 'Physical Therapy & Rehabilitation', category: 'Healthcare' },
  { id: 'nutrition', label: 'Nutrition & Dietetics', category: 'Healthcare' },
  { id: 'medical_tech', label: 'Medical Technology & Lab Science', category: 'Healthcare' },
  { id: 'dentistry', label: 'Dentistry & Oral Health', category: 'Healthcare' },
  { id: 'occupational_therapy', label: 'Occupational Therapy', category: 'Healthcare' },
  { id: 'speech_therapy', label: 'Speech-Language Pathology', category: 'Healthcare' },
  { id: 'respiratory', label: 'Respiratory Therapy', category: 'Healthcare' },
  { id: 'radiology', label: 'Radiology & Imaging', category: 'Healthcare' },
  { id: 'optometry', label: 'Optometry & Vision Care', category: 'Healthcare' },
  { id: 'midwifery', label: 'Midwifery & Maternal Health', category: 'Healthcare' },
  { id: 'public_health', label: 'Public Health', category: 'Healthcare' },
  // Social & Humanities
  { id: 'education', label: 'Education & Teaching', category: 'Social' },
  { id: 'law', label: 'Law & Justice', category: 'Social' },
  { id: 'politics', label: 'Politics & Government', category: 'Social' },
  { id: 'social', label: 'Social Work & Community', category: 'Social' },
  { id: 'history', label: 'History & Culture', category: 'Social' },
  { id: 'communication', label: 'Communication & Journalism', category: 'Social' },
  { id: 'philosophy', label: 'Philosophy & Ethics', category: 'Social' },
  { id: 'criminology', label: 'Criminology & Public Safety', category: 'Social' },
  { id: 'early_childhood', label: 'Early Childhood Education', category: 'Social' },
  { id: 'special_education', label: 'Special Needs Education', category: 'Social' },
  { id: 'library_science', label: 'Library & Information Science', category: 'Social' },
  { id: 'public_admin', label: 'Public Administration', category: 'Social' },
  { id: 'intl_studies', label: 'International Studies & Diplomacy', category: 'Social' },
  { id: 'sociology', label: 'Sociology', category: 'Social' },
  { id: 'linguistics', label: 'Linguistics & Languages', category: 'Social' },
  { id: 'dev_communication', label: 'Development Communication', category: 'Social' },
  { id: 'community_dev', label: 'Community Development', category: 'Social' },
  { id: 'legal_mgmt', label: 'Legal Management', category: 'Social' },
  // Maritime & Transportation
  { id: 'maritime', label: 'Maritime & Seafaring', category: 'Maritime' },
  { id: 'aviation', label: 'Aviation & Aerospace', category: 'Maritime' },
  { id: 'logistics', label: 'Logistics & Supply Chain', category: 'Maritime' },
  { id: 'marine_transport', label: 'Marine Transportation & Navigation', category: 'Maritime' },
  // Others
  { id: 'sports', label: 'Sports & Fitness', category: 'Others' },
  { id: 'tourism', label: 'Tourism & Hospitality', category: 'Others' },
  { id: 'food', label: 'Culinary & Food Science', category: 'Others' },
  { id: 'agriculture', label: 'Agriculture & Farming', category: 'Others' },
  { id: 'veterinary', label: 'Veterinary & Animal Science', category: 'Others' },
  { id: 'military', label: 'Military & Defense', category: 'Others' },
  { id: 'forestry', label: 'Forestry & Natural Resources', category: 'Others' },
  { id: 'fisheries', label: 'Fisheries & Aquaculture', category: 'Others' },
  { id: 'hotel_mgmt', label: 'Hotel & Resort Management', category: 'Others' },
  { id: 'exercise_science', label: 'Exercise & Sports Science', category: 'Others' },
  { id: 'tvet', label: 'Technical-Vocational Training', category: 'Others' },
  { id: 'culinary_mgmt', label: 'Culinary Management', category: 'Others' },
];

// Predefined options for Skills
const SKILL_OPTIONS = [
  // Technical Skills
  { id: 'programming_skill', label: 'Programming / Coding', category: 'Technical' },
  { id: 'data_analysis', label: 'Data Analysis', category: 'Technical' },
  { id: 'web_development', label: 'Web Development', category: 'Technical' },
  { id: 'graphic_design', label: 'Graphic Design', category: 'Technical' },
  { id: 'video_editing', label: 'Video Editing', category: 'Technical' },
  { id: 'math_skills', label: 'Mathematics', category: 'Technical' },
  { id: 'laboratory', label: 'Laboratory Work', category: 'Technical' },
  { id: 'technical_writing', label: 'Technical Writing', category: 'Technical' },
  { id: 'electronics', label: 'Electronics / Circuit Design', category: 'Technical' },
  { id: 'drafting', label: 'Drafting / CAD / Blueprint Reading', category: 'Technical' },
  { id: 'accounting_skill', label: 'Bookkeeping & Accounting', category: 'Technical' },
  { id: 'networking_skill', label: 'Computer Networking & Troubleshooting', category: 'Technical' },
  { id: 'database_skill', label: 'Database Management', category: 'Technical' },
  { id: 'statistical_analysis', label: 'Statistical Analysis', category: 'Technical' },
  { id: 'surveying', label: 'Surveying & Mapping', category: 'Technical' },
  { id: 'lab_equipment', label: 'Medical / Lab Equipment Operation', category: 'Technical' },
  { id: 'machine_operation', label: 'Machine & Equipment Operation', category: 'Technical' },
  { id: 'quality_control', label: 'Quality Control & Testing', category: 'Technical' },
  { id: 'mobile_dev', label: 'Mobile App Development', category: 'Technical' },
  { id: 'ux_ui', label: 'UX / UI Design', category: 'Technical' },
  { id: 'audio_production', label: 'Audio / Sound Production', category: 'Technical' },
  { id: 'film_editing', label: 'Film Editing & Cinematography', category: 'Technical' },
  { id: 'navigation', label: 'Navigation & Seamanship', category: 'Technical' },
  { id: 'flight_ops', label: 'Flight Operations & Instruments', category: 'Technical' },
  { id: 'env_assessment', label: 'Environmental Impact Assessment', category: 'Technical' },
  // Communication Skills
  { id: 'public_speaking', label: 'Public Speaking', category: 'Communication' },
  { id: 'writing_skill', label: 'Writing & Composition', category: 'Communication' },
  { id: 'presentation', label: 'Presentation Skills', category: 'Communication' },
  { id: 'negotiation', label: 'Negotiation', category: 'Communication' },
  { id: 'foreign_language', label: 'Foreign Languages', category: 'Communication' },
  { id: 'filipino_language', label: 'Filipino / Tagalog Communication', category: 'Communication' },
  { id: 'social_media', label: 'Social Media & Digital Communication', category: 'Communication' },
  { id: 'journalism_skill', label: 'Journalism & News Writing', category: 'Communication' },
  { id: 'persuasion', label: 'Persuasion & Advocacy', category: 'Communication' },
  { id: 'interviewing', label: 'Interviewing & Questioning', category: 'Communication' },
  { id: 'report_writing', label: 'Report & Academic Writing', category: 'Communication' },
  { id: 'sign_language', label: 'Sign Language / Braille', category: 'Communication' },
  // Leadership & Management
  { id: 'leadership', label: 'Leadership', category: 'Leadership' },
  { id: 'project_management', label: 'Project Management', category: 'Leadership' },
  { id: 'team_management', label: 'Team Management', category: 'Leadership' },
  { id: 'decision_making', label: 'Decision Making', category: 'Leadership' },
  { id: 'planning', label: 'Planning & Organization', category: 'Leadership' },
  { id: 'time_management', label: 'Time Management', category: 'Leadership' },
  { id: 'event_management', label: 'Event Planning & Management', category: 'Leadership' },
  { id: 'budgeting', label: 'Budgeting & Financial Planning', category: 'Leadership' },
  { id: 'strategic_thinking', label: 'Strategic Thinking', category: 'Leadership' },
  { id: 'delegation', label: 'Delegation & Task Assignment', category: 'Leadership' },
  // Interpersonal Skills
  { id: 'teamwork', label: 'Teamwork & Collaboration', category: 'Interpersonal' },
  { id: 'empathy', label: 'Empathy & Compassion', category: 'Interpersonal' },
  { id: 'customer_service', label: 'Customer Service', category: 'Interpersonal' },
  { id: 'mentoring', label: 'Mentoring & Teaching', category: 'Interpersonal' },
  { id: 'conflict_resolution', label: 'Conflict Resolution', category: 'Interpersonal' },
  { id: 'counseling', label: 'Counseling & Active Listening', category: 'Interpersonal' },
  { id: 'patient_care', label: 'Patient Care & Bedside Manner', category: 'Interpersonal' },
  { id: 'cultural_sensitivity', label: 'Cultural Sensitivity & Diversity', category: 'Interpersonal' },
  { id: 'networking_people', label: 'Professional Networking', category: 'Interpersonal' },
  { id: 'child_interaction', label: 'Working with Children', category: 'Interpersonal' },
  { id: 'elderly_care', label: 'Working with Elderly / PWDs', category: 'Interpersonal' },
  // Analytical Skills
  { id: 'critical_thinking', label: 'Critical Thinking', category: 'Analytical' },
  { id: 'problem_solving', label: 'Problem Solving', category: 'Analytical' },
  { id: 'research', label: 'Research & Investigation', category: 'Analytical' },
  { id: 'attention_detail', label: 'Attention to Detail', category: 'Analytical' },
  { id: 'logical_reasoning', label: 'Logical Reasoning', category: 'Analytical' },
  { id: 'case_analysis', label: 'Case Study / Scenario Analysis', category: 'Analytical' },
  { id: 'scientific_method', label: 'Scientific Method & Experimentation', category: 'Analytical' },
  { id: 'financial_analysis', label: 'Financial Analysis & Forecasting', category: 'Analytical' },
  { id: 'risk_assessment', label: 'Risk Assessment & Management', category: 'Analytical' },
  { id: 'policy_analysis', label: 'Policy Analysis', category: 'Analytical' },
  // Creative Skills
  { id: 'creativity', label: 'Creativity & Innovation', category: 'Creative' },
  { id: 'artistic', label: 'Artistic Ability', category: 'Creative' },
  { id: 'music_skill', label: 'Musical Ability', category: 'Creative' },
  { id: 'storytelling', label: 'Storytelling', category: 'Creative' },
  { id: 'design_thinking', label: 'Design Thinking', category: 'Creative' },
  { id: 'photography_skill', label: 'Photography / Videography', category: 'Creative' },
  { id: 'acting', label: 'Acting & Stage Performance', category: 'Creative' },
  { id: 'illustration', label: 'Drawing & Illustration', category: 'Creative' },
  { id: 'fashion_design', label: 'Fashion & Apparel Design', category: 'Creative' },
  { id: 'animation_skill', label: 'Animation & Motion Graphics', category: 'Creative' },
  { id: 'interior_styling', label: 'Interior Styling & Space Design', category: 'Creative' },
  { id: 'content_creation', label: 'Content Creation & Blogging', category: 'Creative' },
  // Practical & Physical Skills
  { id: 'cooking', label: 'Cooking & Food Preparation', category: 'Practical' },
  { id: 'first_aid', label: 'First Aid & Basic Healthcare', category: 'Practical' },
  { id: 'sports_fitness', label: 'Sports & Physical Fitness', category: 'Practical' },
  { id: 'driving', label: 'Driving & Vehicle Operation', category: 'Practical' },
  { id: 'gardening', label: 'Gardening & Plant Care', category: 'Practical' },
  { id: 'repair_maintenance', label: 'Repair & Maintenance (Tools/Equipment)', category: 'Practical' },
  { id: 'swimming', label: 'Swimming & Water Safety', category: 'Practical' },
  { id: 'animal_handling', label: 'Animal Handling & Care', category: 'Practical' },
  { id: 'carpentry', label: 'Carpentry & Woodworking', category: 'Practical' },
  { id: 'farming', label: 'Farming & Crop Management', category: 'Practical' },
  { id: 'fishing', label: 'Fishing & Aquaculture', category: 'Practical' },
  { id: 'sewing', label: 'Sewing & Textile Craft', category: 'Practical' },
  { id: 'coaching', label: 'Sports Coaching & Training', category: 'Practical' },
];

function Settings({ formData = {}, setFormData, onSave, onBack, onViewProfile, onViewActivity }) {
  // Local draft state — edits stay here until Save is clicked
  const [localFormData, setLocalFormData] = useState(() => ({ ...formData }));
  const [activeSection, setActiveSection] = useState('profile');
  const [gwaError, setGwaError] = useState('');
  const [interestModalOpen, setInterestModalOpen] = useState(false);
  const [skillsModalOpen, setSkillsModalOpen] = useState(false);
  const [toast, setToast] = useState(null);
  const [profilePhoto, setProfilePhoto] = useState(null);
  const pendingPhotoRef = useRef({ changed: false, value: null });
  const [newEmail, setNewEmail] = useState('');
  const fileInputRef = useRef(null);
  
  // Load saved profile photo and email
  useEffect(() => {
    const userId = getTokenPayload()?.user_id;
    if (userId) {
      const savedPhoto = localStorage.getItem(`profilePhoto_${userId}`);
      if (savedPhoto) {
        setProfilePhoto(savedPhoto);
      }
    }
    const savedEmail = getTokenPayload()?.email;
    if (savedEmail) {
      setNewEmail(savedEmail);
    }
  }, []);
  
  const showToast = (message, type = 'info') => {
    setToast({ message, type });
  };
  
  // Handle profile photo upload (preview only, saved on Save Changes)
  const handlePhotoUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      if (file.size > 2 * 1024 * 1024) {
        showToast('Image size must be less than 2MB', 'error');
        return;
      }
      if (!file.type.startsWith('image/')) {
        showToast('Please upload an image file', 'error');
        return;
      }
      const reader = new FileReader();
      reader.onloadend = () => {
        const base64String = reader.result;
        setProfilePhoto(base64String);
        pendingPhotoRef.current = { changed: true, value: base64String };
        showToast('Photo selected — click Save Changes to apply', 'info');
      };
      reader.readAsDataURL(file);
    }
  };
  
  const removePhoto = () => {
    setProfilePhoto(null);
    pendingPhotoRef.current = { changed: true, value: null };
    showToast('Photo removed — click Save Changes to apply', 'info');
  };
  
  // Parse interests and skills from local draft
  const selectedInterests = localFormData?.interests 
    ? localFormData.interests.split(',').map(i => i.trim()).filter(i => i) 
    : [];
  const selectedSkills = localFormData?.skills 
    ? localFormData.skills.split(',').map(s => s.trim()).filter(s => s) 
    : [];
  
  const toggleInterest = (interestId) => {
    const current = [...selectedInterests];
    const index = current.indexOf(interestId);
    if (index > -1) {
      current.splice(index, 1);
    } else {
      current.push(interestId);
    }
    setLocalFormData(prev => ({ ...prev, interests: current.join(',') }));
  };
  
  const toggleSkill = (skillId) => {
    const current = [...selectedSkills];
    const index = current.indexOf(skillId);
    if (index > -1) {
      current.splice(index, 1);
    } else {
      current.push(skillId);
    }
    setLocalFormData(prev => ({ ...prev, skills: current.join(',') }));
  };
  
  const handleChange = (e) => {
    const { name, value } = e.target;
    
    if (name === 'fullname') {
      const capitalizedName = capitalizeName(value);
      setLocalFormData(prev => ({ ...prev, fullname: capitalizedName }));
      return;
    }
    
    if (name === 'age') {
      const ageValue = parseInt(value, 10);
      if (value && ageValue < 0) {
        setLocalFormData(prev => ({ ...prev, age: 0 }));
        return;
      }
    }

    if (name === 'gwa') {
      const gwaValue = parseFloat(value);
      if (value && gwaValue > 100) {
        setGwaError('GWA cannot exceed 100');
      } else if (value && gwaValue < 75) {
        setGwaError('GWA must be at least 75');
      } else {
        setGwaError('');
      }
    }
    
    setLocalFormData(prev => ({ ...prev, [name]: value }));
  };

  // Track original values (from parent prop, not local draft)
  const originalDataRef = useRef(null);
  
  useEffect(() => {
    if (formData && !originalDataRef.current) {
      originalDataRef.current = {
        fullname: formData.fullname || '',
        gwa: formData.gwa || '',
        strand: formData.strand || '',
        age: formData.age || '',
        gender: formData.gender || '',
        interests: formData.interests || '',
        skills: formData.skills || ''
      };
    }
  }, [formData]);

  const getChangedFields = () => {
    const original = originalDataRef.current || {};
    const changes = [];
    const fieldLabels = {
      fullname: 'Full Name',
      gwa: 'GWA',
      strand: 'SHS Strand',
      age: 'Age',
      gender: 'Gender',
      interests: 'Academic Interests',
      skills: 'Skills'
    };
    
    if ((localFormData.fullname || '') !== original.fullname) changes.push(fieldLabels.fullname);
    if ((localFormData.gwa || '') !== original.gwa) changes.push(fieldLabels.gwa);
    if ((localFormData.strand || '') !== original.strand) changes.push(fieldLabels.strand);
    if ((localFormData.age || '') !== original.age) changes.push(fieldLabels.age);
    if ((localFormData.gender || '') !== original.gender) changes.push(fieldLabels.gender);
    if (selectedInterests.join(', ') !== (original.interests || '')) changes.push(fieldLabels.interests);
    if (selectedSkills.join(', ') !== (original.skills || '')) changes.push(fieldLabels.skills);
    
    return changes;
  };

  const handleSaveProfile = async () => {
    const missing = [];
    if (!localFormData.gwa) missing.push('GWA');
    if (!localFormData.strand) missing.push('SHS Strand');
    if (selectedInterests.length === 0) missing.push('Academic Interests');
    if (selectedSkills.length === 0) missing.push('Skills');
    if (missing.length > 0) {
      showToast(`Please fill in: ${missing.join(', ')}`, 'warning');
      return;
    }
    
    if (localFormData.fullname) {
      if (containsBadWords(localFormData.fullname)) {
        showToast('Please use an appropriate name.', 'error');
        return;
      }
      if (!/^[a-zA-Z\s'.-]+$/.test(localFormData.fullname.trim())) {
        showToast('Name can only contain letters, spaces, hyphens, apostrophes, and dots.', 'error');
        return;
      }
    }
    
    const gwaValue = parseFloat(localFormData.gwa);
    if (gwaValue > 100) {
      showToast('GWA cannot exceed 100', 'error');
      return;
    }
    if (gwaValue < 75) {
      showToast('GWA must be at least 75', 'error');
      return;
    }
    
    const userId = getTokenPayload()?.user_id;
    if (!userId) {
      showToast('User ID not found. Please log in again.', 'error');
      return;
    }
    
    const changedFields = getChangedFields();
    const currentEmail = getTokenPayload()?.email || '';
    
    // Check if email was changed
    if (newEmail && newEmail !== currentEmail) {
      // Validate email format
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(newEmail)) {
        showToast('Invalid email format', 'error');
        return;
      }
      
      try {
        const emailRes = await authFetch(`${process.env.REACT_APP_API_URL}/user/${userId}/change-email`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ new_email: newEmail })
        });
        
        const emailData = await emailRes.json();
        
        if (!emailRes.ok) {
          showToast(emailData.detail || 'Failed to update email', 'error');
          return;
        }
        
        // Email updated in backend; will reflect in JWT on next login
        changedFields.push('Email');
      } catch (err) {
        console.error('Error changing email:', err);
        showToast('Failed to update email. Please try again.', 'error');
        return;
      }
    }
    
    authFetch(`${process.env.REACT_APP_API_URL}/user/${userId}/academic-info`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        gwa: parseFloat(localFormData.gwa),
        strand: localFormData.strand,
        fullname: localFormData.fullname || null,
        age: localFormData.age ? parseInt(localFormData.age) : null,
        gender: localFormData.gender || null,
        interests: selectedInterests.join(', ') || null,
        skills: selectedSkills.join(', ') || null
      })
    })
    .then(res => res.json())
    .then(data => {
      // Persist pending photo change to localStorage on save
      if (pendingPhotoRef.current.changed) {
        if (pendingPhotoRef.current.value) {
          localStorage.setItem(`profilePhoto_${userId}`, pendingPhotoRef.current.value);
        } else {
          localStorage.removeItem(`profilePhoto_${userId}`);
        }
        changedFields.push('Profile Photo');
        pendingPhotoRef.current = { changed: false, value: null };
      }
      // Update localStorage userName if fullname changed
      if (localFormData.fullname) {
        localStorage.setItem('userName', localFormData.fullname);
      }
      // Push local edits to parent state now that save succeeded
      setFormData({ ...localFormData });
      showToast('Profile updated successfully!', 'success');
      // Reset original data ref so change tracking resets
      originalDataRef.current = {
        fullname: localFormData.fullname || '',
        gwa: localFormData.gwa || '',
        strand: localFormData.strand || '',
        age: localFormData.age || '',
        gender: localFormData.gender || '',
        interests: selectedInterests.join(', ') || '',
        skills: selectedSkills.join(', ') || ''
      };
      onSave(changedFields);
    })
    .catch(err => {
      console.error('Error saving to backend:', err);
      showToast('Failed to save profile. Please try again.', 'error');
    });
  };

  const userName = localStorage.getItem('userName') || 'User';
    const userUsername = getTokenPayload()?.username || '';

  const settingsSections = [
    { id: 'profile', label: 'Profile Information', icon: '👤' },
  ];

  return (
    <div style={styles.pageWrapper}>
      {/* Background */}
      <div style={styles.bgGradient1}></div>
      <div style={styles.bgGradient2}></div>
      <div style={styles.bgGrid}></div>

      {/* TOP NAVIGATION BAR */}
      <NavBar
        activePage={null}
        onNavigate={(page) => {
          if (page === 'home') onBack();
          else if (page === 'profile') onViewProfile && onViewProfile();
          else if (page === 'activity') onViewActivity && onViewActivity();
        }}
      />

      {/* MAIN CONTENT */}
      <main className="settings-main-content" style={styles.mainContent}>
        <div style={styles.settingsHeader}>
          <h1 className="settings-page-title" style={styles.pageTitle}>
            <span style={styles.pageTitleIcon}>⚙️</span>
            Settings
          </h1>
          <p style={styles.pageSubtitle}>Manage your account settings and preferences</p>
        </div>

        <div className="settings-layout" style={styles.settingsLayout}>
          {/* Sidebar Navigation */}
          <div className="settings-sidebar" style={styles.sidebar}>
            {settingsSections.map(section => (
              <div
                key={section.id}
                onClick={() => setActiveSection(section.id)}
                className="settings-sidebar-nav"
                style={activeSection === section.id ? {
                  ...styles.sidebarItem,
                  ...styles.sidebarItemActive
                } : styles.sidebarItem}
              >
                <span style={styles.sidebarIcon}>{section.icon}</span>
                <span>{section.label}</span>
              </div>
            ))}
          </div>

          {/* Content Area */}
          <div style={styles.contentArea}>
            {/* Profile Information Section - Combined */}
            {activeSection === 'profile' && (
              <div style={styles.section}>
                <h2 style={styles.sectionTitle}>Profile Information</h2>
                <p style={styles.sectionDesc}>Update your personal details, academic info, and preferences</p>
                
                {/* Profile Photo */}
                <div className="settings-photo-section" style={styles.photoSection}>
                  <div style={styles.photoWrapper}>
                    {profilePhoto ? (
                      <img src={profilePhoto} alt="Profile" style={styles.photoImage} />
                    ) : (
                      <div style={styles.photoPlaceholder}>
                        <span style={styles.photoIcon}>{userName.charAt(0).toUpperCase()}</span>
                      </div>
                    )}
                  </div>
                  <div style={styles.photoInfo}>
                    <h3 style={styles.photoLabel}>Profile Photo</h3>
                    <p style={styles.photoHint}>JPG, PNG or GIF. Max 2MB.</p>
                    <div style={styles.photoActions}>
                      <input
                        type="file"
                        ref={fileInputRef}
                        onChange={handlePhotoUpload}
                        accept="image/*"
                        style={{ display: 'none' }}
                      />
                      <button onClick={() => fileInputRef.current?.click()} style={styles.uploadBtn}>
                        Change Photo
                      </button>
                      {profilePhoto && (
                        <button onClick={removePhoto} style={styles.removeBtn}>
                          Remove
                        </button>
                      )}
                    </div>
                  </div>
                </div>

                {/* Basic Info Subsection */}
                <div style={styles.subsectionTitle}>Basic Information</div>
                <div className="settings-form-grid" style={styles.formGrid}>
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Username</label>
                    <div style={styles.readOnlyField}>
                      <span style={styles.atSymbol}>@</span>
                      {userUsername}
                      <span style={styles.readOnlyBadge}>Cannot be changed</span>
                    </div>
                  </div>
                  
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Email Address</label>
                    <div style={styles.readOnlyField}>
                      {newEmail || 'No email set'}
                    </div>
                  </div>
                  
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Full Name</label>
                    <input
                      style={styles.input}
                      type="text"
                      name="fullname"
                      value={localFormData?.fullname || ''}
                      onChange={handleChange}
                      placeholder="Enter your full name"
                    />
                  </div>
                  
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Age</label>
                    <input
                      style={styles.input}
                      type="number"
                      name="age"
                      min="0"
                      value={localFormData?.age || ''}
                      onChange={handleChange}
                      onKeyDown={(e) => { if (e.key === '-' || e.key === '+') e.preventDefault(); }}
                      placeholder="Enter your age"
                    />
                  </div>
                  
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Gender</label>
                    <select
                      style={styles.input}
                      name="gender"
                      value={localFormData?.gender || ''}
                      onChange={handleChange}
                    >
                      <option value="" disabled>Select gender</option>
                      <option value="Male">Male</option>
                      <option value="Female">Female</option>
                    </select>
                  </div>
                </div>

                {/* Academic Details Subsection */}
                <div style={{...styles.subsectionTitle, marginTop: '32px'}}>Academic Details</div>
                <div className="settings-form-grid" style={styles.formGrid}>
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>SHS Strand</label>
                    <select
                      style={styles.input}
                      name="strand"
                      value={localFormData?.strand || ''}
                      onChange={handleChange}
                    >
                      <option value="" disabled>Select your strand</option>
                      <option value="STEM">STEM</option>
                      <option value="ABM">ABM</option>
                      <option value="HUMSS">HUMSS</option>
                      <option value="GAS">GAS</option>
                      <option value="TVL">TVL</option>
                      <option value="None">None</option>
                    </select>
                  </div>
                  
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>General Weighted Average (GWA)</label>
                    <input
                      style={{
                        ...styles.input,
                        ...(gwaError ? { borderColor: '#ef4444' } : {})
                      }}
                      type="number"
                      step="0.01"
                      min="75"
                      max="100"
                      name="gwa"
                      value={localFormData?.gwa || ''}
                      onChange={handleChange}
                      placeholder="75.00 - 100.00"
                    />
                    {gwaError ? (
                      <span style={styles.inputError}>{gwaError}</span>
                    ) : (
                      <span style={styles.inputHint}>Enter a value between 75 and 100</span>
                    )}
                  </div>
                </div>

                {/* Interests & Skills Subsection */}
                <div style={{...styles.subsectionTitle, marginTop: '32px'}}>Interests & Skills</div>
                
                <div style={styles.inputGroup}>
                  <label style={styles.label}>Academic Interests</label>
                  <div
                    onClick={() => setInterestModalOpen(true)}
                    style={styles.clickableField}
                  >
                    {selectedInterests.length > 0 ? (
                      <div style={styles.selectedTagsContainer}>
                        {selectedInterests.map(id => {
                          const interest = INTEREST_OPTIONS.find(o => o.id === id);
                          return (
                            <div key={id} style={styles.selectedTag}>
                              <span>{interest?.label}</span>
                              <span
                                onClick={(e) => {
                                  e.stopPropagation();
                                  toggleInterest(id);
                                }}
                                style={styles.tagRemoveBtn}
                              >
                                ×
                              </span>
                            </div>
                          );
                        })}
                      </div>
                    ) : (
                      <span style={styles.placeholderText}>Click to select your interests...</span>
                    )}
                  </div>
                </div>
                
                <div style={{...styles.inputGroup, marginTop: '20px'}}>
                  <label style={styles.label}>Technical & Soft Skills</label>
                  <div
                    onClick={() => setSkillsModalOpen(true)}
                    style={styles.clickableField}
                  >
                    {selectedSkills.length > 0 ? (
                      <div style={styles.selectedTagsContainer}>
                        {selectedSkills.map(id => {
                          const skill = SKILL_OPTIONS.find(o => o.id === id);
                          return (
                            <div key={id} style={styles.selectedTag}>
                              <span>{skill?.label}</span>
                              <span
                                onClick={(e) => {
                                  e.stopPropagation();
                                  toggleSkill(id);
                                }}
                                style={styles.tagRemoveBtn}
                              >
                                ×
                              </span>
                            </div>
                          );
                        })}
                      </div>
                    ) : (
                      <span style={styles.placeholderText}>Click to select your skills...</span>
                    )}
                  </div>
                </div>

                <div style={styles.sectionFooter}>
                  <button onClick={handleSaveProfile} style={styles.saveBtn}>
                    Save Changes
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      </main>

      {/* ACADEMIC INTERESTS MODAL */}
      {interestModalOpen && (
        <div style={styles.modalOverlay} onClick={() => setInterestModalOpen(false)}>
          <div style={styles.modalContent} onClick={(e) => e.stopPropagation()}>
            <div style={styles.modalHeader}>
              <h2 style={styles.modalTitle}>Select Academic Interests</h2>
              <button onClick={() => setInterestModalOpen(false)} style={styles.closeBtn}>✕</button>
            </div>
            <div style={styles.modalBody}>
              {Object.values(
                INTEREST_OPTIONS.reduce((acc, option) => {
                  if (!acc[option.category]) acc[option.category] = [];
                  acc[option.category].push(option);
                  return acc;
                }, {})
              ).map((categoryItems, idx) => (
                <div key={idx} style={styles.categorySection}>
                  <h3 style={styles.categoryTitle}>{categoryItems[0].category}</h3>
                  <div style={styles.tagsGrid}>
                    {categoryItems.map(option => (
                      <div
                        key={option.id}
                        onClick={() => toggleInterest(option.id)}
                        style={selectedInterests.includes(option.id) ? {
                          ...styles.modalTag,
                          ...styles.modalTagSelected
                        } : styles.modalTag}
                      >
                        <span>{option.label}</span>
                        {selectedInterests.includes(option.id) && (
                          <span style={styles.checkmark}>✓</span>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
            <div style={styles.modalFooter}>
              <button onClick={() => setInterestModalOpen(false)} style={styles.modalCloseBtn}>
                Done ({selectedInterests.length} selected)
              </button>
            </div>
          </div>
        </div>
      )}

      {/* SKILLS MODAL */}
      {skillsModalOpen && (
        <div style={styles.modalOverlay} onClick={() => setSkillsModalOpen(false)}>
          <div style={styles.modalContent} onClick={(e) => e.stopPropagation()}>
            <div style={styles.modalHeader}>
              <h2 style={styles.modalTitle}>Select Technical & Soft Skills</h2>
              <button onClick={() => setSkillsModalOpen(false)} style={styles.closeBtn}>✕</button>
            </div>
            <div style={styles.modalBody}>
              {Object.values(
                SKILL_OPTIONS.reduce((acc, option) => {
                  if (!acc[option.category]) acc[option.category] = [];
                  acc[option.category].push(option);
                  return acc;
                }, {})
              ).map((categoryItems, idx) => (
                <div key={idx} style={styles.categorySection}>
                  <h3 style={styles.categoryTitle}>{categoryItems[0].category}</h3>
                  <div style={styles.tagsGrid}>
                    {categoryItems.map(option => (
                      <div
                        key={option.id}
                        onClick={() => toggleSkill(option.id)}
                        style={selectedSkills.includes(option.id) ? {
                          ...styles.modalTag,
                          ...styles.modalTagSelected
                        } : styles.modalTag}
                      >
                        <span>{option.label}</span>
                        {selectedSkills.includes(option.id) && (
                          <span style={styles.checkmark}>✓</span>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
            <div style={styles.modalFooter}>
              <button onClick={() => setSkillsModalOpen(false)} style={styles.modalCloseBtn}>
                Done ({selectedSkills.length} selected)
              </button>
            </div>
          </div>
        </div>
      )}

      {toast && (
        <Toast
          message={toast.message}
          type={toast.type}
          onClose={() => setToast(null)}
        />
      )}
    </div>
  );
}

const styles = {
  pageWrapper: {
    minHeight: '100vh',
    background: 'linear-gradient(180deg, #030308 0%, #0a0a18 50%, #050510 100%)',
    color: '#f8fafc',
    position: 'relative',
    overflowX: 'clip',
  },
  bgGradient1: {
    position: 'fixed',
    top: '-30%',
    left: '-30%',
    width: '160%',
    height: '160%',
    background: 'radial-gradient(ellipse at 30% 30%, rgba(99, 102, 241, 0.12) 0%, transparent 60%)',
    pointerEvents: 'none'
  },
  bgGradient2: {
    position: 'fixed',
    bottom: '-30%',
    right: '-30%',
    width: '160%',
    height: '160%',
    background: 'radial-gradient(ellipse at 70% 70%, rgba(139, 92, 246, 0.1) 0%, transparent 60%)',
    pointerEvents: 'none'
  },
  bgGrid: {
    position: 'fixed',
    inset: 0,
    backgroundImage: 'linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px)',
    backgroundSize: '80px 80px',
    pointerEvents: 'none'
  },
  navbar: {
    position: 'sticky',
    top: 0,
    zIndex: 100,
    background: 'rgba(5, 5, 16, 0.85)',
    backdropFilter: 'blur(24px)',
    borderBottom: '1px solid rgba(255, 255, 255, 0.04)'
  },
  navContainer: {
    maxWidth: '1400px',
    margin: '0 auto',
    padding: '14px 40px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between'
  },
  navBrand: {
    display: 'flex',
    alignItems: 'center',
    gap: '14px'
  },
  navLogo: {
    width: '48px',
    height: '48px',
    objectFit: 'cover',
    borderRadius: '12px',
    background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%)',
    boxShadow: '0 0 20px rgba(99, 102, 241, 0.4)',
    border: '1px solid rgba(139, 92, 246, 0.3)'
  },
  navBrandName: {
    fontSize: '19px',
    fontWeight: '700',
    color: '#fff'
  },
  navLinks: {
    display: 'flex',
    alignItems: 'center',
    gap: '2px',
    background: 'rgba(255, 255, 255, 0.03)',
    padding: '5px',
    borderRadius: '14px',
    border: '1px solid rgba(255, 255, 255, 0.04)'
  },
  navLink: {
    padding: '10px 20px',
    borderRadius: '10px',
    color: '#8892a6',
    fontSize: '14px',
    fontWeight: '500',
    cursor: 'pointer',
    transition: 'all 0.25s ease'
  },
  navLinkActive: {
    background: 'rgba(255, 255, 255, 0.1)',
    color: '#fff'
  },
  navRight: {
    display: 'flex',
    alignItems: 'center'
  },
  backBtn: {
    padding: '10px 20px',
    background: 'rgba(239, 68, 68, 0.1)',
    border: '1px solid rgba(239, 68, 68, 0.2)',
    borderRadius: '10px',
    color: '#f87171',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer'
  },
  mainContent: {
    position: 'relative',
    zIndex: 1,
    maxWidth: '1100px',
    margin: '0 auto',
    padding: '40px'
  },
  settingsHeader: {
    marginBottom: '32px'
  },
  pageTitle: {
    fontSize: '32px',
    fontWeight: '700',
    color: '#f8fafc',
    margin: '0 0 8px 0',
    display: 'flex',
    alignItems: 'center',
    gap: '12px'
  },
  pageTitleIcon: {
    fontSize: '32px'
  },
  pageSubtitle: {
    fontSize: '15px',
    color: '#64748b',
    margin: 0
  },
  settingsLayout: {
    display: 'grid',
    gridTemplateColumns: '260px 1fr',
    gap: '32px'
  },
  sidebar: {
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255, 255, 255, 0.06)',
    borderRadius: '16px',
    padding: '12px',
    height: 'fit-content',
    position: 'sticky',
    top: '120px'
  },
  sidebarItem: {
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
    padding: '14px 16px',
    borderRadius: '10px',
    color: '#94a3b8',
    fontSize: '14px',
    fontWeight: '500',
    cursor: 'pointer',
    transition: 'all 0.2s ease'
  },
  sidebarItemActive: {
    background: 'rgba(99, 102, 241, 0.15)',
    color: '#a5b4fc'
  },
  sidebarIcon: {
    fontSize: '18px'
  },
  contentArea: {
    minHeight: '500px'
  },
  section: {
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255, 255, 255, 0.06)',
    borderRadius: '20px',
    padding: '32px'
  },
  sectionTitle: {
    fontSize: '20px',
    fontWeight: '700',
    color: '#f8fafc',
    margin: '0 0 8px 0'
  },
  sectionDesc: {
    fontSize: '14px',
    color: '#64748b',
    margin: '0 0 32px 0'
  },
  subsectionTitle: {
    fontSize: '15px',
    fontWeight: '600',
    color: '#94a3b8',
    marginBottom: '16px',
    paddingBottom: '8px',
    borderBottom: '1px solid rgba(255, 255, 255, 0.06)'
  },
  photoSection: {
    display: 'flex',
    alignItems: 'center',
    gap: '24px',
    padding: '24px',
    background: 'rgba(255, 255, 255, 0.02)',
    borderRadius: '16px',
    marginBottom: '32px'
  },
  photoWrapper: {
    width: '100px',
    height: '100px',
    borderRadius: '50%',
    overflow: 'hidden',
    border: '3px solid rgba(99, 102, 241, 0.3)',
    flexShrink: 0
  },
  photoImage: {
    width: '100%',
    height: '100%',
    objectFit: 'cover'
  },
  photoPlaceholder: {
    width: '100%',
    height: '100%',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)'
  },
  photoIcon: {
    fontSize: '36px',
    fontWeight: '700',
    color: 'white'
  },
  photoInfo: {
    flex: 1
  },
  photoLabel: {
    fontSize: '16px',
    fontWeight: '600',
    color: '#f8fafc',
    margin: '0 0 4px 0'
  },
  photoHint: {
    fontSize: '13px',
    color: '#64748b',
    margin: '0 0 12px 0'
  },
  photoActions: {
    display: 'flex',
    gap: '10px'
  },
  uploadBtn: {
    padding: '10px 20px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    border: 'none',
    borderRadius: '10px',
    color: 'white',
    fontSize: '13px',
    fontWeight: '600',
    cursor: 'pointer'
  },
  removeBtn: {
    padding: '10px 20px',
    background: 'rgba(239, 68, 68, 0.1)',
    border: '1px solid rgba(239, 68, 68, 0.2)',
    borderRadius: '10px',
    color: '#f87171',
    fontSize: '13px',
    fontWeight: '600',
    cursor: 'pointer'
  },
  formGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(2, 1fr)',
    gap: '24px'
  },
  inputGroup: {
    display: 'flex',
    flexDirection: 'column'
  },
  label: {
    fontSize: '13px',
    fontWeight: '600',
    color: '#94a3b8',
    marginBottom: '10px'
  },
  input: {
    padding: '14px 18px',
    background: 'rgba(30, 41, 59, 0.8)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '12px',
    color: '#f1f5f9',
    fontSize: '15px',
    outline: 'none',
    width: '100%',
    boxSizing: 'border-box'
  },
  inputHint: {
    fontSize: '12px',
    color: '#64748b',
    marginTop: '6px'
  },
  inputError: {
    fontSize: '12px',
    color: '#ef4444',
    marginTop: '6px'
  },
  readOnlyField: {
    padding: '14px 18px',
    background: 'rgba(255,255,255,0.03)',
    border: '1px solid rgba(255,255,255,0.04)',
    borderRadius: '12px',
    color: 'rgba(255,255,255,0.6)',
    fontSize: '15px',
    display: 'flex',
    alignItems: 'center',
    gap: '8px'
  },
  atSymbol: {
    color: 'rgba(139, 92, 246, 0.8)'
  },
  readOnlyBadge: {
    marginLeft: 'auto',
    fontSize: '11px',
    color: 'rgba(255,255,255,0.4)',
    background: 'rgba(255,255,255,0.05)',
    padding: '3px 8px',
    borderRadius: '4px'
  },
  clickableField: {
    padding: '14px 18px',
    background: 'rgba(30, 41, 59, 0.8)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '12px',
    cursor: 'pointer',
    minHeight: '56px',
    display: 'flex',
    alignItems: 'flex-start',
    flexWrap: 'wrap',
    gap: '10px'
  },
  placeholderText: {
    color: 'rgba(255,255,255,0.4)',
    fontSize: '15px'
  },
  selectedTagsContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '10px',
    width: '100%'
  },
  selectedTag: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    padding: '8px 14px',
    background: 'rgba(99, 102, 241, 0.15)',
    border: '1px solid rgba(99, 102, 241, 0.3)',
    borderRadius: '8px',
    color: '#a5b4fc',
    fontSize: '12px',
    fontWeight: '600'
  },
  tagRemoveBtn: {
    cursor: 'pointer',
    fontWeight: 'bold',
    fontSize: '16px',
    color: '#f87171'
  },
  infoBox: {
    display: 'flex',
    gap: '16px',
    padding: '20px',
    background: 'rgba(99, 102, 241, 0.08)',
    border: '1px solid rgba(99, 102, 241, 0.15)',
    borderRadius: '12px',
    marginTop: '24px'
  },
  infoIcon: {
    fontSize: '20px'
  },
  infoText: {
    fontSize: '13px',
    color: '#94a3b8',
    margin: '6px 0 0 0',
    lineHeight: 1.6
  },
  tipBox: {
    padding: '20px',
    background: 'rgba(16, 185, 129, 0.08)',
    border: '1px solid rgba(16, 185, 129, 0.15)',
    borderRadius: '12px',
    marginTop: '24px'
  },
  tipTitle: {
    fontSize: '14px',
    fontWeight: '600',
    color: '#10b981',
    margin: '0 0 12px 0'
  },
  tipList: {
    margin: 0,
    paddingLeft: '20px',
    fontSize: '13px',
    color: '#94a3b8',
    lineHeight: 1.8
  },
  passwordForm: {
    display: 'flex',
    flexDirection: 'column',
    gap: '20px',
    maxWidth: '400px'
  },
  passwordInputWrapper: {
    position: 'relative',
    display: 'flex',
    alignItems: 'center'
  },
  eyeBtn: {
    position: 'absolute',
    right: '14px',
    background: 'none',
    border: 'none',
    cursor: 'pointer',
    fontSize: '16px',
    padding: '4px'
  },
  errorBox: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    padding: '12px 16px',
    background: 'rgba(239, 68, 68, 0.1)',
    border: '1px solid rgba(239, 68, 68, 0.2)',
    borderRadius: '10px',
    color: '#f87171',
    fontSize: '13px'
  },
  sectionFooter: {
    marginTop: '32px',
    paddingTop: '24px',
    borderTop: '1px solid rgba(255,255,255,0.06)',
    display: 'flex',
    justifyContent: 'flex-end'
  },
  saveBtn: {
    padding: '14px 32px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    border: 'none',
    borderRadius: '12px',
    color: 'white',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    boxShadow: '0 4px 16px rgba(99, 102, 241, 0.25)'
  },
  // Modal styles
  modalOverlay: {
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    background: 'rgba(0, 0, 0, 0.7)',
    backdropFilter: 'blur(8px)',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 1000
  },
  modalContent: {
    background: 'rgba(15, 23, 42, 0.95)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255, 255, 255, 0.08)',
    borderRadius: '24px',
    width: '90%',
    maxWidth: '720px',
    maxHeight: '85vh',
    display: 'flex',
    flexDirection: 'column'
  },
  modalHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '28px 32px',
    borderBottom: '1px solid rgba(255, 255, 255, 0.06)'
  },
  modalTitle: {
    fontSize: '22px',
    fontWeight: '700',
    color: '#f8fafc',
    margin: 0
  },
  closeBtn: {
    background: 'none',
    border: 'none',
    color: '#64748b',
    fontSize: '24px',
    cursor: 'pointer'
  },
  modalBody: {
    flex: 1,
    overflowY: 'auto',
    padding: '28px 32px'
  },
  categorySection: {
    marginBottom: '32px'
  },
  categoryTitle: {
    fontSize: '12px',
    fontWeight: '700',
    color: '#a5b4fc',
    textTransform: 'uppercase',
    letterSpacing: '1px',
    margin: '0 0 16px 0'
  },
  tagsGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(170px, 1fr))',
    gap: '12px'
  },
  modalTag: {
    padding: '14px 16px',
    background: 'rgba(255, 255, 255, 0.03)',
    border: '2px solid rgba(255, 255, 255, 0.06)',
    borderRadius: '12px',
    cursor: 'pointer',
    fontSize: '13px',
    color: '#94a3b8',
    fontWeight: '500',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    gap: '10px',
    transition: 'all 0.2s ease'
  },
  modalTagSelected: {
    background: 'rgba(99, 102, 241, 0.15)',
    borderColor: 'rgba(99, 102, 241, 0.5)',
    color: '#a5b4fc'
  },
  checkmark: {
    color: '#10b981',
    fontSize: '16px',
    fontWeight: 'bold'
  },
  modalFooter: {
    padding: '24px 32px',
    borderTop: '1px solid rgba(255, 255, 255, 0.06)',
    display: 'flex',
    justifyContent: 'flex-end'
  },
  modalCloseBtn: {
    padding: '14px 28px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    border: 'none',
    borderRadius: '12px',
    color: 'white',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer'
  }
};

export default Settings;
