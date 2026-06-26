from core.base_scanner import BaseScanner


class WebTechScan(BaseScanner):
    name = "Web Tech Scan"
    description = "Targets HTTP/HTTPS services to pull headers, titles, and paths"
    flags = ["-sV", "-v", "-p", "80,443,8080"]
    scripts = ["http-enum", "http-headers", "http-title"]