REPORT_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coverage Report</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; transition: background-color 0.5s, color 0.5s; }
        .header { text-align: left; position: relative; }
        .summary { margin: 20px 0; padding: 10px; font-size: 18px; text-align: center; }
        .status-bar { position: fixed; left: 0; top: 0; width: 10px; height: 100vh; }
        .pass .status-bar { background-color: #97bd61; }
        .fail .status-bar { background-color: #ce3e01; }
        
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f4f4f4; }

        /* Light Mode */
        :root {
            --background-color: white;
            --text-color: black;
            --table-header-bg: #f4f4f4;
            --table-cell-bg: white;
        }

        /* Dark Mode */
        .dark-mode {
            --background-color: #1e1e1e;
            --text-color: #ffffff;
            --table-header-bg: #333333;
            --table-cell-bg: #2a2a2a;
        }

        body {
            background-color: var(--background-color);
            color: var(--text-color);
        }
        th { background-color: var(--table-header-bg); }
        td { background-color: var(--table-cell-bg); }
        
        .theme-toggle {
            position: fixed;
            bottom: 10px;
            right: 10px;
            cursor: pointer;
            padding: 8px 12px;
            border: none;
            background-color: var(--table-header-bg);
            color: var(--text-color);
            border-radius: 20px;
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 14px;
        }
        .theme-toggle:hover {
            background-color: var(--table-header-bg);
        }

        /* Coverage Progress Bar */
        .coverage-container {
            width: 100%;
            background-color: #ddd;
            height: 20px;
            border-radius: 5px;
            overflow: hidden;
            position: relative;
            display: flex;
            align-items: center;
            font-size: 12px;
            font-weight: bold;
        }
        .coverage-bar {
            height: 100%;
            position: absolute;
            left: 0;
            top: 0;
            background: #97bd61;
            width: {coverage-percent}%;
            text-align: center;
            line-height: 20px;
            color: white;
        }
        .not-covered-bar {
            height: 100%;
            position: absolute;
            left: {coverage-percent}%;
            top: 0;
            background: #ce3e01;
            width: {not-covered-percent}%;
            text-align: center;
            line-height: 20px;
            color: white;
        }
        /* Coverage Status */
        .covered-yes {
            background-color: #97bd61;
            color: white;
            text-align: center;
            font-weight: bold;
        }

        .covered-no {
            background-color: #ce3e01;
            color: white;
            text-align: center;
            font-weight: bold;
        }
    </style>
</head>
<body id="report-body" class="{status-class}">
    <div class="status-bar"></div>
    
    <button class="theme-toggle" onclick="toggleDarkMode()">
        <span id="theme-icon">🌙</span>
    </button>
    
    <div class="header">
        <h1>{project-name}</h1>
        <h2>Coverage Report</h2>
        <p id="generated" class="generated">Generated: <span id="report-date">{generated-date}</span></p>
    </div>

    <table>
        <thead>
            <tr>
                <th colspan="4">Coverage Status</th>
            </tr>
            <tr>
                <th colspan="4">Minimum Coverage: {min-coverage}</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td colspan="4">
                    <div class="coverage-container">
                        <div class="coverage-bar">{coverage-percent}%</div>
                        <div class="not-covered-bar">{not-covered-percent}%</div>
                    </div>
                </td>
            </tr>
        </tbody>
    </table>

    <table>
        <thead>
            <tr>
                <th colspan="4">Coverage Detail</th>
            </tr>
            <tr>
                <th>Requirement</th>
                <th>Description</th>
                <th>Covered?</th>
                <th>Test Cases</th>
            </tr>
        </thead>
        <tbody id="coverage-table">
            <!-- Rows will be dynamically inserted -->
        </tbody>
    </table>

    <script>
        function toggleDarkMode() {
            document.body.classList.toggle("dark-mode");
            const themeIcon = document.getElementById("theme-icon");
            if (document.body.classList.contains("dark-mode")) {
                themeIcon.textContent = "☀️";
            } else {
                themeIcon.textContent = "🌙";
            }
        }
    </script>
</body>
</html>
"""