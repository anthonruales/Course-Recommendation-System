#!/usr/bin/env python3
"""Phase 3: Technology cluster dedicated questions.
Covers: Software-Dev, Web-Dev, Mobile-Dev, AI-ML, Data-Analytics,
        Cloud-Systems, Cyber-Defense, Game-Dev, Hardware-Systems
"""
import re, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

QID = 504; OID = 4347
def nq(text, qtags, opts):
    global QID, OID
    options = []
    for (otext, otags) in opts:
        options.append({"option_id": OID, "option_text": otext, "trait_tags": otags})
        OID += 1
    q = {"question_id": QID, "question_text": text, "weight": 1.5, "trait_tags": qtags, "options": options}
    QID += 1
    return q

QS = []

# ===== SOFTWARE-DEV (2 on-topic) =====
for t, qt, o in [
("What software development practice interests you most?", {"Software-Dev": 0.9}, [
("Designing clean software architecture and patterns", {"Software-Dev": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.3}),
("Writing automated tests and CI/CD pipelines", {"Software-Dev": 0.9, "Technical-Skill": 0.5, "Analytical-Skill": 0.3}),
("Building APIs and backend service layers", {"Software-Dev": 1.0, "Web-Dev": 0.4, "Data-Analytics": 0.3}),
("Code review and mentoring junior developers", {"Software-Dev": 0.9, "People-Skill": 0.5, "Teaching-Ed": 0.3}),
("DevOps and deployment automation", {"Software-Dev": 0.9, "Cloud-Systems": 0.5, "Technical-Skill": 0.4}),
("Debugging complex production issues", {"Software-Dev": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.3})]),
("Which programming paradigm excites you most?", {"Software-Dev": 0.9, "Analytical-Skill": 0.3}, [
("Object-oriented design with inheritance and polymorphism", {"Software-Dev": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.3}),
("Functional programming with immutable data", {"Software-Dev": 0.9, "Analytical-Skill": 0.5, "Data-Analytics": 0.3}),
("Event-driven and reactive programming", {"Software-Dev": 0.9, "Web-Dev": 0.4, "Technical-Skill": 0.4}),
("Low-level systems programming close to hardware", {"Software-Dev": 0.9, "Hardware-Systems": 0.5, "Technical-Skill": 0.4}),
("Scripting and automation for productivity", {"Software-Dev": 0.8, "Technical-Skill": 0.5, "Admin-Skill": 0.3}),
("Domain-specific language design", {"Software-Dev": 1.0, "Analytical-Skill": 0.5, "Creative-Skill": 0.3})]),
("What software project type would you enjoy building?", {"Software-Dev": 0.9}, [
("Enterprise business management system", {"Software-Dev": 1.0, "Admin-Skill": 0.4, "Finance-Acct": 0.3}),
("Real-time communication platform", {"Software-Dev": 0.9, "Web-Dev": 0.5, "Cloud-Systems": 0.3}),
("Scientific simulation and modeling tool", {"Software-Dev": 0.9, "Data-Analytics": 0.5, "Lab-Research": 0.3}),
("Educational learning management system", {"Software-Dev": 0.9, "Teaching-Ed": 0.5, "Web-Dev": 0.3}),
("Healthcare patient records system", {"Software-Dev": 0.9, "Health-Admin": 0.5, "Patient-Care": 0.3}),
("Open-source developer tools and libraries", {"Software-Dev": 1.0, "Community-Serve": 0.4, "Technical-Skill": 0.3})]),
("What software engineering skill would you develop first?", {"Software-Dev": 0.9, "Technical-Skill": 0.3}, [
("Database design and query optimization", {"Software-Dev": 1.0, "Data-Analytics": 0.5, "Analytical-Skill": 0.3}),
("Algorithm design and data structures", {"Software-Dev": 1.0, "Analytical-Skill": 0.6, "Technical-Skill": 0.3}),
("Git version control and collaboration workflows", {"Software-Dev": 0.9, "Technical-Skill": 0.5, "People-Skill": 0.3}),
("Software security and vulnerability prevention", {"Software-Dev": 0.9, "Cyber-Defense": 0.5, "Technical-Skill": 0.4}),
("Performance profiling and optimization", {"Software-Dev": 0.9, "Analytical-Skill": 0.5, "Technical-Skill": 0.4}),
("Documentation and technical writing", {"Software-Dev": 0.8, "Admin-Skill": 0.4, "Teaching-Ed": 0.4})]),
("Where would you most want to work as a software developer?", {"Software-Dev": 0.9}, [
("Tech startup building innovative products", {"Software-Dev": 1.0, "Startup-Venture": 0.5, "Creative-Skill": 0.3}),
("Large enterprise IT department", {"Software-Dev": 0.9, "Admin-Skill": 0.4, "Industrial-Ops": 0.3}),
("BPO or outsourcing company in the Philippines", {"Software-Dev": 0.9, "People-Skill": 0.3, "Technical-Skill": 0.4}),
("Government digital transformation office", {"Software-Dev": 0.9, "Community-Serve": 0.4, "Admin-Skill": 0.3}),
("Remote freelance software consulting", {"Software-Dev": 0.9, "Startup-Venture": 0.4, "Finance-Acct": 0.3}),
("Research lab developing experimental tools", {"Software-Dev": 0.9, "Lab-Research": 0.5, "AI-ML": 0.3})]),
("What part of the software development lifecycle excites you?", {"Software-Dev": 0.9}, [
("Requirements gathering and system design", {"Software-Dev": 1.0, "Analytical-Skill": 0.5, "People-Skill": 0.3}),
("Writing production code and features", {"Software-Dev": 1.0, "Technical-Skill": 0.5, "Creative-Skill": 0.3}),
("Testing, QA, and quality assurance", {"Software-Dev": 0.9, "Analytical-Skill": 0.5, "Technical-Skill": 0.3}),
("Deployment, monitoring, and operations", {"Software-Dev": 0.9, "Cloud-Systems": 0.5, "Technical-Skill": 0.4}),
("Maintenance and legacy code modernization", {"Software-Dev": 0.9, "Analytical-Skill": 0.4, "Technical-Skill": 0.4}),
("Technical leadership and architecture decisions", {"Software-Dev": 1.0, "People-Skill": 0.4, "Analytical-Skill": 0.4})]),
("Which software development methodology appeals to you?", {"Software-Dev": 0.9, "People-Skill": 0.3}, [
("Agile Scrum with sprints and standups", {"Software-Dev": 1.0, "People-Skill": 0.5, "Admin-Skill": 0.3}),
("Kanban continuous flow and visual boards", {"Software-Dev": 0.9, "Analytical-Skill": 0.4, "Industrial-Ops": 0.3}),
("Test-driven development writing tests first", {"Software-Dev": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.3}),
("Pair programming and collaborative coding", {"Software-Dev": 0.9, "People-Skill": 0.5, "Teaching-Ed": 0.3}),
("Continuous integration and rapid deployment", {"Software-Dev": 0.9, "Cloud-Systems": 0.4, "Technical-Skill": 0.4}),
("Open-source community-driven development", {"Software-Dev": 0.9, "Community-Serve": 0.5, "People-Skill": 0.3})]),
]:
    QS.append(nq(t, qt, o))

