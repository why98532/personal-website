#!/usr/bin/env python3
"""
公众号舆情监控 — HTTP API Server
启动后提供 /api/run 端点，点击「刷新数据」时触发实际抓取
"""

import json
import os
import sys
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

sys.path.insert(0, os.path.dirname(__file__))

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
PUBLIC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs", "public")

PORT = 8765


class MonitorHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self._send_json({})

    def do_GET(self):
        if self.path == "/api/health":
            self._send_json({"status": "ok", "port": PORT})
        elif self.path == "/api/report":
            # Return the latest report without re-running
            try:
                report_path = os.path.join(OUTPUT_DIR, "report.json")
                if os.path.exists(report_path):
                    with open(report_path, "r", encoding="utf-8") as f:
                        self._send_json(json.load(f))
                else:
                    self._send_json({"error": "report not found"}, 404)
            except Exception as e:
                self._send_json({"error": str(e)}, 500)
        else:
            self._send_json({"error": "not found"}, 404)

    def do_POST(self):
        if self.path == "/api/run":
            try:
                print(f"\n{'='*50}")
                print(f"  [API] 收到刷新请求 — {datetime.now().strftime('%H:%M:%S')}")
                print(f"{'='*50}")

                from main import generate_report, save_report

                report = generate_report()
                save_report(report)

                # Also copy to docs/public for the static site
                os.makedirs(PUBLIC_DIR, exist_ok=True)
                public_path = os.path.join(PUBLIC_DIR, "report.json")
                with open(public_path, "w", encoding="utf-8") as f:
                    json.dump(report, f, ensure_ascii=False, indent=2)

                print(f"  [API] 报告已刷新，共 {report['meta']['total_links']} 个链接")
                self._send_json(report)
            except Exception as e:
                import traceback
                traceback.print_exc()
                self._send_json({"error": str(e)}, 500)
        else:
            self._send_json({"error": "not found"}, 404)

    def log_message(self, format, *args):
        print(f"  [API:{datetime.now().strftime('%H:%M:%S')}] {args[0]}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(PUBLIC_DIR, exist_ok=True)

    print(f"  API Server starting on http://localhost:{PORT}")
    print(f"  Endpoints:")
    print(f"    GET  /api/health  — health check")
    print(f"    GET  /api/report  — latest report")
    print(f"    POST /api/run    — run monitor + return fresh report")
    print(f"  Press Ctrl+C to stop")

    server = HTTPServer(("0.0.0.0", PORT), MonitorHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
        server.shutdown()


if __name__ == "__main__":
    main()
