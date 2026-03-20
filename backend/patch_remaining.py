#!/usr/bin/env python3
"""Phase 4: Engineering + Business + Creative + Science + Service clusters."""
import re, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

QID = 547; OID = 4605
def nq(text, qtags, opts, branches):
    global QID, OID
    options = []
    for (otext, otags) in opts:
        options.append({"option_id": OID, "option_text": otext, "trait_tags": otags})
        OID += 1
    q = {"question_id": QID, "question_text": text, "weight": 1.5, "trait_tags": qtags, "options": options}
    QID += 1
    return q, branches

ALL = []  # (question_dict, branches_list)

# ===== ENGINEERING: Civil-Build, Mechanical-Design, Electrical-Power, Environmental-Eng, Industrial-Ops =====
eng_qs = [
# Civil-Build
("What civil engineering project excites you most?", {"Civil-Build": 0.9}, [
("Bridge design and structural analysis", {"Civil-Build": 1.0, "Analytical-Skill": 0.5, "Mechanical-Design": 0.3}),
("High-rise building construction management", {"Civil-Build": 0.9, "Industrial-Ops": 0.5, "Admin-Skill": 0.3}),
("Road and highway infrastructure development", {"Civil-Build": 1.0, "Spatial-Design": 0.4, "Environmental-Eng": 0.3}),
("Water supply and drainage system design", {"Civil-Build": 0.9, "Environmental-Eng": 0.5, "Analytical-Skill": 0.3}),
("Earthquake-resistant building design", {"Civil-Build": 0.9, "Analytical-Skill": 0.5, "Mechanical-Design": 0.3}),
("Geotechnical investigation and soil analysis", {"Civil-Build": 0.9, "Lab-Research": 0.5, "Field-Research": 0.3})], ["engineering"]),
("What construction management task appeals to you?", {"Civil-Build": 0.9, "Industrial-Ops": 0.3}, [
("Project scheduling and timeline management", {"Civil-Build": 1.0, "Admin-Skill": 0.5, "Analytical-Skill": 0.3}),
("Cost estimation and budget control", {"Civil-Build": 0.9, "Finance-Acct": 0.5, "Analytical-Skill": 0.3}),
("Site safety and worker protection", {"Civil-Build": 0.9, "Physical-Skill": 0.4, "Law-Enforce": 0.3}),
("Quality control of materials and concrete", {"Civil-Build": 0.9, "Lab-Research": 0.5, "Analytical-Skill": 0.3}),
("Blueprint reading and structural drafting", {"Civil-Build": 1.0, "Spatial-Design": 0.5, "Technical-Skill": 0.3}),
("Equipment and heavy machinery coordination", {"Civil-Build": 0.9, "Mechanical-Design": 0.4, "Industrial-Ops": 0.4})], ["engineering"]),
("Where in the Philippines would you build?", {"Civil-Build": 0.9}, [
("Metro Manila infrastructure modernization", {"Civil-Build": 1.0, "Industrial-Ops": 0.4, "Admin-Skill": 0.3}),
("Provincial road and bridge networks", {"Civil-Build": 0.9, "Community-Serve": 0.4, "Environmental-Eng": 0.3}),
("Flood control and coastal protection projects", {"Civil-Build": 0.9, "Environmental-Eng": 0.5, "Environmental-Sci": 0.3}),
("Port and airport expansion", {"Civil-Build": 0.9, "Maritime-Sea": 0.3, "Industrial-Ops": 0.4}),
("Affordable housing for Filipino families", {"Civil-Build": 0.9, "Community-Serve": 0.5, "Spatial-Design": 0.3}),
("Railway and mass transit systems", {"Civil-Build": 1.0, "Mechanical-Design": 0.4, "Electrical-Power": 0.3})], ["engineering", "public_service"]),
("What structural engineering topic fascinates you?", {"Civil-Build": 0.9, "Analytical-Skill": 0.3}, [
("Reinforced concrete design and analysis", {"Civil-Build": 1.0, "Analytical-Skill": 0.5, "Lab-Research": 0.3}),
("Steel structure connections and fabrication", {"Civil-Build": 0.9, "Mechanical-Design": 0.5, "Industrial-Ops": 0.3}),
("Foundation design for challenging soil", {"Civil-Build": 0.9, "Field-Research": 0.5, "Analytical-Skill": 0.3}),
("Wind and earthquake load calculations", {"Civil-Build": 1.0, "Analytical-Skill": 0.5, "Data-Analytics": 0.3}),
("Pre-stressed and post-tensioned concrete", {"Civil-Build": 0.9, "Technical-Skill": 0.5, "Lab-Research": 0.3}),
("Inspection and retrofitting of old structures", {"Civil-Build": 0.9, "Analytical-Skill": 0.4, "Physical-Skill": 0.3})], ["engineering", "science"]),
("What civil engineering technology interests you?", {"Civil-Build": 0.9, "Technical-Skill": 0.3}, [
("BIM (Building Information Modeling) software", {"Civil-Build": 1.0, "Software-Dev": 0.4, "Spatial-Design": 0.3}),
("GPS and surveying equipment operation", {"Civil-Build": 0.9, "Field-Research": 0.5, "Technical-Skill": 0.3}),
("CAD drafting and 3D structural modeling", {"Civil-Build": 0.9, "Spatial-Design": 0.5, "Technical-Skill": 0.4}),
("Drone surveying for site mapping", {"Civil-Build": 0.9, "Technical-Skill": 0.5, "Field-Research": 0.3}),
("Structural analysis simulation software", {"Civil-Build": 1.0, "Software-Dev": 0.4, "Analytical-Skill": 0.3}),
("Material testing laboratory equipment", {"Civil-Build": 0.9, "Lab-Research": 0.5, "Technical-Skill": 0.3})], ["engineering", "technology"]),
# Mechanical-Design
("What mechanical engineering work excites you?", {"Mechanical-Design": 0.9}, [
("Machine and mechanism design", {"Mechanical-Design": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.3}),
("HVAC and refrigeration systems", {"Mechanical-Design": 0.9, "Electrical-Power": 0.4, "Technical-Skill": 0.3}),
("Automotive engine and powertrain engineering", {"Mechanical-Design": 0.9, "Technical-Skill": 0.5, "Physical-Skill": 0.3}),
("Manufacturing process and tooling design", {"Mechanical-Design": 0.9, "Industrial-Ops": 0.5, "Technical-Skill": 0.3}),
("Robotics and automation systems", {"Mechanical-Design": 0.9, "Software-Dev": 0.4, "AI-ML": 0.3}),
("Piping and fluid system design", {"Mechanical-Design": 1.0, "Civil-Build": 0.3, "Analytical-Skill": 0.3})], ["engineering"]),
("Which CAD/design tool would you master?", {"Mechanical-Design": 0.9, "Technical-Skill": 0.3}, [
("SolidWorks for 3D mechanical parts", {"Mechanical-Design": 1.0, "Technical-Skill": 0.5, "Spatial-Design": 0.3}),
("AutoCAD for technical drawing and layouts", {"Mechanical-Design": 0.9, "Spatial-Design": 0.5, "Civil-Build": 0.3}),
("ANSYS for finite element stress analysis", {"Mechanical-Design": 1.0, "Analytical-Skill": 0.5, "Software-Dev": 0.3}),
("Fusion 360 for prototyping and 3D printing", {"Mechanical-Design": 0.9, "Creative-Skill": 0.4, "Technical-Skill": 0.4}),
("MATLAB for engineering calculations", {"Mechanical-Design": 0.8, "Analytical-Skill": 0.5, "Software-Dev": 0.4}),
("CNC programming for precision manufacturing", {"Mechanical-Design": 0.9, "Industrial-Ops": 0.5, "Technical-Skill": 0.4})], ["engineering", "technology"]),
("What mechanical systems problem would you solve?", {"Mechanical-Design": 0.9}, [
("Reducing friction and wear in machine parts", {"Mechanical-Design": 1.0, "Lab-Research": 0.4, "Analytical-Skill": 0.3}),
("Improving energy efficiency in engines", {"Mechanical-Design": 0.9, "Environmental-Eng": 0.4, "Analytical-Skill": 0.3}),
("Designing safer vehicle crash structures", {"Mechanical-Design": 0.9, "Analytical-Skill": 0.5, "Physical-Skill": 0.3}),
("Vibration control in rotating machinery", {"Mechanical-Design": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.3}),
("Heat transfer optimization in cooling systems", {"Mechanical-Design": 0.9, "Electrical-Power": 0.4, "Lab-Research": 0.3}),
("Designing prosthetics and medical devices", {"Mechanical-Design": 0.9, "Rehab-Therapy": 0.5, "Patient-Care": 0.3})], ["engineering", "science"]),
("What type of manufacturing fascinates you?", {"Mechanical-Design": 0.9, "Industrial-Ops": 0.3}, [
("CNC machining and precision fabrication", {"Mechanical-Design": 1.0, "Industrial-Ops": 0.5, "Technical-Skill": 0.3}),
("3D printing and additive manufacturing", {"Mechanical-Design": 0.9, "Creative-Skill": 0.4, "Technical-Skill": 0.4}),
("Welding and metal joining techniques", {"Mechanical-Design": 0.9, "Physical-Skill": 0.5, "Technical-Skill": 0.3}),
("Quality control and dimensional inspection", {"Mechanical-Design": 0.9, "Analytical-Skill": 0.5, "Lab-Research": 0.3}),
("Assembly line design and automation", {"Mechanical-Design": 0.9, "Industrial-Ops": 0.5, "Software-Dev": 0.3}),
("Casting and forging processes", {"Mechanical-Design": 1.0, "Physical-Skill": 0.4, "Industrial-Ops": 0.3})], ["engineering"]),
# Electrical-Power
("What electrical engineering area excites you?", {"Electrical-Power": 0.9}, [
("Power generation and distribution systems", {"Electrical-Power": 1.0, "Industrial-Ops": 0.4, "Technical-Skill": 0.3}),
("Renewable energy: solar and wind systems", {"Electrical-Power": 0.9, "Environmental-Eng": 0.5, "Technical-Skill": 0.3}),
("Motor control and industrial automation", {"Electrical-Power": 0.9, "Mechanical-Design": 0.4, "Industrial-Ops": 0.4}),
("Electronics circuit design and PCB layout", {"Electrical-Power": 0.9, "Hardware-Systems": 0.5, "Technical-Skill": 0.4}),
("Building electrical wiring and installation", {"Electrical-Power": 1.0, "Civil-Build": 0.3, "Physical-Skill": 0.3}),
("Smart grid and energy management", {"Electrical-Power": 0.9, "Data-Analytics": 0.4, "Software-Dev": 0.3})], ["engineering"]),
("What power systems challenge would you solve?", {"Electrical-Power": 0.9, "Environmental-Eng": 0.3}, [
("Reducing power outages in Philippine provinces", {"Electrical-Power": 1.0, "Community-Serve": 0.4, "Technical-Skill": 0.3}),
("Integrating solar panels into the power grid", {"Electrical-Power": 0.9, "Environmental-Eng": 0.5, "Technical-Skill": 0.3}),
("Improving transformer and substation efficiency", {"Electrical-Power": 1.0, "Analytical-Skill": 0.4, "Technical-Skill": 0.3}),
("Designing electrical systems for tall buildings", {"Electrical-Power": 0.9, "Civil-Build": 0.5, "Spatial-Design": 0.3}),
("Electric vehicle charging infrastructure", {"Electrical-Power": 0.9, "Mechanical-Design": 0.4, "Environmental-Eng": 0.3}),
("Energy storage and battery technology", {"Electrical-Power": 0.9, "Lab-Research": 0.5, "Environmental-Eng": 0.3})], ["engineering", "science"]),
("Which electrical tool or instrument would you master?", {"Electrical-Power": 0.9, "Technical-Skill": 0.4}, [
("Oscilloscope for signal analysis", {"Electrical-Power": 1.0, "Technical-Skill": 0.5, "Analytical-Skill": 0.3}),
("PLC programming for factory automation", {"Electrical-Power": 0.9, "Software-Dev": 0.4, "Industrial-Ops": 0.4}),
("Power system simulation software (ETAP)", {"Electrical-Power": 1.0, "Software-Dev": 0.4, "Analytical-Skill": 0.3}),
("Circuit simulation with SPICE or Proteus", {"Electrical-Power": 0.9, "Software-Dev": 0.4, "Hardware-Systems": 0.4}),
("Multimeter and clamp meter diagnostics", {"Electrical-Power": 0.9, "Physical-Skill": 0.4, "Technical-Skill": 0.4}),
("AutoCAD Electrical for wiring diagrams", {"Electrical-Power": 0.9, "Spatial-Design": 0.4, "Technical-Skill": 0.3})], ["engineering", "technology"]),
("What electrical engineering career path appeals to you?", {"Electrical-Power": 0.9}, [
("Power plant operations engineer", {"Electrical-Power": 1.0, "Industrial-Ops": 0.5, "Technical-Skill": 0.3}),
("Building systems electrical designer", {"Electrical-Power": 0.9, "Civil-Build": 0.4, "Spatial-Design": 0.3}),
("Renewable energy project developer", {"Electrical-Power": 0.9, "Environmental-Eng": 0.5, "Startup-Venture": 0.3}),
("Electronics engineer in manufacturing", {"Electrical-Power": 0.9, "Industrial-Ops": 0.4, "Hardware-Systems": 0.3}),
("Meralco or utility company engineer", {"Electrical-Power": 1.0, "Community-Serve": 0.3, "Technical-Skill": 0.3}),
("Electrical safety inspector", {"Electrical-Power": 0.9, "Law-Enforce": 0.4, "Analytical-Skill": 0.3})], ["engineering"]),
# Environmental-Eng
("What environmental engineering project motivates you?", {"Environmental-Eng": 0.9}, [
("Wastewater treatment plant design", {"Environmental-Eng": 1.0, "Civil-Build": 0.4, "Lab-Research": 0.3}),
("Air quality monitoring and pollution control", {"Environmental-Eng": 0.9, "Environmental-Sci": 0.5, "Data-Analytics": 0.3}),
("Solid waste management and recycling systems", {"Environmental-Eng": 0.9, "Industrial-Ops": 0.4, "Community-Serve": 0.3}),
("Clean water supply for rural communities", {"Environmental-Eng": 0.9, "Civil-Build": 0.4, "Community-Serve": 0.4}),
("Renewable energy integration projects", {"Environmental-Eng": 0.9, "Electrical-Power": 0.5, "Technical-Skill": 0.3}),
("Environmental impact assessment for developments", {"Environmental-Eng": 1.0, "Analytical-Skill": 0.4, "Legal-Practice": 0.3})], ["engineering", "science"]),
("What environmental remediation method interests you?", {"Environmental-Eng": 0.9, "Lab-Research": 0.3}, [
("Bioremediation using microorganisms", {"Environmental-Eng": 0.9, "Lab-Research": 0.5, "Environmental-Sci": 0.4}),
("Soil contamination cleanup technology", {"Environmental-Eng": 1.0, "Field-Research": 0.4, "Technical-Skill": 0.3}),
("Membrane filtration for water purification", {"Environmental-Eng": 0.9, "Technical-Skill": 0.5, "Lab-Research": 0.3}),
("Industrial emission scrubbing systems", {"Environmental-Eng": 0.9, "Industrial-Ops": 0.4, "Mechanical-Design": 0.3}),
("Constructed wetlands for natural treatment", {"Environmental-Eng": 1.0, "Environmental-Sci": 0.5, "Agri-Nature": 0.3}),
("Landfill engineering and gas capture", {"Environmental-Eng": 0.9, "Civil-Build": 0.4, "Technical-Skill": 0.3})], ["engineering", "science"]),
("Where would you work as an environmental engineer?", {"Environmental-Eng": 0.9}, [
("DENR environmental compliance and monitoring", {"Environmental-Eng": 1.0, "Law-Enforce": 0.4, "Admin-Skill": 0.3}),
("Water district treatment operations", {"Environmental-Eng": 0.9, "Industrial-Ops": 0.4, "Community-Serve": 0.3}),
("Mining company environmental management", {"Environmental-Eng": 0.9, "Field-Research": 0.4, "Industrial-Ops": 0.3}),
("Environmental consulting firm", {"Environmental-Eng": 0.9, "Startup-Venture": 0.4, "Analytical-Skill": 0.3}),
("NGO working on climate change adaptation", {"Environmental-Eng": 0.9, "Community-Serve": 0.5, "Environmental-Sci": 0.3}),
("Manufacturing company sustainability officer", {"Environmental-Eng": 0.9, "Industrial-Ops": 0.5, "Admin-Skill": 0.3})], ["engineering", "public_service"]),
("What green technology fascinates you?", {"Environmental-Eng": 0.9, "Technical-Skill": 0.3}, [
("Solar panel efficiency and installation", {"Environmental-Eng": 0.9, "Electrical-Power": 0.5, "Technical-Skill": 0.3}),
("Electric vehicle and battery technology", {"Environmental-Eng": 0.9, "Mechanical-Design": 0.4, "Electrical-Power": 0.4}),
("Green building design and LEED certification", {"Environmental-Eng": 1.0, "Civil-Build": 0.5, "Spatial-Design": 0.3}),
("Rainwater harvesting and greywater recycling", {"Environmental-Eng": 0.9, "Civil-Build": 0.4, "Community-Serve": 0.3}),
("Biogas and biomass energy from waste", {"Environmental-Eng": 0.9, "Agri-Nature": 0.4, "Lab-Research": 0.3}),
("Smart environmental monitoring sensors", {"Environmental-Eng": 1.0, "Hardware-Systems": 0.4, "Data-Analytics": 0.3})], ["engineering", "technology"]),
# Industrial-Ops
("What industrial operations role suits you?", {"Industrial-Ops": 0.9}, [
("Production planning and scheduling", {"Industrial-Ops": 1.0, "Analytical-Skill": 0.5, "Admin-Skill": 0.3}),
("Quality assurance and control systems", {"Industrial-Ops": 0.9, "Analytical-Skill": 0.5, "Lab-Research": 0.3}),
("Supply chain and logistics management", {"Industrial-Ops": 0.9, "Admin-Skill": 0.5, "Finance-Acct": 0.3}),
("Workplace safety and ergonomics", {"Industrial-Ops": 0.9, "Physical-Skill": 0.4, "Rehab-Therapy": 0.3}),
("Lean manufacturing and process improvement", {"Industrial-Ops": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.3}),
("Facility layout and plant design", {"Industrial-Ops": 0.9, "Spatial-Design": 0.4, "Mechanical-Design": 0.3})], ["engineering", "business"]),
("What manufacturing improvement method interests you?", {"Industrial-Ops": 0.9, "Analytical-Skill": 0.3}, [
("Six Sigma quality and defect reduction", {"Industrial-Ops": 1.0, "Analytical-Skill": 0.5, "Data-Analytics": 0.3}),
("Kaizen continuous improvement culture", {"Industrial-Ops": 0.9, "People-Skill": 0.4, "Admin-Skill": 0.3}),
("5S workplace organization method", {"Industrial-Ops": 0.9, "Admin-Skill": 0.5, "Physical-Skill": 0.3}),
("Value stream mapping for waste elimination", {"Industrial-Ops": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.3}),
("Statistical process control with data", {"Industrial-Ops": 0.9, "Data-Analytics": 0.5, "Analytical-Skill": 0.3}),
("Automation and Industry 4.0 integration", {"Industrial-Ops": 0.9, "Software-Dev": 0.4, "Hardware-Systems": 0.3})], ["engineering", "technology"]),
("Which industry would you optimize operations for?", {"Industrial-Ops": 0.9}, [
("Semiconductor manufacturing in the Philippines", {"Industrial-Ops": 1.0, "Technical-Skill": 0.4, "Hardware-Systems": 0.3}),
("Food and beverage production", {"Industrial-Ops": 0.9, "Food-Science": 0.5, "Nutrition-Diet": 0.2}),
("Pharmaceutical manufacturing", {"Industrial-Ops": 0.9, "Pharmacy": 0.5, "Lab-Research": 0.3}),
("Automotive parts and assembly", {"Industrial-Ops": 0.9, "Mechanical-Design": 0.5, "Technical-Skill": 0.3}),
("Logistics and warehouse operations", {"Industrial-Ops": 1.0, "Admin-Skill": 0.4, "Data-Analytics": 0.3}),
("Construction material production", {"Industrial-Ops": 0.9, "Civil-Build": 0.5, "Mechanical-Design": 0.3})], ["engineering", "business"]),
("What operations research technique would you apply?", {"Industrial-Ops": 0.9, "Data-Analytics": 0.3}, [
("Linear programming for resource allocation", {"Industrial-Ops": 1.0, "Analytical-Skill": 0.5, "Data-Analytics": 0.4}),
("Simulation modeling for process design", {"Industrial-Ops": 0.9, "Software-Dev": 0.4, "Analytical-Skill": 0.4}),
("Queuing theory for service optimization", {"Industrial-Ops": 0.9, "Analytical-Skill": 0.5, "Data-Analytics": 0.3}),
("Inventory management and EOQ modeling", {"Industrial-Ops": 1.0, "Finance-Acct": 0.4, "Analytical-Skill": 0.3}),
("Network analysis for project scheduling", {"Industrial-Ops": 0.9, "Analytical-Skill": 0.5, "Admin-Skill": 0.3}),
("Forecasting demand with time series data", {"Industrial-Ops": 0.9, "Data-Analytics": 0.5, "AI-ML": 0.3})], ["engineering", "technology"]),
]
for t, qt, o, br in eng_qs:
    ALL.append(nq(t, qt, o, br))