# ===== WEB-DEV (7 on-topic) =====
for t, qt, o in [
("What type of website would you most enjoy building?", {"Web-Dev": 0.9}, [
("E-commerce platform with payment integration", {"Web-Dev": 1.0, "Finance-Acct": 0.4, "Software-Dev": 0.3}),
("Social media or community forum platform", {"Web-Dev": 0.9, "People-Skill": 0.3, "Software-Dev": 0.4}),
("Content management system for news or blogs", {"Web-Dev": 0.9, "Digital-Media": 0.5, "Creative-Skill": 0.3}),
("Interactive educational or e-learning site", {"Web-Dev": 0.9, "Teaching-Ed": 0.5, "Software-Dev": 0.3}),
("Government services portal for citizens", {"Web-Dev": 0.9, "Community-Serve": 0.4, "Admin-Skill": 0.3}),
("Portfolio or creative showcase website", {"Web-Dev": 0.9, "Visual-Design": 0.5, "Creative-Skill": 0.4})]),
("Which web development technology stack interests you?", {"Web-Dev": 0.9, "Technical-Skill": 0.3}, [
("React or Vue frontend with Node.js backend", {"Web-Dev": 1.0, "Software-Dev": 0.5, "Technical-Skill": 0.3}),
("Python Django or Flask full-stack development", {"Web-Dev": 0.9, "Software-Dev": 0.5, "Data-Analytics": 0.3}),
("PHP Laravel for rapid web application building", {"Web-Dev": 0.9, "Software-Dev": 0.5, "Technical-Skill": 0.3}),
("WordPress and CMS customization", {"Web-Dev": 0.8, "Digital-Media": 0.4, "Marketing-Sales": 0.3}),
("JAMstack with static site generators", {"Web-Dev": 0.9, "Software-Dev": 0.4, "Cloud-Systems": 0.3}),
("Ruby on Rails convention-over-configuration", {"Web-Dev": 1.0, "Software-Dev": 0.5, "Technical-Skill": 0.3})]),
("What web development challenge excites you most?", {"Web-Dev": 0.9}, [
("Responsive design that works on all screen sizes", {"Web-Dev": 1.0, "Visual-Design": 0.5, "Creative-Skill": 0.3}),
("Web performance optimization and fast load times", {"Web-Dev": 0.9, "Technical-Skill": 0.5, "Analytical-Skill": 0.3}),
("Web accessibility for users with disabilities", {"Web-Dev": 0.9, "Community-Serve": 0.4, "People-Skill": 0.3}),
("Real-time features with WebSockets", {"Web-Dev": 0.9, "Software-Dev": 0.5, "Technical-Skill": 0.4}),
("SEO optimization and search ranking", {"Web-Dev": 0.8, "Marketing-Sales": 0.5, "Data-Analytics": 0.3}),
("Progressive Web App offline capabilities", {"Web-Dev": 1.0, "Mobile-Dev": 0.5, "Technical-Skill": 0.3})]),
("Which web design approach appeals to you?", {"Web-Dev": 0.9, "Visual-Design": 0.3}, [
("Clean minimalist UI with modern typography", {"Web-Dev": 0.9, "Visual-Design": 0.6, "Creative-Skill": 0.3}),
("Data-driven dashboards with charts and graphs", {"Web-Dev": 0.9, "Data-Analytics": 0.5, "Analytical-Skill": 0.3}),
("Interactive animations and micro-interactions", {"Web-Dev": 0.9, "Animation-3D": 0.4, "Creative-Skill": 0.4}),
("User-centered design with A/B testing", {"Web-Dev": 0.9, "Analytical-Skill": 0.5, "Marketing-Sales": 0.3}),
("Component-based design systems", {"Web-Dev": 1.0, "Software-Dev": 0.5, "Visual-Design": 0.3}),
("Dark mode and accessibility-first theming", {"Web-Dev": 0.9, "Visual-Design": 0.5, "Community-Serve": 0.3})]),
("What backend web development area interests you?", {"Web-Dev": 0.9, "Software-Dev": 0.3}, [
("RESTful API design and documentation", {"Web-Dev": 1.0, "Software-Dev": 0.5, "Technical-Skill": 0.3}),
("Database schema design and optimization", {"Web-Dev": 0.9, "Data-Analytics": 0.5, "Software-Dev": 0.3}),
("Authentication and authorization systems", {"Web-Dev": 0.9, "Cyber-Defense": 0.5, "Software-Dev": 0.3}),
("Server-side rendering and caching strategies", {"Web-Dev": 0.9, "Software-Dev": 0.5, "Cloud-Systems": 0.3}),
("File upload and media processing pipelines", {"Web-Dev": 0.9, "Digital-Media": 0.4, "Cloud-Systems": 0.3}),
("Payment gateway and e-commerce integration", {"Web-Dev": 1.0, "Finance-Acct": 0.4, "Software-Dev": 0.3})]),
]:
    QS.append(nq(t, qt, o))

