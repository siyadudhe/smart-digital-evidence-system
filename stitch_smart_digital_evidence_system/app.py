import os
from datetime import datetime
from functools import wraps
from flask import (
    Flask, render_template, request, redirect, url_for, session, flash
)

app = Flask(__name__)
app.secret_key = "forensic_shield_smart_digital_evidence_system_textfile_secret"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EVIDENCE_FILE = os.path.join(BASE_DIR, "evidence.txt")
AUDIT_FILE = os.path.join(BASE_DIR, "audit_log.txt")

# Users dictionary as defined in python logic
USERS = {
    "admin": {
        "password": "admin123",
        "role": "admin",
        "full_name": "Administrator",
        "badge_number": "BADGE-001"
    },
    "officer": {
        "password": "officer123",
        "role": "officer",
        "full_name": "Officer John Doe",
        "badge_number": "BADGE-99214"
    }
}

# --- File Storage Helpers ---

def init_files():
    """Initializes evidence.txt and audit_log.txt with header / initial data if missing."""
    if not os.path.exists(EVIDENCE_FILE):
        sample_records = [
            "EVD-2024-001|CASE-4412-X|Encrypted External SSD|Officer John Doe|2026-07-20|Secured|Samsung 2TB SSD with BitLocker encryption recovered from suspect premises.",
            "EVD-2024-002|CASE-2099-B|Server Authorization Log File|Administrator|2026-07-22|Under Lab Analysis|Raw SSH access logs containing unauthorized root login attempts.",
            "EVD-2024-003|CASE-9910-A|Smartphone Flash Memory Dump|Detective Sarah Jenkins|2026-07-24|Pending Review|Binary NAND dump extracted via hardware reader.",
            "EVD-2024-004|CASE-8902-X|Network Packet Capture (.pcap)|Officer John Doe|2026-07-25|Secured|12GB Wireshark trace recorded during intrusion event."
        ]
        with open(EVIDENCE_FILE, "w", encoding="utf-8") as f:
            for line in sample_records:
                f.write(line + "\n")

    if not os.path.exists(AUDIT_FILE):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(AUDIT_FILE, "w", encoding="utf-8") as f:
            f.write(f"{timestamp} | system | system | SYSTEM_INIT | Text file storage initialized (evidence.txt, audit_log.txt)\n")