# ===== BUSINESS: Finance-Acct, Marketing-Sales, HR-Management, Admin-Skill, Startup-Venture =====
biz_qs = [
("What financial management area interests you?", {"Finance-Acct": 0.9}, [
("Corporate accounting and financial reporting", {"Finance-Acct": 1.0, "Admin-Skill": 0.4, "Analytical-Skill": 0.3}),
("Investment analysis and portfolio management", {"Finance-Acct": 0.9, "Analytical-Skill": 0.5, "Data-Analytics": 0.3}),
("Tax compliance and planning", {"Finance-Acct": 0.9, "Legal-Practice": 0.4, "Analytical-Skill": 0.3}),
("Auditing and internal controls", {"Finance-Acct": 1.0, "Analytical-Skill": 0.5, "Law-Enforce": 0.3}),
("Budgeting and cost management", {"Finance-Acct": 0.9, "Admin-Skill": 0.5, "Industrial-Ops": 0.3}),
("Banking and loan evaluation", {"Finance-Acct": 0.9, "People-Skill": 0.4, "Analytical-Skill": 0.3})], ["business"]),
("Which accounting technology would you learn?", {"Finance-Acct": 0.9, "Technical-Skill": 0.3}, [
("QuickBooks or SAP accounting software", {"Finance-Acct": 1.0, "Software-Dev": 0.3, "Admin-Skill": 0.3}),
("Excel advanced financial modeling", {"Finance-Acct": 0.9, "Data-Analytics": 0.5, "Analytical-Skill": 0.3}),
("Blockchain and cryptocurrency accounting", {"Finance-Acct": 0.8, "Technical-Skill": 0.5, "Software-Dev": 0.4}),
("Data analytics for financial insights", {"Finance-Acct": 0.9, "Data-Analytics": 0.5, "AI-ML": 0.3}),
("Payroll and HR information systems", {"Finance-Acct": 0.9, "HR-Management": 0.4, "Admin-Skill": 0.4}),
("Automated audit and compliance tools", {"Finance-Acct": 0.9, "Software-Dev": 0.4, "Analytical-Skill": 0.3})], ["business", "technology"]),
("What financial career path appeals to you?", {"Finance-Acct": 0.9}, [
("CPA in a major audit firm", {"Finance-Acct": 1.0, "Analytical-Skill": 0.5, "Legal-Practice": 0.3}),
("CFO of a growing Philippine company", {"Finance-Acct": 0.9, "Admin-Skill": 0.5, "People-Skill": 0.3}),
("Stock market analyst or trader", {"Finance-Acct": 0.9, "Data-Analytics": 0.5, "Analytical-Skill": 0.3}),
("Government BIR tax examiner", {"Finance-Acct": 0.9, "Law-Enforce": 0.4, "Legal-Practice": 0.3}),
("Financial planner for families", {"Finance-Acct": 0.9, "People-Skill": 0.5, "Counseling": 0.3}),
("Fintech startup founder", {"Finance-Acct": 0.8, "Startup-Venture": 0.5, "Software-Dev": 0.3})], ["business"]),
("What financial analysis task excites you?", {"Finance-Acct": 0.9, "Analytical-Skill": 0.3}, [
("Ratio analysis to assess company health", {"Finance-Acct": 1.0, "Analytical-Skill": 0.5, "Data-Analytics": 0.3}),
("Cash flow forecasting and projections", {"Finance-Acct": 0.9, "Data-Analytics": 0.5, "Analytical-Skill": 0.3}),
("Variance analysis comparing budget vs actual", {"Finance-Acct": 0.9, "Analytical-Skill": 0.5, "Admin-Skill": 0.3}),
("Loan risk assessment and credit scoring", {"Finance-Acct": 0.9, "Data-Analytics": 0.4, "Analytical-Skill": 0.4}),
("Merger and acquisition valuation", {"Finance-Acct": 1.0, "Analytical-Skill": 0.5, "Legal-Practice": 0.3}),
("Cost-benefit analysis for projects", {"Finance-Acct": 0.9, "Analytical-Skill": 0.5, "Industrial-Ops": 0.3})], ["business"]),
# Marketing-Sales
("What marketing strategy interests you most?", {"Marketing-Sales": 0.9}, [
("Social media marketing and content creation", {"Marketing-Sales": 1.0, "Digital-Media": 0.5, "Creative-Skill": 0.3}),
("Brand strategy and positioning", {"Marketing-Sales": 0.9, "Creative-Skill": 0.5, "Analytical-Skill": 0.3}),
("Data-driven digital advertising campaigns", {"Marketing-Sales": 0.9, "Data-Analytics": 0.5, "Technical-Skill": 0.3}),
("Customer relationship management (CRM)", {"Marketing-Sales": 0.9, "People-Skill": 0.5, "Admin-Skill": 0.3}),
("Product launch and go-to-market planning", {"Marketing-Sales": 1.0, "Admin-Skill": 0.4, "Startup-Venture": 0.3}),
("Influencer marketing and partnerships", {"Marketing-Sales": 0.9, "People-Skill": 0.5, "Digital-Media": 0.4})], ["business"]),
("Which marketing analytics method would you use?", {"Marketing-Sales": 0.9, "Data-Analytics": 0.3}, [
("Customer segmentation and persona building", {"Marketing-Sales": 1.0, "Data-Analytics": 0.5, "Analytical-Skill": 0.3}),
("A/B testing and conversion optimization", {"Marketing-Sales": 0.9, "Data-Analytics": 0.5, "Web-Dev": 0.3}),
("SEO and keyword research analysis", {"Marketing-Sales": 0.9, "Web-Dev": 0.4, "Data-Analytics": 0.4}),
("Social media engagement analytics", {"Marketing-Sales": 0.9, "Digital-Media": 0.5, "Data-Analytics": 0.3}),
("Sales funnel tracking and optimization", {"Marketing-Sales": 1.0, "Data-Analytics": 0.5, "Analytical-Skill": 0.3}),
("Market research surveys and focus groups", {"Marketing-Sales": 0.9, "People-Skill": 0.4, "Analytical-Skill": 0.4})], ["business", "technology"]),
("What sales approach suits you best?", {"Marketing-Sales": 0.9, "People-Skill": 0.3}, [
("Consultative selling with deep client relationships", {"Marketing-Sales": 1.0, "People-Skill": 0.5, "Counseling": 0.3}),
("E-commerce and online store management", {"Marketing-Sales": 0.9, "Web-Dev": 0.5, "Technical-Skill": 0.3}),
("B2B enterprise sales and negotiations", {"Marketing-Sales": 0.9, "People-Skill": 0.5, "Finance-Acct": 0.3}),
("Retail merchandising and store layout", {"Marketing-Sales": 0.9, "Spatial-Design": 0.4, "Creative-Skill": 0.3}),
("Event marketing and trade show management", {"Marketing-Sales": 1.0, "Hospitality-Svc": 0.4, "People-Skill": 0.3}),
("Direct sales and field marketing teams", {"Marketing-Sales": 0.9, "People-Skill": 0.5, "Physical-Skill": 0.3})], ["business"]),
("Where would you apply marketing skills in the Philippines?", {"Marketing-Sales": 0.9}, [
("Digital marketing agency for local brands", {"Marketing-Sales": 1.0, "Digital-Media": 0.5, "Creative-Skill": 0.3}),
("FMCG company brand management", {"Marketing-Sales": 0.9, "Admin-Skill": 0.4, "Analytical-Skill": 0.3}),
("Tourism and destination marketing", {"Marketing-Sales": 0.9, "Tourism-Travel": 0.5, "Hospitality-Svc": 0.3}),
("Real estate sales and property marketing", {"Marketing-Sales": 0.9, "Finance-Acct": 0.4, "People-Skill": 0.3}),
("Tech startup growth marketing", {"Marketing-Sales": 0.9, "Startup-Venture": 0.5, "Data-Analytics": 0.3}),
("NGO fundraising and advocacy campaigns", {"Marketing-Sales": 0.8, "Community-Serve": 0.5, "Social-Work": 0.3})], ["business"]),
# HR-Management
("Which HR function excites you most?", {"HR-Management": 0.9}, [
("Talent acquisition and recruitment strategy", {"HR-Management": 1.0, "People-Skill": 0.5, "Analytical-Skill": 0.3}),
("Training and employee development programs", {"HR-Management": 0.9, "Teaching-Ed": 0.5, "People-Skill": 0.3}),
("Compensation and benefits administration", {"HR-Management": 0.9, "Finance-Acct": 0.5, "Admin-Skill": 0.3}),
("Employee relations and conflict resolution", {"HR-Management": 0.9, "People-Skill": 0.5, "Counseling": 0.4}),
("HR analytics and workforce planning", {"HR-Management": 0.9, "Data-Analytics": 0.5, "Analytical-Skill": 0.3}),
("Labor law compliance (DOLE regulations)", {"HR-Management": 1.0, "Legal-Practice": 0.5, "Admin-Skill": 0.3})], ["business"]),
("What HR technology would you implement?", {"HR-Management": 0.9, "Technical-Skill": 0.3}, [
("HRIS and employee self-service portals", {"HR-Management": 1.0, "Software-Dev": 0.4, "Admin-Skill": 0.3}),
("Applicant tracking and AI resume screening", {"HR-Management": 0.9, "AI-ML": 0.4, "Data-Analytics": 0.3}),
("E-learning and LMS platforms for training", {"HR-Management": 0.9, "Teaching-Ed": 0.5, "Software-Dev": 0.3}),
("Employee engagement survey platforms", {"HR-Management": 0.9, "Data-Analytics": 0.4, "People-Skill": 0.4}),
("Payroll automation and compliance systems", {"HR-Management": 0.9, "Finance-Acct": 0.5, "Software-Dev": 0.3}),
("Performance management and OKR tools", {"HR-Management": 1.0, "Admin-Skill": 0.4, "Analytical-Skill": 0.3})], ["business", "technology"]),
("What HR leadership challenge would you tackle?", {"HR-Management": 0.9, "People-Skill": 0.3}, [
("Reducing employee turnover and improving retention", {"HR-Management": 1.0, "People-Skill": 0.5, "Counseling": 0.3}),
("Building inclusive and diverse workplace culture", {"HR-Management": 0.9, "Community-Serve": 0.4, "People-Skill": 0.4}),
("Managing remote and hybrid work transitions", {"HR-Management": 0.9, "Admin-Skill": 0.5, "Technical-Skill": 0.3}),
("Upskilling workers for Industry 4.0", {"HR-Management": 0.9, "Teaching-Ed": 0.5, "Technical-Skill": 0.3}),
("Handling labor disputes and union negotiations", {"HR-Management": 0.9, "Legal-Practice": 0.5, "People-Skill": 0.4}),
("Designing employee wellness programs", {"HR-Management": 0.9, "Counseling": 0.5, "Public-Health": 0.3})], ["business", "social"]),
# Admin-Skill
("What administrative function do you excel at?", {"Admin-Skill": 0.9}, [
("Organizing files, documents, and databases", {"Admin-Skill": 1.0, "Technical-Skill": 0.4, "Data-Analytics": 0.3}),
("Scheduling meetings and managing calendars", {"Admin-Skill": 0.9, "People-Skill": 0.4, "Technical-Skill": 0.3}),
("Preparing reports and presentations", {"Admin-Skill": 0.9, "Analytical-Skill": 0.5, "Creative-Skill": 0.3}),
("Office supply and resource management", {"Admin-Skill": 0.9, "Industrial-Ops": 0.4, "Finance-Acct": 0.3}),
("Travel coordination and event planning", {"Admin-Skill": 0.9, "Hospitality-Svc": 0.4, "People-Skill": 0.3}),
("Customer and visitor reception management", {"Admin-Skill": 1.0, "People-Skill": 0.5, "Hospitality-Svc": 0.3})], ["business"]),
("What office technology would you master?", {"Admin-Skill": 0.9, "Technical-Skill": 0.3}, [
("Advanced Microsoft Office and spreadsheet skills", {"Admin-Skill": 1.0, "Data-Analytics": 0.4, "Technical-Skill": 0.3}),
("Project management tools like Trello or Asana", {"Admin-Skill": 0.9, "Industrial-Ops": 0.4, "Technical-Skill": 0.3}),
("Enterprise resource planning (ERP) systems", {"Admin-Skill": 0.9, "Industrial-Ops": 0.5, "Finance-Acct": 0.3}),
("Digital document and workflow automation", {"Admin-Skill": 0.9, "Software-Dev": 0.4, "Technical-Skill": 0.4}),
("Customer relationship management (CRM) platforms", {"Admin-Skill": 0.9, "Marketing-Sales": 0.4, "People-Skill": 0.3}),
("Business communication and video conferencing", {"Admin-Skill": 1.0, "People-Skill": 0.4, "Technical-Skill": 0.3})], ["business", "technology"]),
("Which administrative leadership role appeals to you?", {"Admin-Skill": 0.9, "People-Skill": 0.3}, [
("Executive assistant to a CEO", {"Admin-Skill": 1.0, "People-Skill": 0.5, "Analytical-Skill": 0.3}),
("Office manager overseeing daily operations", {"Admin-Skill": 0.9, "Industrial-Ops": 0.4, "People-Skill": 0.4}),
("Records and compliance manager", {"Admin-Skill": 0.9, "Legal-Practice": 0.4, "Analytical-Skill": 0.3}),
("Government bureau administrative officer", {"Admin-Skill": 0.9, "Community-Serve": 0.4, "Admin-Skill": 0.3}),
("BPO operations coordinator", {"Admin-Skill": 0.9, "People-Skill": 0.5, "Technical-Skill": 0.3}),
("Procurement and purchasing specialist", {"Admin-Skill": 1.0, "Finance-Acct": 0.4, "Industrial-Ops": 0.3})], ["business"]),
("What administrative improvement would you prioritize?", {"Admin-Skill": 0.9}, [
("Paperless office and digital transformation", {"Admin-Skill": 1.0, "Technical-Skill": 0.5, "Software-Dev": 0.3}),
("Streamlining approval and processing workflows", {"Admin-Skill": 0.9, "Industrial-Ops": 0.5, "Analytical-Skill": 0.3}),
("Improving interdepartmental communication", {"Admin-Skill": 0.9, "People-Skill": 0.5, "Technical-Skill": 0.3}),
("Organizing training schedules for all staff", {"Admin-Skill": 0.9, "Teaching-Ed": 0.4, "HR-Management": 0.3}),
("Creating standard operating procedures", {"Admin-Skill": 1.0, "Analytical-Skill": 0.4, "Legal-Practice": 0.3}),
("Managing office budget and expenses", {"Admin-Skill": 0.9, "Finance-Acct": 0.5, "Analytical-Skill": 0.3})], ["business"]),
# Startup-Venture
("What stage of startup building excites you?", {"Startup-Venture": 0.9}, [
("Brainstorming business ideas and validation", {"Startup-Venture": 1.0, "Creative-Skill": 0.5, "Analytical-Skill": 0.3}),
("Building the MVP (minimum viable product)", {"Startup-Venture": 0.9, "Software-Dev": 0.5, "Technical-Skill": 0.3}),
("Pitching to investors and fundraising", {"Startup-Venture": 0.9, "People-Skill": 0.5, "Finance-Acct": 0.3}),
("Scaling operations and hiring the team", {"Startup-Venture": 0.9, "HR-Management": 0.4, "Admin-Skill": 0.3}),
("Growth marketing and user acquisition", {"Startup-Venture": 0.9, "Marketing-Sales": 0.5, "Digital-Media": 0.3}),
("Product-market fit iteration and pivoting", {"Startup-Venture": 1.0, "Analytical-Skill": 0.5, "People-Skill": 0.3})], ["business"]),
("What Philippine startup sector interests you?", {"Startup-Venture": 0.9}, [
("Fintech and digital payments", {"Startup-Venture": 0.9, "Finance-Acct": 0.5, "Software-Dev": 0.3}),
("Agritech for Filipino farmers", {"Startup-Venture": 0.9, "Agri-Nature": 0.5, "Technical-Skill": 0.3}),
("Edtech for Philippine education", {"Startup-Venture": 0.9, "Teaching-Ed": 0.5, "Software-Dev": 0.3}),
("Healthtech and telemedicine", {"Startup-Venture": 0.9, "Patient-Care": 0.4, "Health-Admin": 0.3}),
("Logistics and last-mile delivery", {"Startup-Venture": 0.9, "Industrial-Ops": 0.5, "Software-Dev": 0.3}),
("Social enterprise for underserved communities", {"Startup-Venture": 0.8, "Community-Serve": 0.5, "Social-Work": 0.4})], ["business", "technology"]),
("What entrepreneurship skill would you build first?", {"Startup-Venture": 0.9, "People-Skill": 0.3}, [
("Financial modeling and runway planning", {"Startup-Venture": 1.0, "Finance-Acct": 0.5, "Analytical-Skill": 0.3}),
("Public speaking and investor pitch delivery", {"Startup-Venture": 0.9, "People-Skill": 0.5, "Performing-Arts": 0.3}),
("Team leadership and culture building", {"Startup-Venture": 0.9, "People-Skill": 0.5, "HR-Management": 0.3}),
("Customer discovery and user research", {"Startup-Venture": 0.9, "Analytical-Skill": 0.5, "Marketing-Sales": 0.3}),
("Business model canvas and strategy design", {"Startup-Venture": 1.0, "Analytical-Skill": 0.5, "Creative-Skill": 0.3}),
("Lean startup experimentation and testing", {"Startup-Venture": 0.9, "Data-Analytics": 0.4, "Analytical-Skill": 0.4})], ["business"]),
("What startup challenge would you solve?", {"Startup-Venture": 0.9}, [
("Finding product-market fit before funding runs out", {"Startup-Venture": 1.0, "Analytical-Skill": 0.5, "Marketing-Sales": 0.3}),
("Competing with larger established companies", {"Startup-Venture": 0.9, "Marketing-Sales": 0.4, "Creative-Skill": 0.3}),
("Navigating Philippine business regulations", {"Startup-Venture": 0.9, "Legal-Practice": 0.5, "Admin-Skill": 0.3}),
("Building a loyal customer community", {"Startup-Venture": 0.9, "People-Skill": 0.5, "Community-Serve": 0.3}),
("Managing cash flow in early stages", {"Startup-Venture": 0.9, "Finance-Acct": 0.5, "Analytical-Skill": 0.3}),
("Hiring talent without big company budgets", {"Startup-Venture": 1.0, "HR-Management": 0.5, "People-Skill": 0.3})], ["business"]),
]
for t, qt, o, br in biz_qs:
    ALL.append(nq(t, qt, o, br))

