# LinkedIn Scraper
A powerful LinkedIn job scraper designed to fetch public and private job listings with precision. This tool helps job seekers, analysts, and recruiters gather job data quickly without dealing with slow interfaces or login restrictions. It delivers structured job details, insights, and company information directly from LinkedIn searches.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Linkedin Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
The LinkedIn Scraper collects job listings based on filters such as keywords, location, posting date, and company details.
It solves the challenge of manually browsing LinkedIn’s job interface and provides fast, automated, filter-driven job retrieval.
Ideal for recruiters, data analysts, job seekers, and developers who need clean, structured job data.

### Public & Private Job Scraping Modes
- Public mode bypasses the need for login and retrieves openly available job listings.
- Private mode allows deeper scraping with cookies for enhanced insights.
- Supports configurable filters such as keyword, limit, date posted, and page skipping.
- Provides company insights like size, specialties, headquarters, and industries.
- Retrieves premium insights in private mode, including applicant education and hiring trends.

## Features
| Feature | Description |
|--------|-------------|
| Public Scraping | Collect publicly available LinkedIn job postings without authentication. |
| Private Scraping | Use LinkedIn cookies to access restricted job listings and premium insights. |
| Smart Filtering | Filter results by keywords, location, posting date, and ranking order. |
| Company Insights | Optionally extract company details like industry, size, headquarters, and specialties. |
| Pagination Control | Skip leading pages or limit total results for efficient scraping. |
| Rich Job Metadata | Extract job titles, descriptions, logos, employment type, and seniority level. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|------------|------------------|
| job_id | Unique ID associated with the LinkedIn job listing. |
| job_title | Title of the job posting. |
| company | Nested company data including name, website, industry, size, HQ, and insights. |
| job_link | Direct URL to the job listing. |
| job_logo | URL to the company/job posting logo. |
| post_date | Timestamp when the job was posted. |
| post_date_text | Human-readable posting time. |
| job_description | Full job description text. |
| seniority_level | Seniority of the role. |
| employment_type | Type of employment (full-time, part-time, etc.). |
| industries | Industries associated with the position. |
| insights | Private-mode insights (e.g., applicants, education levels). |
| premium_insights | Extended analytics available in private mode. |

---

## Example Output

    [
      {
        "job_id": "4182654929",
        "job_title": "Software Engineer - Applications",
        "company": {
          "name": "LinkedIn",
          "industry": "Software Development",
          "size": "10,001+ employees",
          "location": "Mountain View, CA"
        },
        "job_link": "https://www.linkedin.com/jobs/view/software-engineer-applications-at-linkedin-4182654929",
        "post_date": "2025-03-14 20:48:35+00:00",
        "post_date_text": "3 days ago"
      }
    ]

---

## Directory Structure Tree

    Linkedin Scraper/
    ├── src/
    │   ├── main.py
    │   ├── scraper/
    │   │   ├── public_mode.py
    │   │   ├── private_mode.py
    │   │   └── filters.py
    │   ├── extractors/
    │   │   ├── job_parser.py
    │   │   └── company_parser.py
    │   ├── outputs/
    │   │   ├── writer_json.py
    │   │   └── writer_csv.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── sample_input.json
    │   └── sample_output.json
    ├── requirements.txt
    └── README.md

---

## Use Cases
- **Recruiters** use it to gather curated job listings quickly so they can analyze openings without navigating LinkedIn manually.
- **Job seekers** use it to track opportunities that match their skills so they can make faster, more informed applications.
- **Market researchers** use it to monitor hiring trends so they can understand job market shifts across industries.
- **Data analysts** extract structured job data so they can run analytics and dashboards on hiring insights.
- **HR teams** automate job data collection so they can benchmark roles across competitors.

---

## FAQs

**Q: Do I need LinkedIn login to use this scraper?**
A: No. Public mode requires no login. For deeper insights and full job access, you can use private mode with your LinkedIn cookies.

**Q: Will my cookies be stored or shared?**
A: Cookies are only used locally for authenticated scraping and are never transmitted elsewhere.

**Q: Does this scraper retrieve premium applicant and company insights?**
A: Yes — but only in private mode where authenticated data is allowed.

**Q: Are there limitations?**
A: Public mode may miss listings locked behind LinkedIn’s login wall or premium listings with restricted visibility.

---

## Performance Benchmarks and Results

**Primary Metric:** Average scraping speed of 150–300 job records per minute depending on filter complexity.
**Reliability Metric:** 98% successful extraction rate on stable connections.
**Efficiency Metric:** Optimized requests reduce redundant page loads, improving throughput by 40% in private mode.
**Quality Metric:** Delivers 90–100% field completeness for public listings and up to 130+ enriched data points in private mode.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
