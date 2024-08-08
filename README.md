# LinkxDoctor
*A powerful Python tool for scanning and validating links on a webpage.*

## Overview

**LinkxDoctor** is an advanced, Python-based tool designed to help web developers, SEO specialists, bug hunters, and ethical hackers maintain the integrity of their websites. By scanning any given webpage, LinkxDoctor identifies both broken and valid links, ensuring that all the page hyperlinks function correctly.

As the successor to the [LinkxDoxer](https://github.com/BilalAhmadKhanKhattak/LinkxDoxer), LinkxDoctor builds on its predecessor's foundation with enhanced features, improved performance, and a more user-friendly experience.

## Features

- **Comprehensive Link Scanning**: LinkxDoctor scrapes the entire webpage to collect all hyperlinks, including internal, external, absolute, and relative links.
- **Broken Link Detection**: The tool identifies links that lead to non-existent pages (404 errors) or server issues (500 errors), helping you fix problems before they affect your users.
- **Retry Mechanism**: Temporary network issues? No problem. LinkxDoctor includes a built-in retry mechanism that reattempts failed requests, improving reliability and accuracy.
- **Intelligent URL Handling**: Forget to include `http://` or `https://`? LinkxDoctor will automatically handle missing URL schemes, ensuring smooth operation.
- **Color-Coded Output**: Easily differentiate between valid and broken links with color-coded console messages—green for valid and red for broken links.
- **Save Reports**: After scanning, you have the option to save the results to a text file, making it easy to document and share the link status.

## Why Use LinkxDoctor?

Broken links can severely impact user experience, search engine rankings, and the overall credibility of a website. Regularly checking your site for broken links ensures that visitors and search engines can navigate your site smoothly without encountering dead ends.

**LinkxDoctor** not only identifies these issues but does so efficiently, saving you time and effort. Whether managing a small blog, or a large corporate site, or hunting for bugs and vulnerabilities, LinkxDoctor is an invaluable tool in your website maintenance toolkit.

### For Bug Hunters & Ethical Hackers

LinkxDoctor is also an essential tool for bug hunters and ethical hackers. You can uncover hidden vulnerabilities, misconfigurations, or potential entry points for exploits by identifying broken links. This makes LinkxDoctor a powerful ally in the pursuit of a secure and reliable web presence.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/BilalAhmadKhanKhattak/LinkxDoctor.git
   cd LinkxDoctor
   ```

2. **Install Required Dependencies:**
   Ensure you have Python installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Script:**
   ```bash
   python linkxdoctor.py
   ```

2. **Enter the Website URL:**
   - You will be prompted to enter the URL of the website you want to scan. Ensure the URL includes `http://` or `https://`.
   - The tool will automatically handle missing schemes by prepending `https://` to the URL.

3. **View the Results:**
   - The tool will display a list of valid and broken links in the terminal.
   - Broken links will be highlighted in red, while valid links will appear in green.

4. **Save the Report (Optional):**
   - You will be prompted to save the results to a file.
   - If you choose to save, the tool will create a text file (`links_report.txt` by default) containing the list of valid and broken links.


## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request. Please ensure your code adheres to the existing style and structure.

## License

This project is licensed. See the [LICENSE](LICENSE) file for more details.

## Contact

Created by Bilal Ahmad Khan (Mr. Bilred).  
GitHub: [BilalAhmadKhanKhattak](https://github.com/BilalAhmadKhanKhattak)  
Feel free to reach out if you have any questions or suggestions!

---
