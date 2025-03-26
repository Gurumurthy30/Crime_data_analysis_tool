from neo4j import GraphDatabase

# Neo4j connection details
NEO4J_URI = "bolt://localhost:7687"  # Change if using a remote server
USERNAME = "neo4j"
PASSWORD = "your_password"

# Cypher query for creating nodes
cypher_query = """
// ========= PERSON NODES (25 nodes) =========
CREATE (:Person {person_id: '100001', name: 'Arun Kumar', alias: 'Aru', DOB: '1982-05-10', address: 'Chennai', national_id: 'TN123456', criminal_record_status: 'Yes'});
CREATE (:Person {person_id: '100002', name: 'Meena Rani', alias: 'Meenu', DOB: '1990-03-22', address: 'Coimbatore', national_id: 'TN223456', criminal_record_status: 'No'});
CREATE (:Person {person_id: '100003', name: 'Suresh Kumar', alias: 'Suru', DOB: '1975-11-02', address: 'Madurai', national_id: 'TN323456', criminal_record_status: 'Yes'});
CREATE (:Person {person_id: '100004', name: 'Lakshmi Devi', alias: null, DOB: '1988-07-18', address: 'Tiruchirappalli', national_id: 'TN423456', criminal_record_status: 'No'});
CREATE (:Person {person_id: '100005', name: 'Vijay Kumar', alias: 'Vijay', DOB: '1980-12-05', address: 'Salem', national_id: 'TN523456', criminal_record_status: 'Yes'});
CREATE (:Person {person_id: '100006', name: 'Priya Nair', alias: null, DOB: '1992-04-12', address: 'Tirunelveli', national_id: 'TN623456', criminal_record_status: 'No'});
CREATE (:Person {person_id: '100007', name: 'Ravi Shankar', alias: 'Ravi', DOB: '1978-08-25', address: 'Chennai', national_id: 'TN723456', criminal_record_status: 'Yes'});
CREATE (:Person {person_id: '100008', name: 'Deepa Menon', alias: null, DOB: '1985-09-30', address: 'Coimbatore', national_id: 'TN823456', criminal_record_status: 'No'});
CREATE (:Person {person_id: '100009', name: 'Karthik Raj', alias: 'Karthi', DOB: '1987-06-14', address: 'Madurai', national_id: 'TN923456', criminal_record_status: 'Yes'});
CREATE (:Person {person_id: '100010', name: 'Sita Ram', alias: null, DOB: '1979-01-11', address: 'Tiruchirappalli', national_id: 'TN103456', criminal_record_status: 'No'});
CREATE (:Person {person_id: '100011', name: 'Gopi Krishna', alias: 'Gopi', DOB: '1983-05-20', address: 'Salem', national_id: 'TN113456', criminal_record_status: 'Yes'});
CREATE (:Person {person_id: '100012', name: 'Anita Singh', alias: null, DOB: '1991-07-07', address: 'Tirunelveli', national_id: 'TN123457', criminal_record_status: 'No'});
CREATE (:Person {person_id: '100013', name: 'Ramesh Iyer', alias: 'Ramesh', DOB: '1980-02-15', address: 'Chennai', national_id: 'TN133456', criminal_record_status: 'Yes'});
CREATE (:Person {person_id: '100014', name: 'Vani Sundaram', alias: null, DOB: '1986-10-03', address: 'Coimbatore', national_id: 'TN143456', criminal_record_status: 'No'});
CREATE (:Person {person_id: '100015', name: 'Maheshwaran', alias: 'Mahesh', DOB: '1976-12-29', address: 'Madurai', national_id: 'TN153456', criminal_record_status: 'Yes'});
CREATE (:Person {person_id: '100016', name: 'Divya Patel', alias: null, DOB: '1993-08-17', address: 'Tiruchirappalli', national_id: 'TN163456', criminal_record_status: 'No'});
CREATE (:Person {person_id: '100017', name: 'Sanjay Rao', alias: 'Sanjay', DOB: '1981-04-26', address: 'Salem', national_id: 'TN173456', criminal_record_status: 'Yes'});
CREATE (:Person {person_id: '100018', name: 'Kavitha Menon', alias: null, DOB: '1989-11-05', address: 'Tirunelveli', national_id: 'TN183456', criminal_record_status: 'No'});
CREATE (:Person {person_id: '100019', name: 'Pradeep Varma', alias: 'Prad', DOB: '1977-06-30', address: 'Chennai', national_id: 'TN193456', criminal_record_status: 'Yes'});
CREATE (:Person {person_id: '100020', name: 'Latha Nair', alias: null, DOB: '1994-03-09', address: 'Coimbatore', national_id: 'TN203456', criminal_record_status: 'No'});
CREATE (:Person {person_id: '100021', name: 'Rajan Kumar', alias: 'Rajan', DOB: '1982-10-11', address: 'Madurai', national_id: 'TN213456', criminal_record_status: 'Yes'});
CREATE (:Person {person_id: '100022', name: 'Bhavani Shankar', alias: null, DOB: '1987-12-21', address: 'Tiruchirappalli', national_id: 'TN223457', criminal_record_status: 'No'});
CREATE (:Person {person_id: '100023', name: 'Harish Babu', alias: 'Harish', DOB: '1980-07-04', address: 'Salem', national_id: 'TN233456', criminal_record_status: 'Yes'});
CREATE (:Person {person_id: '100024', name: 'Ritika Roy', alias: null, DOB: '1990-05-15', address: 'Tirunelveli', national_id: 'TN243456', criminal_record_status: 'No'});
CREATE (:Person {person_id: '100025', name: 'Officer Kumar', alias: null, DOB: '1975-02-02', address: 'Chennai', national_id: 'TN253456', criminal_record_status: 'No', role: 'Police Officer'});
CREATE (:Person {person_id: '100026', name: 'Inspector Ramesh', alias: null, DOB: '1970-08-08', address: 'Coimbatore', national_id: 'TN263456', criminal_record_status: 'No', role: 'Police Officer'});
CREATE (:Person {person_id: '100027', name: 'SI Anbu', alias: null, DOB: '1984-11-11', address: 'Madurai', national_id: 'TN273456', criminal_record_status: 'No', role: 'Police Officer'});
CREATE (:Person {person_id: '100028', name: 'Constable Vijay', alias: null, DOB: '1990-01-01', address: 'Tiruchirappalli', national_id: 'TN283456', criminal_record_status: 'No', role: 'Police Officer'});
CREATE (:Person {person_id: '100029', name: 'Officer Deepak', alias: null, DOB: '1978-03-03', address: 'Salem', national_id: 'TN293456', criminal_record_status: 'No', role: 'Police Officer'});
CREATE (:Person {person_id: '100030', name: 'Inspector Shreya', alias: null, DOB: '1983-07-07', address: 'Tirunelveli', national_id: 'TN303456', criminal_record_status: 'No', role: 'Police Officer'});


// ========= CRIME NODES (10 nodes) =========
CREATE (:Crime {crime_id: 'CR1001', crime_type: 'Robbery', date: '2025-01-15', location: 'Chennai', severity: 'High', description: 'Bank robbery at a prominent Chennai bank.'});
CREATE (:Crime {crime_id: 'CR1002', crime_type: 'Fraud', date: '2025-02-10', location: 'Coimbatore', severity: 'Medium', description: 'Online financial scam targeting local residents.'});
CREATE (:Crime {crime_id: 'CR1003', crime_type: 'Homicide', date: '2025-03-05', location: 'Madurai', severity: 'Critical', description: 'Suspicious murder at a residential area.'});
CREATE (:Crime {crime_id: 'CR1004', crime_type: 'Robbery', date: '2025-03-12', location: 'Tiruchirappalli', severity: 'High', description: 'Armed robbery at a jewelry store.'});
CREATE (:Crime {crime_id: 'CR1005', crime_type: 'Cyber Fraud', date: '2025-04-01', location: 'Salem', severity: 'Medium', description: 'Credit card scam reported by multiple victims.'});
CREATE (:Crime {crime_id: 'CR1006', crime_type: 'Homicide', date: '2025-04-15', location: 'Tirunelveli', severity: 'Critical', description: 'Gang-related murder in a suburban locality.'});
CREATE (:Crime {crime_id: 'CR1007', crime_type: 'Robbery', date: '2025-05-05', location: 'Chennai', severity: 'High', description: 'High-profile car theft and robbery.'});
CREATE (:Crime {crime_id: 'CR1008', crime_type: 'Fraud', date: '2025-05-20', location: 'Coimbatore', severity: 'Medium', description: 'Investment fraud scheme discovered.'});
CREATE (:Crime {crime_id: 'CR1009', crime_type: 'Homicide', date: '2025-06-10', location: 'Madurai', severity: 'Critical', description: 'Mysterious death in a quiet neighborhood.'});
CREATE (:Crime {crime_id: 'CR1010', crime_type: 'Cyber Fraud', date: '2025-06-25', location: 'Tiruchirappalli', severity: 'Medium', description: 'Phishing scam affecting several accounts.'});


// ========= MODUS OPERANDI NODES (5 nodes) =========
CREATE (:Modus_Operandi {mo_id: 'MO1001', technique: 'ATM Skimming', common_patterns: 'Use of cloned cards, hidden devices', related_evidence: 'CCTV, electronic logs'});
CREATE (:Modus_Operandi {mo_id: 'MO1002', technique: 'Cyber Fraud', common_patterns: 'Phishing emails, fake websites', related_evidence: 'Digital traces, IP logs'});
CREATE (:Modus_Operandi {mo_id: 'MO1003', technique: 'Armed Robbery', common_patterns: 'Masked entry, use of firearms', related_evidence: 'Bullet casings, CCTV'});
CREATE (:Modus_Operandi {mo_id: 'MO1004', technique: 'Forgery', common_patterns: 'Falsified documents, identity theft', related_evidence: 'Documents, forensic tests'});
CREATE (:Modus_Operandi {mo_id: 'MO1005', technique: 'Carjacking', common_patterns: 'Hijacking vehicles, quick getaway', related_evidence: 'Vehicle debris, witness statements'});


// ========= CASE NODES (7 nodes) =========
CREATE (:Case {case_id: 'CS2001', case_status: 'Under Investigation', court_hearing_dates: ['2025-07-15','2025-08-10'], assigned_officer_id: '100025'});
CREATE (:Case {case_id: 'CS2002', case_status: 'Closed', court_hearing_dates: ['2025-05-05'], assigned_officer_id: '100026'});
CREATE (:Case {case_id: 'CS2003', case_status: 'Trial', court_hearing_dates: ['2025-06-20','2025-07-05'], assigned_officer_id: '100027'});
CREATE (:Case {case_id: 'CS2004', case_status: 'Under Investigation', court_hearing_dates: ['2025-08-01'], assigned_officer_id: '100028'});
CREATE (:Case {case_id: 'CS2005', case_status: 'Closed', court_hearing_dates: ['2025-04-15'], assigned_officer_id: '100029'});
CREATE (:Case {case_id: 'CS2006', case_status: 'Under Investigation', court_hearing_dates: ['2025-09-10'], assigned_officer_id: '100030'});
CREATE (:Case {case_id: 'CS2007', case_status: 'Trial', court_hearing_dates: ['2025-10-05','2025-10-20'], assigned_officer_id: '100025'});


// ========= EVIDENCE NODES (3 nodes) =========
CREATE (:Evidence {evidence_id: 'E3001', type: 'CCTV Footage', collected_from_location: 'Chennai Bank', linked_crime_id: 'CR1001'});
CREATE (:Evidence {evidence_id: 'E3002', type: 'Fingerprint', collected_from_location: 'Jewelry Store', linked_crime_id: 'CR1004'});
CREATE (:Evidence {evidence_id: 'E3003', type: 'Digital Logs', collected_from_location: 'Online Platform', linked_crime_id: 'CR1002'});


// ========= RELATIONSHIPS =========

// -- Link some Persons as perpetrators (COMMITTED) to Crimes --
MATCH (p:Person {person_id:'100001'}), (c:Crime {crime_id:'CR1001'})
CREATE (p)-[:COMMITTED {date: '2025-01-15'}]->(c);

MATCH (p:Person {person_id:'100003'}), (c:Crime {crime_id:'CR1003'})
CREATE (p)-[:COMMITTED {date: '2025-03-05'}]->(c);

MATCH (p:Person {person_id:'100005'}), (c:Crime {crime_id:'CR1004'})
CREATE (p)-[:COMMITTED {date: '2025-03-12'}]->(c);

MATCH (p:Person {person_id:'100007'}), (c:Crime {crime_id:'CR1007'})
CREATE (p)-[:COMMITTED {date: '2025-05-05'}]->(c);

MATCH (p:Person {person_id:'100009'}), (c:Crime {crime_id:'CR1009'})
CREATE (p)-[:COMMITTED {date: '2025-06-10'}]->(c);

MATCH (p:Person {person_id:'100011'}), (c:Crime {crime_id:'CR1002'})
CREATE (p)-[:COMMITTED {date: '2025-02-10'}]->(c);

MATCH (p:Person {person_id:'100013'}), (c:Crime {crime_id:'CR1010'})
CREATE (p)-[:COMMITTED {date: '2025-06-25'}]->(c);

MATCH (p:Person {person_id:'100015'}), (c:Crime {crime_id:'CR1005'})
CREATE (p)-[:COMMITTED {date: '2025-04-01'}]->(c);

MATCH (p:Person {person_id:'100017'}), (c:Crime {crime_id:'CR1008'})
CREATE (p)-[:COMMITTED {date: '2025-05-20'}]->(c);

MATCH (p:Person {person_id:'100019'}), (c:Crime {crime_id:'CR1006'})
CREATE (p)-[:COMMITTED {date: '2025-04-15'}]->(c);

// -- Link Crimes to their Modus Operandi (FOLLOWS) --
MATCH (c:Crime {crime_id:'CR1001'}), (mo:Modus_Operandi {mo_id:'MO1003'})
CREATE (c)-[:FOLLOWS]->(mo);

MATCH (c:Crime {crime_id:'CR1002'}), (mo:Modus_Operandi {mo_id:'MO1002'})
CREATE (c)-[:FOLLOWS]->(mo);

MATCH (c:Crime {crime_id:'CR1003'}), (mo:Modus_Operandi {mo_id:'MO1003'})
CREATE (c)-[:FOLLOWS]->(mo);

MATCH (c:Crime {crime_id:'CR1004'}), (mo:Modus_Operandi {mo_id:'MO1003'})
CREATE (c)-[:FOLLOWS]->(mo);

MATCH (c:Crime {crime_id:'CR1005'}), (mo:Modus_Operandi {mo_id:'MO1002'})
CREATE (c)-[:FOLLOWS]->(mo);

MATCH (c:Crime {crime_id:'CR1006'}), (mo:Modus_Operandi {mo_id:'MO1001'})
CREATE (c)-[:FOLLOWS]->(mo);

MATCH (c:Crime {crime_id:'CR1007'}), (mo:Modus_Operandi {mo_id:'MO1005'})
CREATE (c)-[:FOLLOWS]->(mo);

MATCH (c:Crime {crime_id:'CR1008'}), (mo:Modus_Operandi {mo_id:'MO1004'})
CREATE (c)-[:FOLLOWS]->(mo);

MATCH (c:Crime {crime_id:'CR1009'}), (mo:Modus_Operandi {mo_id:'MO1001'})
CREATE (c)-[:FOLLOWS]->(mo);

MATCH (c:Crime {crime_id:'CR1010'}), (mo:Modus_Operandi {mo_id:'MO1002'})
CREATE (c)-[:FOLLOWS]->(mo);

// -- Associate some Persons with each other (ASSOCIATED_WITH) --
MATCH (p1:Person {person_id:'100001'}), (p2:Person {person_id:'100003'})
CREATE (p1)-[:ASSOCIATED_WITH {relation: 'Accomplice'}]->(p2);

MATCH (p1:Person {person_id:'100005'}), (p2:Person {person_id:'100007'})
CREATE (p1)-[:ASSOCIATED_WITH {relation: 'Gang Member'}]->(p2);

MATCH (p1:Person {person_id:'100009'}), (p2:Person {person_id:'100011'})
CREATE (p1)-[:ASSOCIATED_WITH {relation: 'Family'}]->(p2);

// -- Link Crimes with Evidence (HAS_EVIDENCE) --
MATCH (c:Crime {crime_id:'CR1001'}), (e:Evidence {evidence_id:'E3001'})
CREATE (c)-[:HAS_EVIDENCE]->(e);

MATCH (c:Crime {crime_id:'CR1004'}), (e:Evidence {evidence_id:'E3002'})
CREATE (c)-[:HAS_EVIDENCE]->(e);

MATCH (c:Crime {crime_id:'CR1002'}), (e:Evidence {evidence_id:'E3003'})
CREATE (c)-[:HAS_EVIDENCE]->(e);

// -- Link Persons (as accused/suspects) to Cases (INVESTIGATED_IN) --
MATCH (p:Person {person_id:'100001'}), (cs:Case {case_id:'CS2001'})
CREATE (p)-[:INVESTIGATED_IN]->(cs);

MATCH (p:Person {person_id:'100003'}), (cs:Case {case_id:'CS2003'})
CREATE (p)-[:INVESTIGATED_IN]->(cs);

MATCH (p:Person {person_id:'100005'}), (cs:Case {case_id:'CS2002'})
CREATE (p)-[:INVESTIGATED_IN]->(cs);

MATCH (p:Person {person_id:'100007'}), (cs:Case {case_id:'CS2004'})
CREATE (p)-[:INVESTIGATED_IN]->(cs);

MATCH (p:Person {person_id:'100009'}), (cs:Case {case_id:'CS2005'})
CREATE (p)-[:INVESTIGATED_IN]->(cs);

MATCH (p:Person {person_id:'100011'}), (cs:Case {case_id:'CS2006'})
CREATE (p)-[:INVESTIGATED_IN]->(cs);

MATCH (p:Person {person_id:'100013'}), (cs:Case {case_id:'CS2007'})
CREATE (p)-[:INVESTIGATED_IN]->(cs);

// -- Assign Cases to Police Officers (ASSIGNED_TO) --
MATCH (cs:Case {case_id:'CS2001'}), (p:Person {person_id:'100025'})
CREATE (cs)-[:ASSIGNED_TO]->(p);

MATCH (cs:Case {case_id:'CS2002'}), (p:Person {person_id:'100026'})
CREATE (cs)-[:ASSIGNED_TO]->(p);

MATCH (cs:Case {case_id:'CS2003'}), (p:Person {person_id:'100027'})
CREATE (cs)-[:ASSIGNED_TO]->(p);

MATCH (cs:Case {case_id:'CS2004'}), (p:Person {person_id:'100028'})
CREATE (cs)-[:ASSIGNED_TO]->(p);

MATCH (cs:Case {case_id:'CS2005'}), (p:Person {person_id:'100029'})
CREATE (cs)-[:ASSIGNED_TO]->(p);

MATCH (cs:Case {case_id:'CS2006'}), (p:Person {person_id:'100030'})
CREATE (cs)-[:ASSIGNED_TO]->(p);

MATCH (cs:Case {case_id:'CS2007'}), (p:Person {person_id:'100025'})
CREATE (cs)-[:ASSIGNED_TO]->(p);
"""

def execute_cypher_query(uri, user, password, query):
    # Connect to Neo4j
    driver = GraphDatabase.driver(uri, auth=(user, password))
    try:
        with driver.session() as session:
            session.run(query)
            print("Data successfully inserted into Neo4j!")
    except Exception as e:
        print(f"Error executing Cypher query: {e}")
    finally:
        driver.close()

# Execute the query
execute_cypher_query(NEO4J_URI, USERNAME, PASSWORD, cypher_query)