# ===== AI-ML (7 on-topic) =====
for t, qt, o in [
("Which AI/ML application area excites you most?", {"AI-ML": 0.9}, [
("Computer vision and image recognition", {"AI-ML": 1.0, "Software-Dev": 0.4, "Technical-Skill": 0.3}),
("Natural language processing and chatbots", {"AI-ML": 1.0, "Software-Dev": 0.4, "People-Skill": 0.3}),
("Recommendation systems for content or products", {"AI-ML": 0.9, "Data-Analytics": 0.5, "Marketing-Sales": 0.3}),
("Autonomous vehicles and robotics", {"AI-ML": 0.9, "Hardware-Systems": 0.5, "Mechanical-Design": 0.3}),
("Healthcare AI for diagnosis assistance", {"AI-ML": 0.9, "Patient-Care": 0.5, "Medical-Lab": 0.3}),
("Generative AI for creative content", {"AI-ML": 0.9, "Creative-Skill": 0.5, "Digital-Media": 0.3})]),
("What ML workflow step interests you most?", {"AI-ML": 0.9, "Data-Analytics": 0.3}, [
("Data collection and feature engineering", {"AI-ML": 0.9, "Data-Analytics": 0.6, "Analytical-Skill": 0.3}),
("Model architecture design and selection", {"AI-ML": 1.0, "Analytical-Skill": 0.5, "Software-Dev": 0.3}),
("Training and hyperparameter tuning", {"AI-ML": 1.0, "Technical-Skill": 0.5, "Analytical-Skill": 0.3}),
("Model evaluation and validation testing", {"AI-ML": 0.9, "Analytical-Skill": 0.5, "Data-Analytics": 0.4}),
("Production deployment and MLOps pipelines", {"AI-ML": 0.9, "Cloud-Systems": 0.5, "Software-Dev": 0.4}),
("Ethical AI and bias detection", {"AI-ML": 0.9, "Analytical-Skill": 0.4, "People-Skill": 0.4})]),
("Which AI research direction fascinates you?", {"AI-ML": 0.9}, [
("Deep learning and neural network architectures", {"AI-ML": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.3}),
("Reinforcement learning for autonomous agents", {"AI-ML": 1.0, "Software-Dev": 0.4, "Game-Dev": 0.3}),
("Transfer learning and few-shot adaptation", {"AI-ML": 0.9, "Analytical-Skill": 0.5, "Lab-Research": 0.3}),
("Explainable AI and interpretable models", {"AI-ML": 0.9, "Analytical-Skill": 0.5, "People-Skill": 0.3}),
("Edge AI running models on IoT devices", {"AI-ML": 0.9, "Hardware-Systems": 0.5, "Technical-Skill": 0.4}),
("Federated learning for privacy-preserving ML", {"AI-ML": 0.9, "Cyber-Defense": 0.4, "Data-Analytics": 0.3})]),
("Where would you apply AI in the Philippines?", {"AI-ML": 0.9}, [
("Agriculture crop disease detection", {"AI-ML": 0.9, "Agri-Nature": 0.5, "Field-Research": 0.3}),
("Traffic management and smart city planning", {"AI-ML": 0.9, "Civil-Build": 0.4, "Data-Analytics": 0.3}),
("Filipino language NLP and translation tools", {"AI-ML": 1.0, "Software-Dev": 0.4, "Community-Serve": 0.3}),
("Healthcare diagnostics for underserved areas", {"AI-ML": 0.9, "Patient-Care": 0.5, "Public-Health": 0.3}),
("Financial fraud detection for banks", {"AI-ML": 0.9, "Finance-Acct": 0.5, "Cyber-Defense": 0.3}),
("Disaster prediction and early warning systems", {"AI-ML": 0.9, "Environmental-Sci": 0.5, "Community-Serve": 0.3})]),
("What AI development tool would you master?", {"AI-ML": 0.9, "Technical-Skill": 0.3}, [
("TensorFlow or PyTorch deep learning frameworks", {"AI-ML": 1.0, "Software-Dev": 0.5, "Technical-Skill": 0.3}),
("Jupyter notebooks for research and experiments", {"AI-ML": 0.9, "Data-Analytics": 0.5, "Lab-Research": 0.3}),
("Cloud ML platforms like AWS SageMaker", {"AI-ML": 0.9, "Cloud-Systems": 0.5, "Technical-Skill": 0.4}),
("Computer vision libraries like OpenCV", {"AI-ML": 0.9, "Software-Dev": 0.5, "Digital-Media": 0.3}),
("NLP tools like spaCy or Hugging Face", {"AI-ML": 1.0, "Software-Dev": 0.4, "Data-Analytics": 0.3}),
("AutoML and no-code AI platforms", {"AI-ML": 0.8, "Technical-Skill": 0.4, "Analytical-Skill": 0.4})]),
]:
    QS.append(nq(t, qt, o))

