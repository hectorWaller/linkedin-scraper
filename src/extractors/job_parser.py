thondef parse_job_card(card):
job_id = card.get("data-entity-urn", "").split(":")[-1]

title_el = card.select_one(".base-search-card__title")
title = title_el.get_text(strip=True) if title_el else ""

link_el = card.select_one("a.base-card__full-link")
job_link = link_el["href"] if link_el else ""

logo_el = card.select_one("img.artdeco-entity-image")
logo = logo_el["data-delayed-url"] if logo_el else ""

return {
"job_id": job_id,
"job_title": title,
"job_link": job_link,
"job_logo": logo,
"post_date": "",
"post_date_text": "",
}