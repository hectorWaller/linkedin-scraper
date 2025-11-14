thondef parse_company_block(block):
name = block.get_text(strip=True)
return {"name": name, "industry": "", "size": "", "location": ""}