# ===== DATA-ANALYTICS (8 on-topic) =====
for t, qt, o in [
("What type of data analysis project excites you?", {"Data-Analytics": 0.9}, [
("Customer behavior and market research analysis", {"Data-Analytics": 1.0, "Marketing-Sales": 0.5, "Analytical-Skill": 0.3}),
("Healthcare outcomes and patient data mining", {"Data-Analytics": 0.9, "Health-Admin": 0.5, "Public-Health": 0.3}),
("Financial risk modeling and forecasting", {"Data-Analytics": 0.9, "Finance-Acct": 0.5, "Analytical-Skill": 0.4}),
("Social media sentiment and trend analysis", {"Data-Analytics": 0.9, "Digital-Media": 0.5, "Marketing-Sales": 0.3}),
("Supply chain optimization and logistics", {"Data-Analytics": 0.9, "Industrial-Ops": 0.5, "Analytical-Skill": 0.3}),
("Environmental data and climate pattern analysis", {"Data-Analytics": 0.9, "Environmental-Sci": 0.5, "Field-Research": 0.3})]),
("Which data visualization tool would you master?", {"Data-Analytics": 0.9, "Technical-Skill": 0.3}, [
("Tableau interactive dashboards", {"Data-Analytics": 1.0, "Visual-Design": 0.4, "Technical-Skill": 0.3}),
("Python matplotlib and seaborn for research", {"Data-Analytics": 0.9, "Software-Dev": 0.5, "Lab-Research": 0.3}),
("Power BI for business intelligence reports", {"Data-Analytics": 0.9, "Finance-Acct": 0.4, "Admin-Skill": 0.3}),
("R and ggplot2 for statistical visualization", {"Data-Analytics": 1.0, "Analytical-Skill": 0.5, "Lab-Research": 0.3}),
("D3.js for custom web-based data graphics", {"Data-Analytics": 0.9, "Web-Dev": 0.5, "Creative-Skill": 0.3}),
("Geographic Information Systems (GIS) mapping", {"Data-Analytics": 0.9, "Field-Research": 0.5, "Environmental-Sci": 0.3})]),
("What data engineering challenge interests you?", {"Data-Analytics": 0.9, "Software-Dev": 0.3}, [
("Building data pipelines and ETL workflows", {"Data-Analytics": 1.0, "Software-Dev": 0.5, "Cloud-Systems": 0.3}),
("Data warehouse design and optimization", {"Data-Analytics": 0.9, "Software-Dev": 0.5, "Analytical-Skill": 0.3}),
("Real-time streaming data processing", {"Data-Analytics": 0.9, "Software-Dev": 0.5, "Technical-Skill": 0.4}),
("Data quality and cleansing automation", {"Data-Analytics": 0.9, "Analytical-Skill": 0.5, "Admin-Skill": 0.3}),
("Big data infrastructure management", {"Data-Analytics": 0.9, "Cloud-Systems": 0.5, "Hardware-Systems": 0.3}),
("Data governance and compliance frameworks", {"Data-Analytics": 0.8, "Legal-Practice": 0.4, "Admin-Skill": 0.4})]),
("Which statistical method would you study deeply?", {"Data-Analytics": 0.9, "Analytical-Skill": 0.3}, [
("Regression analysis for prediction", {"Data-Analytics": 1.0, "Analytical-Skill": 0.5, "Finance-Acct": 0.3}),
("Hypothesis testing and experimental design", {"Data-Analytics": 0.9, "Lab-Research": 0.5, "Analytical-Skill": 0.4}),
("Time series forecasting and trend analysis", {"Data-Analytics": 1.0, "Finance-Acct": 0.4, "Analytical-Skill": 0.3}),
("Clustering and segmentation techniques", {"Data-Analytics": 0.9, "AI-ML": 0.4, "Marketing-Sales": 0.3}),
("Bayesian inference and probabilistic models", {"Data-Analytics": 0.9, "AI-ML": 0.4, "Analytical-Skill": 0.5}),
("Survey design and sampling methodology", {"Data-Analytics": 0.9, "Public-Health": 0.4, "Field-Research": 0.3})]),
("Where would you apply data analytics skills?", {"Data-Analytics": 0.9}, [
("Business intelligence for Philippine companies", {"Data-Analytics": 1.0, "Finance-Acct": 0.4, "Admin-Skill": 0.3}),
("Public health disease monitoring and response", {"Data-Analytics": 0.9, "Public-Health": 0.5, "Community-Serve": 0.3}),
("E-commerce and digital marketing optimization", {"Data-Analytics": 0.9, "Marketing-Sales": 0.5, "Web-Dev": 0.3}),
("Sports analytics and team performance tracking", {"Data-Analytics": 0.9, "Sports-Ed": 0.5, "Physical-Skill": 0.3}),
("Government policy evaluation and budgeting", {"Data-Analytics": 0.9, "Finance-Acct": 0.4, "Community-Serve": 0.3}),
("Academic research data analysis", {"Data-Analytics": 0.9, "Lab-Research": 0.5, "Teaching-Ed": 0.3})]),
]:
    QS.append(nq(t, qt, o))

# ===== CLOUD-SYSTEMS (2 on-topic) =====
for t, qt, o in [
("Which cloud computing service model interests you?", {"Cloud-Systems": 0.9}, [
("Infrastructure as a Service (IaaS) management", {"Cloud-Systems": 1.0, "Hardware-Systems": 0.5, "Technical-Skill": 0.3}),
("Platform as a Service (PaaS) for app deployment", {"Cloud-Systems": 0.9, "Software-Dev": 0.5, "Technical-Skill": 0.3}),
("Serverless functions and event-driven computing", {"Cloud-Systems": 0.9, "Software-Dev": 0.5, "Analytical-Skill": 0.3}),
("Managed database and storage services", {"Cloud-Systems": 0.9, "Data-Analytics": 0.5, "Technical-Skill": 0.3}),
("Container orchestration with Kubernetes", {"Cloud-Systems": 1.0, "Software-Dev": 0.4, "Technical-Skill": 0.4}),
("Cloud networking and content delivery", {"Cloud-Systems": 0.9, "Hardware-Systems": 0.4, "Web-Dev": 0.3})]),
("What cloud architecture challenge excites you?", {"Cloud-Systems": 0.9, "Software-Dev": 0.3}, [
("Designing highly available distributed systems", {"Cloud-Systems": 1.0, "Software-Dev": 0.5, "Analytical-Skill": 0.3}),
("Auto-scaling for traffic spikes", {"Cloud-Systems": 0.9, "Technical-Skill": 0.5, "Analytical-Skill": 0.3}),
("Multi-region disaster recovery planning", {"Cloud-Systems": 0.9, "Admin-Skill": 0.4, "Analytical-Skill": 0.4}),
("Cost optimization and resource right-sizing", {"Cloud-Systems": 0.9, "Finance-Acct": 0.4, "Analytical-Skill": 0.4}),
("Microservices communication patterns", {"Cloud-Systems": 0.9, "Software-Dev": 0.5, "Technical-Skill": 0.3}),
("Infrastructure as code with Terraform", {"Cloud-Systems": 1.0, "Software-Dev": 0.5, "Technical-Skill": 0.3})]),
("Which cloud platform would you specialize in?", {"Cloud-Systems": 0.9, "Technical-Skill": 0.3}, [
("AWS cloud solutions architecture", {"Cloud-Systems": 1.0, "Technical-Skill": 0.5, "Software-Dev": 0.3}),
("Microsoft Azure enterprise integration", {"Cloud-Systems": 0.9, "Admin-Skill": 0.4, "Software-Dev": 0.3}),
("Google Cloud Platform data and AI services", {"Cloud-Systems": 0.9, "AI-ML": 0.5, "Data-Analytics": 0.3}),
("DigitalOcean for startup-scale deployments", {"Cloud-Systems": 0.9, "Startup-Venture": 0.4, "Software-Dev": 0.3}),
("Multi-cloud hybrid architecture design", {"Cloud-Systems": 1.0, "Analytical-Skill": 0.4, "Technical-Skill": 0.4}),
("Private cloud for Philippine government agencies", {"Cloud-Systems": 0.9, "Cyber-Defense": 0.4, "Admin-Skill": 0.3})]),
("What cloud security concern would you tackle?", {"Cloud-Systems": 0.9, "Cyber-Defense": 0.3}, [
("Identity and access management policies", {"Cloud-Systems": 0.9, "Cyber-Defense": 0.5, "Admin-Skill": 0.4}),
("Data encryption at rest and in transit", {"Cloud-Systems": 0.9, "Cyber-Defense": 0.5, "Technical-Skill": 0.3}),
("Network security groups and firewalls", {"Cloud-Systems": 1.0, "Cyber-Defense": 0.5, "Hardware-Systems": 0.3}),
("Compliance and audit logging", {"Cloud-Systems": 0.9, "Admin-Skill": 0.5, "Legal-Practice": 0.3}),
("Container security scanning", {"Cloud-Systems": 0.9, "Software-Dev": 0.4, "Cyber-Defense": 0.4}),
("DDoS protection and traffic filtering", {"Cloud-Systems": 1.0, "Cyber-Defense": 0.5, "Technical-Skill": 0.3})]),
("What cloud DevOps practice would you champion?", {"Cloud-Systems": 0.9, "Software-Dev": 0.3}, [
("CI/CD pipeline automation with cloud tools", {"Cloud-Systems": 1.0, "Software-Dev": 0.5, "Technical-Skill": 0.3}),
("Infrastructure monitoring and alerting", {"Cloud-Systems": 0.9, "Technical-Skill": 0.5, "Analytical-Skill": 0.3}),
("Log aggregation and observability platforms", {"Cloud-Systems": 0.9, "Data-Analytics": 0.4, "Technical-Skill": 0.4}),
("GitOps and declarative deployments", {"Cloud-Systems": 0.9, "Software-Dev": 0.5, "Technical-Skill": 0.3}),
("Chaos engineering and resilience testing", {"Cloud-Systems": 1.0, "Analytical-Skill": 0.4, "Technical-Skill": 0.4}),
("Service mesh for microservices management", {"Cloud-Systems": 0.9, "Software-Dev": 0.5, "Technical-Skill": 0.3})]),
]:
    QS.append(nq(t, qt, o))

