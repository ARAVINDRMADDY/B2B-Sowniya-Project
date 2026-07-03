import os

# Data lists
healthcare_list = """EyeCare Industry Outreach Platform
Dental Support Organizations
Veterinarians Email List
Urologist Email List
Surgeon Email List
Social Workers Email List
Rheumatologists Email And Mailing List
Respiratory Therapists Email And Mailing List
Registered Nurses Email List
Radiology Directors Email List
Radiologists Email List
Quality Assurance Directors Email And Mailing List
Pulmonologist Email List
Psychologists Email And Mailing List
Psychiatrists Email List
Professional Career Women in Healthcare Email And Mailing List
Plastic Surgeons Email List
Physician Recruiters Email And Mailing List
Physician Email List
Physician Assistant Email List
Physical Therapists Email List
Pharmacy Director Email List
Pharmaceutical Email List
Pediatricians Email List
Pathologists Email List
Oxygen Therapy Equipment Email List
Orthopedists Email List
Orthopedic Surgeons Email List
Orthodontists Email And Mailing List
Oral Surgeons Email List
Oral and Maxillofacial Surgeons Email And Mailing List
Optometrists Email List
Ophthalmologists Email List
Oncology Nurses Email And Mailing List
Oncologists Email List
Office Based Nurses Email And Mailing List
Obstetrics Email List
Nutritionist Medicine Physician Email List
Nursing Homes Email List
Nursing Home Operators Email And Mailing List
Nurses Email List
Nurse Managers Email And Mailing List
Neurosurgeons Email List
Neurologists Email List
Naturopathic Physicians Email List
Medical Geneticist Email List
Medical And Hospital Equipments Email List
Massage Therapists Email List
IV Infusion Therapy Providers Email List
Internists Email List
Internal Medicine Email List
Infection Control Directors Email List
ICU Directors Email List
Hypnotists Email And Mailing List
Hospital Office Managers Email List
Hospital HR Directors Email List
Hospital Executives Email List
Hospital Decision Makers Email List
Hospital Administrators Email And Mailing List
Home Healthcare Providers Email And Mailing List
HMO and PPO Managers Email And Mailing List
HIPAA Compliance Managers Email List
Hematologist Email List
Heart Disease Specialist Email List
Healthcare Executives Email List
HC Payer And Provider Email List
Global Physician Email List
Geriatric Services Directors Email List
General Surgeons Email And Mailing List
Gastroenterology Director Email List
Gastroenterologists Email And Mailing List
Family Practitioners Email And Mailing List
Family Practice Director Email List
Family Marital Therapists Email List
ENT Specialist Email List
Endocrinologists Email List
Emergency Medicine Specialists Email And Mailing List
Dialysis Nurses Email And Mailing List
Diagnostic Radiologists Email And Mailing List
Diabetes Specialists Email List
Dermatologists Email List
Deputy Medical Director Email List
Denturists Email And Mailing List
Dental Laboratories Email List
Clinical Lab Scientists Email List
Chiropractor Email List
Chief Medical Officer Email List
Chest and Cardiac Surgeons Email and Mailing List
Cardiologists Email List
Cancer Specialists Email List
Bariatrician Email List
Audiologists Email and Mailing List
Athletic Therapists Email List
Asthma Specialist Email List
Arthritis Specialist Email List
Anesthetists Email List
Allergy Immunology Nurses Email List
Ailments Email List
Gynecologists Mailing Database
Cosmetologist Email List
Addiction Counselors Email List
Hospital Email List
Dentist Email List""".split('\n')

tech_list = """Palo Alto Users List
CheckPoint Clients Mailing List
41st Parameter Software
Adobe ColdFusion
ADP Streamline
Aloha POS
Altair
Amazon EC2
Amazon Web Services
Application Performance Management List
AzureDesk
Antivirus Software
Autotask
ACT CRM
Citrix GoToTraining
Citrix XenMobile
Cisco Telepresence Content Server
Accounting Software Users List
ConnectWise
Cypherix
Drift
Ektron
EMC
Five9
Filemaker
Genesys
GoDaddy Hosting
HootSuite
iCims
IBM ECM
ADP Clients List
Affise Users Mailing Database
Actuate
Adobe Connect
Aegis
Akamai
Alterian
Amazon S3
Apache Giraph
Aruba
Adobe CQ5 (CMS)
Value-added Resellers Contact Data
Avaya
Booker
Citrix GoToWebcast
Cisco IOS
Brightcove
Cloud Resellers Contact Database
Drupal
Epic
Epicor ERP
Filenet
Fleet & Asset Management Email List
Gensuite
Gold Mine CRM
HubSpot CRM
Intacct ERP
IBM Informix
Trustwave Users List
3D Animation Software
Adallom
Adobe FrameMaker
Alpha Anywhere
Akana
Amisys
Amazon SimpleDB
ArangoDB
Airwatch
List of Solarwinds Customers
Avaya Aura
Baan
Citrix XenApp
Cisco Network Switches
Terremark
Cloud Service Providers Email List
EduPad
EPiServer
Epicor Retail
FireEye
Freshdesk
GAGEpack
Google Cloud
HP Hardware
IBM AIX
IBM ERP
Citrix Users Contact Database
8x8
Adaptive Insights
Adobe Neolane
Altium
Allscripts
Amazon RDS
Amdocs CRM
Applicant Tracking System
Asentinel
ATG
Automotive Software
Avaya Customers List
Citrix GoToMeeting
Citrix XenDesktop
Cisco
Salesforce CRM Users List
Cloudways
Cyber Security Software
Deltek Costpoint
EHS Software
Email Marketing Software
Evault Deltapro
FireMon
Fullstep
Global eProcure
Hadoop
HP UX
IBM
IBM Gentran""".split('\n')

