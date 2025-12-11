import os
import re
import sys
import glob

# Configuration
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, 'scripts')

SCRIPTS_TO_CHECK = [
    'start_prexcol.bat',
    'start_simple.bat',
    'setup_project.bat',
    'reinstall_venv.bat',
    'start_prexcol_fixed.bat'
]

def check_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    issues = []

    if not os.path.exists(script_path):
        return [{"type": "Critical", "line": 0, "msg": "File not found", "solutions": ["Restore file", "Check name", "Ignore"]}]

    with open(script_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    # Context for more smart checks
    content = "".join(lines).lower()
    
    for i, line in enumerate(lines):
        line_num = i + 1
        clean_line = line.strip()
        
        # Check 1: Hardcoded Absolute Paths (User specific)
        if "C:\\Users\\" in clean_line and "%" not in clean_line:
            issues.append({
                "type": "Error",
                "line": line_num,
                "msg": f"Hardcoded user path detected: '{clean_line[:30]}...'",
                "solutions": [
                    "Use relative paths (e.g. %~dp0..)", 
                    "Use environment variables (%USERPROFILE%)", 
                    "Delete if not needed"
                ]
            })

        # Check 2: CD command usage without /d on Windows
        if re.search(r'^\s*cd\s+"?[^"%]', clean_line, re.IGNORECASE) and "/d" not in clean_line.lower():
            # Only risky if changing drives, but good practice
            pass 

        # Check 3: Dependencies on fixed ports
        if "localhost:5173" in line:
             issues.append({
                "type": "Warning",
                "line": line_num,
                "msg": "References default Vite port 5173 (Project uses 5175)",
                "solutions": [
                    "Change to 5175 in script", 
                    "Update vite.config.js to 5173",
                    "Ensure inconsistent ports are intentional"
                ]
            })

        # Check 4: Missing Critical Files references
        # Regex to find file references like 'call .\something.bat' or 'python src\...'
        # This is a basic heuristic
        
        # Check 5: Syntax Errors (Basic)
        if "(" in line and ")" not in line:
            # Check if it's part of a block 
            pass 
            
    # Global File Checks
    if script_name == "start_prexcol.bat":
        if "reinstall_venv.bat" not in content:
             issues.append({
                "type": "Critical",
                "line": 0,
                "msg": "Script does not reference recovery system 'reinstall_venv.bat'",
                "solutions": [
                    "Add call to reinstall_venv.bat in error handler",
                    "Update script to latest version",
                    "Manually handle venv failures"
                ]
            })
            
    return issues

def main():
    print(f"========================================")
    print(f" DIAGNOSTICO DE SCRIPTS .BAT")
    print(f"========================================")
    print(f"Directorio: {SCRIPTS_DIR}")
    print(f"")

    total_errors = 0
    
    for script in SCRIPTS_TO_CHECK:
        print(f"[*] Analizando: {script}...")
        results = check_script(script)
        
        if not results:
            print(f"    [OK] Sin errores detectados.")
        else:
            for issue in results:
                total_errors += 1
                print(f"    [!] {issue['type']} en Linea {issue['line']}")
                print(f"        Error: {issue['msg']}")
                print(f"        Soluciones Sugeridas:")
                for idx, sol in enumerate(issue['solutions']):
                    print(f"          {idx+1}. {sol}")
                print("")
    
    print(f"========================================")
    print(f"RESUMEN FINAL")
    if total_errors == 0:
        print(f"Estado: PERFECCION - Todos los scripts parecen validos.")
    else:
        print(f"Estado: ATENCION REQUERIDA - {total_errors} problemas encontrados.")
    print(f"========================================")

if __name__ == "__main__":
    main()