# ===== CYBER-DEFENSE (5 on-topic) =====
for t, qt, o in [
("Which cybersecurity domain interests you most?", {"Cyber-Defense": 0.9}, [
("Network security and intrusion detection", {"Cyber-Defense": 1.0, "Hardware-Systems": 0.4, "Technical-Skill": 0.3}),
("Application security and code auditing", {"Cyber-Defense": 0.9, "Software-Dev": 0.5, "Analytical-Skill": 0.3}),
("Digital forensics and incident investigation", {"Cyber-Defense": 0.9, "Forensic-Sci": 0.5, "Law-Enforce": 0.3}),
("Ethical hacking and penetration testing", {"Cyber-Defense": 1.0, "Technical-Skill": 0.5, "Analytical-Skill": 0.3}),
("Security operations center (SOC) monitoring", {"Cyber-Defense": 0.9, "Technical-Skill": 0.5, "Admin-Skill": 0.3}),
("Governance, risk, and compliance management", {"Cyber-Defense": 0.8, "Legal-Practice": 0.5, "Admin-Skill": 0.4})]),
("What cybersecurity threat would you specialize in defending?", {"Cyber-Defense": 0.9}, [
("Ransomware and malware attacks", {"Cyber-Defense": 1.0, "Software-Dev": 0.4, "Technical-Skill": 0.3}),
("Phishing and social engineering scams", {"Cyber-Defense": 0.9, "People-Skill": 0.4, "Teaching-Ed": 0.3}),
("SQL injection and web application attacks", {"Cyber-Defense": 0.9, "Web-Dev": 0.5, "Software-Dev": 0.3}),
("Insider threats and data leaks", {"Cyber-Defense": 0.9, "Admin-Skill": 0.4, "Law-Enforce": 0.3}),
("DDoS and network-level attacks", {"Cyber-Defense": 1.0, "Hardware-Systems": 0.5, "Cloud-Systems": 0.3}),
("Zero-day vulnerabilities and exploits", {"Cyber-Defense": 1.0, "Software-Dev": 0.4, "Lab-Research": 0.3})]),
("What cybersecurity tool would you master?", {"Cyber-Defense": 0.9, "Technical-Skill": 0.3}, [
("Wireshark for network traffic analysis", {"Cyber-Defense": 1.0, "Hardware-Systems": 0.4, "Analytical-Skill": 0.3}),
("Kali Linux penetration testing toolkit", {"Cyber-Defense": 1.0, "Software-Dev": 0.4, "Technical-Skill": 0.4}),
("SIEM platforms for threat detection", {"Cyber-Defense": 0.9, "Data-Analytics": 0.5, "Admin-Skill": 0.3}),
("Vulnerability scanners like Nessus", {"Cyber-Defense": 0.9, "Technical-Skill": 0.5, "Analytical-Skill": 0.3}),
("Endpoint detection and response tools", {"Cyber-Defense": 0.9, "Hardware-Systems": 0.4, "Technical-Skill": 0.4}),
("Web application firewalls and proxies", {"Cyber-Defense": 0.9, "Web-Dev": 0.4, "Cloud-Systems": 0.3})]),
("Where would you practice cybersecurity?", {"Cyber-Defense": 0.9}, [
("DICT or Philippine government cyber unit", {"Cyber-Defense": 1.0, "Law-Enforce": 0.4, "Admin-Skill": 0.3}),
("Bank or financial institution security team", {"Cyber-Defense": 0.9, "Finance-Acct": 0.4, "Technical-Skill": 0.3}),
("Cybersecurity consulting firm", {"Cyber-Defense": 0.9, "Startup-Venture": 0.4, "People-Skill": 0.3}),
("Enterprise SOC for a large company", {"Cyber-Defense": 0.9, "Technical-Skill": 0.5, "Admin-Skill": 0.3}),
("Bug bounty and freelance security research", {"Cyber-Defense": 1.0, "Startup-Venture": 0.4, "Software-Dev": 0.3}),
("Cyber forensics and law enforcement support", {"Cyber-Defense": 0.9, "Forensic-Sci": 0.5, "Law-Enforce": 0.4})]),
("What cybersecurity awareness effort would you lead?", {"Cyber-Defense": 0.9, "Teaching-Ed": 0.3}, [
("Training employees on phishing prevention", {"Cyber-Defense": 0.9, "Teaching-Ed": 0.5, "People-Skill": 0.4}),
("Developing secure coding guidelines for devs", {"Cyber-Defense": 0.9, "Software-Dev": 0.5, "Teaching-Ed": 0.3}),
("Running capture-the-flag competitions", {"Cyber-Defense": 1.0, "Teaching-Ed": 0.4, "Technical-Skill": 0.3}),
("Building security incident response playbooks", {"Cyber-Defense": 0.9, "Admin-Skill": 0.5, "Analytical-Skill": 0.3}),
("Educating Filipinos on online safety", {"Cyber-Defense": 0.9, "Community-Serve": 0.5, "Teaching-Ed": 0.3}),
("Performing red team simulation exercises", {"Cyber-Defense": 1.0, "Technical-Skill": 0.5, "Analytical-Skill": 0.3})]),
]:
    QS.append(nq(t, qt, o))