# ===== CREATIVE: Visual-Design, Animation-3D, Digital-Media, Film-Broadcast, Performing-Arts, Spatial-Design =====
cre_qs = [
# Visual-Design
("What visual design discipline interests you most?", {"Visual-Design": 0.9}, [
("Graphic design for branding and logos", {"Visual-Design": 1.0, "Creative-Skill": 0.5, "Marketing-Sales": 0.3}),
("UI/UX design for apps and websites", {"Visual-Design": 0.9, "Web-Dev": 0.4, "Software-Dev": 0.3}),
("Typography and layout design", {"Visual-Design": 1.0, "Creative-Skill": 0.5, "Analytical-Skill": 0.3}),
("Photography and photo editing", {"Visual-Design": 0.9, "Digital-Media": 0.5, "Creative-Skill": 0.3}),
("Packaging and product design", {"Visual-Design": 0.9, "Industrial-Ops": 0.4, "Marketing-Sales": 0.3}),
("Illustration and concept art", {"Visual-Design": 0.9, "Animation-3D": 0.4, "Creative-Skill": 0.5})], ["creative"]),
("Which design tool would you specialize in?", {"Visual-Design": 0.9, "Technical-Skill": 0.3}, [
("Adobe Photoshop for image editing", {"Visual-Design": 1.0, "Digital-Media": 0.4, "Creative-Skill": 0.3}),
("Figma for collaborative UI/UX design", {"Visual-Design": 0.9, "Web-Dev": 0.4, "Software-Dev": 0.3}),
("Adobe Illustrator for vector graphics", {"Visual-Design": 1.0, "Creative-Skill": 0.5, "Technical-Skill": 0.3}),
("InDesign for publication layout design", {"Visual-Design": 0.9, "Digital-Media": 0.4, "Admin-Skill": 0.3}),
("Canva for rapid social media content", {"Visual-Design": 0.8, "Marketing-Sales": 0.5, "Digital-Media": 0.3}),
("Procreate for digital illustration", {"Visual-Design": 0.9, "Creative-Skill": 0.5, "Animation-3D": 0.3})], ["creative", "technology"]),
("What design career path appeals to you?", {"Visual-Design": 0.9}, [
("Art director at an advertising agency", {"Visual-Design": 1.0, "Marketing-Sales": 0.4, "People-Skill": 0.3}),
("Freelance graphic designer", {"Visual-Design": 0.9, "Startup-Venture": 0.4, "Creative-Skill": 0.3}),
("UX/UI designer at a tech company", {"Visual-Design": 0.9, "Web-Dev": 0.5, "Software-Dev": 0.3}),
("Publication designer for magazines or books", {"Visual-Design": 0.9, "Digital-Media": 0.4, "Creative-Skill": 0.3}),
("Brand identity specialist", {"Visual-Design": 1.0, "Marketing-Sales": 0.5, "Creative-Skill": 0.3}),
("Design educator and mentor", {"Visual-Design": 0.8, "Teaching-Ed": 0.5, "People-Skill": 0.4})], ["creative"]),
# Animation-3D
("What animation style would you specialize in?", {"Animation-3D": 0.9}, [
("3D character animation and rigging", {"Animation-3D": 1.0, "Creative-Skill": 0.5, "Technical-Skill": 0.3}),
("2D frame-by-frame traditional animation", {"Animation-3D": 0.9, "Creative-Skill": 0.5, "Visual-Design": 0.3}),
("Motion graphics for video content", {"Animation-3D": 0.9, "Digital-Media": 0.5, "Film-Broadcast": 0.3}),
("VFX and compositing for film", {"Animation-3D": 0.9, "Film-Broadcast": 0.5, "Technical-Skill": 0.4}),
("Environment and world building in 3D", {"Animation-3D": 1.0, "Spatial-Design": 0.5, "Game-Dev": 0.3}),
("Stop-motion and practical effects", {"Animation-3D": 0.9, "Creative-Skill": 0.5, "Physical-Skill": 0.3})], ["creative", "technology"]),
("Which animation software would you master?", {"Animation-3D": 0.9, "Technical-Skill": 0.3}, [
("Blender for open-source 3D creation", {"Animation-3D": 1.0, "Software-Dev": 0.3, "Creative-Skill": 0.3}),
("Maya for professional character animation", {"Animation-3D": 1.0, "Film-Broadcast": 0.3, "Technical-Skill": 0.3}),
("After Effects for motion graphics", {"Animation-3D": 0.9, "Digital-Media": 0.5, "Visual-Design": 0.3}),
("ZBrush for digital sculpting", {"Animation-3D": 0.9, "Visual-Design": 0.5, "Creative-Skill": 0.3}),
("Unity or Unreal for real-time animation", {"Animation-3D": 0.9, "Game-Dev": 0.5, "Software-Dev": 0.3}),
("Toon Boom for 2D production animation", {"Animation-3D": 0.9, "Creative-Skill": 0.5, "Film-Broadcast": 0.3})], ["creative", "technology"]),
("What animation project would you create?", {"Animation-3D": 0.9, "Creative-Skill": 0.3}, [
("Filipino folklore animated short film", {"Animation-3D": 1.0, "Film-Broadcast": 0.4, "Creative-Skill": 0.4}),
("Educational animated explainer videos", {"Animation-3D": 0.9, "Teaching-Ed": 0.5, "Digital-Media": 0.3}),
("Game cinematic trailer and cutscenes", {"Animation-3D": 0.9, "Game-Dev": 0.5, "Creative-Skill": 0.3}),
("Product visualization and advertisement", {"Animation-3D": 0.9, "Marketing-Sales": 0.5, "Visual-Design": 0.3}),
("Architectural walkthrough and visualization", {"Animation-3D": 0.9, "Spatial-Design": 0.5, "Civil-Build": 0.3}),
("Social media animated content", {"Animation-3D": 0.8, "Digital-Media": 0.5, "Marketing-Sales": 0.3})], ["creative"]),
# Digital-Media
("What digital media content would you produce?", {"Digital-Media": 0.9}, [
("YouTube video production and editing", {"Digital-Media": 1.0, "Film-Broadcast": 0.4, "Creative-Skill": 0.3}),
("Podcast creation and audio storytelling", {"Digital-Media": 0.9, "Performing-Arts": 0.4, "People-Skill": 0.3}),
("Social media content strategy and creation", {"Digital-Media": 0.9, "Marketing-Sales": 0.5, "Creative-Skill": 0.3}),
("Blog and online journalism", {"Digital-Media": 0.9, "Creative-Skill": 0.5, "Analytical-Skill": 0.3}),
("Livestreaming and interactive content", {"Digital-Media": 0.9, "People-Skill": 0.4, "Performing-Arts": 0.3}),
("Infographic and data visualization design", {"Digital-Media": 0.9, "Visual-Design": 0.5, "Data-Analytics": 0.3})], ["creative"]),
("Which digital media platform would you focus on?", {"Digital-Media": 0.9, "Marketing-Sales": 0.3}, [
("YouTube for long-form video content", {"Digital-Media": 1.0, "Film-Broadcast": 0.4, "Creative-Skill": 0.3}),
("TikTok and Reels for short-form video", {"Digital-Media": 0.9, "Creative-Skill": 0.5, "Marketing-Sales": 0.3}),
("Website and blog content management", {"Digital-Media": 0.9, "Web-Dev": 0.5, "Creative-Skill": 0.3}),
("Spotify and Apple Podcasts audio content", {"Digital-Media": 0.9, "Performing-Arts": 0.4, "People-Skill": 0.3}),
("Instagram and Pinterest visual storytelling", {"Digital-Media": 0.9, "Visual-Design": 0.5, "Marketing-Sales": 0.3}),
("Newsletter and email media publishing", {"Digital-Media": 0.9, "Creative-Skill": 0.4, "Marketing-Sales": 0.4})], ["creative"]),
("What digital media skill would you develop?", {"Digital-Media": 0.9, "Creative-Skill": 0.3}, [
("Video editing with Premiere Pro or DaVinci", {"Digital-Media": 1.0, "Film-Broadcast": 0.5, "Technical-Skill": 0.3}),
("Photography and photo manipulation", {"Digital-Media": 0.9, "Visual-Design": 0.5, "Creative-Skill": 0.3}),
("Copywriting and content strategy", {"Digital-Media": 0.9, "Marketing-Sales": 0.5, "Creative-Skill": 0.3}),
("Audio production and sound engineering", {"Digital-Media": 0.9, "Performing-Arts": 0.4, "Technical-Skill": 0.4}),
("Motion graphics and visual effects", {"Digital-Media": 0.9, "Animation-3D": 0.5, "Visual-Design": 0.3}),
("Community management and engagement", {"Digital-Media": 0.8, "People-Skill": 0.5, "Marketing-Sales": 0.3})], ["creative", "technology"]),
# Film-Broadcast
("What film/broadcast production role excites you?", {"Film-Broadcast": 0.9}, [
("Director controlling the creative vision", {"Film-Broadcast": 1.0, "Creative-Skill": 0.5, "People-Skill": 0.3}),
("Cinematographer framing beautiful shots", {"Film-Broadcast": 0.9, "Visual-Design": 0.5, "Creative-Skill": 0.4}),
("Screenwriter crafting compelling stories", {"Film-Broadcast": 0.9, "Creative-Skill": 0.6, "Analytical-Skill": 0.3}),
("Film editor shaping the final narrative", {"Film-Broadcast": 0.9, "Digital-Media": 0.5, "Analytical-Skill": 0.3}),
("Producer managing budget and logistics", {"Film-Broadcast": 0.9, "Finance-Acct": 0.4, "Admin-Skill": 0.4}),
("Sound designer creating audio atmosphere", {"Film-Broadcast": 0.9, "Performing-Arts": 0.4, "Technical-Skill": 0.4})], ["creative"]),
("What film genre would you work in?", {"Film-Broadcast": 0.9, "Creative-Skill": 0.3}, [
("Drama exploring Filipino social issues", {"Film-Broadcast": 1.0, "Social-Work": 0.4, "Community-Serve": 0.3}),
("Documentary capturing real Philippine stories", {"Film-Broadcast": 0.9, "Field-Research": 0.4, "Community-Serve": 0.3}),
("Action film with practical and visual effects", {"Film-Broadcast": 0.9, "Animation-3D": 0.4, "Physical-Skill": 0.3}),
("Comedy bringing joy to Filipino audiences", {"Film-Broadcast": 0.9, "Performing-Arts": 0.5, "Creative-Skill": 0.3}),
("Horror or thriller with suspenseful storytelling", {"Film-Broadcast": 1.0, "Creative-Skill": 0.5, "Analytical-Skill": 0.3}),
("Short film or indie experimental cinema", {"Film-Broadcast": 0.9, "Creative-Skill": 0.5, "Visual-Design": 0.3})], ["creative"]),
("What broadcast media career path appeals to you?", {"Film-Broadcast": 0.9}, [
("Television news producer or reporter", {"Film-Broadcast": 1.0, "People-Skill": 0.5, "Community-Serve": 0.3}),
("Film production company founder", {"Film-Broadcast": 0.9, "Startup-Venture": 0.5, "Admin-Skill": 0.3}),
("Commercial and advertising director", {"Film-Broadcast": 0.9, "Marketing-Sales": 0.5, "Creative-Skill": 0.3}),
("Live event and concert broadcast engineer", {"Film-Broadcast": 0.9, "Performing-Arts": 0.4, "Technical-Skill": 0.4}),
("Streaming platform content creator", {"Film-Broadcast": 0.9, "Digital-Media": 0.5, "Startup-Venture": 0.3}),
("Film school instructor sharing knowledge", {"Film-Broadcast": 0.8, "Teaching-Ed": 0.6, "People-Skill": 0.3})], ["creative"]),
# Performing-Arts
("What performing arts discipline appeals to you?", {"Performing-Arts": 0.9}, [
("Theater acting and stage performance", {"Performing-Arts": 1.0, "People-Skill": 0.4, "Creative-Skill": 0.3}),
("Music performance and composition", {"Performing-Arts": 0.9, "Creative-Skill": 0.5, "Analytical-Skill": 0.3}),
("Dance choreography and movement", {"Performing-Arts": 0.9, "Physical-Skill": 0.5, "Creative-Skill": 0.4}),
("Voice acting and dubbing", {"Performing-Arts": 0.9, "Film-Broadcast": 0.4, "Creative-Skill": 0.3}),
("Musical theater combining all art forms", {"Performing-Arts": 1.0, "Creative-Skill": 0.5, "People-Skill": 0.3}),
("Stand-up comedy and improv performance", {"Performing-Arts": 0.9, "People-Skill": 0.5, "Creative-Skill": 0.3})], ["creative"]),
("What performing arts career interests you?", {"Performing-Arts": 0.9, "People-Skill": 0.3}, [
("Professional stage actor in Filipino theater", {"Performing-Arts": 1.0, "Creative-Skill": 0.5, "People-Skill": 0.3}),
("Music teacher and conductor", {"Performing-Arts": 0.9, "Teaching-Ed": 0.5, "People-Skill": 0.3}),
("Concert or event production manager", {"Performing-Arts": 0.9, "Admin-Skill": 0.5, "Hospitality-Svc": 0.3}),
("Recording artist or studio musician", {"Performing-Arts": 0.9, "Technical-Skill": 0.4, "Creative-Skill": 0.4}),
("Dance troupe director or choreographer", {"Performing-Arts": 0.9, "Physical-Skill": 0.5, "Creative-Skill": 0.3}),
("Arts therapy practitioner", {"Performing-Arts": 0.8, "Counseling": 0.5, "Rehab-Therapy": 0.3})], ["creative", "education"]),
("What performing arts skill would you develop?", {"Performing-Arts": 0.9, "Creative-Skill": 0.3}, [
("Vocal training and singing technique", {"Performing-Arts": 1.0, "Physical-Skill": 0.3, "Creative-Skill": 0.3}),
("Musical instrument mastery", {"Performing-Arts": 0.9, "Technical-Skill": 0.4, "Creative-Skill": 0.4}),
("Script analysis and character development", {"Performing-Arts": 0.9, "Analytical-Skill": 0.5, "Creative-Skill": 0.3}),
("Stage design and lighting direction", {"Performing-Arts": 0.9, "Spatial-Design": 0.5, "Technical-Skill": 0.3}),
("Sound engineering for live performance", {"Performing-Arts": 0.8, "Technical-Skill": 0.5, "Hardware-Systems": 0.3}),
("Video and livestream production for arts", {"Performing-Arts": 0.9, "Digital-Media": 0.5, "Film-Broadcast": 0.3})], ["creative"]),
# Spatial-Design
("What spatial design discipline interests you?", {"Spatial-Design": 0.9}, [
("Interior design for residential spaces", {"Spatial-Design": 1.0, "Creative-Skill": 0.5, "Visual-Design": 0.3}),
("Architecture and building design", {"Spatial-Design": 0.9, "Civil-Build": 0.5, "Analytical-Skill": 0.3}),
("Landscape architecture and outdoor spaces", {"Spatial-Design": 0.9, "Environmental-Sci": 0.4, "Agri-Nature": 0.3}),
("Urban planning and city development", {"Spatial-Design": 0.9, "Civil-Build": 0.4, "Community-Serve": 0.3}),
("Exhibition and museum display design", {"Spatial-Design": 0.9, "Visual-Design": 0.5, "Creative-Skill": 0.3}),
("Stage and set design for events", {"Spatial-Design": 0.9, "Performing-Arts": 0.4, "Creative-Skill": 0.4})], ["creative", "engineering"]),
("Which spatial design tool would you learn?", {"Spatial-Design": 0.9, "Technical-Skill": 0.3}, [
("SketchUp for 3D spatial modeling", {"Spatial-Design": 1.0, "Technical-Skill": 0.5, "Visual-Design": 0.3}),
("Revit for BIM building design", {"Spatial-Design": 0.9, "Civil-Build": 0.5, "Technical-Skill": 0.3}),
("AutoCAD for floor plans and layouts", {"Spatial-Design": 0.9, "Civil-Build": 0.4, "Technical-Skill": 0.4}),
("3ds Max for photorealistic rendering", {"Spatial-Design": 0.9, "Animation-3D": 0.5, "Creative-Skill": 0.3}),
("Lumion for walkthrough visualization", {"Spatial-Design": 0.9, "Animation-3D": 0.4, "Visual-Design": 0.3}),
("VR tools for immersive spatial experience", {"Spatial-Design": 1.0, "Technical-Skill": 0.5, "Software-Dev": 0.3})], ["creative", "technology"]),
("What spatial design project excites you?", {"Spatial-Design": 0.9}, [
("Designing a modern Filipino home", {"Spatial-Design": 1.0, "Creative-Skill": 0.5, "Civil-Build": 0.3}),
("Planning a sustainable community park", {"Spatial-Design": 0.9, "Environmental-Eng": 0.4, "Community-Serve": 0.4}),
("Creating an interactive museum exhibit", {"Spatial-Design": 0.9, "Visual-Design": 0.5, "Teaching-Ed": 0.3}),
("Designing an efficient hospital layout", {"Spatial-Design": 0.9, "Health-Admin": 0.4, "Civil-Build": 0.3}),
("Renovating heritage buildings in Vigan", {"Spatial-Design": 0.9, "Creative-Skill": 0.4, "Tourism-Travel": 0.4}),
("Designing a co-working space for startups", {"Spatial-Design": 0.9, "Startup-Venture": 0.4, "Admin-Skill": 0.3})], ["creative", "engineering"]),
]
for t, qt, o, br in cre_qs:
    ALL.append(nq(t, qt, o, br))