def read_evidence():
    """Reads evidence.txt and returns list of evidence dictionaries."""
    evidence_list = []
    if not os.path.exists(EVIDENCE_FILE):
        init_files()
        
    with open(EVIDENCE_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Split by pipe '|' or fallback to ','
            parts = line.split("|") if "|" in line else line.split(",")
            if len(parts) >= 6:
                ev_id = parts[0].strip()
                case_id = parts[1].strip()
                title = parts[2].strip()
                officer = parts[3].strip()
                date_col = parts[4].strip()
                status = parts[5].strip()
                desc = parts[6].strip() if len(parts) > 6 else ""
                evidence_list.append({
                    "evidence_id": ev_id,
                    "case_id": case_id,
                    "title": title,
                    "officer_name": officer,
                    "date_collected": date_col,
                    "status": status,
                    "description": desc
                })
    return evidence_list

def write_all_evidence(evidence_list):
    """Rewrites evidence.txt with the given evidence list."""
    with open(EVIDENCE_FILE, "w", encoding="utf-8") as f:
        for item in evidence_list:
            line = f"{item['evidence_id']}|{item['case_id']}|{item['title']}|{item['officer_name']}|{item['date_collected']}|{item['status']}|{item.get('description', '')}\n"
            f.write(line)

def append_evidence(item):
    """Appends a single evidence record to evidence.txt."""
    with open(EVIDENCE_FILE, "a", encoding="utf-8") as f:
        line = f"{item['evidence_id']}|{item['case_id']}|{item['title']}|{item['officer_name']}|{item['date_collected']}|{item['status']}|{item.get('description', '')}\n"
        f.write(line)

def log_audit(username, role, action, details=""):
    """Appends an audit log line to audit_log.txt."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} | {username} | {role} | {action} | {details}\n"
    with open(AUDIT_FILE, "a", encoding="utf-8") as f:
        f.write(line)

def read_audit_logs():
    """Reads audit_log.txt and returns list of log dicts."""
    logs = []
    if not os.path.exists(AUDIT_FILE):
        init_files()
        
    with open(AUDIT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(" | ")
            if len(parts) >= 4:
                logs.append({
                    "timestamp": parts[0],
                    "username": parts[1],
                    "role": parts[2],
                    "action": parts[3],
                    "details": parts[4] if len(parts) > 4 else ""
                })
    logs.reverse() # Newest first
    return logs

# --- Decorators & Access Controls ---

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('role') != 'admin':
            flash("Access Denied: Only Administrator role can perform this operation.", "error")
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

# --- Routes ---

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        
        user_info = USERS.get(username)
        if user_info and user_info['password'] == password:
            session['username'] = username
            session['role'] = user_info['role']
            session['full_name'] = user_info['full_name']
            session['badge_number'] = user_info['badge_number']
            
            log_audit(username, user_info['role'], "LOGIN_SUCCESS", f"User logged in successfully from {request.remote_addr}")
            flash(f"Welcome back, {user_info['full_name']}!", "success")
            return redirect(url_for('dashboard'))
        else:
            log_audit(username or "unknown", "none", "LOGIN_FAILED", f"Failed login attempt for username '{username}'")
            flash("Invalid username or password. Please try again.", "error")
            return render_template('login.html', username=username)
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    username = session.get('username', 'unknown')
    role = session.get('role', 'unknown')
    log_audit(username, role, "LOGOUT", "User logged out.")
    session.clear()
    flash("You have been logged out securely.", "info")
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    evidence_list = read_evidence()
    total_evidence = len(evidence_list)
    
    cases = set(item['case_id'] for item in evidence_list)
    total_cases = len(cases)
    
    pending_alerts = sum(1 for item in evidence_list if item['status'] in ('Pending Review', 'Flagged'))
    
    status_counts = {}
    for item in evidence_list:
        st = item['status']
        status_counts[st] = status_counts.get(st, 0) + 1
        
    recent_logs = read_audit_logs()[:6]
    
    return render_template('dashboard.html', 
                           total_evidence=total_evidence,
                           total_cases=total_cases,
                           pending_alerts=pending_alerts,
                           status_counts=status_counts,
                           recent_logs=recent_logs)

@app.route('/add_evidence', methods=['GET', 'POST'])
@login_required
def add_evidence():
    if request.method == 'POST':
        evidence_id = request.form.get('evidence_id', '').strip()
        case_id = request.form.get('case_id', '').strip()
        title = request.form.get('title', '').strip()
        officer_name = request.form.get('officer_name', '').strip() or session.get('full_name')
        date_collected = request.form.get('date_collected', '').strip() or datetime.now().strftime("%Y-%m-%d")
        description = request.form.get('description', '').strip()
        status = request.form.get('status', 'Secured').strip()
        
        if not evidence_id or not case_id or not title:
            flash("Evidence ID, Case ID, and Title are required fields.", "error")
            return render_template('add_evidence.html')
            
        evidence_list = read_evidence()
        if any(ev['evidence_id'].lower() == evidence_id.lower() for ev in evidence_list):
            flash(f"Error: Evidence ID '{evidence_id}' already exists in evidence.txt.", "error")
            return render_template('add_evidence.html')
            
        new_item = {
            "evidence_id": evidence_id,
            "case_id": case_id,
            "title": title,
            "officer_name": officer_name,
            "date_collected": date_collected,
            "status": status,
            "description": description
        }
        append_evidence(new_item)
        log_audit(session['username'], session['role'], "ADD_EVIDENCE", f"Appended evidence {evidence_id} to evidence.txt")
        flash(f"Evidence {evidence_id} successfully recorded in evidence.txt.", "success")
        return redirect(url_for('view_evidence'))
        
    return render_template('add_evidence.html')

@app.route('/view_evidence')
@login_required
def view_evidence():
    query = request.args.get('q', '').strip().lower()
    evidence_list = read_evidence()
    
    if query:
        filtered = []
        for item in evidence_list:
            if (query in item['evidence_id'].lower() or 
                query in item['case_id'].lower() or 
                query in item['title'].lower() or 
                query in item['officer_name'].lower() or 
                query in item['status'].lower() or 
                query in item['description'].lower()):
                filtered.append(item)
        display_list = filtered
    else:
        display_list = evidence_list
        
    total_items = len(evidence_list)
    secured_items = sum(1 for item in evidence_list if item['status'] == 'Secured')
    pending_items = sum(1 for item in evidence_list if item['status'] == 'Pending Review')
    flagged_items = sum(1 for item in evidence_list if item['status'] == 'Flagged')
    
    return render_template('view_evidence.html', 
                           evidence_list=display_list,
                           query=query,
                           total_items=total_items,
                           secured_items=secured_items,
                           pending_items=pending_items,
                           flagged_items=flagged_items)

@app.route('/search_evidence')
@login_required
def search_evidence():
    query = request.args.get('q', '').strip().lower()
    results = []
    if query:
        evidence_list = read_evidence()
        for item in evidence_list:
            if (query in item['evidence_id'].lower() or 
                query in item['case_id'].lower() or 
                query in item['title'].lower() or 
                query in item['officer_name'].lower() or 
                query in item['description'].lower()):
                results.append(item)
        log_audit(session['username'], session['role'], "SEARCH_EVIDENCE", f"Queried evidence.txt for: '{query}' ({len(results)} matches)")
        
    return render_template('search_evidence.html', query=query, results=results)

@app.route('/update_evidence', methods=['GET', 'POST'])
@app.route('/update_evidence/<evidence_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def update_evidence(evidence_id=None):
    evidence_list = read_evidence()
    target_id = evidence_id or request.args.get('evidence_id', '').strip()
    
    record = None
    if target_id:
        record = next((item for item in evidence_list if item['evidence_id'].lower() == target_id.lower()), None)

    if request.method == 'POST':
        form_ev_id = request.form.get('evidence_id', '').strip()
        case_id = request.form.get('case_id', '').strip()
        title = request.form.get('title', '').strip()
        officer_name = request.form.get('officer_name', '').strip()
        date_collected = request.form.get('date_collected', '').strip()
        description = request.form.get('description', '').strip()
        status = request.form.get('status', 'Secured').strip()
        
        updated = False
        for item in evidence_list:
            if item['evidence_id'].lower() == form_ev_id.lower():
                item['case_id'] = case_id
                item['title'] = title
                item['officer_name'] = officer_name
                item['date_collected'] = date_collected
                item['description'] = description
                item['status'] = status
                updated = True
                break
                
        if updated:
            write_all_evidence(evidence_list)
            log_audit(session['username'], session['role'], "UPDATE_EVIDENCE", f"Updated record {form_ev_id} in evidence.txt")
            flash(f"Evidence record {form_ev_id} updated successfully in evidence.txt.", "success")
            return redirect(url_for('view_evidence'))
        else:
            flash(f"Record {form_ev_id} not found in evidence.txt.", "error")

    recent_updates = evidence_list[-5:]
    recent_updates.reverse()
    
    return render_template('update_evidence.html', record=record, target_id=target_id, recent_updates=recent_updates)

@app.route('/delete_evidence', methods=['GET', 'POST'])
@app.route('/delete_evidence/<evidence_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_evidence(evidence_id=None):
    evidence_list = read_evidence()
    target_id = evidence_id or request.args.get('evidence_id', '').strip() or request.form.get('evidence_id', '').strip()
    
    record = None
    if target_id:
        record = next((item for item in evidence_list if item['evidence_id'].lower() == target_id.lower()), None)

    if request.method == 'POST' and request.form.get('confirm_delete') == 'true':
        if not target_id or not record:
            flash("Invalid evidence record target for deletion.", "error")
            return redirect(url_for('view_evidence'))
            
        new_list = [item for item in evidence_list if item['evidence_id'].lower() != target_id.lower()]
        write_all_evidence(new_list)
        
        log_audit(session['username'], session['role'], "DELETE_EVIDENCE", f"Deleted Evidence {target_id} from evidence.txt")
        flash(f"Evidence record {target_id} deleted from evidence.txt.", "success")
        return redirect(url_for('view_evidence'))
        
    return render_template('delete_evidence.html', record=record, target_id=target_id)

@app.route('/audit_logs')
@login_required
@admin_required
def audit_logs():
    logs = read_audit_logs()
    return render_template('audit_logs.html', logs=logs)

if __name__ == '__main__':
    init_files()
    print("ForensicShield Smart Digital Evidence System initialized with Plain Text Storage!")
    print("Files ready: evidence.txt and audit_log.txt")
    print("Serving on http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)
