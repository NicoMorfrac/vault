from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import unquote
import json
import subprocess
import sys
import threading


BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")
SEO_AGENT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent"
SCRIPTS_PATH = SEO_AGENT_PATH / "Scripts"
SEO_BATCH_PATH = BASE_PATH / r"02_AGENTS\SEO"
MARKETING_BATCH_PATH = BASE_PATH / r"02_AGENTS\Marketing"
HOST = "127.0.0.1"
PORT = 8765


RUNNING = {}
HISTORY = []


TASKS = {
    "dashboard": {
        "label": "Refresh Dashboard",
        "cwd": SCRIPTS_PATH,
        "command": [sys.executable, str(SCRIPTS_PATH / "seo_dashboard.py")],
    },
    "pipeline": {
        "label": "Run Full SEO Pipeline",
        "cwd": SEO_BATCH_PATH,
        "command": ["cmd", "/c", "run_seo_pipeline.bat"],
    },
    "marketing_reports": {
        "label": "Run Marketing Reports",
        "cwd": MARKETING_BATCH_PATH,
        "command": ["cmd", "/c", "run_marketing_reports.bat"],
        "refresh_dashboard": True,
    },
    "competitor_monitoring": {
        "label": "Run Competitor Monitoring",
        "cwd": MARKETING_BATCH_PATH,
        "command": ["cmd", "/c", "run_competitor_monitoring.bat"],
        "refresh_dashboard": True,
    },
    "health": {
        "label": "Run Health Check",
        "cwd": SCRIPTS_PATH,
        "command": [sys.executable, str(SCRIPTS_PATH / "seo_pipeline_health_check.py")],
        "refresh_dashboard": True,
    },
    "executive": {
        "label": "Run Executive Review",
        "cwd": SCRIPTS_PATH,
        "command": [sys.executable, str(SCRIPTS_PATH / "seo_executive_review.py")],
        "refresh_dashboard": True,
    },
    "topic_authority": {
        "label": "Run Topic Authority",
        "cwd": SCRIPTS_PATH,
        "command": [sys.executable, str(SCRIPTS_PATH / "seo_topic_authority_map.py")],
        "refresh_dashboard": True,
    },
    "content_gaps": {
        "label": "Run Content Gaps",
        "cwd": SCRIPTS_PATH,
        "command": [sys.executable, str(SCRIPTS_PATH / "seo_content_gap_analysis.py")],
        "refresh_dashboard": True,
    },
    "entity_map": {
        "label": "Run Entity Map",
        "cwd": SCRIPTS_PATH,
        "command": [sys.executable, str(SCRIPTS_PATH / "seo_entity_relationship_map.py")],
        "refresh_dashboard": True,
    },
}


def run_task(task_id):
    task = TASKS[task_id]
    RUNNING[task_id] = {
        "status": "running",
        "label": task["label"],
        "output": "",
    }

    try:
        process = subprocess.run(
            task["command"],
            cwd=task["cwd"],
            text=True,
            capture_output=True,
            input="\n" * 20,
            shell=False,
        )

        output = (process.stdout or "") + (process.stderr or "")

        if process.returncode == 0 and task.get("refresh_dashboard"):
            refresh = subprocess.run(
                [sys.executable, str(SCRIPTS_PATH / "seo_dashboard.py")],
                cwd=SCRIPTS_PATH,
                text=True,
                capture_output=True,
                input="\n" * 20,
                shell=False,
            )
            output += "\n\n--- Dashboard refresh ---\n"
            output += (refresh.stdout or "") + (refresh.stderr or "")
            if refresh.returncode != 0:
                process_returncode = refresh.returncode
            else:
                process_returncode = process.returncode
        else:
            process_returncode = process.returncode

        status = "complete" if process_returncode == 0 else "failed"
        RUNNING[task_id] = {
            "status": status,
            "label": task["label"],
            "returncode": process_returncode,
            "output": output[-12000:],
        }
    except Exception as exc:
        RUNNING[task_id] = {
            "status": "failed",
            "label": task["label"],
            "returncode": 1,
            "output": str(exc),
        }

    HISTORY.insert(0, {"task_id": task_id, **RUNNING[task_id]})
    del RUNNING[task_id]


class DashboardHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SEO_AGENT_PATH), **kwargs)

    def log_message(self, format, *args):
        return

    def send_json(self, payload, status=200):
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = unquote(self.path.split("?", 1)[0])

        if path in ("/", "/dashboard"):
            self.path = "/seo_dashboard.html"
            return super().do_GET()

        if path == "/api/tasks":
            self.send_json({
                "tasks": {
                    task_id: {"label": task["label"]}
                    for task_id, task in TASKS.items()
                },
                "running": RUNNING,
                "history": HISTORY[:10],
            })
            return

        return super().do_GET()

    def do_POST(self):
        path = unquote(self.path.split("?", 1)[0])

        if not path.startswith("/api/run/"):
            self.send_json({"error": "Unknown endpoint"}, status=404)
            return

        task_id = path.rsplit("/", 1)[-1]

        if task_id not in TASKS:
            self.send_json({"error": "Unknown task"}, status=404)
            return

        if task_id in RUNNING:
            self.send_json({
                "status": "already_running",
                "task_id": task_id,
                "label": TASKS[task_id]["label"],
            })
            return

        thread = threading.Thread(target=run_task, args=(task_id,), daemon=True)
        thread.start()

        self.send_json({
            "status": "started",
            "task_id": task_id,
            "label": TASKS[task_id]["label"],
        })


def main():
    server = ThreadingHTTPServer((HOST, PORT), DashboardHandler)
    print("")
    print("================================================")
    print("MORFRAC SEO DASHBOARD SERVER")
    print("================================================")
    print(f"Open: http://{HOST}:{PORT}/")
    print("Press Ctrl+C to stop.")
    print("================================================")
    server.serve_forever()


if __name__ == "__main__":
    main()