# ===== SCIENCE: Lab-Research, Field-Research, Environmental-Sci, Food-Science, Forensic-Sci =====
sci_qs = [
# Lab-Research
("What laboratory research area fascinates you?", {"Lab-Research": 0.9}, [
("Molecular biology and genetic engineering", {"Lab-Research": 1.0, "Medical-Lab": 0.4, "Analytical-Skill": 0.3}),
("Materials science and nanotechnology", {"Lab-Research": 0.9, "Technical-Skill": 0.5, "Mechanical-Design": 0.3}),
("Organic chemistry and synthesis", {"Lab-Research": 0.9, "Pharmacy": 0.4, "Analytical-Skill": 0.3}),
("Cell culture and tissue engineering", {"Lab-Research": 1.0, "Medical-Lab": 0.4, "Patient-Care": 0.3}),
("Environmental sample testing and analysis", {"Lab-Research": 0.9, "Environmental-Sci": 0.5, "Field-Research": 0.3}),
("Pharmaceutical drug testing and validation", {"Lab-Research": 0.9, "Pharmacy": 0.5, "Medical-Lab": 0.3})], ["science"]),
("What lab technique would you master?", {"Lab-Research": 0.9, "Technical-Skill": 0.3}, [
("PCR and DNA amplification methods", {"Lab-Research": 1.0, "Medical-Lab": 0.4, "Technical-Skill": 0.3}),
("Spectroscopy for chemical identification", {"Lab-Research": 0.9, "Analytical-Skill": 0.5, "Technical-Skill": 0.4}),
("Chromatography for compound separation", {"Lab-Research": 0.9, "Pharmacy": 0.4, "Technical-Skill": 0.3}),
("Electron microscopy for nanoscale imaging", {"Lab-Research": 1.0, "Technical-Skill": 0.5, "Analytical-Skill": 0.3}),
("Cell counting and viability assays", {"Lab-Research": 0.9, "Medical-Lab": 0.5, "Patient-Care": 0.3}),
("Statistical design of experiments", {"Lab-Research": 0.9, "Data-Analytics": 0.5, "Analytical-Skill": 0.3})], ["science"]),
("Where would you conduct research?", {"Lab-Research": 0.9}, [
("University research laboratory", {"Lab-Research": 1.0, "Teaching-Ed": 0.4, "Analytical-Skill": 0.3}),
("DOST Philippine government research institute", {"Lab-Research": 0.9, "Community-Serve": 0.4, "Admin-Skill": 0.3}),
("Pharmaceutical company R&D department", {"Lab-Research": 0.9, "Pharmacy": 0.5, "Industrial-Ops": 0.3}),
("Hospital clinical research unit", {"Lab-Research": 0.9, "Patient-Care": 0.5, "Medical-Lab": 0.3}),
("Environmental testing laboratory", {"Lab-Research": 0.9, "Environmental-Sci": 0.5, "Field-Research": 0.3}),
("Biotech startup research lab", {"Lab-Research": 0.9, "Startup-Venture": 0.4, "Technical-Skill": 0.3})], ["science"]),
("What motivates you about lab research?", {"Lab-Research": 0.9}, [
("Discovering new knowledge through experiments", {"Lab-Research": 1.0, "Analytical-Skill": 0.5, "Creative-Skill": 0.3}),
("Developing solutions to Filipino health problems", {"Lab-Research": 0.9, "Public-Health": 0.5, "Community-Serve": 0.3}),
("Publishing research papers in scientific journals", {"Lab-Research": 0.9, "Analytical-Skill": 0.4, "Teaching-Ed": 0.3}),
("Working with precision instruments and technology", {"Lab-Research": 0.9, "Technical-Skill": 0.5, "Hardware-Systems": 0.3}),
("Collaborating with international research teams", {"Lab-Research": 0.9, "People-Skill": 0.4, "Community-Serve": 0.3}),
("Creating practical products from research findings", {"Lab-Research": 0.8, "Startup-Venture": 0.4, "Industrial-Ops": 0.4})], ["science"]),
# Field-Research
("What field research environment would you choose?", {"Field-Research": 0.9}, [
("Marine ecosystems and coral reef surveys", {"Field-Research": 0.9, "Environmental-Sci": 0.5, "Maritime-Sea": 0.3}),
("Rainforest biodiversity documentation", {"Field-Research": 1.0, "Environmental-Sci": 0.5, "Agri-Nature": 0.3}),
("Volcanic and geological field studies", {"Field-Research": 0.9, "Environmental-Sci": 0.4, "Physical-Skill": 0.3}),
("Agricultural crop and soil field trials", {"Field-Research": 0.9, "Agri-Nature": 0.5, "Lab-Research": 0.3}),
("Community health field surveys", {"Field-Research": 0.9, "Public-Health": 0.5, "Community-Serve": 0.3}),
("Archaeological and cultural site documentation", {"Field-Research": 0.9, "Creative-Skill": 0.3, "Teaching-Ed": 0.3})], ["science", "agriculture"]),
("What field research skill would you develop?", {"Field-Research": 0.9, "Physical-Skill": 0.3}, [
("GPS mapping and spatial data collection", {"Field-Research": 1.0, "Technical-Skill": 0.5, "Data-Analytics": 0.3}),
("Wildlife tracking and population counting", {"Field-Research": 0.9, "Environmental-Sci": 0.5, "Physical-Skill": 0.3}),
("Water and soil sampling techniques", {"Field-Research": 0.9, "Lab-Research": 0.5, "Environmental-Sci": 0.3}),
("Interview and survey data gathering", {"Field-Research": 0.9, "People-Skill": 0.5, "Data-Analytics": 0.3}),
("Drone operation for aerial surveying", {"Field-Research": 0.9, "Technical-Skill": 0.5, "Hardware-Systems": 0.3}),
("Specimen collection and preservation", {"Field-Research": 1.0, "Lab-Research": 0.5, "Physical-Skill": 0.3})], ["science"]),
("Where in the Philippines would you do fieldwork?", {"Field-Research": 0.9}, [
("Tubbataha Reef marine protected area", {"Field-Research": 1.0, "Environmental-Sci": 0.5, "Maritime-Sea": 0.3}),
("Sierra Madre mountain biodiversity study", {"Field-Research": 0.9, "Environmental-Sci": 0.5, "Physical-Skill": 0.3}),
("Rice terraces agricultural research station", {"Field-Research": 0.9, "Agri-Nature": 0.5, "Community-Serve": 0.3}),
("Manila Bay environmental monitoring", {"Field-Research": 0.9, "Environmental-Eng": 0.4, "Environmental-Sci": 0.4}),
("Rural community health survey site", {"Field-Research": 0.9, "Public-Health": 0.5, "Community-Serve": 0.3}),
("Taal Volcano geological monitoring station", {"Field-Research": 0.9, "Environmental-Sci": 0.4, "Technical-Skill": 0.3})], ["science"]),
# Environmental-Sci
("What environmental science topic interests you?", {"Environmental-Sci": 0.9}, [
("Climate change impacts on Philippine ecosystems", {"Environmental-Sci": 1.0, "Field-Research": 0.4, "Data-Analytics": 0.3}),
("Marine conservation and reef protection", {"Environmental-Sci": 0.9, "Maritime-Sea": 0.4, "Field-Research": 0.4}),
("Biodiversity conservation and endangered species", {"Environmental-Sci": 0.9, "Field-Research": 0.5, "Community-Serve": 0.3}),
("Air and water pollution monitoring", {"Environmental-Sci": 0.9, "Environmental-Eng": 0.5, "Lab-Research": 0.3}),
("Disaster risk reduction and resilience", {"Environmental-Sci": 0.9, "Community-Serve": 0.5, "Data-Analytics": 0.3}),
("Sustainable resource management", {"Environmental-Sci": 1.0, "Agri-Nature": 0.4, "Environmental-Eng": 0.3})], ["science"]),
("What environmental career path appeals to you?", {"Environmental-Sci": 0.9}, [
("DENR environmental management specialist", {"Environmental-Sci": 1.0, "Admin-Skill": 0.4, "Law-Enforce": 0.3}),
("Wildlife biologist studying Philippine fauna", {"Environmental-Sci": 0.9, "Field-Research": 0.5, "Lab-Research": 0.3}),
("Climate researcher analyzing weather data", {"Environmental-Sci": 0.9, "Data-Analytics": 0.5, "Lab-Research": 0.3}),
("Environmental consultant for projects", {"Environmental-Sci": 0.9, "Environmental-Eng": 0.4, "Startup-Venture": 0.3}),
("Sustainability officer at a corporation", {"Environmental-Sci": 0.9, "Admin-Skill": 0.5, "Industrial-Ops": 0.3}),
("Environmental educator and advocate", {"Environmental-Sci": 0.9, "Teaching-Ed": 0.5, "Community-Serve": 0.4})], ["science", "public_service"]),
("What environmental research method interests you?", {"Environmental-Sci": 0.9, "Lab-Research": 0.3}, [
("Remote sensing and satellite image analysis", {"Environmental-Sci": 0.9, "Data-Analytics": 0.5, "Technical-Skill": 0.3}),
("Water quality laboratory testing", {"Environmental-Sci": 0.9, "Lab-Research": 0.5, "Medical-Lab": 0.3}),
("Ecological field transect surveys", {"Environmental-Sci": 1.0, "Field-Research": 0.5, "Physical-Skill": 0.3}),
("Environmental DNA (eDNA) sampling", {"Environmental-Sci": 0.9, "Lab-Research": 0.5, "Technical-Skill": 0.3}),
("Carbon footprint calculation and modeling", {"Environmental-Sci": 0.9, "Data-Analytics": 0.5, "Analytical-Skill": 0.3}),
("Geographic Information Systems (GIS) mapping", {"Environmental-Sci": 1.0, "Data-Analytics": 0.5, "Technical-Skill": 0.3})], ["science", "technology"]),
# Food-Science
("What food science area interests you most?", {"Food-Science": 0.9}, [
("Food product development and innovation", {"Food-Science": 1.0, "Creative-Skill": 0.4, "Lab-Research": 0.3}),
("Food safety and quality assurance", {"Food-Science": 0.9, "Lab-Research": 0.5, "Industrial-Ops": 0.3}),
("Food microbiology and preservation", {"Food-Science": 0.9, "Lab-Research": 0.5, "Environmental-Sci": 0.3}),
("Sensory evaluation and taste testing", {"Food-Science": 0.9, "Analytical-Skill": 0.5, "People-Skill": 0.3}),
("Food processing technology and equipment", {"Food-Science": 0.9, "Industrial-Ops": 0.5, "Mechanical-Design": 0.3}),
("Nutritional analysis and labeling", {"Food-Science": 0.9, "Nutrition-Diet": 0.5, "Analytical-Skill": 0.3})], ["science"]),
("What food product would you develop?", {"Food-Science": 0.9, "Creative-Skill": 0.3}, [
("Healthy snack from local Filipino ingredients", {"Food-Science": 1.0, "Nutrition-Diet": 0.5, "Agri-Nature": 0.3}),
("Plant-based meat or dairy alternative", {"Food-Science": 0.9, "Lab-Research": 0.4, "Environmental-Sci": 0.3}),
("Shelf-stable emergency food for disasters", {"Food-Science": 0.9, "Community-Serve": 0.4, "Industrial-Ops": 0.3}),
("Fermented food with probiotic benefits", {"Food-Science": 0.9, "Lab-Research": 0.5, "Nutrition-Diet": 0.3}),
("Functional food enriched with vitamins", {"Food-Science": 1.0, "Nutrition-Diet": 0.5, "Pharmacy": 0.3}),
("Traditional Filipino delicacy scaled for export", {"Food-Science": 0.9, "Culinary-Arts": 0.5, "Marketing-Sales": 0.3})], ["science", "agriculture"]),
("Where would you work in food science?", {"Food-Science": 0.9}, [
("Food manufacturing company R&D lab", {"Food-Science": 1.0, "Lab-Research": 0.5, "Industrial-Ops": 0.3}),
("FDA Philippines food testing laboratory", {"Food-Science": 0.9, "Lab-Research": 0.5, "Legal-Practice": 0.3}),
("University food technology department", {"Food-Science": 0.9, "Teaching-Ed": 0.4, "Lab-Research": 0.4}),
("Restaurant chain recipe development", {"Food-Science": 0.9, "Culinary-Arts": 0.5, "Creative-Skill": 0.3}),
("Agricultural processing cooperative", {"Food-Science": 0.9, "Agri-Nature": 0.5, "Community-Serve": 0.3}),
("Food safety consulting firm", {"Food-Science": 0.9, "Startup-Venture": 0.4, "Analytical-Skill": 0.3})], ["science"]),
# Forensic-Sci
("What forensic science specialization interests you?", {"Forensic-Sci": 0.9}, [
("DNA evidence analysis and profiling", {"Forensic-Sci": 1.0, "Lab-Research": 0.5, "Medical-Lab": 0.3}),
("Crime scene investigation and evidence collection", {"Forensic-Sci": 0.9, "Law-Enforce": 0.5, "Field-Research": 0.3}),
("Toxicology and drug testing", {"Forensic-Sci": 0.9, "Pharmacy": 0.4, "Lab-Research": 0.4}),
("Digital forensics and cyber investigation", {"Forensic-Sci": 0.9, "Cyber-Defense": 0.5, "Software-Dev": 0.3}),
("Forensic accounting and fraud investigation", {"Forensic-Sci": 0.9, "Finance-Acct": 0.5, "Law-Enforce": 0.3}),
("Ballistics and firearms examination", {"Forensic-Sci": 1.0, "Law-Enforce": 0.5, "Physical-Skill": 0.3})], ["science", "law"]),
("What forensic lab technique would you learn?", {"Forensic-Sci": 0.9, "Lab-Research": 0.3}, [
("Fingerprint analysis and comparison", {"Forensic-Sci": 1.0, "Analytical-Skill": 0.5, "Law-Enforce": 0.3}),
("Blood pattern analysis and reconstruction", {"Forensic-Sci": 0.9, "Medical-Lab": 0.4, "Analytical-Skill": 0.4}),
("Trace evidence fiber and hair analysis", {"Forensic-Sci": 0.9, "Lab-Research": 0.5, "Analytical-Skill": 0.3}),
("Document examination and forgery detection", {"Forensic-Sci": 0.9, "Analytical-Skill": 0.5, "Legal-Practice": 0.3}),
("Forensic photography and documentation", {"Forensic-Sci": 0.9, "Visual-Design": 0.4, "Digital-Media": 0.3}),
("Anthropological identification of remains", {"Forensic-Sci": 1.0, "Lab-Research": 0.5, "Field-Research": 0.3})], ["science", "law"]),
("Where would you apply forensic science?", {"Forensic-Sci": 0.9}, [
("NBI crime laboratory", {"Forensic-Sci": 1.0, "Law-Enforce": 0.5, "Lab-Research": 0.3}),
("PNP forensics and crime scene unit", {"Forensic-Sci": 0.9, "Law-Enforce": 0.5, "Field-Research": 0.3}),
("Private forensic consulting firm", {"Forensic-Sci": 0.9, "Startup-Venture": 0.4, "Legal-Practice": 0.3}),
("Hospital forensic pathology department", {"Forensic-Sci": 0.9, "Patient-Care": 0.4, "Medical-Lab": 0.4}),
("Digital forensics for corporate investigations", {"Forensic-Sci": 0.9, "Cyber-Defense": 0.5, "Software-Dev": 0.3}),
("Academic forensic science research", {"Forensic-Sci": 0.9, "Lab-Research": 0.5, "Teaching-Ed": 0.3})], ["science"]),
]
for t, qt, o, br in sci_qs:
    ALL.append(nq(t, qt, o, br))