prof_list = """Ceo Email List
CISO Email List
Chief AI officers email list
Supply Chain Executives Email List
Project Directors Managers Email List
IT VP Email List
Directors Email List
CPO Email List
Chartered Accountants Email List
Chairman Email List
Accounting and Taxing Professionals Email List
Event Organizers Email List
General Manager Email List
CSO Email List
COO Email List
CHRO Email List
Chief and VP Software Email List
Chief and VP of Quality Email List
Architect Email List
Chief And VP of Operations mailing List
Canadian Software Developers Email List
Canadian CPA Email List
Canadian CMO Email List
Canadian CFO Email List
Canadian CEO Email List
HR Executives Mailing List
CMO Email List
CIO Email List
CFO Email List
Attorney Email List
CPA Email List""".split('\n')

industry_list = """Oil and Gas Industry Email List
Manufacturing Industries Email List
Cybersecurity Companies Email List
Renewable Energy Email List
Wearable Technology Users
Telecommunication Industry Executives Email List
Supply Chain and Logistics Industry Email List
Real Estate Industry Email List
Printing Publishing Industry Executives Email List
Premix Compound Feed Industry Email List
Plumbing and HVAC Equipment Email List
Pharmaceutical Industry Email List
Pet Care Industry Email List
Mining Industry Email List
Medical Device Equipment Industry Email List
Machinery and Equipment Industry Email List
Logistics Services Email List
Life Science Industry Email List
Legal Services Industry Executives Email List
Large Equipment Shipping Email List
Insurance Service Industry Email List
Hotel Industry Email List
Health Beauty Industry Executives Email List
Health and Wellness Industry Email List
Energy Industry Email List
Education Industry Email List
Consumer Goods and Services Email List
Consulting Services Industry Executives Email List
Computer Software Industry Executives Email List
Chemical Industry Email List
Cement Industry Email List
Business Services Industry Executives Email List
Biotechnology Industry Executives Email List
Banking and Finance Industry Email list
Asset Management Business Email List
Architectural Service Industry Executives Email List
Agriculture Industry Email List
Advertising Industry Email List
Aviation Industry Mailing List
3D Printing Industry Email List
Automotive Industry Email List""".split('\n')

with open('template_top.html', 'r', encoding='utf-8') as f:
    top = f.read()

with open('template_bottom.html', 'r', encoding='utf-8') as f:
    bottom = f.read()

pages = [
    {
        'filename': 'healthcare-more.html',
        'title': 'Healthcare Email Lists',
        'items': healthcare_list
    },
    {
        'filename': 'technology-more.html',
        'title': 'Technology User Lists',
        'items': tech_list
    },
    {
        'filename': 'professionals-more.html',
        'title': 'Segmented Professional Lists',
        'items': prof_list
    },
    {
        'filename': 'industry-more.html',
        'title': 'Industry-Wise Email Lists',
        'items': industry_list
    }
]

for page in pages:
    items_html = ""
    for item in page['items']:
        if item.strip():
            items_html += f"""
                <li class="flex items-start">
                    <svg class="w-2 h-2 text-white/70 mr-3 mt-2 flex-shrink-0" fill="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"></circle></svg>
                    <a href="#" class="text-white/90 hover:text-white transition-colors text-sm font-medium underline underline-offset-4 decoration-white/20 hover:decoration-white/80">{item.strip()}</a>
                </li>"""
                
    main_content = f"""
    <main class="flex-grow bg-[#003B23]">
        <section class="py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="mb-12">
                    <h1 class="text-3xl md:text-4xl font-extrabold text-white tracking-tight">{page['title']}:</h1>
                </div>
                <ul class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-x-8 gap-y-4">
                    {items_html}
                </ul>
            </div>
        </section>
    </main>
    """
    
    full_html = top + main_content + bottom
    
    filepath = os.path.join(r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project", page['filename'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_html)
        
    print(f"Created {page['filename']}")