# ===== MOBILE-DEV (6 on-topic) =====
for t, qt, o in [
("What type of mobile app would you build?", {"Mobile-Dev": 0.9}, [
("FinTech payment or banking app", {"Mobile-Dev": 1.0, "Finance-Acct": 0.4, "Software-Dev": 0.3}),
("Social networking or messaging platform", {"Mobile-Dev": 0.9, "People-Skill": 0.3, "Software-Dev": 0.4}),
("Health and fitness tracking app", {"Mobile-Dev": 0.9, "Patient-Care": 0.4, "Sports-Ed": 0.3}),
("Educational learning and quiz app", {"Mobile-Dev": 0.9, "Teaching-Ed": 0.5, "Software-Dev": 0.3}),
("Local government services app for Filipinos", {"Mobile-Dev": 0.9, "Community-Serve": 0.4, "Admin-Skill": 0.3}),
("Augmented reality entertainment app", {"Mobile-Dev": 0.9, "Game-Dev": 0.5, "Animation-3D": 0.3})]),
("Which mobile development framework interests you?", {"Mobile-Dev": 0.9, "Technical-Skill": 0.3}, [
("Flutter for cross-platform with Dart", {"Mobile-Dev": 1.0, "Software-Dev": 0.5, "Technical-Skill": 0.3}),
("React Native with JavaScript", {"Mobile-Dev": 0.9, "Web-Dev": 0.5, "Software-Dev": 0.4}),
("Native Android with Kotlin", {"Mobile-Dev": 1.0, "Software-Dev": 0.5, "Technical-Skill": 0.3}),
("Native iOS with Swift", {"Mobile-Dev": 1.0, "Software-Dev": 0.5, "Technical-Skill": 0.3}),
("Kotlin Multiplatform for shared logic", {"Mobile-Dev": 0.9, "Software-Dev": 0.5, "Technical-Skill": 0.4}),
("Progressive Web Apps as mobile alternative", {"Mobile-Dev": 0.8, "Web-Dev": 0.6, "Technical-Skill": 0.3})]),
("What mobile UX challenge interests you?", {"Mobile-Dev": 0.9, "Visual-Design": 0.3}, [
("Offline-first design for low-connectivity areas", {"Mobile-Dev": 1.0, "Community-Serve": 0.4, "Technical-Skill": 0.3}),
("Gesture-based navigation and touch interactions", {"Mobile-Dev": 0.9, "Visual-Design": 0.5, "Creative-Skill": 0.3}),
("Push notifications and user engagement", {"Mobile-Dev": 0.9, "Marketing-Sales": 0.4, "People-Skill": 0.3}),
("Accessibility for elderly and disabled users", {"Mobile-Dev": 0.9, "Community-Serve": 0.5, "People-Skill": 0.3}),
("Battery and data usage optimization", {"Mobile-Dev": 1.0, "Technical-Skill": 0.5, "Analytical-Skill": 0.3}),
("Multi-language support including Filipino", {"Mobile-Dev": 0.9, "Community-Serve": 0.4, "Software-Dev": 0.3})]),
("What mobile backend integration interests you?", {"Mobile-Dev": 0.9, "Cloud-Systems": 0.3}, [
("Firebase or Supabase real-time database", {"Mobile-Dev": 1.0, "Cloud-Systems": 0.5, "Software-Dev": 0.3}),
("RESTful and GraphQL API consumption", {"Mobile-Dev": 0.9, "Web-Dev": 0.5, "Software-Dev": 0.3}),
("Mobile payment gateway integration", {"Mobile-Dev": 0.9, "Finance-Acct": 0.4, "Technical-Skill": 0.3}),
("Local SQLite and device storage management", {"Mobile-Dev": 0.9, "Software-Dev": 0.5, "Data-Analytics": 0.3}),
("Cloud messaging and notification services", {"Mobile-Dev": 1.0, "Cloud-Systems": 0.4, "Technical-Skill": 0.3}),
("Mobile analytics and crash reporting", {"Mobile-Dev": 0.9, "Data-Analytics": 0.5, "Technical-Skill": 0.3})]),
]:
    QS.append(nq(t, qt, o))