# ===== SERVICE: Teaching-Ed, Social-Work, Community-Serve, Law-Enforce, Legal-Practice,
#                Sports-Ed, Hospitality-Svc, Tourism-Travel, Culinary-Arts =====
svc_qs = [
# Teaching-Ed
("What would you most enjoy teaching?", {"Teaching-Ed": 0.9}, [
("Science experiments and lab activities", {"Teaching-Ed": 0.9, "Lab-Research": 0.5, "Analytical-Skill": 0.3}),
("Mathematics and problem-solving strategies", {"Teaching-Ed": 0.9, "Analytical-Skill": 0.5, "Data-Analytics": 0.3}),
("English language and literature", {"Teaching-Ed": 1.0, "Creative-Skill": 0.4, "People-Skill": 0.3}),
("Physical education and sports", {"Teaching-Ed": 0.9, "Sports-Ed": 0.5, "Physical-Skill": 0.3}),
("ICT and computer literacy skills", {"Teaching-Ed": 0.9, "Technical-Skill": 0.5, "Software-Dev": 0.3}),
("Values education and social-emotional learning", {"Teaching-Ed": 0.9, "Counseling": 0.5, "Community-Serve": 0.3})], ["education"]),
("Which teaching approach appeals to you?", {"Teaching-Ed": 0.9, "Creative-Skill": 0.3}, [
("Project-based learning with real-world problems", {"Teaching-Ed": 1.0, "Analytical-Skill": 0.5, "Creative-Skill": 0.3}),
("Gamification and interactive digital lessons", {"Teaching-Ed": 0.9, "Game-Dev": 0.4, "Software-Dev": 0.3}),
("Outdoor and experiential field learning", {"Teaching-Ed": 0.9, "Field-Research": 0.5, "Physical-Skill": 0.3}),
("One-on-one mentoring and tutoring", {"Teaching-Ed": 0.9, "People-Skill": 0.5, "Counseling": 0.3}),
("Collaborative group learning activities", {"Teaching-Ed": 0.9, "People-Skill": 0.5, "Community-Serve": 0.3}),
("Flipped classroom with video content", {"Teaching-Ed": 0.9, "Digital-Media": 0.5, "Creative-Skill": 0.3})], ["education"]),
("Where would you teach in the Philippines?", {"Teaching-Ed": 0.9}, [
("Public elementary school in a rural area", {"Teaching-Ed": 1.0, "Community-Serve": 0.5, "Social-Work": 0.3}),
("Private high school with modern facilities", {"Teaching-Ed": 0.9, "Technical-Skill": 0.3, "Admin-Skill": 0.3}),
("University or college institution", {"Teaching-Ed": 0.9, "Lab-Research": 0.4, "Analytical-Skill": 0.3}),
("Technical-vocational training center (TESDA)", {"Teaching-Ed": 0.9, "Technical-Skill": 0.5, "Industrial-Ops": 0.3}),
("Online education platform reaching all Filipinos", {"Teaching-Ed": 0.9, "Digital-Media": 0.5, "Software-Dev": 0.3}),
("Special education school for differently-abled", {"Teaching-Ed": 0.9, "Rehab-Therapy": 0.4, "Counseling": 0.4})], ["education", "public_service"]),
("What education leadership role would you pursue?", {"Teaching-Ed": 0.9, "Admin-Skill": 0.3}, [
("School principal managing faculty and programs", {"Teaching-Ed": 1.0, "Admin-Skill": 0.5, "People-Skill": 0.3}),
("Curriculum developer for DepEd", {"Teaching-Ed": 0.9, "Analytical-Skill": 0.5, "Creative-Skill": 0.3}),
("Education technology specialist", {"Teaching-Ed": 0.9, "Software-Dev": 0.4, "Technical-Skill": 0.4}),
("Guidance counselor and student affairs", {"Teaching-Ed": 0.9, "Counseling": 0.5, "People-Skill": 0.4}),
("Education researcher and policy advisor", {"Teaching-Ed": 0.9, "Data-Analytics": 0.4, "Legal-Practice": 0.3}),
("Teacher training and professional development", {"Teaching-Ed": 1.0, "People-Skill": 0.5, "Admin-Skill": 0.3})], ["education"]),
# Community-Serve
("What community service area motivates you?", {"Community-Serve": 0.9}, [
("Disaster relief and emergency response", {"Community-Serve": 1.0, "Physical-Skill": 0.4, "People-Skill": 0.3}),
("Youth development and empowerment programs", {"Community-Serve": 0.9, "Teaching-Ed": 0.5, "People-Skill": 0.3}),
("Environmental cleanup and conservation", {"Community-Serve": 0.9, "Environmental-Sci": 0.5, "Physical-Skill": 0.3}),
("Healthcare outreach in underserved areas", {"Community-Serve": 0.9, "Public-Health": 0.5, "Patient-Care": 0.3}),
("Livelihood training for out-of-school youth", {"Community-Serve": 0.9, "Teaching-Ed": 0.5, "Startup-Venture": 0.3}),
("Advocacy for indigenous peoples' rights", {"Community-Serve": 0.9, "Legal-Practice": 0.4, "Social-Work": 0.4})], ["public_service", "social"]),
("What community development approach appeals to you?", {"Community-Serve": 0.9, "People-Skill": 0.3}, [
("Grassroots organizing and barangay engagement", {"Community-Serve": 1.0, "People-Skill": 0.5, "Social-Work": 0.3}),
("Grant writing and NGO fundraising", {"Community-Serve": 0.9, "Finance-Acct": 0.4, "Marketing-Sales": 0.3}),
("Volunteer coordination and management", {"Community-Serve": 0.9, "Admin-Skill": 0.5, "People-Skill": 0.4}),
("Community needs assessment and research", {"Community-Serve": 0.9, "Data-Analytics": 0.4, "Analytical-Skill": 0.3}),
("Building partnerships with local government", {"Community-Serve": 0.9, "People-Skill": 0.5, "Legal-Practice": 0.3}),
("Social enterprise development for communities", {"Community-Serve": 0.8, "Startup-Venture": 0.5, "Finance-Acct": 0.3})], ["public_service", "social"]),
("Where would you serve your community?", {"Community-Serve": 0.9}, [
("Local government unit (LGU) planning office", {"Community-Serve": 1.0, "Admin-Skill": 0.5, "Legal-Practice": 0.3}),
("International NGO like Red Cross or Habitat", {"Community-Serve": 0.9, "People-Skill": 0.5, "Admin-Skill": 0.3}),
("DSWD social welfare programs", {"Community-Serve": 0.9, "Social-Work": 0.5, "People-Skill": 0.3}),
("Peace Corps or volunteer service abroad", {"Community-Serve": 0.9, "People-Skill": 0.4, "Teaching-Ed": 0.3}),
("Church or religious organization outreach", {"Community-Serve": 0.9, "People-Skill": 0.5, "Counseling": 0.3}),
("Community cooperative or livelihood project", {"Community-Serve": 0.9, "Startup-Venture": 0.4, "Finance-Acct": 0.3})], ["public_service", "social"]),
# Social-Work
("What social work practice area interests you?", {"Social-Work": 0.9}, [
("Child welfare and protection services", {"Social-Work": 1.0, "Counseling": 0.4, "Legal-Practice": 0.3}),
("Medical social work in hospitals", {"Social-Work": 0.9, "Patient-Care": 0.5, "Health-Admin": 0.3}),
("School social work and student support", {"Social-Work": 0.9, "Teaching-Ed": 0.5, "Counseling": 0.3}),
("Community organizing and development", {"Social-Work": 0.9, "Community-Serve": 0.5, "People-Skill": 0.4}),
("Disaster response and crisis social work", {"Social-Work": 0.9, "Community-Serve": 0.5, "People-Skill": 0.3}),
("Correctional and rehabilitation social work", {"Social-Work": 0.9, "Law-Enforce": 0.4, "Counseling": 0.3})], ["social", "public_service"]),
("Which vulnerable population would you serve?", {"Social-Work": 0.9, "People-Skill": 0.3}, [
("Abused and neglected children", {"Social-Work": 1.0, "Counseling": 0.5, "Legal-Practice": 0.3}),
("Persons with disabilities seeking support", {"Social-Work": 0.9, "Rehab-Therapy": 0.4, "Community-Serve": 0.3}),
("Homeless and street-connected individuals", {"Social-Work": 0.9, "Community-Serve": 0.5, "Public-Health": 0.3}),
("Overseas Filipino worker families", {"Social-Work": 0.9, "Counseling": 0.5, "People-Skill": 0.4}),
("Senior citizens needing care and support", {"Social-Work": 0.9, "Patient-Care": 0.5, "Counseling": 0.3}),
("Indigenous communities facing displacement", {"Social-Work": 0.9, "Community-Serve": 0.5, "Legal-Practice": 0.3})], ["social", "public_service"]),
# Law-Enforce
("Which law enforcement specialization appeals to you?", {"Law-Enforce": 0.9}, [
("Criminal investigation and detective work", {"Law-Enforce": 1.0, "Forensic-Sci": 0.4, "Analytical-Skill": 0.3}),
("Cybercrime prevention and digital policing", {"Law-Enforce": 0.9, "Cyber-Defense": 0.5, "Technical-Skill": 0.3}),
("Drug enforcement and anti-narcotics", {"Law-Enforce": 0.9, "Forensic-Sci": 0.4, "Physical-Skill": 0.3}),
("Traffic management and road safety", {"Law-Enforce": 0.9, "Admin-Skill": 0.4, "Community-Serve": 0.3}),
("Intelligence and counter-terrorism", {"Law-Enforce": 1.0, "Analytical-Skill": 0.5, "Physical-Skill": 0.3}),
("Community policing and public relations", {"Law-Enforce": 0.9, "People-Skill": 0.5, "Community-Serve": 0.4})], ["law", "public_service"]),
("What law enforcement skill would you develop?", {"Law-Enforce": 0.9, "Physical-Skill": 0.3}, [
("Crime scene processing and evidence handling", {"Law-Enforce": 1.0, "Forensic-Sci": 0.5, "Analytical-Skill": 0.3}),
("Interview and interrogation techniques", {"Law-Enforce": 0.9, "People-Skill": 0.5, "Counseling": 0.3}),
("Emergency response and crisis management", {"Law-Enforce": 0.9, "Physical-Skill": 0.5, "People-Skill": 0.3}),
("Report writing and case documentation", {"Law-Enforce": 0.9, "Admin-Skill": 0.5, "Analytical-Skill": 0.3}),
("Surveillance and undercover operations", {"Law-Enforce": 0.9, "Technical-Skill": 0.4, "Physical-Skill": 0.4}),
("Firearms proficiency and tactical training", {"Law-Enforce": 1.0, "Physical-Skill": 0.5, "Technical-Skill": 0.3})], ["law", "physical"]),
("What law enforcement career path attracts you?", {"Law-Enforce": 0.9}, [
("PNP officer rising through the ranks", {"Law-Enforce": 1.0, "People-Skill": 0.4, "Admin-Skill": 0.3}),
("NBI special agent and investigator", {"Law-Enforce": 0.9, "Forensic-Sci": 0.5, "Analytical-Skill": 0.3}),
("Philippine Coast Guard officer", {"Law-Enforce": 0.9, "Maritime-Sea": 0.5, "Physical-Skill": 0.3}),
("PDEA anti-drug enforcement agent", {"Law-Enforce": 0.9, "Physical-Skill": 0.4, "Forensic-Sci": 0.3}),
("Bureau of Fire Protection officer", {"Law-Enforce": 0.9, "Physical-Skill": 0.5, "Community-Serve": 0.3}),
("Criminology professor and researcher", {"Law-Enforce": 0.8, "Teaching-Ed": 0.5, "Lab-Research": 0.3})], ["law", "public_service"]),
# Legal-Practice
("What area of law interests you most?", {"Legal-Practice": 0.9}, [
("Criminal law and prosecution/defense", {"Legal-Practice": 1.0, "Law-Enforce": 0.4, "Analytical-Skill": 0.3}),
("Corporate and business law", {"Legal-Practice": 0.9, "Finance-Acct": 0.4, "Admin-Skill": 0.3}),
("Family law and custody matters", {"Legal-Practice": 0.9, "Counseling": 0.4, "Social-Work": 0.3}),
("Labor and employment law", {"Legal-Practice": 0.9, "HR-Management": 0.5, "People-Skill": 0.3}),
("Environmental and mining law", {"Legal-Practice": 0.9, "Environmental-Sci": 0.4, "Legal-Practice": 0.3}),
("Intellectual property and technology law", {"Legal-Practice": 0.9, "Technical-Skill": 0.4, "Software-Dev": 0.3})], ["law"]),
("What legal career path appeals to you?", {"Legal-Practice": 0.9, "People-Skill": 0.3}, [
("Trial lawyer arguing cases in court", {"Legal-Practice": 1.0, "People-Skill": 0.5, "Analytical-Skill": 0.3}),
("Public attorney helping indigent Filipinos", {"Legal-Practice": 0.9, "Community-Serve": 0.5, "Social-Work": 0.3}),
("Corporate legal counsel for a company", {"Legal-Practice": 0.9, "Admin-Skill": 0.5, "Finance-Acct": 0.3}),
("Judge or magistrate in the judiciary", {"Legal-Practice": 1.0, "Analytical-Skill": 0.5, "People-Skill": 0.3}),
("Legal researcher and law professor", {"Legal-Practice": 0.9, "Teaching-Ed": 0.5, "Lab-Research": 0.3}),
("Mediator and alternative dispute resolution", {"Legal-Practice": 0.9, "Counseling": 0.5, "People-Skill": 0.4})], ["law"]),
("What legal skill would you prioritize?", {"Legal-Practice": 0.9, "Analytical-Skill": 0.3}, [
("Legal research and case analysis", {"Legal-Practice": 1.0, "Analytical-Skill": 0.5, "Lab-Research": 0.3}),
("Contract drafting and negotiation", {"Legal-Practice": 0.9, "People-Skill": 0.5, "Analytical-Skill": 0.3}),
("Courtroom advocacy and oral argument", {"Legal-Practice": 0.9, "People-Skill": 0.5, "Performing-Arts": 0.3}),
("Regulatory compliance and auditing", {"Legal-Practice": 0.9, "Admin-Skill": 0.5, "Finance-Acct": 0.3}),
("Legal writing and memorandum preparation", {"Legal-Practice": 1.0, "Analytical-Skill": 0.5, "Admin-Skill": 0.3}),
("Client counseling and case management", {"Legal-Practice": 0.9, "Counseling": 0.4, "People-Skill": 0.4})], ["law"]),
# Hospitality-Svc
("What hospitality management area excites you?", {"Hospitality-Svc": 0.9}, [
("Hotel front office and guest relations", {"Hospitality-Svc": 1.0, "People-Skill": 0.5, "Admin-Skill": 0.3}),
("Food and beverage service management", {"Hospitality-Svc": 0.9, "Culinary-Arts": 0.4, "Admin-Skill": 0.3}),
("Event and banquet coordination", {"Hospitality-Svc": 0.9, "Admin-Skill": 0.5, "Creative-Skill": 0.3}),
("Housekeeping and facility management", {"Hospitality-Svc": 0.9, "Admin-Skill": 0.5, "Physical-Skill": 0.3}),
("Revenue management and room pricing", {"Hospitality-Svc": 0.9, "Finance-Acct": 0.5, "Data-Analytics": 0.3}),
("Resort and spa wellness operations", {"Hospitality-Svc": 0.9, "Rehab-Therapy": 0.3, "People-Skill": 0.4})], ["hospitality"]),
("What hospitality skill would you develop?", {"Hospitality-Svc": 0.9, "People-Skill": 0.3}, [
("Guest complaint resolution and service recovery", {"Hospitality-Svc": 1.0, "People-Skill": 0.5, "Counseling": 0.3}),
("Reservation system and booking management", {"Hospitality-Svc": 0.9, "Technical-Skill": 0.4, "Admin-Skill": 0.4}),
("Fine dining service and table management", {"Hospitality-Svc": 0.9, "Culinary-Arts": 0.4, "People-Skill": 0.3}),
("Multilingual communication for foreign guests", {"Hospitality-Svc": 0.9, "People-Skill": 0.5, "Tourism-Travel": 0.3}),
("Hospitality marketing and promotions", {"Hospitality-Svc": 0.9, "Marketing-Sales": 0.5, "Digital-Media": 0.3}),
("Staff training and service excellence coaching", {"Hospitality-Svc": 0.8, "Teaching-Ed": 0.5, "People-Skill": 0.4})], ["hospitality"]),
("Where would you work in hospitality?", {"Hospitality-Svc": 0.9}, [
("Five-star resort in Boracay or Palawan", {"Hospitality-Svc": 1.0, "Tourism-Travel": 0.4, "People-Skill": 0.3}),
("International hotel chain management", {"Hospitality-Svc": 0.9, "Admin-Skill": 0.5, "Finance-Acct": 0.3}),
("Cruise ship guest services", {"Hospitality-Svc": 0.9, "Maritime-Sea": 0.4, "People-Skill": 0.4}),
("Airline cabin crew and in-flight service", {"Hospitality-Svc": 0.9, "Tourism-Travel": 0.4, "Physical-Skill": 0.3}),
("Convention center and MICE operations", {"Hospitality-Svc": 0.9, "Admin-Skill": 0.5, "Marketing-Sales": 0.3}),
("Eco-lodge or boutique hotel owner", {"Hospitality-Svc": 0.9, "Startup-Venture": 0.5, "Environmental-Sci": 0.3})], ["hospitality"]),
# Tourism-Travel
("What tourism sector excites you most?", {"Tourism-Travel": 0.9}, [
("Eco-tourism and sustainable travel", {"Tourism-Travel": 1.0, "Environmental-Sci": 0.5, "Community-Serve": 0.3}),
("Cultural and heritage tourism", {"Tourism-Travel": 0.9, "Creative-Skill": 0.4, "Teaching-Ed": 0.3}),
("Adventure tourism and outdoor activities", {"Tourism-Travel": 0.9, "Physical-Skill": 0.5, "Sports-Ed": 0.3}),
("Medical and wellness tourism", {"Tourism-Travel": 0.9, "Patient-Care": 0.4, "Hospitality-Svc": 0.3}),
("MICE (meetings, incentives, conventions)", {"Tourism-Travel": 0.9, "Admin-Skill": 0.5, "Marketing-Sales": 0.3}),
("Food and culinary tourism tours", {"Tourism-Travel": 0.9, "Culinary-Arts": 0.5, "Hospitality-Svc": 0.3})], ["hospitality"]),
("What tourism marketing strategy would you use?", {"Tourism-Travel": 0.9, "Marketing-Sales": 0.3}, [
("Social media travel content creation", {"Tourism-Travel": 1.0, "Digital-Media": 0.5, "Creative-Skill": 0.3}),
("Destination branding for Philippine provinces", {"Tourism-Travel": 0.9, "Marketing-Sales": 0.5, "Creative-Skill": 0.3}),
("Travel package bundling and pricing", {"Tourism-Travel": 0.9, "Finance-Acct": 0.4, "Analytical-Skill": 0.3}),
("Partnership with DOT for national campaigns", {"Tourism-Travel": 0.9, "Admin-Skill": 0.4, "Community-Serve": 0.3}),
("Online booking platform and website SEO", {"Tourism-Travel": 0.9, "Web-Dev": 0.5, "Technical-Skill": 0.3}),
("Influencer and vlogger collaboration", {"Tourism-Travel": 1.0, "Digital-Media": 0.5, "People-Skill": 0.3})], ["hospitality", "business"]),
("What Philippine tourism challenge would you solve?", {"Tourism-Travel": 0.9, "Community-Serve": 0.3}, [
("Developing tourism in less-visited provinces", {"Tourism-Travel": 1.0, "Community-Serve": 0.5, "Marketing-Sales": 0.3}),
("Protecting natural sites from over-tourism", {"Tourism-Travel": 0.9, "Environmental-Sci": 0.5, "Community-Serve": 0.3}),
("Improving tourist safety and information", {"Tourism-Travel": 0.9, "Law-Enforce": 0.3, "Admin-Skill": 0.3}),
("Training local communities for tourism jobs", {"Tourism-Travel": 0.9, "Teaching-Ed": 0.5, "Community-Serve": 0.4}),
("Building accessible tourism for PWDs", {"Tourism-Travel": 0.9, "Rehab-Therapy": 0.3, "Community-Serve": 0.4}),
("Creating digital tourism maps and apps", {"Tourism-Travel": 0.9, "Mobile-Dev": 0.5, "Software-Dev": 0.3})], ["hospitality", "public_service"]),
# Culinary-Arts
("What culinary specialization appeals to you?", {"Culinary-Arts": 0.9}, [
("Filipino cuisine and traditional cooking", {"Culinary-Arts": 1.0, "Creative-Skill": 0.4, "Agri-Nature": 0.3}),
("Pastry arts and baking", {"Culinary-Arts": 0.9, "Creative-Skill": 0.5, "Food-Science": 0.3}),
("International cuisine and fusion cooking", {"Culinary-Arts": 0.9, "Creative-Skill": 0.5, "Tourism-Travel": 0.3}),
("Catering management and event food service", {"Culinary-Arts": 0.9, "Hospitality-Svc": 0.5, "Admin-Skill": 0.3}),
("Food styling and photography for media", {"Culinary-Arts": 0.9, "Digital-Media": 0.5, "Visual-Design": 0.3}),
("Research and development for food products", {"Culinary-Arts": 0.9, "Food-Science": 0.5, "Lab-Research": 0.3})], ["hospitality"]),
("What kitchen management skill interests you?", {"Culinary-Arts": 0.9, "Admin-Skill": 0.3}, [
("Menu planning and recipe costing", {"Culinary-Arts": 1.0, "Finance-Acct": 0.4, "Nutrition-Diet": 0.3}),
("Kitchen team leadership and brigade system", {"Culinary-Arts": 0.9, "People-Skill": 0.5, "Admin-Skill": 0.3}),
("Food safety and sanitation (HACCP)", {"Culinary-Arts": 0.9, "Food-Science": 0.5, "Lab-Research": 0.3}),
("Inventory and supply chain for fresh produce", {"Culinary-Arts": 0.9, "Industrial-Ops": 0.4, "Agri-Nature": 0.3}),
("Restaurant concept and interior design", {"Culinary-Arts": 0.9, "Spatial-Design": 0.5, "Creative-Skill": 0.3}),
("Social media presence and food blogging", {"Culinary-Arts": 0.8, "Digital-Media": 0.5, "Marketing-Sales": 0.4})], ["hospitality"]),
("What culinary career path excites you?", {"Culinary-Arts": 0.9}, [
("Executive chef at a top hotel restaurant", {"Culinary-Arts": 1.0, "People-Skill": 0.4, "Hospitality-Svc": 0.3}),
("Restaurant owner and entrepreneur", {"Culinary-Arts": 0.9, "Startup-Venture": 0.5, "Finance-Acct": 0.3}),
("Culinary instructor at a cooking school", {"Culinary-Arts": 0.9, "Teaching-Ed": 0.5, "People-Skill": 0.3}),
("Food writer and recipe book author", {"Culinary-Arts": 0.9, "Creative-Skill": 0.5, "Digital-Media": 0.3}),
("Private chef for VIP clients", {"Culinary-Arts": 0.9, "People-Skill": 0.5, "Hospitality-Svc": 0.3}),
("Food product developer for a company", {"Culinary-Arts": 0.9, "Food-Science": 0.5, "Industrial-Ops": 0.3})], ["hospitality"]),
# Sports-Ed
("What sports education role interests you?", {"Sports-Ed": 0.9}, [
("PE teacher designing fitness curricula", {"Sports-Ed": 1.0, "Teaching-Ed": 0.5, "Physical-Skill": 0.3}),
("Team sports coach and strategist", {"Sports-Ed": 0.9, "Analytical-Skill": 0.4, "People-Skill": 0.4}),
("Athletic trainer and injury prevention", {"Sports-Ed": 0.9, "Rehab-Therapy": 0.5, "Physical-Skill": 0.4}),
("Sports nutritionist for athletes", {"Sports-Ed": 0.9, "Nutrition-Diet": 0.5, "Physical-Skill": 0.3}),
("Sports event and competition organizer", {"Sports-Ed": 0.9, "Admin-Skill": 0.5, "Hospitality-Svc": 0.3}),
("Sports analytics and performance tracking", {"Sports-Ed": 0.8, "Data-Analytics": 0.5, "Technical-Skill": 0.3})], ["physical", "education"]),
("Which sport would you coach or teach?", {"Sports-Ed": 0.9, "Physical-Skill": 0.3}, [
("Basketball coaching and team development", {"Sports-Ed": 1.0, "People-Skill": 0.5, "Physical-Skill": 0.3}),
("Swimming and aquatic sports instruction", {"Sports-Ed": 0.9, "Physical-Skill": 0.5, "Maritime-Sea": 0.2}),
("Martial arts and self-defense training", {"Sports-Ed": 0.9, "Physical-Skill": 0.6, "People-Skill": 0.3}),
("Track and field athletics coaching", {"Sports-Ed": 0.9, "Physical-Skill": 0.5, "Analytical-Skill": 0.3}),
("Volleyball or badminton coaching", {"Sports-Ed": 1.0, "People-Skill": 0.5, "Physical-Skill": 0.3}),
("Fitness and gym training program design", {"Sports-Ed": 0.9, "Rehab-Therapy": 0.3, "Physical-Skill": 0.5})], ["physical", "education"]),
# Agri-Nature
("What agricultural practice interests you most?", {"Agri-Nature": 0.9}, [
("Crop production and sustainable farming", {"Agri-Nature": 1.0, "Environmental-Sci": 0.4, "Physical-Skill": 0.3}),
("Animal husbandry and livestock management", {"Agri-Nature": 0.9, "Physical-Skill": 0.4, "Lab-Research": 0.3}),
("Fisheries and aquaculture", {"Agri-Nature": 0.9, "Maritime-Sea": 0.4, "Environmental-Sci": 0.3}),
("Agricultural technology and precision farming", {"Agri-Nature": 0.9, "Technical-Skill": 0.5, "Data-Analytics": 0.3}),
("Organic farming and permaculture design", {"Agri-Nature": 0.9, "Environmental-Eng": 0.4, "Community-Serve": 0.3}),
("Post-harvest handling and food storage", {"Agri-Nature": 0.9, "Food-Science": 0.5, "Industrial-Ops": 0.3})], ["agriculture"]),
("What Philippine agricultural problem would you solve?", {"Agri-Nature": 0.9, "Community-Serve": 0.3}, [
("Typhoon-resistant crop varieties for farmers", {"Agri-Nature": 1.0, "Lab-Research": 0.4, "Environmental-Sci": 0.3}),
("Market access for smallholder farmers", {"Agri-Nature": 0.9, "Marketing-Sales": 0.4, "Startup-Venture": 0.3}),
("Soil health and fertility restoration", {"Agri-Nature": 0.9, "Environmental-Sci": 0.5, "Lab-Research": 0.3}),
("Irrigation and water management systems", {"Agri-Nature": 0.9, "Environmental-Eng": 0.5, "Civil-Build": 0.3}),
("Pest and disease management without chemicals", {"Agri-Nature": 0.9, "Environmental-Sci": 0.4, "Lab-Research": 0.4}),
("Youth engagement and farm succession planning", {"Agri-Nature": 0.9, "Community-Serve": 0.5, "Teaching-Ed": 0.3})], ["agriculture", "public_service"]),
]
for t, qt, o, br in svc_qs:
    ALL.append(nq(t, qt, o, br))