# ===== GAME-DEV (11 on-topic) =====
for t, qt, o in [
("What game development role appeals to you?", {"Game-Dev": 0.9}, [
("Game programmer writing gameplay systems", {"Game-Dev": 1.0, "Software-Dev": 0.5, "Technical-Skill": 0.3}),
("Level designer building game worlds", {"Game-Dev": 0.9, "Spatial-Design": 0.5, "Creative-Skill": 0.4}),
("Game artist creating characters and assets", {"Game-Dev": 0.9, "Visual-Design": 0.5, "Animation-3D": 0.4}),
("Sound designer composing game audio", {"Game-Dev": 0.9, "Performing-Arts": 0.5, "Creative-Skill": 0.3}),
("Game designer crafting mechanics and rules", {"Game-Dev": 1.0, "Analytical-Skill": 0.5, "Creative-Skill": 0.3}),
("QA tester finding bugs and balance issues", {"Game-Dev": 0.8, "Analytical-Skill": 0.5, "Technical-Skill": 0.3})]),
("Which game engine would you specialize in?", {"Game-Dev": 0.9, "Technical-Skill": 0.3}, [
("Unity for cross-platform and mobile games", {"Game-Dev": 1.0, "Software-Dev": 0.5, "Mobile-Dev": 0.3}),
("Unreal Engine for AAA-quality graphics", {"Game-Dev": 1.0, "Animation-3D": 0.4, "Technical-Skill": 0.3}),
("Godot for open-source lightweight games", {"Game-Dev": 0.9, "Software-Dev": 0.5, "Community-Serve": 0.2}),
("RPG Maker for story-driven experiences", {"Game-Dev": 0.8, "Creative-Skill": 0.5, "Visual-Design": 0.3}),
("Custom engine built from scratch", {"Game-Dev": 0.9, "Software-Dev": 0.6, "Technical-Skill": 0.4}),
("Roblox Studio for social gaming platforms", {"Game-Dev": 0.8, "People-Skill": 0.4, "Digital-Media": 0.3})]),
("What game genre would you create?", {"Game-Dev": 0.9, "Creative-Skill": 0.3}, [
("RPG with deep story and character progression", {"Game-Dev": 1.0, "Creative-Skill": 0.5, "Visual-Design": 0.3}),
("Strategy game with complex resource management", {"Game-Dev": 0.9, "Analytical-Skill": 0.5, "Data-Analytics": 0.3}),
("Action game with precise controls and physics", {"Game-Dev": 1.0, "Software-Dev": 0.4, "Physical-Skill": 0.3}),
("Educational game teaching Filipino youth", {"Game-Dev": 0.9, "Teaching-Ed": 0.5, "Community-Serve": 0.3}),
("VR/AR immersive experience", {"Game-Dev": 0.9, "Animation-3D": 0.5, "Hardware-Systems": 0.3}),
("Mobile casual game for mass market", {"Game-Dev": 0.9, "Mobile-Dev": 0.5, "Marketing-Sales": 0.3})]),
]:
    QS.append(nq(t, qt, o))

# ===== HARDWARE-SYSTEMS (3 on-topic) =====
for t, qt, o in [
("What hardware systems area interests you most?", {"Hardware-Systems": 0.9}, [
("Computer networking and router configuration", {"Hardware-Systems": 1.0, "Technical-Skill": 0.5, "Cloud-Systems": 0.3}),
("Server rack setup and data center management", {"Hardware-Systems": 0.9, "Admin-Skill": 0.4, "Cloud-Systems": 0.4}),
("IoT sensors and embedded systems programming", {"Hardware-Systems": 0.9, "Software-Dev": 0.5, "Electrical-Power": 0.3}),
("PC assembly, troubleshooting, and repair", {"Hardware-Systems": 1.0, "Technical-Skill": 0.5, "Physical-Skill": 0.3}),
("Telecommunications and wireless systems", {"Hardware-Systems": 0.9, "Electrical-Power": 0.5, "Technical-Skill": 0.3}),
("Industrial control systems (SCADA/PLC)", {"Hardware-Systems": 0.9, "Industrial-Ops": 0.5, "Electrical-Power": 0.3})]),
("Which hardware certification would you pursue?", {"Hardware-Systems": 0.9, "Technical-Skill": 0.3}, [
("Cisco CCNA networking certification", {"Hardware-Systems": 1.0, "Cloud-Systems": 0.4, "Technical-Skill": 0.4}),
("CompTIA A+ for hardware support", {"Hardware-Systems": 1.0, "Technical-Skill": 0.5, "People-Skill": 0.3}),
("AWS Solutions Architect for cloud infra", {"Hardware-Systems": 0.8, "Cloud-Systems": 0.6, "Software-Dev": 0.3}),
("CompTIA Network+ for network administration", {"Hardware-Systems": 0.9, "Technical-Skill": 0.5, "Admin-Skill": 0.3}),
("Arduino/Raspberry Pi IoT specialization", {"Hardware-Systems": 0.9, "Electrical-Power": 0.4, "Software-Dev": 0.4}),
("VMware or Hyper-V virtualization expert", {"Hardware-Systems": 0.9, "Cloud-Systems": 0.5, "Technical-Skill": 0.3})]),
("What hardware troubleshooting scenario excites you?", {"Hardware-Systems": 0.9}, [
("Diagnosing network connectivity failures", {"Hardware-Systems": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.3}),
("Recovering data from failing storage drives", {"Hardware-Systems": 0.9, "Data-Analytics": 0.3, "Technical-Skill": 0.5}),
("Fixing overheating servers in a data center", {"Hardware-Systems": 0.9, "Physical-Skill": 0.4, "Technical-Skill": 0.4}),
("Setting up secure wireless access points", {"Hardware-Systems": 0.9, "Cyber-Defense": 0.5, "Technical-Skill": 0.3}),
("Configuring RAID and storage solutions", {"Hardware-Systems": 1.0, "Analytical-Skill": 0.4, "Cloud-Systems": 0.3}),
("Building custom workstations for specific tasks", {"Hardware-Systems": 0.9, "Mechanical-Design": 0.3, "Technical-Skill": 0.4})]),
("Where would you work in hardware systems?", {"Hardware-Systems": 0.9}, [
("Enterprise IT department managing infrastructure", {"Hardware-Systems": 1.0, "Admin-Skill": 0.4, "Technical-Skill": 0.3}),
("Internet service provider or telco company", {"Hardware-Systems": 0.9, "Electrical-Power": 0.4, "Technical-Skill": 0.3}),
("Data center operations and management", {"Hardware-Systems": 0.9, "Cloud-Systems": 0.5, "Admin-Skill": 0.3}),
("IoT development lab or smart factory", {"Hardware-Systems": 0.9, "Industrial-Ops": 0.5, "Software-Dev": 0.3}),
("IT consulting for small and medium businesses", {"Hardware-Systems": 0.9, "People-Skill": 0.4, "Startup-Venture": 0.3}),
("Computer repair and tech support shop", {"Hardware-Systems": 0.9, "People-Skill": 0.4, "Technical-Skill": 0.4})]),
]:
    QS.append(nq(t, qt, o))

# Build tree nodes
TREE = {}
for q in QS:
    qid = q["question_id"]
    tags = q["trait_tags"]
    branches = ["technology"]
    if any(t in tags for t in ["Mechanical-Design", "Electrical-Power", "Industrial-Ops"]):
        branches.append("engineering")
    if any(t in tags for t in ["Finance-Acct", "Marketing-Sales", "Admin-Skill"]):
        branches.append("business")
    if any(t in tags for t in ["Visual-Design", "Creative-Skill", "Animation-3D"]):
        branches.append("creative")
    if any(t in tags for t in ["Community-Serve", "Teaching-Ed"]):
        branches.append("education")
    TREE[qid] = {"level": 2, "weight": 1.5, "branches": branches}


def main():
    with open("questions_enhanced.py", "r", encoding="utf-8") as f:
        qe = f.read()

    first_id = QS[0]["question_id"]
    if f'"question_id": {first_id}' in qe:
        print(f"Q{first_id} already exists — skipping insertion.")
    else:
        insert_point = qe.rfind("\n]\n\nTRAIT_SECONDARY_MAP")
        if insert_point == -1:
            print("ERROR: Cannot find insertion point"); sys.exit(1)
        lines = ["    # ==================== TECHNOLOGY DEDICATED QUESTIONS ===================="]
        for q in QS:
            lines.append("    {")
            lines.append(f'        "question_id": {q["question_id"]},')
            lines.append(f'        "question_text": {repr(q["question_text"])},')
            lines.append(f'        "weight": {q["weight"]},')
            lines.append(f'        "trait_tags": {q["trait_tags"]},')
            lines.append('        "options": [')
            for opt in q["options"]:
                lines.append(f'            {{"option_id": {opt["option_id"]}, "option_text": {repr(opt["option_text"])}, "trait_tags": {opt["trait_tags"]}}},')
            lines.append("        ]")
            lines.append("    },")
        new_content = qe[:insert_point] + "\n" + "\n".join(lines) + qe[insert_point:]
        with open("questions_enhanced.py", "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Added {len(QS)} tech questions (Q{QS[0]['question_id']}-Q{QS[-1]['question_id']})")

    import importlib
    for m in ["questions_enhanced", "adaptive_assessment"]:
        if m in sys.modules: del sys.modules[m]
    from questions_enhanced import QUESTIONS_POOL_ENHANCED
    q_lookup = {q["question_id"]: q for q in QUESTIONS_POOL_ENHANCED}
    print(f"Total questions: {len(QUESTIONS_POOL_ENHANCED)}")

    with open("adaptive_assessment.py", "r", encoding="utf-8") as f:
        aa = f.read()

    new_ids = [q["question_id"] for q in QS]
    if f"{new_ids[0]}:" not in aa.split("QUESTION_TREE_NODES")[1][:20000]:
        tree_start = aa.find("QUESTION_TREE_NODES = {")
        brace_depth = 0; pos = tree_start + len("QUESTION_TREE_NODES = {")
        while pos < len(aa):
            if aa[pos] == '{': brace_depth += 1
            elif aa[pos] == '}':
                if brace_depth == 0:
                    insert_lines = [f'    {qid}: {{"level": {n["level"]}, "weight": {n["weight"]}, "branches": {n["branches"]}}},' for qid, n in TREE.items()]
                    aa = aa[:pos] + "\n" + "\n".join(insert_lines) + "\n" + aa[pos:]
                    print(f"Added {len(TREE)} tree nodes"); break
                brace_depth -= 1
            pos += 1

    tfm_match = re.search(r'TRAIT_FOLLOWUP_MAP\s*=\s*\{', aa)
    tfm_start = tfm_match.start()
    brace_depth = 0; pos = tfm_match.end()
    while pos < len(aa):
        if aa[pos] == '{': brace_depth += 1
        elif aa[pos] == '}':
            if brace_depth == 0: tfm_end = pos + 1; break
            brace_depth -= 1
        pos += 1
    local_ns = {}; exec(aa[tfm_start:tfm_end], {}, local_ns)
    tfm = local_ns["TRAIT_FOLLOWUP_MAP"]

    for q in QS:
        qid = q["question_id"]
        all_traits = set(q["trait_tags"].keys())
        for opt in q["options"]:
            for t2 in opt.get("trait_tags", {}).keys(): all_traits.add(t2)
        for trait in all_traits:
            if trait in tfm and qid not in tfm[trait]: tfm[trait].append(qid)

    def score(qid, trait):
        q = q_lookup.get(qid)
        if not q: return 0
        total = sum(o.get("trait_tags", {}).get(trait, 0) for o in q["options"])
        avg = total / max(len(q["options"]), 1)
        tmax = {}
        for o in q["options"]:
            for t2, v in o.get("trait_tags", {}).items():
                if t2 not in tmax or v > tmax[t2]: tmax[t2] = v
        return avg + (10.0 if tmax and max(tmax, key=tmax.get) == trait else 0)

    reordered = {}
    for trait, qids in sorted(tfm.items()):
        scored = [(qid, score(qid, trait)) for qid in qids]
        scored.sort(key=lambda x: -x[1])
        reordered[trait] = [qid for qid, _ in scored]

    tfm_lines = ["TRAIT_FOLLOWUP_MAP = {"]
    for trait in sorted(reordered.keys()):
        tfm_lines.append(f'    "{trait}": {reordered[trait]},')
    tfm_lines.append("}")
    aa = aa[:tfm_start] + "\n".join(tfm_lines) + aa[tfm_end:]

    with open("adaptive_assessment.py", "w", encoding="utf-8") as f:
        f.write(aa)
    print("Updated adaptive_assessment.py")

    for m in ["questions_enhanced", "adaptive_assessment"]:
        if m in sys.modules: del sys.modules[m]
    from adaptive_assessment import TRAIT_FOLLOWUP_MAP
    for t in ["Software-Dev", "Web-Dev", "Mobile-Dev", "AI-ML", "Data-Analytics",
              "Cloud-Systems", "Cyber-Defense", "Game-Dev", "Hardware-Systems"]:
        on = 0
        for qid in TRAIT_FOLLOWUP_MAP[t][:30]:
            q = q_lookup.get(qid)
            if not q: continue
            tmax = {}
            for o in q["options"]:
                for tr, v in o.get("trait_tags", {}).items():
                    if tr not in tmax or v > tmax[tr]: tmax[tr] = v
            if tmax and max(tmax, key=tmax.get) == t: on += 1
        print(f"  {t}: {on}/30 on-topic")


if __name__ == "__main__":
    main()