# ==================== PATCHING LOGIC ====================
def main():
    with open("questions_enhanced.py", "r", encoding="utf-8") as f:
        qe = f.read()
    questions = [q for q, _ in ALL]
    first_id = questions[0]["question_id"]
    if f'"question_id": {first_id}' in qe:
        print(f"Q{first_id} already exists — skipping."); return
    insert_point = qe.rfind("\n]\n\nTRAIT_SECONDARY_MAP")
    if insert_point == -1:
        print("ERROR: insertion point not found"); sys.exit(1)
    lines = ["    # ==================== ENGINEERING+BUSINESS+CREATIVE+SCIENCE+SERVICE QUESTIONS ===================="]
    for q in questions:
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
    qe = qe[:insert_point] + "\n" + "\n".join(lines) + qe[insert_point:]
    with open("questions_enhanced.py", "w", encoding="utf-8") as f:
        f.write(qe)
    print(f"Added {len(questions)} questions (Q{questions[0]['question_id']}-Q{questions[-1]['question_id']})")

    import importlib
    for m in ["questions_enhanced", "adaptive_assessment"]:
        if m in sys.modules: del sys.modules[m]
    from questions_enhanced import QUESTIONS_POOL_ENHANCED
    q_lookup = {q["question_id"]: q for q in QUESTIONS_POOL_ENHANCED}
    print(f"Total questions: {len(QUESTIONS_POOL_ENHANCED)}")

    with open("adaptive_assessment.py", "r", encoding="utf-8") as f:
        aa = f.read()

    # Add tree nodes
    tree_data = {q["question_id"]: br for q, br in ALL}
    first_check = f"{questions[0]['question_id']}:"
    if first_check not in aa.split("QUESTION_TREE_NODES")[1][:30000]:
        ts = aa.find("QUESTION_TREE_NODES = {")
        bd = 0; p = ts + len("QUESTION_TREE_NODES = {")
        while p < len(aa):
            if aa[p] == '{': bd += 1
            elif aa[p] == '}':
                if bd == 0:
                    ins = [f'    {qid}: {{"level": 2, "weight": 1.5, "branches": {br}}},' for qid, br in tree_data.items()]
                    aa = aa[:p] + "\n" + "\n".join(ins) + "\n" + aa[p:]
                    print(f"Added {len(tree_data)} tree nodes"); break
                bd -= 1
            p += 1

    # Update TRAIT_FOLLOWUP_MAP
    tfm_match = re.search(r'TRAIT_FOLLOWUP_MAP\s*=\s*\{', aa)
    tfm_start = tfm_match.start()
    bd = 0; p = tfm_match.end()
    while p < len(aa):
        if aa[p] == '{': bd += 1
        elif aa[p] == '}':
            if bd == 0: tfm_end = p + 1; break
            bd -= 1
        p += 1
    ns = {}; exec(aa[tfm_start:tfm_end], {}, ns)
    tfm = ns["TRAIT_FOLLOWUP_MAP"]

    for q in questions:
        qid = q["question_id"]
        all_traits = set(q["trait_tags"].keys())
        for opt in q["options"]:
            for t in opt.get("trait_tags", {}).keys(): all_traits.add(t)
        for trait in all_traits:
            if trait in tfm and qid not in tfm[trait]: tfm[trait].append(qid)

    def sc(qid, trait):
        q = q_lookup.get(qid)
        if not q: return 0
        total = sum(o.get("trait_tags",{}).get(trait,0) for o in q["options"])
        avg = total / max(len(q["options"]),1)
        tmax = {}
        for o in q["options"]:
            for t,v in o.get("trait_tags",{}).items():
                if t not in tmax or v > tmax[t]: tmax[t] = v
        return avg + (10.0 if tmax and max(tmax, key=tmax.get) == trait else 0)

    reordered = {}
    for trait, qids in sorted(tfm.items()):
        scored = [(qid, sc(qid, trait)) for qid in qids]
        scored.sort(key=lambda x: -x[1])
        reordered[trait] = [qid for qid, _ in scored]

    tlines = ["TRAIT_FOLLOWUP_MAP = {"]
    for trait in sorted(reordered.keys()):
        tlines.append(f'    "{trait}": {reordered[trait]},')
    tlines.append("}")
    aa = aa[:tfm_start] + "\n".join(tlines) + aa[tfm_end:]

    with open("adaptive_assessment.py", "w", encoding="utf-8") as f:
        f.write(aa)
    print("Updated adaptive_assessment.py")

    # Validate
    for m in ["questions_enhanced", "adaptive_assessment"]:
        if m in sys.modules: del sys.modules[m]
    from adaptive_assessment import TRAIT_FOLLOWUP_MAP
    under = {}
    for trait, qids in TRAIT_FOLLOWUP_MAP.items():
        on = 0
        for qid in qids[:30]:
            q = q_lookup.get(qid)
            if not q: continue
            tmax = {}
            for o in q["options"]:
                for t,v in o.get("trait_tags",{}).items():
                    if t not in tmax or v > tmax[t]: tmax[t] = v
            if tmax and max(tmax, key=tmax.get) == trait: on += 1
        if on < 10: under[trait] = on
        else: print(f"  {trait}: {on}/30 on-topic")
    if under:
        print(f"\nStill under 10: {under}")

if __name__ == "__main__":
    main()
